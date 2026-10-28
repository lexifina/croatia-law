"""Checks the git repository against the official text: every version of the Constitution, read back from git, must equal
the Narodne novine text it was made from.

    python -X utf8 scripts/croatia-law/check_repo.py [--repo ../croatia-law] [--no-record]

Offline, from the cached NN pages. Per version:
1. File by file: the files in git at the version's tag are exactly the files the build's parser makes from the page
   (same names, same bytes).
2. Word for word: all the words of the whole Constitution assembled from git (markdown marks removed) equal all the words
   of the official page after its title, read independently of the parser (every text node of the page, not the
   parser's paragraphs). For the two derived versions (the Ispravak and the 2013 referendum change) the words must equal
   the words of their base text except for the differences the Ispravak page or the Constitutional Court decision itself
   states: every changed or inserted run of words must occur in that official act.
3. The staged commit (2013-07-01) has the same tree as the commit before it.
4. tools/ustav.py run on three days prints the same text as the files at that day's tag.
The result is written to verification.json next to this script (unless --no-record), for REPRODUCE.md.
"""
import argparse
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import html as lhtml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

TOKEN = re.compile(r'\w+|[^\w\s]')
BLOCK = ('div', 'br', 'p', 'td', 'th', 'tr', 'table', 'h1', 'h2', 'h3', 'center', 'li')


def flat_words(raw: bytes, after_title: bool) -> list[str]:
    """Every word in the page's text, inline elements joining the words around them and block elements separating."""
    doc = lhtml.fromstring(raw.decode('utf-8'))
    c = doc.xpath('//div[@class="sl-content"]')[0]

    def text(e) -> str:
        if not isinstance(e.tag, str):
            return e.tail or ''
        gap = ' ' if e.tag in BLOCK else ''
        return gap + (e.text or '') + ''.join(text(x) for x in e) + gap + (e.tail or '')
    s = text(c).replace('\u00a0', ' ').replace('\u00ad', '')
    if after_title:
        m = re.search(r'U\s*S\s*T\s*A\s*V\s+REPUBLIKE\s+HRVATSKE', s)
        s = s[m.end():]
        s = re.sub(r'^\s*\(pročišćeni tekst\)', '', s)
        s = re.sub(r'^\s*\d{3,4}\b', '', s)      # the item number NN prints after the title of the 1990 page
    return TOKEN.findall(s)


def repo_words(lines: list[str]) -> list[str]:
    return TOKEN.findall(' '.join(re.sub(r'^#+ ', '', l) for l in lines))


def files_at(repo: str, rev: str) -> dict[str, str]:
    out = subprocess.run(['git', 'ls-tree', '-r', rev, f'{build.SLUG}/'], cwd=repo, capture_output=True, text=True,
                         encoding='utf-8').stdout.split('\n')
    blobs = []
    for line in out:
        if line:
            info, f = line.split('\t', 1)
            blobs.append((f.split('/', 1)[1][:-3], info.split()[2]))
    data = subprocess.run(['git', 'cat-file', '--batch'], cwd=repo, input=''.join(f'{sha}\n' for _, sha in blobs).encode(),
                          capture_output=True).stdout
    res, pos = {}, 0
    for name, _ in blobs:
        nl = data.index(b'\n', pos)
        size = int(data[pos:nl].split()[2])
        res[name] = data[nl + 1:nl + 1 + size].decode('utf-8')
        pos = nl + 1 + size + 1
    return res


def assembled(files: dict[str, str]) -> list[str]:
    def order(k):
        m = re.fullmatch(r'clanak-(\d+)', k)
        return (1, int(m.group(1))) if m else (0, 0)
    lines = []
    for k in sorted(files, key=order):
        lines += files[k].split('\n')
    return lines


def sub_sequence(small: list[str], big: list[str]) -> bool:
    n = len(small)
    return n == 0 or any(big[i:i + n] == small for i in range(len(big) - n + 1))


def fits(seg: list[str], at: int, got: list[str], big: list[str]) -> bool:
    """A changed run of words occurs in the official act, allowing the diff to have drawn the run's edges a few words
    to one side (an inserted sentence and the full stop next to it can be split either way)."""
    n = len(seg)
    return n == 0 or any(0 <= at + s and got[at + s:at + s + n] == seg and sub_sequence(got[at + s:at + s + n], big)
                         or sub_sequence(got[max(0, at + s):at + s + n], big) for s in range(-3, 4))


