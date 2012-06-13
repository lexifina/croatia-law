PRILOG 1
POPIS RAČUNA PRORAČUNA
Naziv županije/grada/općine
Broj računa
Račun po IBAN konstrukciji
Oznaka grada/ općine
Mjerodavna ispostava Porezne uprave
I. ZAGREBAČKA ŽUPANIJA
(sjedište u Zagrebu)
VELIKA GORICA
2390001-1854100005
HR9523900011854100005
541
VELIKA GORICA
II. KRAPINSKO-ZAGORSKA ŽUPANIJA
(sjedište u Krapini)
KRAPINSKE TOPLICE
2360000-1821200008
HR9723600001821200008
212
ZABOK
IV. KARLOVAČKA ŽUPANIJA
(sjedište u Karlovcu)
TOUNJ
2500009-1855700003
HR3125000091855700003
557
OGULIN
VI. KOPRIVNIČKO-KRIŽEVAČKA ŽUPANIJA
(sjedište u Koprivnici)
MOLVE
2412009 -1827000007
HR4124120091827000007
270
ĐURĐEVAC
XIV. OSJEČKO-BARANJSKA ŽUPANIJA
(sjedište u Osijeku)
OSJEČKO-BARANJSKA
ŽUPANIJA
2360000-1800014000
HR2423600001800014000
312
XVI. VUKOVARSKO-SRIJEMSKA ŽUPANIJA
(sjedište u Vukovaru)
TORDINCI
2402006-1845800000
HR3424020061845800000
458
VINKOVCI
PRILOG 4
POPIS DOPUŠTENIH MODELA ZA ZAJEDNIČKE PRIHODE PRORAČUNA I DRUGE PRIHODE ZA FINANCIRANJE JAVNIH POTREBA
A. ZAJEDNIČKI PRIHODI PRORAČUNA
2. ZAJEDNIČKI PRIHODI DRŽAVNOG, GRADSKIH I OPĆINSKIH PRORAČUNA
Račun/naziv računa
Model
05
67
1001005-17...2895K
HRxx100100517...2895K Naknada za zahvaćanje vode za javnu vodoopskrbu
05
67
PRILOG 5
OPIS FORMATA »MAGNETNI IZVADAK«
Datoteka PVBDIggmmddxxxxx.BNK obvezno sadrži sljedeće vrste sloga:
Tip sloga »900« - koji sadrži - SLOG PAKETA - »LABELU«
Tip sloga »903« - koji sadrži - VODEĆI SLOG GRUPE PODATAKA
Tip sloga »905« - koji sadrži - SLOG POJEDINAČNE TRANSAKCIJE
Tip sloga »907« - koji sadrži - ZAKLJUČNI SLOG GRUPE PODATAKA
Tip sloga »909« - koji sadrži - ZAKLJUČNI SLOG PAKETA
Tip sloga »999« - koji sadrži - ZAKLJUČNI SLOG DATOTEKE
1. SLOG PAKETA - »LABELA« - TIP SLOGA = 900
Opisuje paket i pojavljuje se jednom na početku magnetnog nositelja podataka.
SADRŽAJ I STRUKTURA SLOGA TIPA »900«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj BYTES
1.
IZ900DVBDIPOS
VBDI - pošiljatelja (banka)
M
N
1
7
7
7
2.
IZ900NAZBAN
Naziv banke
M
C
8
57
50
50
3.
IZ9000OIBBNK
OIB banke
M
N
58
68
11
11
4.
IZ900IMEDAT
Izraz imena datoteke bez oznake ekstenzije
M
C
69
86
18
18
5.
IZ900VBDIPRIM
VBDI primatelja (FINA) = 7777779
M
N
87
93
7
7
6.
IZ900BRPAK
Redni broj paketa
M
N
94
98
5
5
7.
IZ900TKS
Oznaka kodne stranice
M
N
99
102
4
4
8.
IZ900DATUM
Datum obrade - tekući datum (GGGGMMDD)
M
C
103
110
8
8
9.
IZ900VRIZ
Vrsta izvatka
M
N
111
113
3
3
10.
IZ900REZ1
Rezerva
O
C
114
988
875
875
11.
IZ900LOKGRE
Lokacija greške
M
C
989
995
7
7
12.
IZ900SIFGRES
Šifra greške
M
C
996
997
2
2
13.
IZ900TIPSL
Tip sloga - oznaka 900
M
C
998
1000
3
3
2. VODEĆI SLOG GRUPE PODATAKA - TIP SLOGA = 903
Podaci koji određuju grupu su:
- račun imatelja računa - transakcijski račun za koji se formira izvadak,
- datum izvršenog plaćanja,
- broj izvatka,
- podbroj izvatka - vrijednost podbroja izvatka predstavlja redni broj unutar rednog broja izvatka i
- valuta transakcijskog računa.
Vodeći slog grupe podataka, zajedno sa slogovima pojedinačnih transakcija (naloga) i zaključnim slogom grupe podataka čine »logičku cjelinu«, tj. Izvadak na magnetnom nositelju podataka.
Kontrola ispravnosti prijenosa odnosno prijema na razini paketa za cijelu grupu obavlja se preko podatka »redni broj grupe u paketu«. Za svaku sljedeću »grupu« ovaj podatak se mijenja s inkrementom »1«. Ako dođe do razlike, datoteka ne prolazi formalnu kontrolu.
SADRŽAJ I STRUKTURA SLOGA TIPA »903«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj bytes
1.
IZ903VBDI
Vodeći broj banke
M
N
1
7
7
7
2.
IZ903BIC
BIC - Identifikacijska šifra banke
O
C
8
18
11
11
3.
IZ903RACUN
Račun klijenta
M
C
19
39
21
21
(npr: HR5523600001100012345 ili 23600001100000001)
4.
IZ903VLRN
Valuta transakcijskog računa
M
C
40
42
3
3
5.
IZ903NAZKLI
Naziv klijenta
M
C
43
112
70
70
6.
IZ903SJEDKLI
Sjedište klijenta
M
C
113
147
35
35
7.
IZ903MB
Matični broj
O
N
148
155
8
8
8.
IZ903OIBKLI
OIB klijenta
O
N
156
166
11
11
9.
IZ903RBIZV
Redni broj izvatka
M
N
167
169
3
3
10.
IZ903PODBROJ
Podbroj izvatka
O
N
170
172
3
3
11.
IZ903DATUM
Datum izvatka (GGGGMMDD)
M
C
173
180
8
8
12.
IZ903DATIZVR
Datum izvršenja (GGGGMMDD)
O
C
181
188
8
8
13.
IZ903BRGRU
Redni broj grupe u paketu
M
N
189
193
5
5
14.
IZ903POSLFINA
Poslovnica izdavanja izvatka
O
N
194
198
5
5
15.
IZ903DINIZV
Dinamika izdavanja izvadaka
M
C
199
199
1
1
16.
IZ903NACIN
Način izdavanja izvatka
O
C
200
200
1
1
17
IZO903FORIZV
Format izdavanja izvadaka
M
N
201
201
1
1
18.
IZ903VRIZ
Vrsta izvatka
M
N
202
204
3
3
19.
IZ903REZ1
Rezerva
O
C
205
979
775
775
20.
IZ903SIFGRE1
FINA upisuje pokazatelj na obavezno polje iz sloga tipa 905 ili sumarno polje iz sloga tipa 907 koje nije popunjeno u inicijalnoj datoteci
M
N
980
987
8
8
21.
IZ903LOKGRE
Lokacija greške
M
N
988
994
7
7
22.
IZ903SIFGRES2
Ostale greške na izvatku
M
C
995
997
3
3
23.
IZ903TIPSL
Tip sloga - oznaka 903
M
C
998
1000
3
3
3. SLOG POJEDINAČNE TRANSAKCIJE - TIP SLOGA = 905
Pojedinačnom (izvršenom) transakcijom označava se svaki prijenos novčanih sredstava (izvršenjem naloga za plaćanje) »na teret«, odnosno »u korist« računa proračuna.
SADRŽAJ I STRUKTURA SLOGA TIPA »905«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj bytes
1.
IZ905OZTRA
Oznaka transakcije
M
N
1
2
2
2
2.
IZ905RNPRPL
Račun primatelja - platitelja (npr: HR5523600001100012345 ili 23600001100000002)
O
C
3
36
34
34
3.
IZ905NAZPRPL
Naziv primatelja - platitelja
O
C
37
106
70
70
4.
IZ905ADRPRPL
Adresa primatelja - platitelja
O
C
107
141
35
35
5.
IZ905SJPRPL
Sjedište primatelja - platitelja
O
C
142
176
35
35
6.
IZ905DATVAL
Datum valute (GGGGMMDD)
M
C
177
184
8
8
7.
IZ905DATIZVR
Datum izvršenja (GGGGMMDD)
M
C
185
192
8
8
8.
IZ905VLPL
Valuta pokrića
O
C
193
195
3
3
9.
IZ905TECAJ
Tečaj/koeficijent
O
N
196
210
15
15
10.
IZ905IZNPRIJEPRER
Iznos u valuti pokrića
O
N
211
225
15
15
11.
IZ905IZNOS
Iznos
M
N
226
240
15
15
12.
IZ905MODPL
Model platitelja
O
C
241
244
4
4
13.
IZ905PNBPL
Poziv na broj platitelja
O
C
245
266
22
22
14.
IZ905MODPR
Model primatelja
O
C
267
270
4
4
15.
IZ905PNBPR
Poziv na broj primatelja
O
C
271
292
22
22
16.
IZ905SIFNAM
Šifra namjene
O
C
293
296
4
4
17.
IZ905OPISPL
Opis plaćanja
O
C
297
436
140
140
18.
IZ905VBDI
Vodeći broj depozitne institucije primatelja/platitelja
M
N
437
443
7
7
19.
IZ905TIPPREK
Oznaka tipa broja za reklamaciju: 1 - za transakcije inicirane u FINI 2 - za transakcije inicirane izvan FINE
M
C
444
444
1
1
20.
IZ905REKLA
Broj za reklamaciju
M
C
445
476
32
32
21.
IZ5VRPRIH
Vrsta prihvata
O
N
477
479
3
3
22.
IZ5IZVDOK
Izvor dokumenta
O
N
480
482
3
3
23.
IZ905REZ1
Rezerva
O
C
483
997
515
515
24.
IZ905TIPSL
Tip sloga - oznaka 905
M
C
998
1000
3
3
4. ZAKLJUČNI SLOG GRUPE PODATAKA - TIP SLOGA = 907
Slijedi pojedinačne slogove (stavke) unutar grupe podataka. Koristi se za potvrdu pripadnosti pojedinačnih slogova (stavaka), određenoj grupi podataka, te za kontrolu potpunosti prijenosa podataka iz grupe.
U sebi nosi kumulativne podatke za izvršene pojedinačne transakcije. Kumulira se podatak »iznos« iz pojedinačnih slogova (stavaka), prema oznaci vrste transakcije.
SADRŽAJ I STRUKTURA SLOGA TIPA »907«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj bytes
1.
IZ907RACUN
Račun klijenta (npr: HR5523600001100012345 ili 23600001100000002)
M
C
1
21
21
21
2.
IZ907VLRN
Valuta računa
M
C
22
24
3
3
3.
IZ907NAZIV
Naziv klijenta
M
C
25
94
70
70
4.
IZ907RBIZV
Redni broj Izvatka
M
N
95
97
3
3
5.
IZ907PRRBIZV
Redni broj prethodnog izvatka
O
N
98
100
3
3
6.
IZ907DATUM
Datum izvatka (GGGGMMDD)
M
C
101
108
8
8
7.
IZ907DATPRSAL
Datum prethodnog salda (GGGGMMDD)
O
C
109
116
8
8
8.
IZ907PPPOS
Predznak prethodnog salda
M
C
117
117
1
1
9.
IZ907PRSAL
Prethodni saldo
M
N
118
132
15
15
10.
IZ907PREZER
Predznak rezervacije
O
C
133
133
1
1
11.
IZ907IZNREZ
Iznos rezervacije
O
N
134
148
15
15
12.
IZ907DATOKV
Datum dozvoljenog prekoračenja (GGGGMMDD)
O
C
149
156
8
8
13.
IZ907IZNOKV
Dozvoljeno prekoračenje (okvirni kredit)
O
N
157
171
15
15
14.
IZ907IZNZAPSR
Iznos zapljenjenih sredstava
O
N
172
186
15
15
15.
IZ907PRASPSTA
Predznak raspoloživog stanja
O
C
187
187
1
1
16.
IZ907IZNRASP
Iznos raspoloživog stanja
O
N
188
202
15
15
17.
IZ907KDUGU
Ukupni dugovni promet
M
N
203
217
15
15
18.
IZ907KPOTR
Ukupni potražni promet
M
N
218
232
15
15
19.
IZ907PRNOS
Predznak novog salda
M
C
233
233
1
1
20.
IZ907KOSAL
Novi saldo
M
N
234
248
15
15
21.
IZ907BRGRU
Redni broj grupe u paketu
M
N
249
253
5
5
22.
IZ907BRSTA
Broj stavaka u grupi
M
N
254
259
6
6
23.
IZ907TEKST
Tekstualna poruka
O
C
260
679
420
420
24.
IZ907REZ
Rezerva
O
C
680
997
318
318
25.
IZ907TIPSL
Tip sloga - oznaka 907
M
C
998
1000
3
3
5. ZAKLJUČNI SLOG PAKETA - TIP SLOGA = 909
Određuje kraj formata (PAKETA) i javlja se jednom na kraju magnetnog nositelja podataka.
SADRŽAJ I STRUKTURA SLOGA TIPA »909«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj bytes
01.
IZ909IMEDAT
Izraz imena datoteke bez oznake ekstenzije
M
C
1
18
18
18
02.
IZ909NAZBAN
Naziv banke
M
C
19
68
50
50
03.
IZ909DATUM
Datum obrade - tekući datum (GGGGMMDD)
M
C
69
76
8
8
04.
IZ909UKGRU
Ukupan broj grupa (tip sloga 903)
M
N
77
81
5
5
05.
IZ909UKSTAV
Ukupan broj stavaka (tip sloga 905)
M
N
82
87
6
6
06.
IZ909REZ
Rezerva
O
C
88
997
910
910
07.
IZ909TIPSL
Tip sloga - oznaka 909
M
C
998
1000
3
3
6. ZAKLJUČNI SLOG DATOTEKE - TIP SLOGA = 999
Nakon zaključnog sloga tipa »909« nalazi se slog tipa »999«.
Iza toga sloga je MS-DOS EOF.
SADRŽAJ I STRUKTURA SLOGA TIPA »999«
Redni broj
Naziv polja
Opis polja
M/O
Tip
od
do
Broj mjesta
Broj bytes
01.
IZ999REZ1
Rezervirana mjesta
O
C
1
997
997
997
02.
IZ999TIPSL
Tip sloga - oznaka 999
M
C
998
1000
3
3
| 65 13.06.2012 Naredba o izmjeni i dopuni Naredbe o načinu uplaćivanja prihoda proračuna, obveznih doprinosa te prihoda za financiranje drugih javnih potreba u 2012. godini 65 13.06.2012 Naredba o izmjeni i dopuni Naredbe o načinu uplaćivanja prihoda proračuna, obveznih doprinosa te prihoda za financiranje drugih javnih potreba u 2012. godini
