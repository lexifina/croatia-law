"""Croatia: acts of the official part of Narodne novine, each as first published, when nothing later changes it.

Reads only a local copy of Narodne novine pages (narodne-novine.nn.hr) and writes corpus.d parts (SCHEMA.md in
scripts/gitlaw_common). Deterministic: the same inputs give the same bytes.

    python -X utf8 parse_acts.py --src <folder with index.jsonl, raw/> --retrieved YYYY-MM-DD
                                 [--exclude <data/zakoni.json of the published repository>] [--report holds.jsonl]

Inputs, in --src:
- index.jsonl: one row per document of the official part, from the Narodne novine search lists (href, title, issue,
  year, document number, kind, issue day);
- index-totals.json: {year: {"total": the number of documents the search says the year has}};
- raw/<year>/<YYYY_MM_issue_doc>.html.gz: each document's page, cut to its ELI metadata block, its title line and its
  text (<div class="sl-content">).

What becomes an act here: a zakon, uredba, pravilnik, odluka, naredba, naputak, uputa or statut, with its text as
printed in Narodne novine. Its one version takes effect on the day its own entry-into-force sentence names ("stupa na
snagu danom objave", "osmoga dana od dana objave", a calendar date, "danom donošenja"); there is no default day
(Ustav čl. 90: a law takes effect at the earliest on the eighth day after publication unless it says otherwise).

An act is held back (written to the report with the reason) when:
- a later document's ELI metadata says it amends, changes, corrects or repeals it;
- a later document's title names it as amended, supplemented, corrected or repealed, or a later act of the same kind
  has the same title (a replacement);
- a later text cites it by name and Narodne novine number with a later number after its own (an amended text), or
  next to wording that changes or repeals it;
- not every later document has been read yet (the check above can't be complete);
- its entry-into-force sentence can't be read, its articles don't run 1..N, it has pictures, or no text.
Appointments, dismissals, pardons and other decisions about named people are left out.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import json
import os
import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = HERE / "corpus.d"
SITE = "https://narodne-novine.nn.hr"

KINDS = {"zakon": "zakon", "uredba": "uredba", "uredba na temelju zakonske ovlasti": "uredba",
         "uredba sa zakonskom snagom": "uredba", "pravilnik": "pravilnik", "odluka": "odluka", "naredba": "naredba",
         "naputak": "naputak", "uputa": "uputa", "statut": "statut"}
# Kind word stems: nominative/accusative/genitive/locative forms of each kind as it opens a title or a citation.
STEMS = [("zakon", r"zakon(?:a|u|om|ik|ika|iku)?"), ("uredba", r"uredb(?:a|e|u|i|om)"),
         ("pravilnik", r"pravilnik(?:a|u|om)?"), ("odluka", r"odluk(?:a|e|u|om)|odluci"),
         ("naredba", r"naredb(?:a|e|u|i|om)"), ("naputak", r"naput(?:ak|ka|ku|kom)"),
         ("uputa", r"uput(?:a|e|u|i|om)"), ("statut", r"statut(?:a|u|om)?")]
STEM_RE = re.compile(r"^(" + "|".join(p for _, p in STEMS) + r")\b", re.I)
PERSONAL = re.compile(r"imenovanj|razrješenj|razriješen|pomilovanj|odlikovanj|postavljenj|opoziv|izbor[ua]? (?:suca|sudaca|"
                      r"člana|članova|predsjednika|zamjenika|pravobranitelj|glavnog)|prestanku (?:dužnosti|mandata|službe)|"
                      r"umirovljenj|dodjeli (?:čina|državljanstva)|stjecanju čina|unaprjeđenj|unapređenj|državljanstv",
                      re.I)
MONTHS = {m: i for i, m in enumerate(["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja",
                                       "kolovoza", "rujna", "listopada", "studenoga", "prosinca"], 1)}
MONTHS.update({"studenog": 11, "veljace": 2, "sijecnja": 1, "ozujka": 3})
ORD = {"prvog": 1, "drugog": 2, "trećeg": 3, "četvrtog": 4, "petog": 5, "šestog": 6, "sedmog": 7, "osmog": 8,
       "devetog": 9, "desetog": 10, "jedanaestog": 11, "dvanaestog": 12, "petnaestog": 15, "šesnaestog": 16,
       "dvadesetog": 20, "tridesetog": 30, "šezdesetog": 60, "devedesetog": 90}
BLOCK = re.compile(r"<br\s*/?>|</?(?:p|div|h[1-6]|li|ul|ol|table|tbody|thead|tr|center|blockquote)\b[^>]*>", re.I)
ARTICLE = re.compile(r"^Članak\s+(\d+)\s*\.?\s*([a-z])?\s*\.?$")
SIGN = re.compile(r"^(?:KLASA|Klasa|URBROJ|Urbroj|Ur\.\s*broj|Broj|BROJ)\s*:|^Zagreb,\s*\d{1,2}\.")
VR = re.compile(r"\bv\.\s*r\.\s*$|\bv\.r\.\s*$")
CHANGE_VERB = re.compile(r"mijenja|briše|brišu|dodaje|dodaju|zamjenjuje|ukida|ukidaju|prestaj|izvan snage|stavlja se|"
                         r"stavljaju se|ne primjenjuj", re.I)
AMEND_TITLE = re.compile(r"(?:izmjen\w*|dopun\w*|ispravak|ispravk\w*|prestank\w* važenja|prestanku važenja|"
                         r"stavljanju izvan snage|ukidanju)\s+(?:i\s+(?:dopun\w*|izmjen\w*)\s+)?(.+)$", re.I)
NN_CITE = re.compile(r"\b(" + "|".join(p for _, p in STEMS) + r")\s+((?:o|za|u|na|od|kojim|kojom)\s(?:[^()]|\((?!\s*[»\"„“«']?\s*Narodne)[^()]{0,40}\)){1,300}?)\s*"
                     r"\(\s*[»\"„“«']?\s*Narodne\s+novine\s*[«\"“”»']?\s*,?\s*(?:br\.|broj|br)\s*([^)]{1,400})\)", re.I)
NN_NUM = re.compile(r"(\d{1,3})\s*([A-Za-z]?)\s*/\s*(\d{4}|\d{2})\b")


class Hold(Exception):
    pass


def norm(s: str) -> str:
    s = html.unescape(s).replace("\xa0", " ").replace("­", "").replace("​", "")
    s = s.replace("–", "-").replace("—", "-").replace("„", '"').replace("“", '"').replace("”", '"')
    s = re.sub(r"[ \t\r\n]+", " ", s)
    return s.strip()


def lines_of(fragment: str) -> list[str]:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<(style|script)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = re.sub(r"</t[dh]\s*>", "\t", fragment, flags=re.I)
    out = []
    for chunk in BLOCK.split(fragment):
        t = re.sub(r"<[^>]+>", "", chunk)
        if "\t" in t:
            cells = [norm(c) for c in t.split("\t")]
            while cells and not cells[-1]:
                cells.pop()
            t = " | ".join(cells).strip()
        else:
            t = norm(t)
        if t:
            out.append(t)
    return out


def subj(title: str) -> tuple[str | None, str]:
    """(kind, subject) of an act's name: 'Zakona o sportu' -> ('zakon', 'o sportu')."""
    t = norm(title)
    t = re.sub(r"\s*\([^)]*\)\s*$", "", t)
    m = STEM_RE.match(t)
    if not m:
        return None, t.lower()
    w = m.group(1).lower()
    kind = next(k for k, p in STEMS if re.fullmatch(p, w, re.I))
    rest = t[m.end():].strip().lower()
    rest = re.sub(r"[\"'»«.,;:]+", "", rest)
    return kind, re.sub(r"\s+", " ", rest)


