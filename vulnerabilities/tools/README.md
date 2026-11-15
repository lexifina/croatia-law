# Tools

The scripts behind this Croatia-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/croatia-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only croatia-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py` and `late_ext_rebut.py` sit two folders above the scripts, next to
`config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (both of the two here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Croatian and English, light and dark |
| `config.json` | The repository, the Croatian category names, the top-level folders that are not law, and the chart's labels |

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

Two limits of global-law's detectors show in this repository and were left as they are (see the edge cases):
`ingest/refscan.py` reads an article's number only from the first line of its file, which here is often a chapter heading,
and does not read Croatian file names (`clanak-128.md`); and `ingest/textscan.py` does not read "do kraja <year>. godine",
dates written with spaces, "zaključno s <date>", "studenog" or "do dana <date>".
