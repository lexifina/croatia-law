# Croatian Constitution, change by change

The Constitution of the Republic of Croatia (Ustav Republike Hrvatske) as a git repository. Each amending act is one
commit, credited to that act and dated the day it took effect, at noon in Zagreb. The text is the official text published in
[Narodne novine](https://narodne-novine.nn.hr): the Constitution as first published (NN 56/1990) and the consolidated
texts ("pročišćeni tekst") the Sabor's Constitution Committee published after each change.

**Private. Reuse conditions are unclear** (see `LICENSE`); do not publish.

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did čl. 62 say on 1 January 2012? | `python tools/ustav.py 2012-01-01 ustav 62` |
| The whole Constitution on 1 January 2005 | `python tools/ustav.py 2005-01-01 ustav` |
| Which act wrote each paragraph of čl. 62? | `git blame ustav/clanak-062.md` |
| Every change to čl. 62, with the act and the day | `git log --follow ustav/clanak-062.md` |
| Everything one act changed | `git show --stat nn/2001-28` |
| Every change with its author and in-force day | `git log --format="%an %(trailers:key=In-force,valueonly,separator=) %s"` |
| Changes whose text is derived, not an official consolidated text | `git log --grep="Label: tekst izveden" --grep="Label: nema pročišćenog"` |
| Provisions printed before they took effect | `git log --grep="već ispisuje odredbe"` |

## The dates, and which one we use

Each act has the day it was enacted (`Enacted:`), the day it was published in Narodne novine (`Published:`) and the day it
took effect (`In-force:`). **Commits are dated the day the change took effect**, at noon in Zagreb (CET, or CEST in summer
time). The in-force day is read from the act's own wording ("stupa na snagu danom objave", "danom proglašenja", "kad ju
proglasi Zastupnički dom") and the wording is quoted in the `Evidence:` trailer. The one day the wording does not give
(the accession of Croatia to the EU) is taken from the Treaty of Accession and says so. All dates are 1970 or later.

## What "author" means

The author of a commit is the act that made the change: `NN 113/2000`, with an address ending `@narodne-novine.invalid`, so
`git blame` names the act. The committer is always `Lexifina`.

## The commits

| Day | Author | What |
| --- | --- | --- |
| 1990-12-22 | NN 56/1990 | The Constitution as proclaimed |
| 1997-12-15 | NN 135/1997 | Ustavni zakon o izmjenama i dopunama (text of the consolidated NN 8/1998) |
| 2000-11-09 | NN 113/2000 | Promjena Ustava (text of the consolidated NN 124/2000) |
| 2001-03-28 | NN 28/2001 | Promjena Ustava (text of the consolidated NN 41/2001, as printed) |
| 2001-03-28 | NN 55/2001 (ispravak) | The Ispravak of the NN 41/2001 text; derived, labelled |
| 2010-06-16 | NN 76/2010 | Promjena Ustava (text of the consolidated NN 85/2010) |
| 2013-07-01 | NN 76/2010 | Staged commencement: the EU provisions take effect; no file changes |
| 2013-12-01 | NN 5/2014 (referendum 2013) | The fifth change, by referendum: čl. 62 gets a new stavak 2; derived, labelled |

## What it does not show, and what is labelled

- **Consolidated texts, not the acts' own words.** Each version's text is the Committee's consolidated text. The act says
  "čl. 35. mijenja se i glasi"; the consolidated text is the result. A consolidated text can carry editorial corrections
  that the act does not state (punctuation, wording), and we do not separate them: every difference between two
  consecutive texts is credited to the act whose consolidated text it is, and each commit carries a `Label:` saying so.
- **Numbers move.** Articles are numbered as in each consolidated text; a change that adds an article renumbers the rest, so
  `clanak-062.md` is not always the same provision across 2000 or 2010, and `git log --follow` on a file follows a number,
  not a provision. (The Constitutional Court notes the same: what the 2013 change calls article 62 is article 61 in the
  text as proclaimed.) The 1990 page of Narodne novine is a transcription with a few typographical oddities, kept as
  published.
- **2001-03-28, the Ispravak (NN 55/2001).** The NN 41/2001 text had four misprints; the Ispravak lists them. The first
  commit of that day is the NN 41/2001 text as printed; the second applies the four corrections by a script that checks
  every word it uses against the Ispravak page. Its `In-force` is the day of the Promjena it corrects.
- **2010-06-16 and 2013-07-01.** NN 76/2010 took effect on proclamation (16 June 2010) except some provisions that take
  effect on accession to the EU. The NN 85/2010 text prints them all; they are in the 2010-06-16 commit, labelled as
  printed early, and the 2013-07-01 commit (no file changes) records the day they took effect.
- **2013-12-01.** Narodne novine published no consolidated text after the 2013 referendum, and no act: the Constitutional
  Court's decision (NN 5/2014, 93) declares the change in force on 1 December 2013, quoting the amendment. The commit is the
  NN 85/2010 text with that one sentence inserted as čl. 62 stavak 2 by a script. It is derived and labelled.
- The record ends 2013-12-01: no later change to the Constitution is known to us. The consolidated texts are
  informational; only the printed Narodne novine is authoritative.

## Files

`ustav/izvorisne-osnove.md` is the preamble; `ustav/clanak-NNN.md` is one article. The `#` line is the article number;
`##` lines above it are the part or chapter headings that open there; every other line is one paragraph (stavak), and
list items keep their dash.

## How it is checked, and built

`tools/check_repo.py` reads every version back from git on its in-force day and compares it with the official page, file by
file and word for word; `tools/test_repo.py` runs the commands above. `tools/build.py` writes the repository from the
cached official pages and gives the same hashes. [`REPRODUCE.md`](REPRODUCE.md) has every source, step, the software and
what an AI model did (it wrote the build tools; it wrote no legal text and no model runs at build time).
[`corpus.json`](corpus.json) describes the corpus for global-law.