STOP_WORDS = {"o", "i", "u", "na", "za", "od", "do", "te", "s", "sa", "se", "iz", "po", "pri", "prema", "kod", "ili", "a",
              "kao", "koji", "koja", "koje", "kojim", "kojima", "br", "broj", "nn", "narodne", "novine", "izvan", "snage"}
CHANGE_WORD = re.compile(r"^(?:izmjen|dopun|ukidan|poništ|prestan|važenj|isprav|stavlj)")
CHANGE_TITLE = re.compile(r"izmjen|dopun|ukidanj|poništenj|prestank|stavljanj\w*\s+izvan\s+snage|ispravak", re.I)


def stem(w: str) -> str:
    m = re.match(r"^(.{3,}?)(?:oga|ega|ome|emu|ima|om|em|og|eg|im|ih|a|e|i|o|u)?$", w)
    return (m.group(1) if m else w)[:6]


def core(title: str) -> frozenset[str]:
    """A title's words, without small words and the words that say a text changes, stripped of case endings."""
    words = re.findall(r"[0-9a-zčćžšđ]+", norm(title).lower())
    return frozenset(stem(w) for w in words if w not in STOP_WORDS and not CHANGE_WORD.match(w))


def same_subject(a: str, b: str) -> bool:
    if not a or not b:
        return False
    n = min(len(a), len(b), 60)
    return a[:n] == b[:n] and abs(len(a) - len(b)) < 40 or a == b


def nn_list(s: str) -> list[tuple[int, str, int]]:
    out = []
    for n, suf, y in NN_NUM.findall(s):
        yy = int(y)
        if yy < 100:
            yy += 1900 if yy >= 90 else 2000
        out.append((int(n), suf.upper(), yy))
    return out


def issue_key(issue: str, year: int) -> tuple[int, str, int]:
    m = re.match(r"(\d+)([A-Za-z]?)", issue or "")
    return (int(m.group(1)), m.group(2).upper(), year) if m else (0, "", year)


def parse_day(s: str) -> str | None:
    m = re.search(r"(\d{1,2})\.\s*([a-zčćžšđ]+)\s+(\d{4})", s)
    if m and m.group(2) in MONTHS:
        try:
            return date(int(m.group(3)), MONTHS[m.group(2)], int(m.group(1))).isoformat()
        except ValueError:
            return None
    m = re.search(r"(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})", s)
    if m:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1))).isoformat()
        except ValueError:
            return None
    return None


def in_force(text: str, pub: str, adopted: str | None) -> tuple[str, str]:
    """(day, how) from the act's entry-into-force sentence (the one about the whole act, "Ovaj Zakon ...")."""
    sents = re.findall(r"[^.\n]*?stup(?:a|aju|it će|it ce)\s+na\s+snagu[^\n]*", text)
    if not sents:
        raise Hold("in_force_missing")
    general = [x for x in sents if re.search(r"\b(?:Ov(?:aj|a|o|e|i)|Taj)\s+(?:[A-ZČĆŽŠĐ]\w+\s+)?(?:Zakon|Uredb|Pravilnik|Odluk|Naredb|Naputak|Uput|Statut|Kodeks|Zakonik)", x)
               and not re.match(r"\s*(?:\(\d+\)\s*)?(?:Iznimno|Odredb|Članak|Članci)", x)]
    if len(general) == 1:
        s = general[0]
    elif len(sents) == 1:
        s = sents[0]
    else:
        raise Hold("in_force_ambiguous:" + " / ".join(x.strip()[:80] for x in sents[:3]))
    if len(sents) > 1:
        s = s + " osim"  # other provisions have their own day
    low = s.lower()
    cut = re.split(r"\b(?:osim|izuzev|iznimno|a odredb[ae]|s iznimkom)\b", low)[0]
    note = "exceptions" if cut != low else ""
    p = date.fromisoformat(pub)
    # Another gazette, notice board or website named next to Narodne novine: a day counted from "the publication"
    # could be counted from that one, so only a calendar date or the adoption day is read then.
    other = re.search(r"služben\w*\s+(?:vjesnik|glasnik|novin|list|glasil)|glasnik\w*|glasil\w*|oglasn\w+\s+ploč|"
                      r"mrežn\w+\s+stranic|internetsk\w+\s+stranic", cut)

    def rel(day: str, how: str) -> tuple[str, str]:
        if other:
            raise Hold("in_force_other_publication:" + s.strip()[:120])
        return day, how
    if re.search(r"stup\w*(?: it će)?\s+na\s+snagu\s+(?:danom|na dan|s danom)\s+(?:njezine |njegove |njihove )?objav", cut):
        return rel(pub, "danom objave" + (" " + note if note else ""))
    if re.search(r"(?:danom|na dan|s danom)\s+(?:njezina |njegova )?donošenja", cut):
        if not adopted:
            raise Hold("adopted_day_unknown")
        return adopted, "danom donošenja" + (" " + note if note else "")
    m = re.search(r"\b(" + "|".join(o[:-2] for o in ORD) + r")(?:oga|og|i|ega|eg)\s+dana?\s+(?:od\s+dana|nakon\s+dana|nakon|od|po)\s+"
                  r"(?:njezine |njegove |njihove )?objav", cut)
    if m:
        n = ORD[m.group(1) + "og"]
        return rel((p + timedelta(days=n)).isoformat(), f"{m.group(1)}oga dana od objave" + (" " + note if note else ""))
    if re.search(r"(?:sljedećeg|slijedećeg|idućeg|prvog)\s+dana\s+(?:od\s+dana|nakon\s+dana|nakon|od|po)\s+(?:njezine |njegove )?objav|"
                 r"dan(?:om)?\s+nakon\s+(?:dana\s+)?(?:njezine |njegove )?objav", cut):
        return rel((p + timedelta(days=1)).isoformat(), "dan nakon objave" + (" " + note if note else ""))
    if re.search(r"prvog\w*\s+dana\s+(?:sljedećeg|slijedećeg|idućeg)\s+mjeseca\s+(?:od\s+dana|nakon|po)\s+(?:njezine |njegove )?objav|"
                 r"prvog\w*\s+dana\s+mjeseca\s+(?:koji\s+slijedi|nakon|što\s+slijedi)", cut):
        y, mth = (p.year + 1, 1) if p.month == 12 else (p.year, p.month + 1)
        return rel(date(y, mth, 1).isoformat(), "prvoga dana sljedećeg mjeseca" + (" " + note if note else ""))
    m = re.search(r"na\s+snagu\s+(?:dana\s+)?(\d{1,2}\.\s*[a-zčćžšđ]+\s+\d{4})", cut)
    if m:
        d = parse_day(m.group(1))
        if d:
            if d < pub and not (adopted and d >= adopted):
                raise Hold(f"in_force_before_publication:{d}")
            return d, "nadnevak" + (" " + note if note else "")
    raise Hold("in_force_unreadable:" + s.strip()[:160])


