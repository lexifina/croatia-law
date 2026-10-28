# How this history was made, and how to make it again

This file records how the repository was built: the sources, the commands, the software, the decisions made by hand, and
what an AI model did and did not do. The build writes it, so it describes the build that made this commit.

## Short version

```sh
git clone <this repository> && cd croatia-law
pip install lxml
python -X utf8 tools/build.py --repo ../rebuilt --today 2026-10-28
git -C ../rebuilt rev-parse main        # the same hash as this repository's main
python -X utf8 tools/check_repo.py --repo ../rebuilt     # needs tools/.cache from the build above
python -X utf8 tools/test_repo.py --repo ../rebuilt
```

`tools/build.py` needs Python 3.12 or later with `lxml`, git and curl. It reads the 12 Narodne novine pages
below (or its own cache, `.cache/` next to the script) and writes this repository into `--repo`. With the same pages and
the same `--today` it gives the same commits with the same hashes. `data/verzije.json` lists the sha256 of every page, so a
rebuild can show it read the same bytes; Narodne novine could change a page, and then the hashes change too.

## Sources

All law text comes from **Narodne novine** (narodne-novine.nn.hr), the official gazette of the Republic of Croatia
(Narodne novine d.d.), as the HTML page of each document (`/clanci/sluzbeni/<year>_<month>_<issue>_<item>.html`; the same
documents have ELI addresses, given below). Nothing was typed in, summarised or rewritten. Pages were fetched on
2026-10-28 with curl, one at a time, at most 2.5 requests a second (the "Pristup podatcima" page
asks scripts for at most three a second), with a descriptive User-Agent. robots.txt was read: none of these pages is
disallowed. Terms of use: see `LICENSE`; reuse conditions are unclear and the repository stays private.

| Issue | Document | ELI address |
| --- | --- | --- |
| NN 56/1990 | Odluka o proglašenju Ustava Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/1990/56/1091` |
| NN 56/1990 | Ustav Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/1990/56/1092` |
| NN 135/1997 | Ustavni zakon o izmjenama i dopunama Ustava Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/1997/135/1944` |
| NN 8/1998 | Ustav Republike Hrvatske (pročišćeni tekst) | `https://narodne-novine.nn.hr/eli/sluzbeni/1998/8/121` |
| NN 113/2000 | Odluka o proglašenju promjene Ustava Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/2000/113/2224` |
| NN 124/2000 | Ustav Republike Hrvatske (pročišćeni tekst) | `https://narodne-novine.nn.hr/eli/sluzbeni/2000/124/2332` |
| NN 28/2001 | Promjena Ustava Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/2001/28/487` |
| NN 41/2001 | Ustav Republike Hrvatske (pročišćeni tekst) | `https://narodne-novine.nn.hr/eli/sluzbeni/2001/41/705` |
| NN 55/2001 | Ispravak Ustava Republike Hrvatske (pročišćeni tekst) | `https://narodne-novine.nn.hr/eli/sluzbeni/2001/55/883` |
| NN 76/2010 | Promjena Ustava Republike Hrvatske | `https://narodne-novine.nn.hr/eli/sluzbeni/2010/76/2214` |
| NN 85/2010 | Ustav Republike Hrvatske (pročišćeni tekst) | `https://narodne-novine.nn.hr/eli/sluzbeni/2010/85/2422` |
| NN 5/2014 | Odluka Ustavnog suda SuP-O-1/2014 (referendum od 1. prosinca 2013.) | `https://narodne-novine.nn.hr/eli/sluzbeni/2014/5/93` |

**zakon.hr** is a private, unofficial site. Its terms forbid robots, scrapers and automated extraction, so it was not
scraped, and no text, date or amending act comes from it. Its public page for the Constitution lists the Narodne novine
issues that carry the Constitution and its changes (56/90, 135/97, 8/98, 113/00, 124/00, 28/01, 41/01, 55/01, 76/10,
85/10, 5/14); that list was used only as a pointer to which Narodne novine issues to read, and every issue was then read
from Narodne novine itself. The Constitutional Court decision NN 5/2014 no. 93 (which lists the same issues in its own
text) confirms the list. **legalize-dev** has no Croatian repository (no `legalize-hr`).

## The versions

| In force | Author | Kind | Text | Acts (NN) |
| --- | --- | --- | --- | --- |
| 1990-12-22 | NN 56/1990 | Ustav | official text | 56/1990 / text 56/1990 |
| 1997-12-15 | NN 135/1997 | Ustavni zakon | official text | 135/1997 / text 8/1998 |
| 2000-11-09 | NN 113/2000 | Promjena Ustava | official text | 113/2000 / text 124/2000 |
| 2001-03-28 | NN 28/2001 | Promjena Ustava | official text | 28/2001 / text 41/2001 |
| 2001-03-28 | NN 55/2001 (ispravak) | Ispravak | derived | 55/2001 / text 41/2001 |
| 2010-06-16 | NN 76/2010 | Promjena Ustava | official text | 76/2010 / text 85/2010 |
| 2013-07-01 | NN 76/2010 | Promjena Ustava | staged, no files | 76/2010 |
| 2013-12-01 | NN 5/2014 (referendum 2013) | Promjena Ustava (narodna ustavotvorna inicijativa) | derived | 5/2014 / text 85/2010 |