def derived_ok(base: list[str], got: list[str], act_words: list[str]) -> tuple[bool, str]:
    sm = difflib.SequenceMatcher(None, base, got, autojunk=False)
    notes = []
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            continue
        old, new = base[a1:a2], got[b1:b2]
        if not fits(new, b1, got, act_words) or old and not fits(old, a1, base, act_words):
            return False, f'{op} {" ".join(old)!r} -> {" ".join(new)!r} is not in the official act'
        notes.append(f'{op} {len(old)}->{len(new)} words')
    return True, '; '.join(notes)


def tool(repo: str, *args: str) -> str:
    out = subprocess.run([sys.executable, '-X', 'utf8', 'tools/ustav.py', *args], cwd=repo, capture_output=True, text=True,
                         encoding='utf-8')
    assert out.returncode == 0, out.stderr
    return out.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(HERE.parents[2] / 'croatia-law'))
    ap.add_argument('--no-record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    versions = build.versions_units(offline=True)
    bad = wbad = nfiles = nwords = 0
    prev_words = {}
    for v in versions:
        files = files_at(args.repo, v['tag'])
        if v.get('staged'):
            same = files == prev_files
            print(f'{"ok" if same else "MISMATCH"} {v["day"]} {v["tag"]}: staged commit, same files as the one before')
            bad += not same
            versions_checked = 1
            continue
        expected = {k: build.unit_text(ls).rstrip('\n') + '\n' for k, ls in v['units'].items()}
        nfiles += len(expected)
        if files != expected:
            bad += 1
            diff = sorted(set(files) ^ set(expected)) or [k for k in expected if files.get(k) != expected[k]]
            print(f'MISMATCH {v["tag"]}: {diff[:5]}')
        got = repo_words(assembled(files))
        raw = build.fetch(v['text'], offline=True)
        base = flat_words(raw, True)
        nwords += len(got)
        if v.get('derive') == 'ispravak':
            ok, note = derived_ok(base, got, flat_words(build.fetch(v['act'], offline=True), False))
        elif v.get('derive') == 'referendum':
            ok, note = derived_ok(base, got, flat_words(build.fetch(v['act'], offline=True), False))
            ins = [o for o in difflib.SequenceMatcher(None, base, got, autojunk=False).get_opcodes() if o[0] != 'equal']
            ok = ok and len(ins) == 1 and ins[0][0] == 'insert'
        else:
            ok, note = got == base, f'{len(base)} official words'
            if not ok:
                i = next((i for i, (a, b) in enumerate(zip(base, got)) if a != b), min(len(base), len(got)))
                note = f'official {len(base)} vs repo {len(got)} words; first difference at {i}: {" ".join(base[max(0, i - 5):i + 5])!r} / {" ".join(got[max(0, i - 5):i + 5])!r}'
        if not ok:
            wbad += 1
        print(f'{"ok" if ok else "WORDS MISMATCH"} {v["day"]} {v["tag"]}: {note}')
        prev_files = files
    tool_ok = 0
    for day, tag in (('1998-01-01', 'nn/1997-135'), ('2005-01-01', 'nn/2001-55'), ('2020-01-01', 'nn/2014-5')):
        printed = tool(args.repo, day, 'ustav')
        files = files_at(args.repo, tag)
        order = sorted(files, key=lambda k: (0, 0) if k == 'izvorisne-osnove' else (1, int(k.split('-')[1])))
        want = ''.join(files[k] + '\n' for k in order)
        if printed == want:
            tool_ok += 1
        else:
            bad += 1
            print(f'MISMATCH tools/ustav.py on {day} differs from the files at {tag}')
    n = len(versions)
    print(f'{n} versions checked ({nfiles} files), {bad} mismatches; {n - 1} versions word for word ({nwords} words), '
          f'{wbad} mismatches; tool on 3 days: {tool_ok} equal')
    if not args.no_record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['check'] = {'versions': n, 'files': nfiles, 'mismatches': bad, 'wordcheck': n - 1, 'words': nwords,
                        'word_mismatches': wbad, 'tool_days_equal': tool_ok}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(1 if bad or wbad else 0)


if __name__ == '__main__':
    main()
