# How this repository was made (Croatia)

This file is written by the build on 2026-11-09, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-04 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |
| Narodne novine, službeni dio (narodne-novine.nn.hr) | <https://narodne-novine.nn.hr> | 2026-11-09 | Official texts; not protected by copyright (ZAPSP čl. 8) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| 8051 acts | every act, with its kind, number, status and span, is listed in [ACTS.md](ACTS.md) | 8322 | |

The build made 11557 commits:

| Commits | Kind |
| ---: | --- |
| 11287 | first version of an act |
| 270 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `buducnost`: laws not yet in force on 2026-11-09.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 11649 laws in the record.
- 19709 tags.

## Dates

Each commit is dated at noon (Europe/Zagreb) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Ustav Republike Hrvatske, čl. 90: zakoni i drugi propisi objavljuju se u Narodnim novinama prije stupanja na snagu; zakon stupa na snagu najranije osmoga dana od dana objave, osim ako zbog osobito opravdanih razloga zakonom nije određeno drugo. No default day is applied here: each act is dated by its own entry-into-force sentence. https://narodne-novine.nn.hr/eli/sluzbeni/2014/5/90

## How the history is built

`tools/build/build.py` (and, for later publishes, `tools/build/append.py`) turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/build/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/build/SCHEMA.md`.

- Corpus: sha256 `79d09deea308c90ed969412da9ec21a6d13121fd1e2ce3ca86fc6a26946eb538` (118721756 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `ca294ab3d2553b6e8322e838325b576a0939da6b`, `check.py` `f7f9c39fff1b1f9a3aded2ad3364a27fb0908033`, `on.py` `0be88de7820b2dafe9f94fa40472a48776aa4cf5`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Every act's decisions made by hand (98 in all) are listed in that act's own README.md, under "Decisions made by hand".

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