How each date was read: the in-force day is the one the act's own wording gives and the `Evidence:` trailer of each commit
quotes it. 1990-12-22: "Proglašava se i stupa na snagu Ustav". 1997-12-15: čl. 20, "stupa na snagu danom objave u
Narodnim novinama" (NN 135/1997 is dated 15 December 1997). 2000-11-09 and 2001-03-28: "stupa na snagu danom proglašenja" /
"kad ju proglasi Zastupnički dom", read with the Odluka o proglašenju of that session day (published a week or five days
later). 2010-06-16: "danom proglašenja", which the NN 85/2010 text itself dates as 16 June 2010. 2013-07-01: the
provisions the act sets to "danom pristupanja Republike Hrvatske Europskoj uniji"; the date of accession is not in any
Narodne novine page used here and comes from the Treaty of Accession (OJ L 112, 24.4.2012, art. 3(2): 1 July 2013). 2013-12-01:
the Constitutional Court's finding that the fifth change "stupila na snagu 1. prosinca 2013.". Commits are dated noon in
Zagreb on that day; the time-zone rule (CET, CEST from the last Sunday of March to the last Sunday of October, `start <= day
< end`) is written out in `build.py`. Every commit carries `In-force:`; no date is before 1970.

## What was decided by hand, and what is labelled

- **Consolidated texts.** The Constitution was not republished in full with each change; the Sabor's committee published a
  consolidated text each time (NN 8/1998, 124/2000, 41/2001, 85/2010). The version text is that consolidated text, not the
  act's own words. Differences between two consolidated texts are credited to the act whose text it is; punctuation or wording
  corrections the committee made without an act's saying so are not separated (labelled in every commit).
- **The first version** is the NN 56/1990 page of the Constitution as first published; the page is a transcription with a few
  typographical oddities (stray spaces, a hyphen), kept as published.
- **Ispravak NN 55/2001** (derived). Narodne novine published only the list of four corrections to the NN 41/2001 text. The
  build applies them to the NN 41/2001 text with a script (`apply_ispravak`) that asserts each old and new string occurs in the
  Ispravak page; the first of the two commits that day is the text as printed. The check requires every changed run of words to
  occur in the Ispravak.
- **2013 referendum change** (derived). No consolidated text exists after 2010 in Narodne novine. The build inserts the one
  sentence the Constitutional Court's decision quotes (čl. 62, new stavak 2) into the NN 85/2010 text (`apply_referendum`).
- **Provisions printed early.** The NN 85/2010 text prints, from 2010-06-16, the provisions that took effect only on 2013-07-01
  (čl. 9 st. 2 in part, 133 st. 4, 144 to 146). They stay in that commit, labelled, and the 2013-07-01 commit (no file changes)
  records when they took effect. The text before 2013-07-01 therefore includes provisions not yet in force.
- **Numbering.** Files are named by the article number of each consolidated text; numbers move when an article is added.
- **File format.** One file per article; the preamble is one file; a heading line is recognised by its numbering (a Roman or
  Arabic number and no closing punctuation); soft hyphens (U+00AD) that some pages carry inside words are removed.
- **Scope.** The Constitution only. Narodne novine's own pages give no consolidated versions with in-force dates for ordinary
  laws, and the one source that does (zakon.hr) forbids automated use, so no second act was added.

## What an AI model did

The build tools (`build.py`, `check_repo.py`, `test_repo.py`, `reproduce.py`, `ustav.py`) and the README were written by an AI
agent (Claude Sonnet 5.5, model id `claude-sonnet-5-5`, in Claude Code), who also chose the sources and read the dates from the
acts' wording. No AI model wrote any legal text, and no model runs when the repository is built. The two derived versions use
only words that appear in the official acts, and the check confirms that.

## How it was checked

1. `tools/check_repo.py` (`8 versions checked (1030 files), 0 mismatches; 7 versions word for word (69752 words) against the official pages, 0 mismatches; tools/ustav.py equal to the files on 3 of 3 days`): every version, read back from git at its tag, equals the file-by-file parse of the
   official page, and its words equal all the words of the page read independently of the parser. The two derived versions
   equal their base text except for runs of words that occur in the Ispravak or in the Constitutional Court's decision.
2. Determinism. A second build from the same cache into an empty folder gave the same history: the last law commit was `988512d6d07502df56680b17f2615ea1fa2abb50` in both, and every one of the 8 law commits and 8 tags had the same hash.
3. `tools/test_repo.py` (6 of 6 passed):
   - pass: blame names an act: ustav/clanak-062.md lines by NN 5/2014 (referendum 2013), NN 56/1990, NN 76/2010
   - pass: text before and after an amendment: ustav/clanak-062.md 2013-11-30 != 2013-12-01; ustav/clanak-007.md 2001-03-27 != 2001-03-28
   - pass: log --follow in date order: ustav/clanak-062.md 4 commits, newest first: ['2013-12-01', '2010-06-16', '1997-12-15', '1990-12-22']
   - pass: tags resolve, In-force on every law commit: 8 tags resolve; 8 law commits carry In-force
   - pass: only the documentation commit is by Lexifina: only the documentation commit 55021cdcb6 is by Lexifina; 7 distinct authors
   - pass: README commands run: 8 README commands ran and printed output

## The software

Python 3.12.10, lxml 6.1.3, git version 2.46.0.windows.1; `tools/build.py` has git blob hash `6a8705ff16084b865114b301e254fedb15fb03a0`. Authors are `NN n/yyyy` with an address ending
`@narodne-novine.invalid`; the committer is `Lexifina <croatia-law@lexifina.com>`. The documentation commit is dated 2026-10-28,
the day the pages were retrieved.
