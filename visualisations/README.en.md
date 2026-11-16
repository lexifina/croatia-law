# Croatian law in 20 charts

[Hrvatski](README.md)

Charts on every country's law, from the whole of global-law: [global-law visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations). These are the charts on Croatia alone.

Twenty charts on Croatian law, drawn only from the data in this repository: the acts of the official part of Narodne novine since 1990 (laws, Government decrees, rules, decisions and others) and their history, the Constitution with every change, international treaties, Constitutional Court decisions that repeal provisions, corrections, and official election results.

Open [`hrvatsko-pravo-u-20-grafikona.html`](hrvatsko-pravo-u-20-grafikona.html) in a browser. The page is one file with all its data inside; it loads only the d3 and topojson libraries, the maps of charts 17 and 20 and its fonts from the web. The controls at the top right switch the language (Croatian or English) and the theme (automatic, light or dark). Each chart names its data path in the repository, its record count and its limits, and has a table of every number under it. Hover over a mark for the exact values.

The charts are descriptive: they show what the sources record, not why.

## The charts

### I. Narodne novine and the law-makers

#### 1. How many acts Narodne novine prints

Acts of the official part by year and kind: 1,334 a year on average from 1991 to 2025, 9% of them laws.

![How many acts Narodne novine prints](stills/en/01.png)

#### 2. New acts and amendments

For each five-year period, how many acts only amend or supplement an existing act: 60% of laws, 39% of Government decrees, 38% of rules and 19% of decisions.

![New acts and amendments](stills/en/02.png)

#### 3. What the laws are about

Every law since 1990 by the subject read from its title, by five-year period: taxes, the budget and contributions most often (12%).

![What the laws are about](stills/en/03.png)

#### 4. The calendar of laws

Laws by month and year of publication: December and July, at the end of the Sabor's regular sessions, bring 36% of the laws; January and August 2%.

![The calendar of laws](stills/en/04.png)

#### 5. The Government amending laws by decree

Decrees by which the Government, authorised by the Sabor, amends or supplements a law: 124 since December 2000, 122 of them while the Sabor was not sitting.

![The Government amending laws by decree](stills/en/05.png)

#### 6. How long laws are

The number of articles of every new law: the median grew from 19 in the 1990s to 43 since 2020.

![How long laws are](stills/en/06.png)

### II. Entry into force, amendments and corrections

#### 7. When laws take effect

The gap between publication and entry into force: 60% of laws take effect on the eighth day after publication, the earliest the Constitution (Article 90) allows without especially justified reasons.

![When laws take effect](stills/en/07.png)

#### 8. The busiest days

The fifteen days on which the most acts took effect: 438 on 1 January 2024, most of them decisions of municipalities and cities on income tax rates.

![The busiest days](stills/en/08.png)

#### 9. The most amended laws

Amendments to the most amended laws by year: the Value Added Tax Act 28 times since 1998.

![The most amended laws](stills/en/09.png)

#### 10. How soon the first amendment comes

The share of new laws not yet amended, by years since publication (Kaplan–Meier estimate): half of the laws of the 2000s and 2010s were amended within 4.5 years.

![How soon the first amendment comes](stills/en/10.png)

#### 11. What is left of the laws

Where the new laws of each five-year period stand today: of the laws of 2005–2009, 6% are in force and never amended.

![What is left of the laws](stills/en/11.png)

#### 12. Corrections of printed text

Corrections by year and the kind of act corrected, and how late they came: 1,526 since 1990; one law in 25 needed one.

![Corrections of printed text](stills/en/12.png)

### III. The Constitution, the Constitutional Court and elections

#### 13. How the Constitution changed

Words added and deleted at each change of the Constitution: most in 2000 (+3,307 and −963), fewest by the 2013 referendum (+7).

![How the Constitution changed](stills/en/13.png)

#### 14. The Constitutional Court repeals provisions

Constitutional Court decisions that repeal or annul provisions, by year and kind of act (191 decisions, 78 on provisions of laws), and a list of the laws whose provisions the Court repealed since 2015.

![The Constitutional Court repeals provisions](stills/en/14.png)

#### 15. Turnout in elections to the Sabor

Turnout in the ten constituencies at every election since 2003: lowest in 2020 (46.0%), back to 61.4% in 2024.

![Turnout in elections to the Sabor](stills/en/15.png)

### IV. The European Union and the world

#### 16. EU law in the laws

Laws that name EU directives or regulations in their first three articles: 38% since 2014, and 58% in the accession year, 2013.

![EU law in the laws](stills/en/16.png)

#### 17. Who Croatia makes treaties with

Treaty acts by the other party, on a map and by decade: Bosnia and Herzegovina (49) and Hungary (48) most often.

![Who Croatia makes treaties with](stills/en/17.png)

### V. Money, taxes and the coast

#### 18. The minimum wage in three currencies

The minimum wage amounts set in acts of Narodne novine, converted to euros at the rates in the acts themselves: from HRD 8,170 in 1992 to EUR 1,050 in 2026.

![The minimum wage in three currencies](stills/en/18.png)

#### 19. Municipal and city income tax rates

