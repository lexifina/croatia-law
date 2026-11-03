# How this repository was made (Croatia)

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-03 | Official texts; not protected by copyright (ZAPSP čl. 8) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| 4427 acts | every act, with its kind, number, status and span, is listed in [ACTS.md](ACTS.md) | 4427 | |

The build made 4427 commits:

| Commits | Kind |
| ---: | --- |
| 4427 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `buducnost`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4442 laws in the record.
- 8862 tags.

## Dates

Each commit is dated at noon (Europe/Zagreb) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Ustav Republike Hrvatske, čl. 90: zakoni i drugi propisi objavljuju se u Narodnim novinama prije stupanja na snagu; zakon stupa na snagu najranije osmoga dana od dana objave, osim ako zbog osobito opravdanih razloga zakonom nije određeno drugo. No default day is applied here: each act is dated by its own entry-into-force sentence. https://narodne-novine.nn.hr/eli/sluzbeni/2014/5/90

## How the history is built

`tools/build/build.py` (and, for later publishes, `tools/build/append.py`) turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/build/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/build/SCHEMA.md`.

- Corpus: sha256 `415def6563782ff8e6e3c43a96548975c287304738935890aa1f245c429fa921` (76941566 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6a75a05e2f381deb50fb7cb6ad297cc3fe964a71`, `check.py` `d36188b60926167ff377bd58f0b03f30cc9a1a52`, `on.py` `55bf92027127e36254521d114abde53cfefbb67d`.
- Python 3.14.0; git version 2.52.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Every act's decisions made by hand (35 in all) are listed in that act's own README.md, under "Decisions made by hand".

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- none
- none
- none
- none
- none