INCOMING = ("amended_by", "changed_by", "repealed_by", "corrected_by", "consolidated_by")


def eli_url(u: str) -> str:
    """One spelling of an ELI address: some pages write 'https:/narodne-novine...' with one slash."""
    return re.sub(r"^(https?):/+", r"\1://", u.strip()).rstrip("/")


def eli_meta(t: str) -> dict:
    out: dict = defaultdict(list)
    for about, prop, val in re.findall(r'<meta about="([^"]+)" property="http://data\.europa\.eu/eli/ontology#(\w+)"\s+'
                                       r'(?:content|resource)="([^"]*)"', t):
        out[prop].append(val)
    return out


def split_units(lines: list[str], kind: str, title: str) -> tuple[dict, list[str], str | None]:
    amending = bool(re.search(r"izmjen|dopun|ispravk|prestank|stavljanju izvan snage", title, re.I))
    """Units of an act from its page lines: (units, unquoted body lines for the in-force search, signature day)."""
    # Articles run 1, 2, 3, ...: a line "Članak N." opens a unit only when N is the next number. Others (numbers out
    # of turn, "Članak 5.a") are wording the act quotes, e.g. an amending act's new text. Quote depth (»...«) guards
    # a quoted heading that happens to carry the next number; a heading the depth count calls quoted but that comes
    # straight after the previous article's closing quote resynchronises the count.
    depth, marks, arts = 0, [], []
    for i, ln in enumerate(lines):
        m = ARTICLE.match(ln)
        if m and not m.group(2) and int(m.group(1)) == len(arts) + 1:
            prev = lines[i - 1] if i else ""
            if not prev.endswith(":") and (depth == 0 or not amending or re.search(r"«\s*\.?$", prev)):
                depth = 0
                arts.append(i)
        marks.append(depth)
        depth = max(0, depth + ln.count("»") - ln.count("«"))
    if arts:
        last = arts[-1]
        gap = [ln for ln in lines[last + 1:] if (m := ARTICLE.match(ln)) and not m.group(2) and int(m.group(1)) > len(arts) + 1]
        later = [i for i in range(last + 1, len(lines)) if (m := ARTICLE.match(lines[i])) and not m.group(2)
                 and int(m.group(1)) == len(arts) + 1]
        if later:
            raise Hold(f"article_out_of_turn:{len(arts) + 1}")
        if gap and not any(SIGN.match(x) for x in lines[last + 1:]):
            raise Hold("article_gap:" + gap[0][:30])
    kw = {"zakon": r"ZAKON|KODEKS|ZAKONIK", "uredba": r"UREDB[AU]", "pravilnik": r"PRAVILNIK", "odluka": r"ODLUK[AU]",
          "naredba": r"NAREDB[AU]", "naputak": r"NAPUTAK", "uputa": r"UPUT[AU]", "statut": r"STATUT"}[kind]
    kw_re = re.compile(r"^(?:(?:" + kw + r")\b|(?:IZMJEN\w*|DOPUN\w*)(?:\s+I\s+(?:DOPUN|IZMJEN)\w*)?\s+(?:" + kw[:4] + r"))")
    # The title block: the last line before the first article (or anywhere, when there are no articles) that opens
    # with the kind word in capitals; for a law, everything above it (the President's proclamation) is not the law.
    limit = arts[0] if arts else len(lines)
    tpos = [i for i in range(limit) if kw_re.match(lines[i]) and lines[i].upper() == lines[i]]
    if not tpos:
        raise Hold("title_line_missing")
    ti = tpos[-1]
    tj = ti + 1
    while tj < limit and lines[tj].upper() == lines[tj] and re.match(r"^(?:O|ZA|U|NA|OD|KOJ\w+|I|TE)\s", lines[tj]):
        tj += 1
    units: dict = {"naslov": {"label": "Naslov", "kind": "title", "text": title + "\n"}}
    if kind != "zakon":
        # The enacting formula: from "Na temelju ..." to the title (issuer and document number above it are not text).
        k = next((i for i in range(ti) if re.match(r"^(?:Na temelju|Temeljem|Na osnovi|Sukladno)\b", lines[i])), None)
        if k is not None:
            units["uvod"] = {"label": "Uvod", "kind": "preamble", "text": "".join(x + "\n" for x in lines[k:ti])}
    # The end of the text: the signature block after the last article (Klasa/Urbroj/place and date ... v. r.).
    start = arts[0] if arts else tj
    after = arts[-1] if arts else tj
    end = next((i for i in range(after, len(lines)) if SIGN.match(lines[i])), None)
    if end is None:
        vr = next((i for i in range(after + 1, len(lines)) if VR.search(lines[i])), None)
        if vr is not None:
            end = vr
            while end - 1 > after and end > vr - 4 and len(lines[end - 1]) < 90 and not re.search(r"[.:;]$", lines[end - 1]):
                end -= 1
            if end == vr or not re.match(r"^(?:Predsjedni|Ministr|Ravnatelj|Guverner|Direktor|Pravobranitelj|Načelni|"
                                         r"Gradonačelni|Župan|Zamjeni|Glavn|Državn|Potpredsjedni|Upravitelj|Dekan|Rektor)",
                                         lines[end]):
                raise Hold("signature_block_unreadable")
        else:
            end = len(lines)
    sig_end = next((i + 1 for i in range(end, len(lines)) if VR.search(lines[i])), len(lines))
    sig_day = None
    for i in range(end, sig_end):
        m = re.match(r"^[A-ZČĆŽŠĐ][\w ]+,\s*(\d{1,2}\.\s*[a-zčćžšđ]+\s+\d{4})", lines[i])
        if m:
            sig_day = parse_day(m.group(1))
            break
    annex = lines[sig_end:]
    if arts:
        heads = lines[tj:arts[0]]
        nums = []
        for n, i in enumerate(arts):
            j = arts[n + 1] if n + 1 < len(arts) else end
            m = ARTICLE.match(lines[i])
            num, suf = int(m.group(1)), (m.group(2) or "")
            nums.append((num, suf))
            jj = j
            # A chapter or section title right before the next article belongs to the next article.
            if n + 1 < len(arts):
                while jj - 1 > i + 1 and marks[jj - 1] == 0 and is_heading(lines[jj - 1]):
                    jj -= 1
            text = "".join(f"## {x}\n" for x in heads) + f"# Članak {num}.{suf + '.' if suf else ''}\n" + "".join(x + "\n" for x in lines[i + 1:jj])
            key = f"clanak-{num:03d}{suf}"
            if key in units:
                raise Hold(f"article_twice:{key}")
            units[key] = {"label": f"čl. {num}{'.' + suf if suf else ''}", "kind": "art", "text": text}
            heads = lines[jj:j]
    else:
        if not lines[tj:end]:
            raise Hold("no_text")
        units["tekst"] = {"label": "Tekst", "kind": "text", "text": "".join(x + "\n" for x in lines[tj:end])}
    if annex:
        units["prilog"] = {"label": "Prilog", "kind": "annex", "text": "".join(x + "\n" for x in annex)}
    # The entry-into-force sentence is looked for in the last article (then the last three), or the whole text.
    body = lines[arts[-1]:end] if arts else lines[start:end]
    if arts and not re.search(r"stup\w*\s+na\s+snagu", "\n".join(body)):
        body = lines[arts[max(0, len(arts) - 3)]:end]
    return units, body, sig_day