The lower and higher rates in the decisions of municipalities and cities in force from 1 January 2024: 59% of the decisions set 20% and 30%.

![Municipal and city income tax rates](stills/en/19.png)

#### 20. The boundary of the maritime domain

Acts that fix the boundary of the maritime domain, on a map and by year: 539 since 1996, most in 2002 (126).

![The boundary of the maritime domain](stills/en/20.png)

## Data

As of commit `52dec3c296` (16 November 2026).

| Dataset | Where in the repository | Records | Coverage |
| --- | --- | ---: | --- |
| Git history | branch `main` | 86,360 commits | every act enters as one commit in its own name, with the days it was published (`Published:`) and took effect (`In-force:`); the commit date is the day it took effect |
| Acts of the official part of Narodne novine | `<kind>/<year>/<number>/` | 37,685 acts | 1990–2026; each act is as first printed, later changes are not applied to its text |
| Laws of the earlier build | `data/zakoni.json` | 747 laws | laws not also among the acts above |
| Acts held back | `data/held.json` | 9,706 acts | acts of the same kinds the repository holds back from main: they have a number and a title, but no text |
| List of acts with links | `registry/data/acts.json` | 34,219 acts | status, and the later acts that amend, repeal, replace or cite each act |
| Constitution | `ustav/` | 7 versions | consolidated texts of 1990, 1997, 2000, 2001, 2010 and 2013 |
| International treaties | `medunarodni/` | 1,175 acts | 1992–2026, the ratifying and publishing acts |
| Corrections | `data/ispravci.csv` | 1,526 | 1990–2026 |
| Constitutional Court repeals | `data/ustavni-sud-ukidanja.csv` | 225 operative points | decisions printed in Narodne novine; still being collected |
| Election results | `izbori/` | 129 | Sabor 2003–2024, President, European Parliament |
| Case law | `caselaw/` | 45,278 decisions | Constitutional Court 14,008, Supreme Court 31,270 (1990–1997); being loaded, not charted |
| Local acts | `local/` | 183 acts | a pilot: 13 units of Primorje-Gorski Kotar County; not charted |

## Limits

- **The links between acts are not complete.** Charts 10 and 11 read the amendments and status of laws from `registry/data/acts.json`; the 3,466 acts added after that list have no links yet, so they are left out.
- **Acts held back have no text.** Charts 1–4 and 9 also count the 9,706 acts held back, by their Narodne novine number and title; the charts that read the text or the day of entry into force cannot include them.
- **Categories are read from titles.** The subject of a law (chart 3), amending acts (2, 9), the other party to a treaty (17) and the acts on the minimum wage and the maritime domain boundary (18, 20) are recognised by words in titles, by the rules in `src/prep.py`; whatever no rule recognises is shown as "Other". EU law (16) is looked for only in the first three articles of a law.
- **Case law is still being loaded.** Chart 14 shows only the Constitutional Court repeals printed in Narodne novine collected so far; the rest of the case law in `caselaw/` is not charted.
- **Elections:** chart 15 shows the ten constituencies within Croatia; the XI (voters living abroad) and XII (national minorities) are not shown.
- **Minimum wage:** between 1995 and 2008 no act in the repository sets an amount; the 1994 amounts were set for income tax purposes.
- **Maritime domain:** 243 of the 539 acts give the boundary as coordinates; 242 are on the map, as the act with a misprinted zone digit is left off.
- **Partial periods** (2026 and the five-year period that includes it) are drawn lighter.

## Rebuilding

```sh
python visualisations/src/make.py            # git log + tables + texts -> src/.build/ -> hrvatsko-pravo-u-20-grafikona.html
node visualisations/src/stills.cjs           # images for these READMEs (needs Playwright; PLAYWRIGHT=<path> if not global)
```

`make.py` reads everything from git objects, so it also works in a blobless or `--no-checkout` clone: it fetches the texts the charts read (some 16,000 small files) in batches. It reads `origin/main` (or `HEAD`) by default; `--ref` picks another branch or commit. It writes nothing into the repository except the page and the `src/.build/` folder (which git ignores).

| File | What it does |
| --- | --- |
| `src/make.py` | extracts the history, the tables and the texts into `src/.build/`, then runs `prep.py` and `build.py` |
| `src/prep.py` | computes every number for the 20 charts and the data profile into `src/.build/data.json` |
| `src/page.tpl.html` | the page: text in both languages, the charts (d3), the tables |
| `src/build.py` | puts `data.json` into the template and writes the page |
| `src/stills.cjs` | draws each chart as a PNG into `stills/hr/` and `stills/en/` |

## Licence

See [`LICENSE`](../LICENSE). Narodne novine's terms of use say its content may be used only under the conditions the law prescribes and give no licence to republish it; [`registry/REPRODUCE.md`](../registry/REPRODUCE.md) relies on the Copyright Act (ZAPSP, čl. 18. st. 3.), under which official texts are not protected. `LICENSE` grants no licence for the law text, the history or the tools until that question is settled. The short quotations of legislation on the page are taken from the text in this repository, as Narodne novine prints it.
