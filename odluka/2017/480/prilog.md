PRILOG 1.
PODATKOVNI SKUPOVI ZAHTJEVA I ODGOVORA ZA WEB I BATCH RAZMJENU PODATAKA,
IZVORI PODATAKA IZ SUSTAVA EDIP TE POPIS I OPIS UPOZORAVAJUĆIH I RESTRIKTIVNIH PORUKA
1. Podatkovni skupovi zahtjeva i odgovora za web i batch razmjenu podataka
1.1 WEB razmjena podataka
Zahtjev za dohvatom podataka iz sustava EDIP
Dohvat podataka o dohocima i primicima iz sustava EDIP vrši se prema sljedećim ulaznim podacima.
Podatkovni skup za upit:
ULAZNI PODACI
RBR. | OPIS
1 | ID poruke
2 | Šifra institucije koja traži podatke iz EDIP-a
3 | OIB korisnika sustava - institucije
4 | OIB referenta
5 | Šifra svrhe za koju se traže podaci iz sustava EDIP
6 | OIB obveznika za kojega se traže podaci iz sustava EDIP
7
Indikator razdoblja za koji se traže podaci iz sustava EDIP
»1« - ako se traže podaci za godinu
»2« - ako se traže podaci za mjesec
»3« - ako se traže podaci za razdoblje od tri mjeseca
8 | Početak razdoblja za koje se traže podaci
9 | Kraj razdoblja za koje se traže podaci
Odgovor na zahtjev za dohvatom podataka iz sustava EDIP
Podatkovni skup za odgovor:
ODGOVOR
1 | Prezime
2 | Ime
3 | Adresa prebivališta/boravišta
4 | Šifre upozoravajućih sistemskih poruka
5 | Opisi upozoravajućih sistemskih poruka
6 | Dohodak od nesamostalnog rada
7 | Porez i prirez na dohodak od nesamostalnog rada
8 | Dohodak od nesamostalnog rada - plaća
9 | Porez i prirez na dohodak od nesamostalnog rada - plaća
10 | Dohodak od nesamostalnog rada - mirovina
11 | Porez i prirez na dohodak od nesamostalnog rada - mirovina
12 | Dohodak od samostalne djelatnosti
13 | Porez i prirez na dohodak od samostalne djelatnosti
14 | Dohodak od kapitala
15 | Porez i prirez na dohodak od kapitala
16 | Dohodak od imovine i imovinskih prava
17 | Porez i prirez na dohodak od imovine i imovinskih prava
18 | Dohodak od osiguranja
19 | Porez i prirez na dohodak od osiguranja
20 | Drugi dohodak
21 | Porez i prirez na drugi dohodak
22 | Inozemni dohodak
23 | Porez i prirez na inozemni dohodak
24 | Povrat/uplata poreza i prireza po godišnjoj prijavi
25 | Ukupni dohodak
26 | Ukupni porez i prirez
27 | Šifra neoporezivog primitka
28 | Iznos neoporezivog primitka
29 | Opis neoporezivog primitka
30 | Ukupno neoporezivi primici
31 | Neoporezivi dohodak iz aplikacije Imovina-otuđenje - dohodak koji je oslobođen plaćanja poreza
1.2 Batch razmjena podataka
Opis, sadržaj i struktura datoteke
Struktura datoteke sastoji se od sljedećih tipova slogova:
• Tip sloga »0« - početni slog
• Tip sloga »1« - slog za podatke iz sustava EDIP
• Tip sloga »9« - završni slog
Svi slogovi su duljine 2000 znakova.
Sva polja tipa N (numeric) poravnavaju se desno i upisuju s vodećim nulama i sa predznakom ispred. Sva polja tipa C (character) poravnavaju se lijevo. Ako pravila za popunjavanje ne zahtijevaju popunjenost nekih polja, takva polja se popunjavaju s prazninama (blankovima). Obvezni podaci u opisu sloga označeni su sa M (Mandatory), dok su neobavezni označeni sa O (Optional).
Svaki redak u datoteci treba zaključiti s kodnom sekvencom Hex(0D)+Hex(0A)=Cr+Lf.
Zapis se treba ostvariti u kodnoj stranici CP = 1250. Za obradni sustav ovo je predodređena kodna stranica kojom se osigurava ispravno interpretiranje svih znakova tijekom faza obrade i u izvještajima.
IMENA DATOTEKA
Ulazna datoteka (dostavlja korisnik): EDIPŠifraKorisnikaŠifraSvrheGGGGMMDDRedniBrojDatoteke.txt
Primjer: EDIPKS122S00820160118001.txt
Izlazna datoteka (dostavlja APIS-IT): EDIPAPISŠifraKorisnikaŠifraSvrheGGGGMMDDRedniBrojDatoteke.txt
Primjer: EDIPAPISK1225S00820160118001.txt
Ulazna datoteka
POČETNI SLOG - TIP SLOGA »0«
Ovaj slog pojavljuje se samo jednom u datoteci i to isključivo kao prvi slog.
POČETNI SLOG - TIP SLOGA »0«
RBR. | PODATAK | OPIS
1 | Tip sloga | »0«
2 | Indikator razdoblja | Indikator razdoblja za koji se traži potvrda »1« - godina, »2« - mjesec, »3« - kvartal
3 | Datum OD | Početak razdoblja za koje se traže podaci
4 | Datum DO | Kraj razdoblja za koje se traže podaci
5 | Šifra korisnika | xxxxx
6 | OIB korisnika | OIB korisnika
7 | Aplikacija | xxxx
8 | Šifra svrhe | xxx - xxxxxxx
9 | Datum zahtjeva
Datum kada je datoteka upućena na obradu
DD.MM.YYYY
10 | Redni broj | Redni broj datoteke poslane u istom danu
SLOG ZA PODATKE IZ SUSTAVA EDIP - TIP SLOGA »1«
Ovaj slog sadrži podatke OIB-ove obveznika za koje se traže podaci.
SLOG ZA PODATKE IZ SUSTAVA EDIP - TIP SLOGA »1«
RBR | PODATAK | OPIS
1 | Tip sloga | »1«
2 | OIB | OIB obveznika
ZAVRŠNI SLOG - TIP SLOGA »9«
Ovaj slog sadrži ukupan broj OIB-ova za koje se traže podaci, broj svih ponavljanja sloga tip »1«.
SLOG ZA PODATKE IZ SUSTAVA EDIP - TIP SLOGA »9«
RBR | PODATAK | OPIS
1 | Tip sloga | »9«
2 | Fiksni tekst | »UKUPAN BROJ OIB-ova:«
3 | Ukupno obveznika | Broj OIB-a u datoteci
Izlazna datoteka
POČETNI SLOG - TIP SLOGA »0«
Ovaj slog pojavljuje se samo jednom u datoteci i to isključivo kao prvi slog.
POČETNI SLOG - TIP SLOGA »0«
RBR | PODATAK | OPIS
1 | Tip sloga | »0«
2 | Indikator razdoblja | Indikator razdoblja za koji se traži potvrda »1« - godina, »2« - mjesec, »3« - kvartal
3 | Datum OD | Početak razdoblja za koje se traže podaci
4 | Datum DO | Kraj razdoblja za koje se traže podaci
5 | Šifra korisnika | xxxxx
6 | OIB korisnika | OIB korisnika
7 | Aplikacija | ‘xxxxx
8 | Šifra svrhe | xxxxx - xxxxxxxxxxxxx
9 | Datum zahtjeva
Datum kada je datoteka upućena na obradu
DD.MM.YYYY
10 | Redni broj | Redni broj datoteke poslane u istom danu
SLOG ZA PODATKE IZ SUSTAVA EDIP - TIP SLOGA »1«
Ovaj slog sadrži podatke OIB-ove obveznika za koje se traže podaci.
SLOG ZA PODATKE IZ EDIP SUSTAVA - TIP SLOGA »1«
RBR | PODATAK | OPIS
1 | Tip sloga | »1«
2 | OIB | OIB obveznika
3 | NES_DOH | Dohodak od nesamostalnog rada - ukupno
4 | NES_PIP | Porez i prirez na dohodak od nesamostalnog rada - ukupno
5 | NES_PLA_DOH | Dohodak od nesamostalnog rada - plaća
6 | NES_PLA_PIP | Porez i prirez na dohodak od nesamostalnog rada - plaća
7 | NES_MIR_DOH | Dohodak od nesamostalnog rada - mirovina
8 | NES_MIR_PIP | Porez i prirez na dohodak od nesamostalnog rada - mirovina
9 | SAM_DOH | Dohodak od samostalne djelatnosti
10 | SAM_PIP | Porez i prirez na dohodak od samostalne djelatnosti
11 | KAP_DOH | Dohodak od kapitala
12 | KAP_PIP | Porez i prirez na dohodak od kapitala
13 | IMO_DOH | Dohodak od imovine i imovinskih prava
14 | IMO_PIP | Porez i prirez na dohodak od imovine i imovinskih prava
15 | OSI_DOH | Dohodak od osiguranja
16 | OSI_PIP | Porez i prirez na dohodak od osiguranja
17 | DRU_DOH | Drugi dohodak
18 | DRU_PIP | Porez i prirez na drugi dohodak
19 | INO_DOH | Inozemni dohodak
20 | INO_PIP | Porez i prirez na inozemni dohodak
21 | GPDOH_PIP | Povrat/uplata poreza i prireza po godišnjoj prijavi
22 | UKU_DOH | Ukupni dohodak
23 | UKU_PIP | Ukupni porez i prirez
24 | Blok od sljedeća dva podatka ponavlja se 60 puta
a | SIF_NOP_PRM | Šifra neoporezivog primitka
b | NOP_PRM | Iznos neoporezivog primitka
25 | UKU_NOP_PRM_JOPPD | Ukupno neoporezivi primici
26 | NOP_PRM_IMOOT | Neoporezivi dohodak iz aplikacije IMOOT(otuđenje imovine) - primitak koji je oslobođen plaćanja poreza
27 | Prezime | Prezime
28 | Ime | Ime
29 | Adresa prebivališta/boravišta | Adresa prebivališta/boravišta
30 | Opis svrhe | Opis svrhe
31 | Šifre restriktivnih sistemskih poruka(10) | Šifra restriktivne sistemske poruke
32 | Šifre upozoravajućih sistemskih poruka(20) | Šifra upozoravajuće sistemske poruke
ZAVRŠNI SLOG - TIP SLOGA »9«
Ovaj slog sadrži ukupan broj OIB-ova za koje se traže podaci, broj svih ponavljanja sloga tip »1«.
SLOG ZA PODATKE IZ EDIP SUSTAVA - TIP SLOGA »9«
RBR | PODATAK | OPIS
1 | Tip sloga | »9«
2 | Fiksni tekst | »UKUPAN BROJ OBRAĐENIH OIB-ova:«
3 | Ukupno obveznika | Broj OIB-a u datoteci
2. Izvori podataka za sustava EDIP
→ JOPPD obrasci podneseni u razdoblju za koje se podaci daju
→ godišnja prijava poreza na dohodak
→ rješenja o paušalnom utvrđivanju poreza na dohodak od samostalne djelatnosti,
→ rješenja o najmu ili zakupu pokretnina i nekretnina,
→ rješenja o paušalnom utvrđivanju por. na doh. ostvarenom obavljanjem djelat. iznajmlj. stanova, soba i postelja putnicima i turistima te organiziranja kampova
→ rješenja od otuđenja imovine
→ obrazac EPOM
→ aplikacija ino-mirovina
→ knjigovodstvena kartica.
3. Popis i opis upozoravajućih i restriktivnih poruka
Popis poruka u slučaju kada nisu dobiveni podaci iz EDIP sustava
ŠIFRA PORUKE | OPIS PORUKE
WS001
NISTE OVLAŠTENI ZA KORIŠTENJE SUSTAVA
Poruka se daje u slučaju kada korisnik nema potrebne dozvole unesene u autentikacijskom sustavu Porezne uprave.
WS002
VALIDACIJSKE GREŠKE + OPIS NA ENGLESKOM - max 210 znakova
Poruka se daje u slučaju kada xml poruka nije ispravna po shemi, javlja se ova greška sa opisom validacijskih pogrešaka.
WS003
NEISPRAVNO RAZDOBLJE
Poruka se daje kada se upiše razdoblje koje nije protokolom predviđeno ili kada ne odgovara indikatoru razdoblja.
WS004
ŠIFRA INSTITUCIJE NE ODGOVARA POŠILJATELJU
Poruka se daje u slučaju kada OIB iz aplikativnog certifikata ne odgovara upisanoj šifri institucije u xml poruci.
WS005
NEISPRAVAN DIGITALNI POTPIS
Poruka se daje u slučaju kada kontrola izračuna digitalnog potpisa, kontrola na poziciju unutar xml i kontrola da li je taj certfikat s kojim je potpisano nije na listi dozvoljenih certifikata.
WS006
APLIKATIVANI CERTIFIKAT NE ODGOVARA TLS CERTIFIKATU
Poruka se daje u slučaju kada OIB iz aplikativnog certifikata nije isti OIB-u iz poslužiteljskog certifikata.
WS011
NEISPRAVNO RAZDOBLJE
Poruka se daje kada se upiše razdoblje koje nije protokolom predviđeno ili kada ne odgovara indikatoru razdoblja.
WS999
SISTEMSKA POGREŠKA. KONTAKTIRAJTE HELP DESK
Poruka se daje u slučaju kada se pojavi nepredviđena pogreška.
WS012
NEISPRAVAN OIB OBVEZNIKA
Poruka se daje kada OIB za koji se traže podaci nije formalno ispravan.
RP002
KORISNIK NEMA OVLAŠTENJA ZA TRAŽENU SVRHU
Poruka se daje kada korisnik traži podatke za svrhu, koja nije predviđena Protokolom koji je potpisao.
RP003
NEISPRAVNO RAZDOBLJE
Poruka se daje kada se podaci traže za razdoblje koje nije protokolom predviđeno ili kada ne odgovara indikatoru razdoblja (samo za batch razmjenu).
RP004
NEISPRAVAN ILI NEPOSTOJEĆI OIB OBVEZNIKA
Poruka se daje u slučaju kada OIB za koji se traže podaci nije formalno ispravan ili kada nije u OIB sustavu.
RP005
PONIŠTEN OIB OBVEZNIKA
Poruka se daje u slučaju kada je OIB za koji se traže podaci poništen.
RP006
OIB POZIVATELJA NIJE AKTIVAN OIB FIZIČKE OSOBE
Poruka se daje kada OIB zaposlenika institucije koji pristupa podacima, nije OIB fizičke osobe ili nije aktivan OIB.
RP007
OIB ZA KOJI TRAŽITE PODATKE NEMA PREBIVALIŠTE/BORAVIŠTE NA PODRUČJU VAŠE JEDINICE.
UKOLIKO ŽELITE PRISTUPITI PODACIMA PONOVITE UPIT
Poruka se daje kada se EDIP-u pristupa preko web servisa, i to ukoliko je korisnik iz domene JLPRS, a obveznik nema prebivalište/boravište na području te jedinice. U slučaju da korisnik ipak odluči zatražiti podatke, EDIP sustav očekuje ponovljeni upit u sljedećih pet minuta.
RP008
OIB KORISNIKA SUSTAVA NIJE AKTIVAN
Poruka se daje kada se OIB kojim se Korisnik predstavio EDIP sustavu, nije u OIB sustavu u statusu aktivan.
RP009
OIB KORISNIKA SUSTAVA NE ODGOVARA OIB-u RANIJE UNESENOM U SUSTAV
Poruka se daje kada se EDIP-u pristupa preko web servisa ili batch aplikacije, a OIB kojim se Korisnik predstavio nije isti kao OIB koji je zabilježen u sustavu.
RP010
POTVRDA SE MOŽE IZDATI SAMO FIZIČKOJ OSOBI
Poruka se daje kada se podaci traže za OIB koji ne pripada fizičkoj osobi.
Napomena: Poruke koje imaju početna slova »WS« pojavljuju se samo u web aplikaciji
Popis upozoravajućih poruka
ŠIFRA PORUKE | TEKST PORUKE/ Opis poruke
UP001
DOHODAK I NEOPOREZIVI PRIMICI NISU EVIDENTIRANI OD STRANE POREZNE UPRAVE
Ova poruka se daje u slučaju kada za obveznika ne postoje podaci u mjesecu ili za razdoblje za koje se potvrda traži.
UP002
PODACI SE TEMELJE NA GODIŠNJOJ PRIJAVI DOHOTKA KOJA NIJE VERIFICIRANA
Poruka se daje kada se izdaje potvrda o visini dohotka na temelju unesene i neverificirane godišnje prijave poreza na dohodak.
UP003
NEOPOREZIVI PRIMICI SU ISKAZANI IZ JOPPD OBRAZACA PODNESENIH U RAZDOBLJU ZA KOJE SE POTVRDA TRAŽI, A MOGU SE ODNOSITI I NA PRIMITKE ISPLAĆENE U PRETHODNIM RAZDOBLJIMA
Poruka se daje u slučaju postojanja neoporezivih primitaka za šifre iz priloga 4. JOPPD obrasca, a koje se prema zadanim pravilima iskazuju na potvrdi o visini dohodaka i primitaka.
UP004
OBVEZNIK OSTVARUJE DOHODAK OD IMOVINE, IZNOS DOHOTKA UTVRDITI S NADLEŽNOM ISPOSTAVOM
Poruka se daje u slučaju kad porezni obveznik ima evidentirana stanja na šifri računa 1511 (PREDUJAM POREZA I PRIREZA NA DOHODAK OD IZNAJMLJ.STANOVA, SOBA I POSTELJA) ili 1503 (PREDUJAM POREZA I PRIREZA NA DOHODAK OD NAJAMNINE I ZAKUPNINE PO RJEŠENJU PU), a nema sistemski izdanog rješenja.
UP006
OBVEZNIK OBAVLJA SAMOSTALNU DJELATNOST. PODACI O DOHOTKU MOGU SE DOBITI UVIDOM/IZDAVANJE POTVRDE ZA PRETHODNU KALENDARSKU GODINU
Poruka se ispisuje u slučaju kada obveznik ima u Registru poreznih obveznika oznaku obveze dohotka od djelatnosti - poslovne knjige/paušal ili dohotka od imovine - poslovne knjige važeću u prethodnoj godini i koja važi u razdoblju godine za koje se potvrda izdaje, a potvrda se izdaje za mjesec ili razdoblje.
UP007
OBVEZNIK JE POČEO OBAVLJATI SAMOSTALNU DJELATNOST U GODINI ZA KOJU SE POTVRDA IZDAJE
Poruka se ispisuje u slučaju kada obveznik ima u Registru poreznih obveznika oznaku obveze dohotka od djelatnosti - poslovne knjige/paušal ili dohotka od imovine - poslovne knjige otvorenu u godini odnosno razdoblju godine za koje se potvrda izdaje, a potvrda se izdaje za mjesec ili razdoblje.
UP008
OBVEZNIK OSTVARUJE DOHODAK OD OTUĐENJA IMOVINE, IZNOS DOHOTKA UTVRDITI S NADLEŽNOM ISPOSTAVOM
Poruka se u upisuje u slučaju kad porezni obveznik ima evidentirana stanja (zaduženja/uplate) na šifri računa 1635 (PREDUJAM POREZA I PRIREZA NA DOHODAK OD OTUĐENJA NEKRETNINA I IMOVINSKIH PRAVA), a nema sistemski izdanog rješenja.
UP009
OBVEZNIK OSTVARUJE DOHODAK OD OTUĐENJA IMOVINE. NAVEDENI DOHODAK U IZNOSU:______ I POREZ I PRIREZ:__________ ZADUŽENI SU U RAZDOBLJU ZA KOJE SE POTVRDA TRAŽI, A ODNOSI SE NA GODINU XXXX
Poruka se ispisuje u slučaju kada porezni obveznik ima zaduženje na knjigovodstvenoj kartici na računu 1635 (PREDUJAM POREZA I PRIREZA NA DOHODAK OD OTUĐENJA NEKRETNINA I IMOVINSKIH PRAVA).
UP010
OBVEZNIK JE OBVEZAN PODNIJETI GODIŠNJU PRIJAVU POREZA NA DOHODAK S OSNOVE DOHOTKA NA KOJI JE PREDUJAM PLAĆEN U INOZEMSTVU
Poruka se upisuje u slučaju postojanja neoporezivih primitaka za šifre iz priloga 4. JOPPD-a: 36, 43, 47, 48, 50 (koje se odnose na primitke za koje je predujam poreza na doh. plaćen u inozemstvu, a u tuzemstvu se isti ne plaćaju, te je stoga obveznik obvezan podnijeti godišnju poreznu prijavu). Poruka se ispisuje na potvrdama za kalendarsku 2014. godinu.
UP011
OBVEZNIK OBAVLJA SAMOSTALNU DJELATNOST - OBVEZAN JE PODNIJETI GODIŠNJU PRIJAVU POREZA NA DOHODAK
Poruka se ispisuje u slučaju kada je porezni obveznik evidentiran u Registru poreznih obveznika kao obveznik poreza na dohodak od djelatnosti - poslovne knjige ili kao obveznik poreza na dohodak od imovine - poslovne knjige, a nema podnesenu godišnju prijavu poreza na dohodak.
UP012
OBVEZNIK JE OBVEZAN PODNIJETI GOD. PRIJAVU POREZA NA DOHODAK -ISTODOBNO U TIJEKU ISTOG MJ. POR. RAZD. OSTVARIO JE DOH. OD NESAM. RADA KOD DVA ILI VIŠE POSLODAVACA - MOGUĆ RAZLIČITI IZNOS POR. I PRI. OD NES. RADA
Poruka se ispisuje u slučaju kada porezni obveznik ima više JOPPD obrazaca s preklapanjem u mjesecima isplate. Poruka se ispisuje na potvrdama za kalendarsku 2014. godinu.
UP013
OBVEZNIK JE OBVEZAN PODNIJETI GOD. PRIJAVU POREZA NA DOHODAK - JER JE UZDRŽAVANI ČLAN S PK OBRASCA U POR. RAZDOBLJU OSTVARIO PRIMITKE VEĆE OD PROP. IZNOSA - MOGUĆ RAZLIČITI IZNOS POR. I PRI. OD NESAM. RADA
Poruka se ispisuje u slučaju kada porezni obveznik ima na PK obrascu prijavljenog uzdržavanog člana koji je u godini za koju se Potvrda traži imao primitak veći od iznosa predviđenog za tu godinu. Poruka se ispisuje na potvrdama za kalendarsku 2014. godinu.
UP014
OBVEZNIK JE ČLAN POSADE BRODA U MEĐUNARODNOJ PLOVIDBI - OBVEZAN JE PODNIJETI GODIŠNJU PRIJAVU POREZA NA DOHODAK
Poruka se ispisuje u slučaju kada je porezni obveznik podnosilac DPOM obrasca sa iskazanih manje od 183 dana plovidbe.
UP015
OBVEZNIK JE OBAVEZAN PODNIJETI EPOM OBRAZAC
Poruka se ispisuje ako je obveznik obavezan podnijeti EPOM obrazac, ali ga nije podnio.
UP016
OBVEZNIK JE OBVEZAN PODNIJETI PO-SD OBRAZAC
Poruka se ispisuje za sve obveznike koji u Registru poreznih obveznika imaju obvezu dohotka od djelatnosti - paušal, a ne postoji unesen PO-SD obrazac.
UP017
OBVEZNIK JE OBVEZAN PRIJAVITI PODATKE O VISINI INO MIROVINE
Poruka se ispisuje ako obveznik u Registru poreznih obveznika ima oznaku ino-mirovine, a Porezna uprava nema podataka o visini ino-mirovine.
UP018
OBVEZNIK JE ZA TRAŽENO RAZDOBLJE OSTVARIO INO-MIROVINU ČIJI IZNOS NIJE ISKAZAN/NIJE ISKAZAN U CIJELOSTI, STVARNO STANJE UTVRDITI S NADLEŽNOM ISPOSTAVOM
Poruka se ispisuje ako obveznik u Registru poreznih obveznika ima oznaku ino-mirovine, a Porezna uprava nema podataka o visini ino-mirovine u zadanom razdoblju ili dijelu razdoblja.
UP019
OBVEZNIK JE U PRETHODNOM RAZDOBLJU EVIDENTIRAN KAO ČLAN POSADE BRODA U MEĐUNARODNOJ PLOVIDBI - IZNOS DOHOTKA UTVRDITI S NADLEŽNOM ISPOSTAVOM
Ova poruka se ispisuje kod obveznika koji su za kalendarsku godinu koja prethodi kalendarskoj godini za koju se potvrda izdaje imali unesen D-POM OBRAZAC.
Poruka se na potvrdi ispisuje početkom godine do trenutka do kada se unese DPOM obrazac.
UP020
POREZNA UPRAVA ĆE KOD OBVEZNIKA PROVESTI POSEBAN POSTUPAK UTVRĐIVANJA GODIŠNJEG POREZA NA DOHODAK S OSNOVE DOHOTKA NA KOJI JE PREDUJAM PLAĆEN U INOZEMSTVU
Poruka se ispisuje za godinu 2015. na dalje, u slučaju postojanja neoporezivih primitaka za šifre iz priloga 4. JOPPD-a: 36, 43, 47, 48, 50 (koje se odnose na primitke za koje je predujam poreza na doh. plaćen u inozemstvu, a u tuzemstvu se isti ne plaćaju, te je stoga obveznik obvezan podnijeti godišnju poreznu prijavu).
UP021
POREZNA UPRAVA ĆE KOD OBVEZNIKA PROVESTI POSEBAN POSTUPAK UTVRĐIVANJA GODIŠNJEG POREZA NA DOHODAK OBZIROM DA JE ISTODOBNO U TIJEKU ISTOG MJ. POR. RAZD. OSTVARIO DOH. OD NESAM. RADA KOD DVA ILI VIŠE POSLODAVACA
Poruka se ispisuje za godinu 2015. na dalje, u slučaju kada porezni obveznik ima više JOPPD obrazaca s preklapanjem u mjesecima isplate.
UP022
POREZNA UPRAVA ĆE KOD OBVEZNIKA PROVESTI POSEBAN POSTUPAK UTVRĐIVANJA GODIŠNJEG POREZA NA DOHODAK OBZIROM DA JE UZDRŽAVANI ČLAN S PK OBRASCA U POR. RAZDOBLJU OSTVARIO VEĆE PRIMITKE OD PROPISANOG IZNOSA
Poruka se ispisuje za godinu 2015. na dalje u slučaju kada porezni obveznik ima na PK obrascu prijavljenog uzdržavanog člana koji je u godini za koju se Potvrda traži imao primitak veći od iznosa predviđenog za tu godinu.
UP023
OBVEZNIKU JE NADZOROM UTVRĐEN DOHODAK I POREZ I PRIREZ KOJI SE MOŽE ODNOSITI I NA PRETHODNA RAZDOBLJA. IZNOS DOHOTKA UTVRDITI S NADLEŽNOM ISPOSTAVOM.
Poruka se ispisuje kod obveznika koji u razdoblju za koje se potvrda traži imaju unesene JOPPD obrasce s oznakama GG701-GG709 - JOPPD IZVJEŠĆA PO NADZORU te GG710-GG719 - JOPPD IZVJEŠĆA TEMELJEM POREZNE NAGODBE.
UP024
ZA OBVEZNIKA SU DOSTAVLJENI JOPPD OBRASCI KOJI UTJEČU NA VISINU DOHOTKA. IZNOS DOHOTKA UTVRDITI S NADLEŽNOM ISPOSTAVOM.
Poruka se ispisuje za godinu 2015. na dalje u slučajevima kada je za poreznog obveznika u ISPU zaprimljen novi izvorni JOPPD obrazac i/ili dopuna JOPPD obrasca i/ili ispravak JOPPD obrasca, nakon provedenog Godišnjeg obračuna poreza na dohodak, a odnosi se na razdoblje za koje je proveden Godišnji obračun.
PRILOG 2.
SVRHE ZA RAZMJENU PODATAKA O DOHOCIMA I PRIMICIMA IZ SUSTAVA EDIP
ŠIFRA SVRHE | OPIS SVRHE
S001 | PRAVA IZ SUSTAVA SOCIJALNE SKRBI
S002 | PRAVO NA DOPLATAK ZA DJECU
S003 | PRAVO NA NAKNADU ZA VRIJEME PRIVREMENE SPRIJEČENOSTI ZA RAD
S004 | OSLOBOĐENJE OD PLAĆANJA UPRAVNIH I JAVNOBILJEŽNIČKIH PRISTOJBI
S005 | PRAVO NA BESPLATNU PRAVNU POMOĆ
S006 | PRAVO NA PLAĆENE DOPRINOSE ZA UMJETNIKE
S007 | PRAVO NA SMJEŠTAJ U UČENIČKOM/STUDENTSKOM DOMU
S008 | PRAVO NA OPSKRBNINU I BESPLATNE ŠKOLSKE UDŽBENIKE
S009 | PRAVO NA DODJELU STIPENDIJE
S010 | SUBVENCIONIRANJE I/ILI UTVRĐIVANJE CIJENE VRTIĆA
S011 | SUBVENCIONIRANJE PREHRANE I/ILI PRIJEVOZA DJECI
S012 | OTPIS DUGOVA
S013 | PRAVO NA ALIMENTACIJU
S014 | BANKOVNO POSLOVANJE (KREDITI, LEASING,...)
S015 | OSTVARIVANJE PRAVA IZ MIROVINSKOG OSIGURANJA
S016 | PRAVO NA DODATAK NA MIROVINU
S017 | OSTVARIVANJE PRAVA NA INVALIDNINU
S018 | DOPUNSKO ZDRAVSTVENO OSIGURANJE
S019 | OSTVARIVANJE PRAVA NA UZDRŽAVANJE U INOZEMSTVU
S020 | IZBJEGAVANJE DVOSTRUKOG OPOREZIVANJA
S021 | OBRADA EU OBRAZACA
S022 | OSLOBOĐENJE OD PLAĆANJA KOMUNALNE NAKNADE
S023 | PRAVA IZ SUSTAVA SOCIJALNE SKRBI - JLPRS
S024 | JEDNOKRATNA NOVČANA POMOĆ - MINISTARSTVO BRANITELJA
S025 | JEDNOKRATNA NOVČANA POMOĆ - JLPRS
S026 | ZA POTREBE OPĆINSKOG DRŽAVNOG ODVJETNIŠTVA
S027 | REGULIRANJE PRAVA NA STAMBENO ZBRINJAVANJE
S028 | SUBVENCIONIRANJE JAVNOG PRIJEVOZA
S029 | PRAVO NA POMOĆ I UZDRŽAVANJE
S030 | PRAVO NA ZDRAVSTVENO OSIGURANJE U EU
S031 | DOBIVANJE VIZE
S032 | PRAVO NA OPSKBRNINU - MINISTARSTVO BRANITELJA
S033 | DOZVOLA ZA MALI OBALNI RIBOLOV
S034 | JEDNOKRATNA NOVČANA POMOĆ - URED DRŽAVNE UPRAVE
S035 | REGULIRANJE PRAVA I DODATAKA NA INOZEMNU MIROVINU
S036 | ZA POTREBE ŽUPANIJSKOG DRŽAVNOG ODVJETNIŠTVA
S037 | OSTVARIVANJE PRAVA IZ ZDRAVSTVENOG OSIGURANJA
S038 | OSTVARIVANJE STUDENTSKIH PRAVA
S039 | POVRAT POREZA IZ INOZEMSTVA
S040 | ZA POTREBE OPĆINSKOG SUDA
S041 | ZA POTREBE MUP-a
S042 | NA OSOBNI ZAHTJEV STRANKE
S043 | OSTVARIVANJE PRAVA NA UZDRŽAVANJE U RH
S044 | JEDNOKRATNA NOVČANA POMOĆ - UDRUGA/ZAKLADA
S045 | ZA POTREBE ŽUPANIJSKOG SUDA
S046 | OSLOBOĐENJE OD PLAĆANJA NOVČANIH/PREKRŠAJNIH KAZNA
S047 | ZA POTREBE TRGOVAČKOG SUDA
S048 | OTVARANJE ZAŠTIĆENOG RAČUNA
S049 | ZA POTREBE PREKRŠAJNOG SUDA
S050 | UPIS UČENIKA I/ILI UTVRĐIVANJE CIJENE USLUGE ZA PRODUŽENI BORAVAK ILI CJELODNEVNI ODGOJNO OBRAZOVNI RAD
S051 | REGULIRANJE PRAVA NA OTPIS DUGA, ODGODU/OBROČNU OTPLATU DUGA, TE ODGODU OVRHE
S052 | ZA POTREBE ŠKOLOVANJA U INOZEMSTVU
S053 | PROVEDBA ČLANKA 173. STAVAK 7. OVRŠNOG ZAKONA
S055 | ZA POTREBE CARINSKE UPRAVE
S056 | ZA POTREBE POSTUPKA OSTVARIVANJA OBITELJSKO PRAVNE ZAŠTITE
S058 | OSTVARIVANJE PRAVA NA POSEBNI DOPLATAK ZA HRVI IZ DOMOVINSKOGA RATA
S059 | OSTVARIVANJE PRAVA NAOSLOBOĐENJE OD TROŠKOVA ŠKOLARINE
S061 | OSTVARIVANJE PRAVA NA NOVČANU NAKNADU ZA VRIJEME NEZAPOSLENOSTI