def is_heading(ln: str) -> bool:
    """A chapter or section title line: numbered in capitals, all capitals, or a short line with no closing mark."""
    if " | " in ln or len(ln) > 150 or re.match(r"^(?:-|\(|\d+\)|[a-z]\))", ln):
        return False
    if re.match(r"^(?:[IVXLC]+|\d+)\.\s+\S", ln) and ln.upper() == ln:
        return True
    if re.match(r"^(?:GLAVA|DIO|ODJELJAK|POGLAVLJE|Glava|Dio|Odjeljak|Poglavlje)\b", ln):
        return True
    if ln.upper() == ln and re.search(r"[A-ZČĆŽŠĐ]{3}", ln):
        return True
    return not re.search(r"[.;:,]$", ln) and ln[:1].isupper() and len(ln) < 120


def title_facts(title: str) -> list:
    """[kind, subject, words, and for an amending title the same three of the act it names (or None)]."""
    k, s = subj(title)
    m = AMEND_TITLE.search(norm(title))
    k2 = s2 = c2 = None
    if m:
        k2, s2 = subj(m.group(1))
        c2 = sorted(core(re.sub(r"\s*\(.*$", "", m.group(1))))
    return [k, s, sorted(core(title)), k2, s2, c2]


def page_facts(h: str, r: dict, raw: bytes) -> dict:
    """What one page tells: its outgoing ELI links, its citations of other acts, and (for a kind published here) its
    own reading: the in-force day or why it is held. Depends on the page bytes only."""
    t = raw.decode("utf-8", "replace")
    meta = eli_meta(t)
    links = [[prop, eli_url(target)] for prop in ("amends", "changes", "repeals", "corrects", "consolidates")
             for target in meta.get(prop, [])]
    inc = [[prop, eli_url(src)] for prop in INCOMING for src in meta.get(prop, [])]
    i = t.find('<div class="sl-content">')
    body = norm(re.sub(r"<[^>]+>", " ", t[i:])) if i >= 0 else ""
    cites = []
    starts = [x.start() for x in re.finditer(r"Članak \d+\s*\.", body)]
    for m in NN_CITE.finditer(body):
        k, s = subj(m.group(1) + " " + m.group(2))
        nums = nn_list(m.group(3))
        a0 = max([x for x in starts if x <= m.start()] or [0])
        a1 = min([x for x in starts if x > m.end()] or [len(body)])
        span = body[max(a0, m.start() - 4000):min(a1, m.end() + 4000)]
        verb = bool(CHANGE_VERB.search(span) or CHANGE_VERB.search(body[max(0, m.start() - 160):m.end() + 260]))
        for j, n in enumerate(nums):
            after = any(x[2] > n[2] or (x[2] == n[2] and x[0] > n[0]) for x in nums[j + 1:])
            cites.append([k, s, n[0], n[1], n[2], after, verb])
    out = {"links": links, "inc": inc, "eli": "ELI metadata" in t[:6000], "cites": cites,
           "sha": hashlib.sha256(raw).hexdigest()}
    kind = KINDS.get(r.get("kind", ""))
    if kind:
        try:
            pub = (meta.get("date_publication") or [r["date"]])[0]
            if pub != r["date"]:
                raise Hold(f"publication_day_conflict:{pub} vs {r['date']}")
            adopted = (meta.get("date_document") or [None])[0]
            if i < 0:
                raise Hold("no_text")
            if re.search(r"<img\b", t[i:], re.I):
                raise Hold("has_pictures")
            units, lines, sig_day = split_units(lines_of(t[i:]), kind, norm(r["title"]))
            day, how = in_force("\n".join(lines), pub, adopted or sig_day)
            out["ok"] = [day, how, pub, adopted or None]
        except Hold as e:
            out["hold"] = str(e)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--retrieved", required=True, help="the day the inputs were retrieved (YYYY-MM-DD)")
    ap.add_argument("--exclude", help="data/zakoni.json of the published repository: laws already there are skipped")
    ap.add_argument("--report")
    ap.add_argument("--rejects", help="JSON {slug: reason}: acts held back by hand")
    ap.add_argument("--cache", help="a file to keep each page's reading in between runs (same output, faster)")
    ap.add_argument("--frontier", choices=["all", "amenders"], default="all",
                    help="publish a year once every later document (all) or every later amender has been read")
    ap.add_argument("--compare-frontiers", action="store_true", help="self-check of the amender frontier; writes nothing")
    ap.add_argument("--relations", help="relations.jsonl: per act, the ELI relations Narodne novine lists for it, with "
                                        "the day they were read ({stem, status, fetched, incoming: [{rel, from_eli}]})")
    ap.add_argument("--compare-early", action="store_true", help="self-check of the early release; writes nothing")
    a = ap.parse_args()
    src = Path(a.src)
    index: dict[str, dict] = {}
    for ln in (src / "index.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if not r.get("year"):
            # A list row with no kind: "NN 124/2026, (1486),  30.10.2026."
            m = re.match(r"\s*NN\s+([0-9A-Za-z]+)/(\d{4}),\s*\(([^)]*)\),\s*(?:(.*?),\s*)?(\d{1,2})\.(\d{1,2})\.(\d{4})\.?\s*$",
                         r.get("meta", ""))
            if m:
                r.update({"issue": m.group(1), "year": int(m.group(2)), "doc": m.group(3).strip(),
                          "kind": (m.group(4) or "").strip(),
                          "date": f"{m.group(7)}-{int(m.group(6)):02d}-{int(m.group(5)):02d}"})
        if r.get("year") and r.get("doc"):
            index.setdefault(r["href"], r)
    rejects = json.loads(Path(a.rejects).read_text(encoding="utf-8")) if a.rejects and Path(a.rejects).exists() else {}
    excluded = set()
    if a.exclude and Path(a.exclude).exists():
        for z in json.loads(Path(a.exclude).read_text(encoding="utf-8")):
            excluded.add(z["url"].rstrip("/"))
    # The cache holds page readings only: it stays valid while the code above main() (the page reading) is unchanged.
    source = Path(__file__).read_text(encoding="utf-8")
    code = hashlib.sha256(source[:source.index("\ndef main(")].encode("utf-8")).hexdigest()
    cache = {"code": code, "docs": {}, "parts": {}}
    if a.cache and Path(a.cache).exists():
        try:
            c = json.loads(gzip.decompress(Path(a.cache).read_bytes()).decode("utf-8"))
            if c.get("code") == code:
                cache = c
        except (OSError, ValueError):
            pass

    def stem_of(href: str) -> str:
        return href.rsplit("/", 1)[1][:-5]

    files: dict[str, tuple[int, int, Path]] = {}
    if (src / "raw").exists():
        for y in os.scandir(src / "raw"):
            if y.is_dir():
                for e in os.scandir(y.path):
                    if e.name.endswith(".html.gz"):
                        st = e.stat()
                        files[e.name[:-8]] = (st.st_size, st.st_mtime_ns, Path(e.path))
    # Coverage: the oldest year from which every later document has been read.
    per_year: dict[int, list[int]] = defaultdict(lambda: [0, 0])
    for h, r in index.items():
        per_year[r["year"]][0] += 1
        per_year[r["year"]][1] += stem_of(h) in files
    # A year counts as read only when its list holds as many documents as the search said it has (index-totals.json)
    # and every one of them has its page.
    totals = {}
    if (src / "index-totals.json").exists():
        totals = {int(k): v["total"] for k, v in json.loads((src / "index-totals.json").read_text(encoding="utf-8")).items()}
    frontier = max(per_year) + 1 if per_year else 9999
    # Amender frontier: the oldest year from which every document that could change an act has been read. Those
    # are: laws; titles that amend, correct, repeal, consolidate or interpret; court decisions and judgments (they can
    # annul provisions); and every document of a kind published here that is not about named people (a new
    # regulation or decision can repeal an earlier one in its closing articles). Left out: decisions about named
    # people (rješenja, appointments) and collective agreements.
    amend_re = re.compile(r"izmjen|dopun|ispravak|prestank|ukidan|stavljanju izvan snage|pročišćen|vjerodostojn|"
                          r"Ustavnog suda|upravnog suda", re.I)

    def amender(r: dict) -> bool:
        kind = r.get("kind", "")
        if kind in ("zakon", "izmjene i dopune", "pročišćeni tekst", "presuda", "ostalo") or amend_re.search(r.get("title", "")):
            return True
        return bool(KINDS.get(kind)) and not PERSONAL.search(r.get("title", ""))

    amenders_left: dict[int, int] = defaultdict(int)
    for h, r in index.items():
        if amender(r) and stem_of(h) not in files:
            amenders_left[r["year"]] += 1
    am_frontier = max(per_year) + 1 if per_year else 9999
    for y in sorted(per_year, reverse=True):
        if amenders_left.get(y, 0) == 0 and per_year[y][0] >= totals.get(y, per_year[y][0] + 1):
            am_frontier = y
        else:
            break
    for y in sorted(per_year, reverse=True):
        tot, have = per_year[y]
        if have >= tot and tot >= totals.get(y, tot + 1):
            frontier = y
        else:
            break

    eli_of = lambda r: f"{SITE}/eli/sluzbeni/{r['year']}/{r['issue']}/{r['doc']}"  # noqa: E731
    by_eli = {eli_url(eli_of(r)): h for h, r in index.items()}
    pub_day = {h: r["date"] for h, r in index.items()}
    facts: dict[str, dict] = {}
    for h, r in index.items():
        s = stem_of(h)
        if s not in files:
            continue
        size, mt, path = files[s]
        hit = cache["docs"].get(s)
        if hit and hit[0] == size and hit[1] == mt:
            facts[h] = hit[2]
            continue
        facts[h] = page_facts(h, r, gzip.decompress(path.read_bytes()))
        cache["docs"][s] = [size, mt, facts[h]]
    if a.cache:
        tmp = Path(a.cache + ".tmp")
        tmp.write_bytes(gzip.compress(json.dumps(cache, ensure_ascii=False).encode("utf-8"), 3))
        tmp.replace(a.cache)
    incoming: dict[str, set[tuple[str, str]]] = defaultdict(set)
    cites: dict[tuple, list] = defaultdict(list)
    for h, f in facts.items():
        r = index[h]
        for prop, target in f["links"]:
            th = by_eli.get(eli_url(target))
            if th and th != h:
                incoming[th].add((f"{prop}:{r['issue']}/{r['year']}-{r['doc']}", h))
        for k, s, n0, n1, n2, after, verb in f["cites"]:
            cites[(n0, n1, n2)].append((k, s, h, after, verb))
    titles_named: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    same_title: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    kind_in_issue: dict[tuple, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    named_core: dict[frozenset, list[tuple[str, str]]] = defaultdict(list)
    tcache = cache.setdefault("titles", {})
    cores = {}
    for h, r in index.items():
        tf = tcache.get(r["title"])
        if tf is None:
            tf = tcache[r["title"]] = title_facts(r["title"])
        k, s, c, k2, s2, c2 = tf
        cores[h] = frozenset(c)
        if k:
            same_title[(k, s)].append((r["date"], h))
            kind_in_issue[issue_key(r["issue"], r["year"])][k] += 1
        if c2 is not None:
            if k2:
                titles_named[(k2, s2)].append((r["date"], h))
            named_core[frozenset(c2)].append((r["date"], h))
    postings: dict[str, set[str]] = defaultdict(set)
    for h, c in cores.items():
        for w in c:
            postings[w].add(h)

    def overlapping_later(h: str) -> list[str]:
        """Later documents whose title holds every word of this act's title and changes, cancels or repeats it."""
        c = cores[h]
        if len(c) < 3:
            return []
        # An amending act shares its words with every later amendment of the same act and is not changed by them;
        # only a correction (Ispravak) carrying all its words counts for it.
        only_corrections = bool(CHANGE_TITLE.search(index[h]["title"]))
        hits = None
        for w in sorted(c, key=lambda w: len(postings[w])):
            hits = set(postings[w]) if hits is None else hits & postings[w]
            if not hits:
                return []
        day = index[h]["date"]
        if only_corrections:
            return sorted(x for x in hits if x != h and index[x]["date"] >= day
                          and re.match(r"\s*Ispravak\b", index[x]["title"]))
        return sorted(x for x in hits if x != h and index[x]["date"] >= day
                      and (CHANGE_TITLE.search(index[x]["title"]) or cores[x] == c))

    # Relations Narodne novine lists for an act (its own page's ELI block, and the newest status-200 relations record)
    rel: dict[str, dict] = {}
    if a.relations and Path(a.relations).exists():
        for ln in Path(a.relations).read_text(encoding="utf-8").splitlines():
            try:
                x = json.loads(ln)
            except ValueError:
                continue
            if x.get("status") == 200 and x.get("stem") and x.get("fetched", "") >= rel.get(x["stem"], {}).get("fetched", ""):
                rel[x["stem"]] = x
    unread_days = sorted(r["date"] for h, r in index.items() if stem_of(h) not in files)
    latest_unread = unread_days[-1] if unread_days else "0000-00-00"

    def listed_incoming(h: str) -> list[str]:
        f = facts.get(h) or {}
        out = [f"{prop}:{src}" for prop, src in f.get("inc", [])]
        x = rel.get(stem_of(h))
        if x:
            out += [f"{i.get('rel')}:{eli_url(i.get('from_eli', ''))}" for i in x.get("incoming", [])]
        return sorted(set(out))

    def early_ok(h: str, r: dict) -> bool:
        """An act from 2015 on may be decided before the frontier reaches its year when Narodne novine's relations
        record for it lists nothing that changes it and every document published from 14 days before that record
        was read on has been read (the record may lag that long); the title and citation rules still apply."""
        x = rel.get(stem_of(h))
        if r["year"] < 2015 or not x or x.get("incoming"):
            return False
        since = (date.fromisoformat(x["fetched"][:10]) - timedelta(days=14)).isoformat()
        return latest_unread < since

    def evaluate(year_read, counts=lambda src, act: True, early=lambda h, r: False):
        """Decide every act. year_read(year): every document that could change an act of that year has been read.
        counts(src, act): whether the page src is used as evidence against the act (for the frontier check).
        early(h, r): the act may be decided before its year is read (early release)."""
        chosen: dict[int, list[tuple[str, str, dict, dict]]] = defaultdict(list)
        holds = []
        skipped = defaultdict(int)
        for h in sorted(index, key=lambda x: (index[x]["year"], stem_of(x))):
            r = index[h]
            kind = KINDS.get(r.get("kind", ""))
            if not kind:
                skipped["kind:" + str(r.get("kind"))] += 1
                continue
            title = norm(r["title"])
            if re.match(r"(?:Odluka|Rješenje|Odluka i Rješenje)\s+Ustavnog\s+suda|Ispravak\b|Odluka o proglašenju\b", title):
                skipped["court_or_correction"] += 1
                continue
            if PERSONAL.search(title):
                skipped["personal"] += 1
                continue
            if eli_of(r) in excluded:
                skipped["already_published"] += 1
                continue
            doc = re.sub(r"[^a-z0-9-]", "", r["doc"].lower())
            slug = f"{kind}-{r['year']}-{doc}"
            try:
                if slug in rejects:
                    raise Hold("rejected:" + str(rejects[slug])[:200])
                f = facts.get(h)
                li = listed_incoming(h)
                if li:
                    raise Hold("eli_incoming:" + ",".join(li[:5]))
                if not year_read(r["year"]) and not early(h, r):
                    raise Hold(f"later_documents_not_all_read:frontier={frontier}")
                if f is None:
                    raise Hold("page_missing")
                inc = sorted(lab for lab, src in incoming.get(h, ()) if counts(src, h))
                if inc:
                    raise Hold("eli_changed_by:" + ",".join(inc[:5]))
                k, s = subj(title)
                if k:
                    later = [x for d, x in titles_named.get((k, s), []) if x != h and d >= r["date"]]
                    if later:
                        raise Hold("named_as_amended:" + ",".join(stem_of(x) for x in later[:5]))
                    repl = [x for d, x in same_title.get((k, s), []) if x != h and d >= r["date"]]
                    if repl:
                        raise Hold("same_title_later:" + ",".join(stem_of(x) for x in repl[:5]))
                nc = [x for d, x in named_core.get(cores[h], []) if x != h and d >= r["date"]] \
                    if len(cores[h]) >= 2 and not CHANGE_TITLE.search(title) else []
                if nc:
                    raise Hold("named_as_amended:" + ",".join(stem_of(x) for x in nc[:5]))
                ov = overlapping_later(h)
                if ov:
                    raise Hold("title_words_later:" + ",".join(stem_of(x) for x in ov[:5]))
                own = issue_key(r["issue"], r["year"])
                only_one = kind_in_issue[own].get(kind, 0) == 1
                for ck, cs, who, after, verb in cites.get(own, []):
                    if who == h or ck != kind or pub_day.get(who, "") < r["date"] or not counts(who, h):
                        continue
                    if (k and same_subject(cs, s)) or only_one:
                        if after:
                            raise Hold(f"cited_with_later_numbers:{stem_of(who)}")
                        if verb:
                            raise Hold(f"cited_with_change_wording:{stem_of(who)}")
                if "hold" in f:
                    raise Hold(f["hold"])
            except Hold as e:
                holds.append({"slug": slug, "nn": f"{r['issue']}/{r['year']}", "title": title[:160], "reason": str(e)})
                continue
            chosen[r["year"]].append((slug, h, r, f))
        return chosen, holds, skipped

    if a.compare_frontiers:
        # Self-check of the amender frontier on years where everything has been read: count only amenders (and the
        # act's own year and earlier) as evidence, and compare the held set with the full reading.
        full, full_holds, _ = evaluate(lambda y: y >= frontier)
        lite, lite_holds, _ = evaluate(lambda y: y >= frontier,
                                       lambda src, act: amender(index[src]) or index[src]["year"] <= index[act]["year"])
        fh = {x["slug"] for x in full_holds}
        lh = {x["slug"] for x in lite_holds}
        missed = sorted(fh - lh)
        print(json.dumps({"years_from": frontier, "held_full": len(fh), "held_amenders_only": len(lh),
                          "held_by_full_not_by_amenders": len(missed), "examples": missed[:20],
                          "reasons": [x["reason"][:80] for x in full_holds if x["slug"] in set(missed[:20])]},
                         ensure_ascii=False))
        return
    if a.compare_early:
        # Self-check of the early release on years where everything has been read: for acts with a clean relations
        # record, count as evidence only documents published from 14 days before the record was read (what early
        # release relies on reading), and compare the held set with the full reading.
        def recent_only(src: str, act: str) -> bool:
            x = rel.get(stem_of(act))
            if not x or x.get("incoming") or index[act]["year"] < 2015:
                return True
            since = (date.fromisoformat(x["fetched"][:10]) - timedelta(days=14)).isoformat()
            return index[src]["date"] >= since
        _, full_holds, _ = evaluate(lambda y: y >= frontier)
        _, lite_holds, _ = evaluate(lambda y: y >= frontier, recent_only)
        fh = {x["slug"] for x in full_holds}
        lh = {x["slug"] for x in lite_holds}
        cand = {x["slug"] for x in full_holds + lite_holds}
        clean = sum(1 for h, r in index.items() if r["year"] >= max(frontier, 2015) and rel.get(stem_of(h))
                    and not rel[stem_of(h)].get("incoming"))
        missed = sorted(fh - lh)
        print(json.dumps({"years_from": frontier, "clean_records_in_those_years": clean, "held_full": len(fh),
                          "held_early": len(lh), "held_by_full_not_by_early": len(missed), "examples": missed[:20],
                          "reasons": [x["reason"][:80] for x in full_holds if x["slug"] in set(missed[:20])],
                          "acts_considered": len(cand)}, ensure_ascii=False))
        return
    if a.frontier == "amenders":
        chosen, holds, skipped = evaluate(lambda y: y >= am_frontier, early=early_ok if rel else (lambda h, r: False))
    else:
        chosen, holds, skipped = evaluate(lambda y: y >= frontier)

    PARTS.mkdir(exist_ok=True)
    written = []
    country = {
        "code": "HR", "name": "Croatia", "slug": "croatia", "lang": "hr", "tz": "Europe/Zagreb",
        "future_branch": "buducnost",
        "publisher": {"name": "Narodne novine (narodne-novine.nn.hr)", "email": "nn@narodne-novine.invalid"},
        "default_in_force_rule": {
            "text": "Ustav Republike Hrvatske, čl. 90: zakoni i drugi propisi objavljuju se u Narodnim novinama prije "
                    "stupanja na snagu; zakon stupa na snagu najranije osmoga dana od dana objave, osim ako zbog osobito "
                    "opravdanih razloga zakonom nije određeno drugo. No default day is applied here: each act is dated by "
                    "its own entry-into-force sentence.",
            "source": "https://narodne-novine.nn.hr/eli/sluzbeni/2014/5/90"},
        "licence_note": "Text from Narodne novine (narodne-novine.nn.hr), the official gazette of the Republic of Croatia. "
                        "Laws, regulations and other official texts are not protected by copyright (Zakon o autorskom "
                        "pravu i srodnim pravima, čl. 8)."}
    for year in sorted(chosen):
        rows = sorted(chosen[year], key=lambda x: x[0])
        fp = hashlib.sha256(json.dumps([[s, r["title"], f["sha"], f["ok"]] for s, _, r, f in rows] + [a.retrieved, source],
                                       ensure_ascii=False).encode("utf-8")).hexdigest()
        f_part = PARTS / f"60-akti-{year}.json"
        if cache["parts"].get(str(year)) == fp and f_part.exists():
            written.append((f_part.name, len(rows)))
            continue
        laws, acts = {}, []
        before = {}
        whole = hashlib.sha256(source.encode("utf-8")).hexdigest()
        if f_part.exists() and cache.get("part_code", {}).get(str(year)) == whole:
            try:
                old = json.loads(f_part.read_text(encoding="utf-8"))
                before = {x["slug"]: (x, old["laws"].get(x["slug"])) for x in old.get("acts", [])}
            except (OSError, ValueError, KeyError):
                before = {}
        for slug, h, r, f in rows:
            day, how, pub, adopted = f["ok"]
            prev = before.get(slug)
            if prev and prev[1] and prev[0]["versions"][0]["sha256"] == f["sha"] and prev[0]["versions"][0]["from"] == day \
                    and prev[0]["title"] == norm(r["title"]) and prev[1].get("published") == pub:
                acts.append(prev[0])
                laws[slug] = prev[1]
                continue
            kind = slug.split("-", 1)[0]
            title = norm(r["title"])
            raw = gzip.decompress(files[stem_of(h)][2].read_bytes())
            t = raw.decode("utf-8", "replace")
            units, _, _ = split_units(lines_of(t[t.find('<div class="sl-content">'):]), kind, title)
            day, how, pub, adopted = f["ok"]
            label = f"{title} (NN {r['issue']}/{r['year']})"
            url = eli_of(r)
            note = ("Its entry-into-force article gives some provisions a different day; the whole text is dated by its "
                    "general day.") if "exceptions" in how else None
            laws[slug] = {"label": label, "title": title, "kind": "law" if kind == "zakon" else "decree",
                          "enacted": adopted, "published": pub, "url": url, "temporary_until": None, "restores": None,
                          "note": None}
            acts.append({"slug": slug, "short": title, "title": title, "url": url, "first_law": slug, "earlier_laws": [],
                         "versions": [{"from": day, "source_url": SITE + h, "sha256": f["sha"], "units": units,
                                       "credits": {}, **({"note": note} if note else {})}]})
        out = {"laws": laws, "acts": acts}
        out["sources"] = [{"name": "Narodne novine, službeni dio (narodne-novine.nn.hr)", "url": SITE,
                           "retrieved": a.retrieved, "licence": "Official texts; not protected by copyright (ZAPSP čl. 8)",
                           "notes": "Each document's page with its ELI metadata; the yearly search lists for titles, "
                                    "issues and issue days."}]
        out["decisions"] = [
            "An act is published here as first printed in Narodne novine, one version, from its page on "
            "narodne-novine.nn.hr; the issuer's name, the document number and the signature block (Klasa, Urbroj, place "
            "and date, signature) are not part of its text; for a law, the President's proclamation above it is not "
            "either.",
            "Its one version takes effect on the day its own entry-into-force sentence names: the publication day "
            "(\"danom objave\"), the Nth day after it (\"osmoga dana od dana objave\" = publication day + 8), a calendar "
            "date, the first day of the next month, or the adoption day (\"danom donošenja\": the ELI date_document, "
            "else the place and date above the signature). When the sentence also names another gazette or a website, "
            "only a calendar date or the adoption day is read.",
            "An act is published only when every later document of the official part has been read and none of them "
            "amends, corrects or repeals it by its ELI metadata, names it in an amending, correcting or repealing title, "
            "reuses its title, or cites it by name and Narodne novine number with a later number after its own or next to "
            "wording that changes or repeals it; the others are held back until their later versions are built.",
            "Decisions about named people (appointments, dismissals, pardons, decorations, citizenship), Constitutional "
            "Court decisions and corrections (Ispravak) are left out.",
            "Each version's sha256 is that of the cached page cut to its ELI metadata, title and text."]
        out["ai_use"] = ["none"]
        tmp = f_part.with_suffix(".tmp")
        tmp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
        tmp.replace(f_part)
        pub_f = PARTS / f"60-akti-{year}.PUBLISH"
        if not pub_f.exists():
            pub_f.write_text("Parsed from the official Narodne novine page of each act; one version, as first published; "
                             "held back: acts a later document amends, corrects, repeals or cites as amended "
                             "(parse_acts.py).\n", encoding="utf-8", newline="\n")
        cache["parts"][str(year)] = fp
        cache.setdefault("part_code", {})[str(year)] = whole
        written.append((f_part.name, len(rows)))
    cf = PARTS / "00-country.json"
    body = json.dumps({"country": country, "acts": []}, ensure_ascii=False, indent=1) + "\n"
    if not cf.exists() or cf.read_text(encoding="utf-8") != body:
        tmp = cf.with_suffix(".tmp")
        tmp.write_text(body, encoding="utf-8", newline="\n")
        tmp.replace(cf)
    if not (PARTS / "00-country.PUBLISH").exists():
        (PARTS / "00-country.PUBLISH").write_text("Country block only (no acts).\n", encoding="utf-8", newline="\n")
    if a.cache:
        tmp = Path(a.cache + ".tmp")
        tmp.write_bytes(gzip.compress(json.dumps(cache, ensure_ascii=False).encode("utf-8"), 3))
        tmp.replace(a.cache)
    if a.report:
        Path(a.report).write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in holds), encoding="utf-8")
    reasons = defaultdict(int)
    for x in holds:
        reasons[x["reason"].split(":")[0]] += 1
    print(json.dumps({"documents": len(index), "pages": len(files), "frontier": frontier, "amender_frontier": am_frontier, "frontier_mode": a.frontier,
                      "published": sum(n for _, n in written), "held": len(holds), "held_by_reason": dict(reasons),
                      "skipped": dict(skipped), "parts": len(written)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
