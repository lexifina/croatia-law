# Tools

The scripts behind this Croatia-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/croatia-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only croatia-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `redo.py` sit two folders above the scripts, next to
`config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to the folders since a move of act folders (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (both of the two here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Croatian and English, light and dark |
| `config.json` | The repository, the Croatian category names, the top-level folders that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py` | The same for Vietnamese dates, references and amounts (found by the Vietnam run); it changes nothing here, but `redo.py` runs it on every repository |
| `patch_es.py` | The same for Spanish dates and for "marco" and "escudo" read as currencies; here it takes out the name "Marco" (the Marco Polo II programme, the signatory Marco Pisa) |
| `patch_ca.py` | The same for Catalan dates and time limits, the Catalan peseta, and "sucre" (sugar) read as the Ecuadorian sucre; it changes nothing here |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder since a repository moved its act folders (`data/paths.json`), so that an act's history is not split in two at the move; `run.sh` runs it after the history is indexed. This repository has no `data/paths.json`, and it rewrote no path |
| `patch_build_r7.py` | Brings a country's `build_vulns.py` up to date: lapsed-limit reviews matched on 400 characters of context, not 80, and a file deleted before a move of folders linked under its old folder (already applied to the `build_vulns.py` here) |
| `redo.py` | Runs the patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`, `map_moved.py` among them, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as
`bash run_triage.sh '^(caselaw|ustavni-sud|izbori|sabor|data|tools|registry)/|(^|/)(README(\.en)?\.md|ACTS\.md|REPRODUCE\.md|PLAN\.md|record\.json|corpus\.json)$'`.

Changes made for this repository:

- `add_root.py` counts as law not only `Kind: law` but also `decree` (Government decrees, decisions, rules, orders and
  instructions), `as-enacted` and `Zakon` (acts as first printed), `Uredba sa zakonskom snagom`, `treaty`, `publisher`
  (versions taken from official consolidated texts) and the kinds of the Constitution's versions (`Ustav`, `Ustavni zakon`,
  `Promjena Ustava`, `Ispravak`). Without them, the history detectors, which read only rows of kind `law`, would read 3,304 of
  the 37,976 commits that change law here. Court decisions (`court`) and documentation keep their own kind.
- `build_vulns.py` counts as `other`, beside the folders in `config.json`, the repository's own notes: `README.md`,
  `README.en.md`, `ACTS.md`, `REPRODUCE.md` and `record.json`, at the root and in each act's folder.
- `build_vulns.py` gives each retroactive-date flag the path of the first text file of its act (global-law's detector
  names only the act), so that court decisions and Sabor declarations count as not law; the laws of the earlier build, all
  credited to Lexifina, get no path.
- `run.sh` takes `LE_WORKERS` and `LE_GREP_THREADS` from the environment, and was run as
  `LE_WORKERS=3 LE_GREP_THREADS=3 bash run.sh 3` on a machine shared with other runs.

The run was then repeated with `redo.py`, and twice more with `--keep-reviews`, which keeps every review already made and sends to the model only strong flags not yet reviewed. Of `patch_detectors.py`'s fixes, these change this repository's flags:

- Dates (`ingest/textscan.py`): "studenog" as well as "studenoga", numeric dates written with spaces ("do 31. 12. 2015."), "do kraja 2015. godine", "zaključno s <date>" and "do dana <date>" are now read, "listopada" is October (it is November in Polish, which came first in the month list), and "najkasnije" marks a deadline, which ranks lower among lapsed time limits and is left out of empty periods. Lapsed time limits went from 16,689 to 18,210; empty periods from 2 to 1 (a principal's licence "najkasnije do 31. prosinca 2011.").
- References (`ingest/refscan.py`): an article is now known by its file name (`clanak-128.md`) and by an article heading that follows a chapter heading at the top of its file. References to deleted provisions went from 57 to 4; the 55 that are gone, among them the four that survived the first review, cited articles this repository holds.
- Currencies (`detectors/currency_scan.py`): the Belgian franc is read, "DM" only in capitals, and "lira" only at the start of a word; dead currencies went from 9,248 to 9,252 (Belgian francs in five exchange-rate lists and a treaty and "francs" in a treaty's French text added; four "dm" decimetres, two "Francovich" and sixteen words with "lira" inside, such as "kontrolira", removed; a new false match, "bef" inside the identifiers of Supreme Court source links, added).

`ingest/refscan.py` at first gave each act to one of the parallel parts by Python's `hash()` of the act's folder, which is different in every process, so each part took its own random third of the acts: some acts were read by no part and others by two, and the three-part run found 2 of the 4 references to deleted provisions. `patch_detectors.py` now splits the acts by a fixed checksum (and `ingest/textscan.py` sorts its rows before it splits them), and the last run found the same 4 as a single-part run. Ties among the strongest flags sent to the model are now broken the same way in every run.

One limit of global-law's detectors still shows in this repository and was left as it is (see the edge cases):
`ingest/textscan.py` does not read "do zaključno <date>" (42 phrases with a past date in law texts), "do konca <year>. godine" (7) or "do kraja kalendarske <year>. godine" (1), of 15,638 such phrases.

A last run, `redo.py --full`, repeated every step with the current patches, keeping every review already made. What changed
for this repository:

- References to repealed placeholders and dead fines (`detectors/placeholder_ref.py`, `detectors/dead_fine.py`): the earlier
  `redo.py` passes did not run these two detectors again, so their last run predated the fix that reads `clanak-N` file names,
  when no file name gave an article and they found nothing. Run again, with "brisan" read only as a whole word ("brisan",
  "brisana", "brisano") not followed by "iz", they found 9 references and no dead fine (see EDGE-CASES). Two of the 9 are misread
  because the detector looks for a repeal word only in the first 70 characters of the cited article, and the cut fell inside
  "brisano iz" and "brisanju".
- Currencies (`detectors/currency_scan.py`): the Latvian "lati" and "latu" are read only as words, not inside "plati",
  "isplatu", "nadoplatu", "naplatu", "alati", "latica" or "Latinski" (197 flags); "BEF" only in capitals, not inside the
  identifiers of Supreme Court source links (9); the Spanish "marco" only in lower case, not the name "Marco" (6). Dead
  currencies went from 9,252 to 9,040. The other new currency fixes ("liraglutid", no Swiss franc, francs CFP, French "lire"
  and "sucre", the dinar left out only for French, Arabic and Serbian texts) change nothing here.
- The model reviewed 20 more lapsed time limits; one survived, a duty met in time (see EDGE-CASES). Lapsed-limit reviews are
  matched to flags on 400 characters of context (`patch_build_r7.py`); this moved no match here.
- Lapsed time limits, retroactive dates, references to deleted provisions, repeal gaps, empty periods, duplicate numbers and
  publisher notes came out the same, flag for flag.
