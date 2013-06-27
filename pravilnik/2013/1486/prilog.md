PRILOG 1
SPECIFIKACIJE FORMATA ENC UREĐAJA I TEHNIČKI OPIS ZA USLUGU EENC-a
ENC uređaj mora biti kompatibilan sa sljedećim standardima i specifikacijama:
- CEN TC278 DSRC 5.8 GHz Europski standard,
- GSS 3.0 svjetska interoperabilna specifikacija,
- ISO 14906 programski povezana definicija za DSRC (dedicated short range communication),
- TIS, CESARE, CARDME i PISTA transakcijski modeli uključujući i otvorenost za ostale standardizirane modele.
Podaci i prijenos moraju biti zaštićeni kriptografskim algoritmom koji mora jamčiti autentičnost ENC uređaja.
Osnovne mogućnosti
• Zapisivanje i čitanje transakcija
• Multi-servis sposobnost
• Kontrolirani pristup od operatera
• Centralna poslovna evidencija
• On-Board Account Managemant
• Povijest transakcija
• LED i/ili zvučni signal prilikom transakcija
Zaštita podataka
• DES algoritam s raznoliko podešenim ključevima
Izvedba
• Vrijeme aktiviranje manje od 2ms
• Vijek trajanja minimalno 5 godina
Arhitektura
• Mikrovalni antenski strujni krug
- Transponderski tip
- 5.8 GHz
• ASIC komponente
- Analogni strujni modul
- Digitalni strujni modul
- RISC 32 bitni procesor
- procesorsko primjenjiv RAM
- minimalno 2328 byte programske memorije
Temperaturni uvjeti rada
• Radna temperatura -25 °C do +85 °C (EN 60068)
Napajanje i potrošnja
• 3.6 V 2200 mAmps baterija
• Sleep mode potrošnja manja od 25 µA
• Vijek trajanja baterije min. 5 godina
Parametriziranje podataka
• Skidanje podataka i sigurnosnih ključeva preko mikrovalne veze:
- u trenutku proizvodnje
- od strane operatera prilikom prestanka korištenje uređaja
INTERNA STRUKTURA ENC-a
Jedinica u vozilu (ENC) implementira EFC aplikaciju prema ISO 14906. Sadrži sistemsku aplikaciju i jednu EFC aplikaciju baziranu na standardiziranom modelu koji je čitljiv u interoperabilnom sustavu. Također ima zvučni signal i/ili LED diodu za indikaciju plaćanja cestarine na stazi.
Transakcije između opreme na stazi (RSE) i jedinice u vozilu (ENC) opisane su u standardima ENV 12253, ENV 12795, ENV 12834 i ENV13372.
Sistemska aplikacija sadrži podatke koji se koriste interno na samoj jedinici. Identifikacijski broj EID = 0.
EFC aplikacija sadrži podatke koje koristi ENC sustav za obradu transakcija. Identifikacijski broj EID = 1.
LISTA ATRIBUTA
Šifra atributa
Atribut
Tip
Element
Veličina (u bitovima)
Pristup (R/O=samo čitaj; R/W=čitaj/piši)
0
EFC Kontekst
Oznaka
Octet string
(6 bajtova)
Dobavljač Ugovora:
Kod države
Broj koncesionara
10
14
R/O
Tip ugovora
16
Verzija konteksta
8
97
Račun
Octet string
(6 bajtova)
Broj računa proizvoda
48
R/O
98
Proizvod
Octet string
(11 bajtova)
Tip proizvoda
8
R/O
Identifikacija proizvoda
16
Datum i vrijeme kodiranja/važenja
32
Datum isteka
16
Skupina
4
Ograničenje duljine
12
99
D_VET
Octet string
(14 bajtova)
Tip zapisa
4
R/W
Kod postaje:
Kod koncesionara:
Kod države
Koncesionar
Postaja
10
7
10
Staza
7
Smjer staze
1
Skupina cestarine
4
Datum i vrijeme prolaza
30
Rezervirano
7
Iznos cestarine
20
Obzervacijski kod
7
Pokazivač povijesti
5
100 → 115
D_HIS
Octet string
(14 bajtova)
Tip zapisa
4
R/W
Kod postaje:
Kod koncesionara:
Kod države
Koncesionar
Postaja
10
7
10
Staza
7
Smjer staze
1
Skupina cestarine
4
Datum i vrijeme prolaza
30
Rezervirano
7
Iznos cestarine
20
Obzervacijski kod
7
Pokazivač povijesti
5
116
VPR
Octet string
(15 bajtova)
VPR registarska oznaka
88
R/W
Broj sekvence VPR tranzitnog identifikatora
32
117
Registarska oznaka 1
Octet string
(15 bajtova)
Registarska oznaka 1
120
R/O
118
Registarska oznaka 2
Octet string
(15 bajtova)
Registarska oznaka 2
120
R/O
119
Registarska oznaka 3
Octet string
(15 bajtova)
Registarska oznaka 3
120
R/O
120
Ime korisnika
Octet string
(26 bajtova)
Ime i prezime korisnika
208
R/O
125
D_EVE
Octet string
(6 bajtova)
Serijski broj ENC-a
32
R/O
Datum proizvodnje
13
Dopunski bitovi
3
127
Rezervirano
DETALJI KODIRANJA
Sva polja su binarno kodirana osim onih označenih drugim formatom:
Kod države: Identifikator države. Kodiran je u ITA2 (treba biti HR)
Broj koncesionara: npr. Identifikator HAC-a u državi je 1.
Tip ugovora: npr. tip HAC-ovog ugovora je 1
Verzija konteksta: npr. HAC-ova verzija konteksta je 2.
Broj računa proizvoda: Ovo je identifikator račun proizvoda pretplate. Kodiran je u BCD kako slijedi: SGGPP999999L
S: Broj dionice,
GG: Broj postaje,
PP: POS broj,
999999: broj sekvence,
L: Luhn ključ.
Tip proizvoda: Označava tip proizvoda, može biti:
21
Pretplata naknadnim plaćanjem
22
Besplatni
28
Unaprijed plaćena pretplata za velike i male korisnike
45
Mjesečne i godišnje pretplate
Identifikator proizvoda: Samo kao identifikacijska oznaka za pretplatu.
00xx
Pretplata naknadnim plaćanjem
52xx
Besplatni: Policija
53xx
Besplatni: Hitna pomoć
54xx
Besplatni: Vatrogasci
55xx
Besplatni: snage UN-a
56xx
Besplatni: Humanitarne organizacije
57xx
Besplatni: Ostali
58xx
Besplatni: HAC vozila
59xx
Besplatni: HAC dozvole
60xx
Besplatni: Invalidi
61xx
Besplatni: HV
62xx
Besplatni: otok Krk
01xx
Unaprijed plaćena pretplata za male korisnike
02xx
Unaprijed plaćena pretplata za velike korisnike
01xx
Mjesečna pretplata
02xx
Godišnja pretplata
Napomena: Svako novo dodavanje proizvoda od strane bilo kojeg koncesionara dovodi do ažuriranja tabele tipa proizvoda i identifikacije proizvoda
Datum i vrijeme kodiranja/valjanosti: Datum i vrijeme zadnjeg kodiranja na ENC-u, ili početak važenja proizvoda.
Važno: Ako je početak važenja u budućnosti tada se ovo polje ispunjava s datumom i vremenom početka važenja. Inače se ovo polje popunjava sa datumom i vremenom kodiranja.
Napomena: Ova informacija se kodira u 32 bita u formatu kako slijedi:
Y
Y
Y
Y
Y
Y
M
M
M
M
D
D
D
D
D
h
h
h
h
h
m
m
m
m
m
m
s
s
s
s
s
s
YYYYYY: Broj godina od godine 2000 u 6 bita (primjer: godina 2004 → 4),
MMMM: Mjesec kodiran u 4 bita (1 → 12),
DDDDD: Dan kodiran u 5 bita (1 → 31),
hhhhh: Sat kodiran u 5 bita (0 → 23),
mmmmmm: Minuta kodirana u 6 bita (0 → 59),
ssssss: Sekunda kodirana u 6 bita (0 → 59).
Datum isteka: Datum isteka računa proizvoda.
Napomena: Informacija je kodirana na 16 bita u sljedećem formatu:
Y
Y
Y
Y
Y
Y
M
M
M
M
D
D
D
D
D
0
YYYYYY: Broj godina od godine 2000 u 6 bita (primjer: godina 2004 → 4),
MMMM: Broj mjeseci kodiran u 4 bita (1 → 12),
DDDDD: Broj dana kodiran u 5 bita (1 → 31),
0: Nekorišteni bit.
Skupina vozila: Skupina vozila, može biti:
00
Sve skupine dopuštene
01
Skupina 1
02
Skupina 2
03
Skupina 3
04
Skupina 4
05
Skupina 5
Ograničenje duljine puta: Kod tablice koja sadrži listu ovlaštenih putova za karticu.
Tip zapisa:
1
Ulazna točka u zatvorenom sustavu
2
Izlazna točka u zatvorenom sustavu
3
Izlazna točka u otvorenom sustavu
13
ENC je vraćen HAC-u
14
ENC je poništen
15
Prvi zapis (nije važno)
Kod države postaje: Identifikator države koncesionara gdje se izvršila zadnja transakcija (treba biti 191).
Koncesionar postaje: Identifikator koncesionara kod koje se izvršila zadnja transakcija.
Postaja: Identifikator postaje (dionica + postaja) gdje se izvršila zadnja transakcija.
Staza: Identifikator staze u kojoj se izvršila zadnja transakcija.
Smjer staze:
0
Ulaz
1
Izlaz
Skupina cestarine: Skupina korištena za izračun cijene
01
Skupina 1
02
Skupina 2
03
Skupina 3
04
Skupina 4
05
Skupina 5
Datum i vrijeme transakcije: Vrijeme i datum izvršenja zadnje transakcije.
Napomena: Informacija je kodirana sa 29 bita u sljedećem formatu:
Y
Y
Y
Y
M
M
M
M
D
D
D
D
D
h
h
h
h
h
m
m
m
m
m
m
s
s
s
s
s
s
YYYY: Broj godina od 2000 kodiran u 4 bita (primjer: godina 2004 → 4),
MMMM: Mjesec kodiran u 4 bita (1 → 12),
DDDDD: Dan kodiran u 5 bita (1 → 31),
hhhhh: Sat kodiran u 5 bita (0 → 23),
mmmmmm: Minuta kodirana u 6 bita (0 → 59),
ssssss: Sekunda kodirana u 6 bita (0 → 59)
Iznos cestarine: Cijena cestarine transakcije.
Obzervacijski kod: Daje informaciju o zadnjoj transakciji.
Pokazivač povijesti: Daje poziciju zadnje prošle transakcije.
VPR registracijska oznaka: Registracijska oznaka prepoznata od VPR sustava (11 znakova maksimalno, lijevo poravnani postavljeni desno sa razmacima (0x20)).
Broj sekvence VPR tranzitnog identifikatora: Ovo je broj sekvence koji identificira transakciju neovisno o tipu tranzitnog medija.
Registarske oznake 1, 2 i 3: Registarske oznake korisnika (15 znakova maksimalno, lijevo poravnani postavljeni desno sa razmacima (0x20)).
Ime i prezime: Ime i prezime besplatnog korisnika (26 znakova maksimalno, lijevo poravnani postavljeni desno sa razmacima (0x20)).
Serijski broj ENC-a: Identifikator ENC (ovaj broj je jedinstveni za svakog proizvođača).
Datum proizvodnje: Datum proizvodnje ENC-a.
Napomena: Ova informacija je kodirana u 13 bita u sljedećem formatu:
Y
Y
Y
Y
Y
Y
Y
W
W
W
W
W
W
YYYYYYY: Broj godina od 2000 kodiran u 7 bitova (primjer: godina 2004 → 4),
WWWWWW: Broj tjedana od početka godine (1 → 53).
PRILOG 2
Formati za razmjenu podataka između pružatelja usluge EENC-a i Hrvatskih autocesta d.o.o. i koncesionara za javne ceste u koncesiji
Formati podataka za razmjenu trebaju biti u skladu sa EN 15509:2007 (CEN) odnosno sa HRN EN 15509:2008 »Cestovni prijevoz i prometna telematika-Elektroničko prikupljanje naknade-Interoperabilni aplikacijski profil za DSRC«
U razmjenu podataka ulazi svaka transakcija (prolazak vozila kroz naplatnu postaju jedne ugovorne strane) gdje je cestarina plaćena na naplatnoj postaji Hrvatskih autocesta d.o.o., odnosno koncesionara s ENC uređajem pružatelja usluge EENC-a.
Formati zapisa koji su navedeni u sljedećem tekstu sadrže podatke koji su prihvaćeni iz već postojećih sustava za razmjenu podataka u Europskom interoperabilnom načinu plaćanja cestarine. Pojedini nazivi i termini su ostavljeni u engleskom izvorniku obzirom da nije moguće adekvatno ih prevesti na hrvatski jezik.
Popis obrađenih ENC uređaja
Ova tablica zajednička svim postajama stvara popis ENC uređaja koji će se obraditi
Zajednička tablica nalazi se na BADGESTLP.999 (999 = verzija tablice)
Opis evidencije:
Položaj
Oblik
Oznaka
1-4
4[X]
ID proizvođača šifriran u 4 heksadekadske znamenke
5-8
4[X]
Klasa opreme šifrirana u 4 HEKSADEKADNE znamenke
9-28
20[X]
Označeno
29
[9]
Postavljanje MMI formata
1. Nema zvučnog signala
2. CSSI format
3. GSS format
30-33
4[X]
Resetiranje vremena između Set_MMI i
otpuštanje u milisekundama šifriranim u 4 HEKSADEKADNE znamenke
34-35
2[X]
Parametar Set_MMI šifriran u 2 HEKSADEKADNE znamenke
36
[9]
OBEStatus Format:
1. Odsutno
2. CSSI format
3. GSS format
Ova se tablica uzima u obzir čim postane valjana.
Ako ta tablica nije prisutna u ENC traci, operater ne može otvoriti zadatak.
POPIS IZDAVATELJA ENC UREĐAJA
Ta je tablica zajednička svim postajama kako bi se definirao popis organizacija čiji se ENC uređaji prihvaćaju u trakama.
Zajednička tablica nalazi se na: EMETTLP.999 (999 = verzija tablice)
Opis evidencije:
Položaj
Format
Oznaka
1-3
3[9]
Šifra države pošiljatelja u formatu ISO 3166 Numerički-3
4-8
5[9]
Šifra pošiljatelja u formatu ISO 14906 1 .. 16383
9-11
3[9]
Pozadina ISO 14906 verzije 1 .. 255
12
[9]
Pokazatelj vrste ugovora (ITOC):
Trx TIS: CIP Treatment na D_Pro/F_Idu
0. Trx CARDME s TOC upravljanjem po državi.
1. Trx CARDME s TOC upravljanjem po pošiljatelju.
13-22
10[X]
Naziv TOC tablice
23
[9]
Vrsta izračuna AC-CR
0. Nema
1. Izračun iz glavne šifre
2. Izračun iz izvedene šifre
3. Lozinka
4. Definirano po proizvodu
Ostale vrijednosti = 0
24-55
32[X]
Vrijednost za izračun AC CR-32 HEKSADEKADNE znamenke
za šifriranje do 16 bajtova za kombiniranje s vrstom izračuna.
56-58
3[9]
Broj šifre koja se koristi za izračun Autentikatora izdavatelja 111 .. 114
59-61
3[9]
Broj šifre koja se koristi za izračun Autentikatora operatera 115 .. 118
62-93
32[X]
Vrijednost glavne šifre koja će se koristiti za upravljanje sa 32 HEKSADEKADSKE
znamenke Autentikatora operatera za šifriranje 16 bajtova
94
[9]
Način oporavka diverzifikatora
1. Odsutno
2. U VST-u
3. U atributu
95-96
2[X]
Položaj diverzifikatora izražena u 2 HEKSADEKADSKE znamenke i funkcija načina oporavka
1. nije značajno
2. Pomak u polju VST parametra
3. broj atributa
Un Offset (pomak) označava početni položaj korisnih podataka o atributima
(nakon vrste spremnika i duljine ako ta polja postoje)
97
[9]
Način oporavka RndOBE
1. Izvedite Get_Nonce
2. U VST-u
98-99
2[X]
du Položaj diverzifikatora izražen u 2 HEKSADEKADSKE znamenke i funkcija načina oporavka
1. nije značajno
2. Pomak u polju VST parametra
Un Offset (pomak) označava početni položaj korisnih podataka o atributima
(nakon vrste spremnika i duljine ako ta polja postoje)
Ova se tablica uzima u obzir čim postane valjana.
Ako u traci nema tablice, nije moguće otvoriti položaj u traci.
Prilikom obrade odašiljača pomoću ITOC-a na 1, pretraživanje na CARDME tablicama proizvoda provodi se pomoću Država+Odašiljač na nula + vrsta ugovora + Kontekstna verzija na nula, no tijekom obrade odašiljača ITOC-om na 2, te pretrage uzimaju u obzir odašiljač i kontekstu verziju.
Popis CARDME proizvoda
Ta je tablica zajednička svim postajama kako bi se definirao popis organizacija čiji se ENC uređaji prihvaćaju u trakama.
Zajednička tablica nalazi se na: PROCARDME..999 (999 = verzija tablice)
Opis evidencije:
Položaj
Format
Oznaka
1-10
10[X]
Naziv TOC tablice
11-13
3[9]
Šifra države pošiljatelja u formatu ISO 3166 Numerički-3
14-18
5[9]
Šifra pošiljatelja u ISO 14906 0 (ITOC na 1) 1 .. 16383 (ITOC na 2)
19-23
5[9]
Vrsta ugovora 1 .. 65535
24-26
3[9]
Kontekstna verzija u ISO 149060 (ITOC na 1) 1. Format 255 (ITOC na 2)
27-30
4[X]
Skraćena oznaka (4 znaka)
31-50
20[X]
Oznaka u zapisniku (20 znakova)
51
[9]
Vrsta podrške
1: magnetski, 3: TIS, ...
52
[X]
Za jednokratnu upotrebu
O (Da) ili N (Ne); Ostali znakovi = N1
53
[X]
Prihvaćeno u automatskoj traci
O (Da) ili N (Ne); Ostali znakovi = O1
54
[X]
Sukcesivna upotreba za N plaćanja
O (Da) ili N (Ne); Ostali znakovi = O1
55-58
4[X]
Dozvoljeni gradijenti načina nabave. 32-bitna Maska izražena u 4 HEKSADEKALNE znamenke
Značenje bitova u skladu s njihovom težinom je sljedeće:
0. Tabeliranje
1. Očitanje crtičnog koda
59-62
4[X]
Način nabave za ulazne podatke dozvoljen. 32-bitna Maska izražena u 4 HEKSADEKALNE znamenke
Značenje bitova u skladu s njihovom težinom je sljedeće:
0. TT očitavanje u ručnom načinu
1. TT očitavanje u automatskom načinu
2. TT očitavanje na automatskoj postaji
3. Tabeliranje postaje u ručnom načinu
4. Tabeliranje postaje u TT načinu
5. Tabeliranje postaje u automatskom načinu
6. Tabeliranje postaje u TT automatskom načinu
7. TLPC u ručnom načinu
8. TLPC u automatskom načinu
63-66
4[X]
Automatski unosi kao pratnja pribavljanju u načinu smanjene kvalitete. Masq.
32-bitna izražena u 4 HEKSADEKALNE znamenke
Značenje bitova u skladu s njihovom težinom je sljedeće:
0. Datum valjanosti
1. Registracija vozila
2. Registracija ENC uređaja
67
[9]
Obrada atributa VehicleLicensePlateNumber (broj registracijske tablice vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
68
[9]
Obrada atributa VehicleClass (razred vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
69
[9]
Obrada atributa VehicleDimensions (dimenzije vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
70
[9]
Obrada atributa VehicleAxles (Osovine vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
71
[9]
Obrada atributa VehicleWeightLimits (ograničenja težine vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
72
[9]
Obrada atributa VehicleAuthenticator (autentikator vozila)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
73
[9]
Obrada atributa VehicleSpecificCharacteristics (značajke karakteristične za vozilo)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
74
[9]
Obrada atributa ContractAuthenticator (Autentikator ugovora)
0. Nema ENC uređaja
1. Postoji na ENC uređaju
2. Postoji na ENC uređaju i potrebno za prijenos pošiljatelju
75
[9]
Obrada atributa D_GES
0. Ne postoji ili ignorirati
1. Treba obraditi
76
[9]
Obrada atributa ReceiptText (tekst primitka)
0. Ne postoji ili ignorirati
1. Treba obraditi
77
[9]
Obrada IssuerAuthenticator (Autentikatora izdavatelja)
0. Nije potrebno
1. Potrebno za prijenos pošiljatelju
78-79
2[X]
Broj atributa koristi se za izračun IssuerAuthenticator (Autentikatora izdavatelja)
izražena u heksadekadskim znamenkama
80
[9]
Obrada OperatorAuthenticator (Autentikatora operatera)
0. Nije potrebno
1. Potrebno za prijenos pošiljatelju
2. Provjeriti u traci
81-82
2[X]
Pripisivanje broja koji se koristi za izračun OperatorAuthenticator (Autentikatora operatera)
izraženog u heksadekadskim znamenkama
83
[9]
Obrada transakcijskog brojača EquipmentStatus (status opreme)
0. Ne
1. Da
84
[9]
Obrada abnormalnih bitova EquipmentStatus (status opreme)
0. Ne
1. Da
85
[9]
Provjera PaymentMeans.ExpiryDate (NačinPlaćanja. DatumIsteka)
0. Ne
1. Da
86-87
2[9]
Primarna komercijalna priroda
10: Naknadno plaćanje
20: Izuzeto/besplatno
30: Plaćanje unaprijed
40: Plaćanje unaprijed podmireno u traci
41: Plaćanje unaprijed s odgođenom naplatom
50: Umanjenje na lokaciji
60: Naknadno plaćanje bez ugovora (kabinska kartica)
70: Specifično
90: Sistemska kartica (alatska kabina, održavanje, ...)
88
[X]
Dozvoljeni kontrolni razredi
O (Da) ili N (Ne); Ostali znakovi = N1
89
[X]
Postaje za kontrolnu referencu
O (Da) ili N (Ne); Ostali znakovi = N1
90
[X]
Kontrola kalendara
O (Da) ili N (Ne); Ostali znakovi = N1
91
[9]
Izdavanje dokumenta u traci
0: nema izdanih dokumenata
1 ili drugi znak: primitak
92
[X]
Vrsta brojenja
E: Kuna, P: Prolaz, N: Ništa, ... ; Drugi znak = N1
93-94
2[9]
Sekundarna komercijalna priroda
Novčići: n/d
10: Naknadno plaćanje
99: Ostala sredstva neposrednog plaćanja
95
[X]
Dozvoljeni kontrolni razredi
O (Da) ili N (Ne); Ostali znakovi = N1
96
[X]
Postaje za kontrolnu referencu
O (Da) ili N (Ne); Ostali znakovi = N1
97
[X]
Kontrola kalendara
O (Da) ili N (Ne); Ostali znakovi = N1
98
[9]
Izdavanje dokumenta u traci
0: nema izdanih dokumenata
1 ili drugi znak: primitak
99
[X]
Vrsta brojenja
E: Kuna, P: Prolaz, N: Ništa, ... ; Drugi znak = N1
100
[9]
Vrsta izračuna AC-CR
0. nema
1. Izračun iz glavne šifre
2. Izračun iz izvedene šifre
3. Lozinka
4. Definirano po izdavatelju
Ostale vrijednosti = 0
101-104
4[X]
16 bitna maska izražena u 4 HEKSADEKALNIM znamenkama s
popisom razreda koji se prihvaćaju za ovaj proizvod
Značenje bitova u skladu s njihovom težinom je sljedeće
0. Razred 1
1. Razred 2
2. Razred 3
3. Razred 4
4. Razred 5
Ova se tablica uzima u obzir čim postane valjana.
Ako u ENC traci nema tablice, nije moguće otvoriti zadatak.
1.1. POPIS IZNIMKI ZA CARDME (TIS-PL)
Postavlja popis iznimaka korištenih tijekom kontroliranja CARDME
Zajednička tablica nalazi se na: LEXCARDME..999 (999 = verzija tablice)
Opis evidencije:
Položaj
Format
Opis
1-19
19[X]
Broj PAN1
1-3
3[X]
Praznina : ne koristi se
4-8
5[X]
Praznina : ne koristi se
20
[9]
‘0’ = sivi popis
‘1’ = crni popis
1 Brojevi su poravnani ulijevo i upotpunjeni pratećim prazninama. Zamjenski znak * postavljen ispred prvog razmaka zamjenjuje bilo koji slijed brojeva. ASCII redoslijed povećavajućih brojeva PAN-a
Ova se tablica uzima u obzir čim postane valjana.
Isti broj ne bi se smio nalaziti na crnim i sivim popisima.
Ako u traci nema tablice, nije moguće otvoriti Zadatak.
ENC transakcija (CC) format
Ova se poruka šalje nakon ENC plaćanja.
Polje
Lg
Format
Opis
Korišteno
1-53
53
[X]
Zaglavlje II : Vrsta poruke ‘CC’
Da
54-853
800
[X]
Transakcija (vidjeti ispod)
Da
Podatkovni element
Izvor
Položaji
Format
Vrijednost (Ako je konstantna) /
Ostalo /
Podatkovni element
(1)
(2)
(3)
Naslov/značenje
Atribut
Duljina
Početak
Kraj
O/F
G/D
pravila ispunjavanja
Šifra bilježenja
2
01
02
9(2)
O
10
Identifikacija uporabe u općem sustavu
03
50
O
Identifikator pružatelja tranzitne usluge
8
03
10
X(8)
O
Šifra države
03
05
9(3)
O
D
ISO 3166 - 1 brojčani Hrvatska = 191
Broj u redu čekanja za pružatelja tranzitnih usluga
06
10
9(5)
O
D
značajno u državi Vrijednost od 1 do 16383
Identifikacija Potrošnje u sustavu pružatelja usluge
0
Izlazak iz identifikatora pružatelja tranzitne usluge
8
11
18
X(8)
O
identifikator pružatelja usluge
Šifra države
11
13
9(3)
O
D
ISO 3166 - 1 brojčani Hrvatska = 191
Broj u redu čekanja za pružatelja tranzitnih usluga
14
18
9(5)
O
D
značajno u državi Vrijednost od 1 do 16383
Broj potrošnje
29
19
47
X(29)
O
Mreža
19
20
9(2)
Postaja br.
21
22
9(2)
Traka br.
23
25
X(3)
Zadatak br.
25
27
9(2)
Poslovna transakcija br.
27
32
9(5)
Indeks za dupliciranu transakciju
32
33
9(1)
Prolaz DHM
34
47
9(14)
F
Format GGGGMDDHHmmss
Umreženje
1
48
48
9
O
Vrijednost 0: mono-društvena transakcija, nije izrezana
Vrijednost 1 do 9: mono-društvena transakcija, izrezana: broj u redu rezanja nadređene transakcije, od ulaza do izlaza
Regulacijski broj
1
49
49
9
O
Regulacijski broj, povećava se ako se pošalje »+« transakcija, nakon čega slijedi »-« na istom identifikatoru
0 do 9
Znak transakcije
Ostalo
Znak transakcije
1
50
50
[X]
O
Pozitivno (+): nova transakcija, Negativno (-): otkazana transakcija
Modifikacija transakcije obrađuje se otkazivanjem i dodavanjem evidencije potrošnje
Regularizacijska šifra
Ostalo
Regularizacija
Tekst
3
51
53
XXX
F
Regularizacijska šifra, kojom se daje knjigovodstveni razlog za događaje, primjerice simulaciju prolaza, reintegraciju u traku na pogreški razreda...
Šifra izdavača oznake
8
54
61
X(8)
O
Identifikacija TAG pitanja je
ContractProvider (pružatelj ugovora) šifriram u EFC-ContextMark (EFC-kontekstna oznaka) za TAG,
Šifra države
54
56
9(3)
O
je CountryCode (šifra države) za ContractProvider (pružatelj ugovora) ISO 3166 - 1 numerički Hrvatska = 191
Kod izdavača u državi
57
61
9(5)
O
0 à 16383
Vrsta ugovora
EFC_
Vrsta ugovora
5
62
66
9(5)
O
0 à 65535
Značajno za izdavača navedenog iznad
Broj računa
Ostalo
20
67
86
X(20)
F
u slučaju uokvirenog PAN-a s klijentovim brojem, ovaj je izdvojen ovdje
Značajno za izdavača navedenog na početku.
Šifra »komercijalnog ugovora«
20
87
106
X(20)
F
ako postoji komercijalni ugovor kod pružatelja usluge za korišteni način plaćanja za ovu potrošnju, inače razmak
identifikator pružatelja usluge
87
94
X(8)
O
Šifra države
87
89
9(3)
O
ISO 3166 - 1 brojčani Hrvatska = 191
Kod izdavača u državi
90
94
X(5)
O
Značajno u državi
Broj komercijalnog ugovora kod pružatelja usluge
95
106
X(12)
O
Način plaćanja
32
Sredstvo plaćanja
107
139
O
Broj osobnog računa (PAN)
Broj
osobnog računa
19
107
125
X(19)
O
PAN
Datum isteka sredstava plaćanja
….DatumIsteka
8
126
133
9(8)
F
Format GGGGMMDD, dešifriranje 7 bitova za godinu na -127 (1990 do 2117) - 4 bajta za mjesec (1 do 12), 5 bajtova za dan (1 do 31)
Postavljeno na 0 ako nema datuma isteka.
Broj popisa referentnih odmarališta
.Kontrola uporabe
4
134
137
9999
F
0 do1023
Broj kalendarskog popisa
.Kontrola uporabe
2
138
139
99
F
0 do 63
Transakcija cestarine
TSP
Ulazni podaci
Ulazna postaja
10
140
149
X(10)
O
Postaviti na 0 ako je točka evidencije OE/OS - U slučaju putovanja od putovanja umrežene veze, mogao bi biti fiktivni broj postaja
Šifra države
140
142
XXX
O
ISO 3166 - 1 brojčani Hrvatska = 191
Identifikator pružatelja tranzitne usluge
143
144
XX
O
.
Mrežna šifra
145
146
XX
O
Značajno za pružatelja tranzitnih usluga
Ako se ne koristi, ispuniti razmakom.
Broj u čekanju za postaju
147
149
XXX
O
Značajno u gornjoj hijerarhiji informacija
Ulazni DHM
14
150
163
9(14)
F
Format GGGGMDDHHmmss
Izlazni podaci
Izlazna postaja
10
164
173
X(10)
U slučaju putovanja od putovanja umrežene veze, mogao bi biti fiktivni broj postaja kraja koncesije
Šifra države
Šifra države
164
166
XXX
O
ISO 3166 - 1 brojčani Hrvatska = 191
Šifra pružatelja tranzitne usluge
167
168
XX
O
Značajno u šifri države.
Mrežna šifra
169
170
XX
O
Značajno za pružatelja tranzitnih usluga
Ako se ne koristi, ispuniti razmakom.
Broj u čekanju za postaju
171
173
XXX
O
Značajno u gornjoj hijerarhiji informacija
Broj trake
2
174
175
XX
F
Izlazni DHM
14
176
189
9(14)
O
Format AAAAMMJJHHmmss
Točka evidencije
2
190
191
XX
O
G
OE = Otvori ulaz
OS = Otvori izlaz
FS = Zatvori izlaz
Načini funkcioniranja postaja/trake
3
192
194
XXX
F
Normalan rad = NOR, Održavanje = MAI, Neodređeno = IND
Način pribavljanja ulazne postaje
2
195
196
99
O
D
Postaviti na 0 ako je točka evidencije = OE ili OS,
Način pribavljanja ulazne postaje
1 = magnetska traka
2 = crtični kod,
3 = vanjska ENC antena,
4 = ENC stolna antena,
5 = tipkovnica,
6 = Smartcard,
7 = Naknadno pribavljanje
Način pribavljanja plaćanja
2
197
198
99
O
D
Način pribavljanja plaćanja
1 = magnetska traka
2 = crtični kod,
3 = vanjska ENC antena,
4 = ENC stolna antena,
5 = tipkovnica,
6 = Smartcard,
7 = Naknadno pribavljanje
Podaci o razredu vozila
Način određivanja razreda
1
199
199
X
O
Način određivanja razreda:
. A - implicirano u traci posvećenoj razredu
. B - ručno u ručnoj traci
. C - automatsko u traci (prethodni AVC)
. D - automatsko kroz podatke o oznaci
. E - bijeli popis
Prethodni AVC na izlazu
2
200
201
XX
F
Ispunjava se ako je traka opremljena prethodnim AVC-om
Naknadni AVC na izlazu
2
202
203
XX
F
Ispunjava se u traci ako je opremljena naknadnim AVC-om
Razred izvorno tabelira prikupljač cestarine
2
204
205
XX
F
Indikator modifikacije razreda
1
206
206
[X]
F
Indikator modifikacije razreda
1: promijeni u niži razred
2: otkazivanje pogreške razreda
Konačni razred
2
207
208
XX
O
Konačni razred
Stanje kilometraže
5
209
213
9999V9
O
D
Podaci o vozarini
Vrsta vozarine
5
214
218
X(5)
F
Indikator modulacije vozarine
Šifra vozarine
5
219
223
X(5)
F
Šifra vozarine primjenjuje se u skladu s tablicom o vozarini
Kod valute
3
224
226
999
O
ISO 4217 Numerički eks: HRK = 191
Osnovna cijena bez PDV-a.
11
227
237
9(11)
O
Stopa rasta ili smanjenja cijene
238
243
F
Ta dva polja moraju biti biti prisutna ili odsutna istovremeno.
Znak
1
238
238
[X]
F
Pozitivno: »+«
Negativno: »-«
Stopa
5
239
243
999V99
F
D
Iznos, izražen u najmanjoj jedinici valute naznačen u početnoj evidenciji
Iznos rasta ili smanjenja cijene
244
255
F
Ta dva polja moraju biti biti prisutna ili odsutna istovremeno.
Znak
1
244
244
[X]
F
Pozitivno: »+«
Negativno: »-«
Iznos
11
245
255
9(11)
F
D
Iznos, izražen u najmanjoj jedinici valute naznačen u početnoj evidenciji
Povećana ili smanjena vozarina bez PDV-a
11
256
266
9(11)
O
Povećana ili smanjena cijena bez poreza: osnovna cijena bez poreza +/- ((osnovna cijena bez poreza x %Rai/red) +/- iznos rai/red)
Iznos, izražen u najmanjoj jedinici valute naznačen u početnoj evidenciji
Stopa PDV-a
4
267
270
99V99
O
Iznos PDV-a
11
271
281
9(11)
O
Iznos PDV-a: (cijena bez poreza rai/red x stopa PDV.a)/100 Iznos, izražen u najmanjoj jedinici valute naznačen u početnoj evidenciji
Vozarina uključujući PDV
11
282
292
9(11)
O
Cijena bez PDV-a rai/red + iznos PDV-a
Iznos, izražen u najmanjoj jedinici valute naznačen u početnoj evidenciji
Podaci o transakcijskom upravljanju
Način pribavljanja registracijske tablice
2
293
294
99
O
D
0 = N.U,
1 = automatski,
2 = Tabelirano.
Registracijska tablica vozila
15
295
309
X(15)
F
Registracijska tablica vozila koje prolazi kroz traku
Šifra praćenja događaja
310
327
X(18)
F
Polje mora biti ispunjeno bez praznina
Šifra 1
3
310
312
XXX
F
Šifra 2
3
313
315
XXX
F
Šifra 3
3
316
318
XXX
F
Šifra 4
3
319
321
XXX
F
Šifra 5
3
322
324
XXX
F
Šifra 6
3
325
327
XXX
F
Podaci iz atributa oznake
F
Datum proizvodnje
4
328
331
9(4)
F
Datum proizvodnje. Dobavljanje informacija samo putem antene
Dobavljač
VST
ObeConfiguration (ObeKonfiguracija)
manufacturerId (IdProizvođača)
5
332
336
9(5)
F
Dobavljanje samo putem antene.
Serijski broj
24
EquipmentOBUId (IdENCOpreme)
10
337
346
9(10)
F
Dobavljanje samo putem antene
Kontekstna verzija
EFC-ContextMark (EFC kontekstna oznaka)
3
347
349
999
O
ContextVersion. dobavljanje samo putem antene, crtični kod, tipkovnica.
Razred opreme
VST
Razred opreme obeConfiguration.
5
350
354
9(5)
F
.
Status
VST
obeConfiguration obeStatus
5
355
359
9(5)
F
Dobavljanje samo putem antene.
Brojač transakcija
26
Status opreme
4
360
363
9(4)
F
0 à 4095 Dobavljanje samo putem antene.
Bitovi s anomalijom
2
364
365
99
F
0 à 15
Bit 0: logička pogreška
Bit 1: podaci koje treba ponovno poslati
Bit 2: pretplata na crnoj listi
Bit 3: rezervirano
Dobavljanje samo putem antene.
Podaci o posljednjoj transakciji
33
ReceiptData1 (Podaci o primitku 1)
366
446
F
DHM
14
366
379
9(14)
O
Format GGGGMMDDHHmmss, preciznost 2s
Izlazak iz identifikatora pružatelja tranzitne usluge
8
380
387
X(8)
O
Šifra države
380
382
9(3)
O
ISO 3166-1 numerički
Broj čekanja u redu
383
387
X(5)
O
značajno u državi
Prolazna postaja
Lokacija postaje
10
388
397
X(10)
O
Značajno za pružatelja usluga
0 à 65535 NF EN ISO 14906
Smjer trake
1
398
398
9
F
0/1
Broj trake
3
399
401
999
F
0. - 127.
Vrsta transakcije ili usluge
1
402
402
9
F
1: Otvori sustav
2: Ulaz: Zatvori sustav
3: Izlaz: Zatvori sustav
4: Kontrolna točka
Rezultat transakcije
3
403
405
999
F
0 - 256
Razred koji se koristi za određivanje vozarine
3
406
408
999
F
0 - 256
Deklarirani razred
3
409
411
999
F
0 - 256
Plaćeni iznos
11
412
422
X(11)
O
Naknada za sesiju u naknadi
Cijena s PDV-om
5
412
416
9(5)
O
Jedinica plaćanja
6
417
422
9(6)
F
Jedinica naknade, vrsta jedinice plaćanja
Jedinica valute/vrsta/vrsta
2
417
418
99
F
Jedinica plaćanja:
Primjeri: 1 ako je cijena s porezom izražena u desetinama, 2 ako je cijena s porezom izražena u stotinama, ….
Šifra valute/pružatelja/vrijednosti
4
419
422
9(4)
F
Jedinica plaćanja: 0191 za Hrvatsku
Identifikator ugovora oznake
8
423
430
X(8)
O
Registracija izdavatelja ugovora o ENC-u.
Odgovara ContractProvider (Pružatelju ugovora) kodiranom u EFC- ContextMark (Kontekstna oznaka) ENC-a, u formatu »upravljanje«.
Šifra države
423
425
9(3)
O
D
Odgovora CountryCode (Šifri države) ContractProvider (Pružatelja ugovora)
Prema ISO 3166-1 numerički
Kod izdavača u državi
426
430
9(5)
O
D
Je ContractIssuer (Izdavač ugovora) za ContractProvider (Pružatelja ugovora)
1 do 16383
Vrsta ugovora
5
431
435
9(5)
O
1 do 65535
Značajno za izdavača postavljenog na početku.
Kontekstna verzija
3
436
438
999
O
ContextVersion (Kontekstna verzija).
Autentikator transakcije
8
439
446
X(8)
F
Podaci o drugoj posljednjoj transakciji
34
ReceiptData2 (Podaci o primitku 2)
447
527
F
Prolaz DHM
14
447
460
9(14)
O
Format GGGGMMDDHHmmss, preciznost 2s
Izlazak iz identifikatora pružatelja tranzitne usluge
8
461
468
X(8)
O
Šifra države
461
463
9(3)
O
ISO 3166-1 numerički
Broj čekanja u redu
464
468
X(5)
O
Značajno u državi
Prolazna postaja
Lokacija postaje
10
469
478
X(10)
O
Značajno za pružatelja usluga
0 à 65535
Smjer trake
1
479
479
9
F
0/1
Broj trake
3
480
482
999
F
0. - 127.
Vrsta transakcije ili usluge
1
483
483
9
F
1: Otvori sustav
2: Ulaz u zatvaranje sustava
3: Izlaz iz zatvaranja sustava
4: Kontrolna točka
Rezultat transakcije
3
484
486
999
F
0 - 256 ResultOp (RezultatOP)
Razred koji se koristi za određivanje vozarine primijenjene prilikom izračuna cijene
3
487
489
999
F
0 - 256 INT1
Deklarirani razred
3
490
492
999
F
0 - 256 INT1
Plaćeni iznos
11
493
503
X(11)
O
SessionFee (Naknada za sesiju) za PaymentFee (Naknada za plaćanje)
Cijena s PDV-om
5
493
497
9(5)
O
Cijena s PDV-om
Jedinica plaćanja
6
498
503
9(6)
F
Jedinica naknade, vrsta jedinice plaćanja
Jedinica valute/vrsta/ vrsta
2
498
499
99
F
Jedinica plaćanja:
Primjeri: 1 ako je cijena s porezom izražena u desetinama, 2 ako je cijena s porezom izražena u stotinama
Šifra valute/pružatelja/vrijednosti
4
500
503
9(4)
F
Jedinica plaćanja: 0191 za Hrvatsku
Identifikator izdavača ugovora oznake
8
504
511
X(8)
O
Identifikator izdavača ugovora oznake (odgovara ContractProvider (Pružatelju ugovora) šifriranom u EFC-ContextMark na oznaci)
Šifra države
504
506
9(3)
O
D
je šifra države pružatelja ugovora
ISO 3166-1 numerički
Kod izdavača u državi
507
511
9(5)
O
D
je izdavač ugovora pružatelja ugovora
1 à 16383
Vrsta ugovora
5
512
516
9(5)
O
1 à 65535
Značajno za izdavača postavljenog na početku.
Kontekstna verzija
3
517
519
999
O
Kontekstna verzija.
Autentikator transakcije
8
520
527
X(8)
F
Podaci o vozilu: registracijska tablica
16
Broj registracijske tablice vozila
18
528
545
X(18)
F
Šifra države
528
530
999
ISO 3166-1 numerički
Od oznake TAG, crtičnog koda ili tabuliranja ako je MP šifra
Vrsta abecede
531
532
99
0. - 63.
Broj registracijske tablice
533
545
X(13)
Od oznake TAG, crtičnog koda ili tabuliranja ako je MP šifra.
Podaci o vozilu: klasifikacija
17
Vozilo
Klasa
4
546
549
X(4)
F
Prikolica (prisutna)
546
546
9
0 / 1
Interoperabilni razred
547
547
9
0 -
Lokalni razred
548
549
99
0 à 15, kombinira se s podacima o prikolici
Informacije o vozilu: dimenzije
18
Dimenzije vozila
9
550
558
X(9)
F
Duljina vozila
Vozilo
Ukupna duljina
550
552
999
Visina vozila
Vozilo
Ukupna visina
553
555
999
Širina vozila
Vozilo
Ukupna širina
556
558
999
Informacije o osovinama vozila
19
Osovine vozila
6
559
564
X(6)
F
Visina vozila na prvoj osovini
1 oktet
Prva osovina vozila
Visina
559
561
999
Vrsta kotača
2 bita
Vrsta gume
562
562
9
0 : nije naznačeno
1 : jedan kotač,
2 : dvostruki kotači
Broj osovina
6 bitova
Broj osovina
563
564
99
0. - 63.
Podaci o vozilu Ograničenje težine
20
Ograničenje težine vozila
15
565
579
X(15)
F
Ukupna težina vozila (PTAC)
2 okteta
Maksimalna težina opterećenja vozila
565
569
9(5)
0 - 65535
Ukupna težina s prikolicom
2 okteta
Maksimalna težina vlačnog vozila
570
574
9(5)
0 - 65535
Težina bez opterećenja
2 okteta
Težina vozila bez opterećenja
575
579
9(5)
0 - 65535,
Podaci o vozilu Određene karakteristike
22
Karakteristike specifične za vozilo
13
580
592
X(13)
F
Ekološke karakteristike
: Razred euro emisija
4 bitova
Euro razredi
580
581
99
0 - 15
0 : ako nije naznačeno
Šifra COP emisije
4 bitova
Vrijednost COP
582
583
99
0 - 15
Karakteristike motora
8 bitova
Motorske
karakteristike
584
586
999
0 - 255
»Forme«
8 bitova
Deskriptivne
karakteristike
587
589
999
0. - 255.
Rezervni
8 bitova
Buduće karakteristike
590
592
999
0. - 255.
Autentikator podataka o vozilu
23
Autentikator vozila
8
593
600
X(8)
F
X(8)
Heksadecimalna vrijednost
Autentikator podataka o ugovoru
4
Autentikator ugovora
8
601
608
X(8)
F
I
X(8)
Heksadecimalni
Autentikator izdavača
51
609
659
X(51)
F
AutentikatorIzdavača
Nasumična varijabilna heksadecimalna vrijednost
609
616
X(8)
O
Heksadecimalna vrijednost
Broj atributa (koji sadrži šifru)
617
619
999
O
111 à 114
620
651
X(32)
O
G
Vrijednost korištenog atributa
Rezultat izračuna
652
659
X(8)
O
Heksadecimalni
Slobodno
141
660
800
X(141)
slobodno
800
O : Obavezno/F : Dodatno
Format: G : Poravnano ulijevo i upotpunjeno prazninama s desne strane / D : Poravnano udesno i upotpunjeno prazninama s lijeve strane
PRILOG 3
Tehnički opis i specifikacija opreme elementa interoperabilnosti za prihvat usluge EENC-a
a) ENC antena na ulaznoj stazi s pripadajućom upravljačko-procesnom jedinicom
1. ENC antena
ENC antena komunicira s ENC uređajem uz pomoć dvosmjernog (bi-direkcionalnog) RF mikrovalnog modemskog linka na 5,8 GHz u skladu sa CEN DSRC standardima. ENC antena sukladna je slijedećim standardima:
- [ENV12253]
- [EN60950]
- [EN55022]
- [EN61000-4-2]
- [EN61000-4-3]
- [EN61000-4-4]
- [EN61000-4-6]
- [EN300674]
- [73/23/EEC)
- [89/336/EEC]
1.2. ENC antena ima minimalno sljedeće tehničke karakteristike:
Osnovna frekvencija : 5.805 GHz ± 25 MHz
Nosiva frekvencija F1 : 5.7975 GHz ± 2.5 MHz
Nosiva frekvencija F2 : 5.8025 GHz ± 2.5 MHz
Nosiva frekvencija F3 : 5.8075 GHz ± 2.5 MHz
Nosiva frekvencija F4 : 5.8125 GHz ± 2.5 MHz
Polarizacija antene : lijevo kružna
Pojačanje antene : 17 dBi (izotropno)
Upadni kut (lateralno) : 17°
Upadni kut (longitudinalno) : 25°
PIRE (kontinuirani val) : 26 to 32 dBm
Prijamna osjetljivost : -98 dBm (BER < 1.10-6)
Downlink binary rate : 500 Kb/s
Code : FMO
Uplink binary rate : 250 Kb/s
Radna temperatura : -30 °C do +70 °C
Funkcija (vlažna temp.) : 35°C, 95% relat. vlažnost
Zaštita : IP65 standard CEI 529
Elektromagnetska osjetljivost : CEI 801-3 standard 3
MTBF : >30.000 sati
2. Upravljačko-procesna jedinica
Upravljačko-procesna jedinica ima industrijski standardizirani (brand name) hardver i softver koji ima veliku autonomiju rada i visoku razinu pouzdanosti. Svi podaci dobiveni od perifernih uređaja obrađuju se u realnom vremenu. U slučaju pada komunikacije ili bilo kojeg drugog oblika degradiranog režima rada upravljačko-
-procesna jedinica radi autonomno i pohranjuje podatke minimalno 90 dana. Čak i ukoliko ne postoji veza prema centralnoj bazi podataka uravljačko-procesna jedinica je u mogućnosti identificirati operatera. Upravljačko-procesna jedinica vrši samodijagnozu vlastite ispravnosti kao i ispravnosti svih perifernih uređaja priključenih na njega te obavijesti o pogreškama šalje na nadzorno računalo. U slučaju da upravljačko-procesna jedinica prestane funkcionirati može se napraviti restart sustava bez gubitka podataka, a sustav će se ponovo pokrenuti i doći u stanje u kojem je bio prije prestanka rada. O navednom događaju postoji zapis na temelju kojeg je moguće utvrditi uzrok pogreške koja je dovela do restarta sustava i uvjeta u kojima je nastala (vrijeme, radno mjesto, operater i slično). Ova funkcija bitna je kako bi se omogućio neprekidni rad sustava u što većem broju slučajeva, a bez potrebe za intervencijom servisnog osoblja. Medij za pohranu podataka ima veliku pouzdanost, MTBF od najmanje 1.000.000 sati.
b) ENC antenu na izlaznoj stazi s pripadajućom upravljačko-procesnom jedinicom
Tehnički opis ENC antenskog sustava i upravljačko-procesne jedinice isti je kao pod točkom a).
c) Video nadzor visokog stupnja pouzdanosti na svim stazama opremljenim ENC antenama s pripadajućom upravljačko procesnom jedinicom
Svaka ulazna i izlazna staza opremljena je s kamerom i infracrvenim reflektorom visoke pouzdanosti koja služi za prepoznavanje registracijskih tablica vozila. Kamera je pozicionirana na način da na prepoznavanje registracijske tablice ne utječe položaj ni brzina vozila kao niti loši uvjeti okoliša (kiša, magla, snijeg, noć, …). Kamera je smještena u kućište koje je otporno na sve vremenske uvijete, a unutar kućišta moraju biti osigurani optimalni uvjeti za rad kamere (bez prašine, vode, kondenzacije, …). Na ulaznim stazama snima se i prepoznaje registracija vozila koja se na izlaznim stazama uspoređuje s registracijom vozila u stazi.
d) Sustav za utvrđivanje skupina vozila na ENC stazi s pripadajućom upravljačko-procesnom jedinicom
Na izlaznim prolazima razlikujemo predklasifikaciju i naknadnu klasifikaciju vozila.
Svrha predklasifikacije vozila je određivanje skupine vozila kao bi se mogla odrediti visina cestarine za pojedino vozilo. Predklasifikacija ispunjava sljedeće specifikacije:
- primijenjuje svu potrebnu opremu da bi se razlikovala vozila u skladu s tablicom klasifikacije vozila.
- predklasifikacija razdijeljuje odnosno detektira i pravilno kategorizira vozila prema odluci o visini cestarine sa parametrima visine na 1.3 m i 1.9 m. Za raspoznavanje druge od treće skupine vozila koncesionar može koristiti pomoćni kriterij ukupne visine od 2,80 - 3 m.
- detektira i klasificira vozila do brzine od 60 km/h.
- šalje upravljačko-procesnoj jedinici sve informacije o skupini vozila.
- osigurava dijagnostičke informacije o svakom uređaju instaliranom za klasifikaciju (tj. optičke zavjese, detektora petlje, uređaj za brojanje osovina, itd.).
- u stanju je obraditi najmanje 5.000.000 (pet milijuna) osovina prije greške.
- Predklasifikacija je instalirana na izlaznim prolazima i biti će kompatibilna s opremom naknadne klasifikacije vozila.
- točnost predklasifikacije je najmanje 99,5% u najgorim radnim uvjetima
- vrijeme razdvajanja između dva vozila je 12 ms ili bolje.
- projektirana je tako da zadrži točnost čak ako osovina vozila nije paralelna s osovinom gazila.
Princip raspoznavanja skupine vozila sukladno odluci o visini cestarine:
KRITERIJ
SKUPINA VOZILA
VISINA
BROJ OSOVINA
> 1,30 kod prve osovine
> 1,90 ukupna visina
2
3
4 i više
NE
NE
DA
NE
NE
1
NE
NE
DA
DA
NE
2
NE
NE
DA
DA
DA
2
NE
DA
DA
NE
NE
2
NE
DA
DA
DA
NE
3
NE
DA
DA
DA
DA
3
DA
NE
DA
NE
NE
1
DA
NE
DA
DA
NE
2
DA
NE
DA
DA
DA
2
DA
DA
DA
NE
NE
2
DA
DA
DA
DA
NE
3
DA
DA
DA
DA
DA
3
DA
DA
DA
NE
NE
3
DA
DA
DA
DA
NE
3
DA
DA
DA
DA
DA
4
Princip raspoznavanja skupine vozila s pomoćnim kriterijem:
KRITERIJ
SKUPINA VOZILA
VISINA
BROJ OSOVINA
> 1,30 kod prve osovine
> 1,90 ukupna visina
> 2,80 - 3,00 ukupna visina
2
3
4 i više
NE
NE
NE
DA
NE
NE
1
NE
NE
NE
DA
DA
NE
2
NE
NE
NE
DA
DA
DA
2
NE
DA
NE
DA
NE
NE
2
NE
DA
NE
DA
DA
NE
3
NE
DA
NE
DA
DA
DA
3
DA
NE
NE
DA
NE
NE
1
DA
NE
NE
DA
DA
NE
2
DA
NE
NE
DA
DA
DA
2
DA
DA
NE
DA
NE
NE
2
DA
DA
NE
DA
DA
NE
3
DA
DA
NE
DA
DA
DA
3
DA
DA
DA
DA
NE
NE
3
DA
DA
DA
DA
DA
NE
3
DA
DA
DA
DA
DA
DA
4
Svrha naknadne klasifikacije vozila je potvrda da skupina vozila koja je određena pretklasifikacijom ili koju je odabrao blagajnik odgovora stvarnoj skupini vozila. Ukoliko se skupine vozila određene predklasifikacijom ili odabirom blagajnika i naknadnom klasifikacijum razlikuju transakcija se prilikom pohrane u bazu podataka obilježava za potrebe naknadne provjere.
Specifikacija naknadne klasifikacije isti su kao i kod predklasifikacije.
e) Telekomunikacijska oprema i infrastruktura potrebna za prijenos EENC podataka unutar informacijskih sustava
Svaka lokacija na kojoj se nalazi bilo koji dio sustava EENC povezana je računalno komunikacijskom mrežom. Računalno komunikacijska mreža se temelji na TCP/IP protokolu i omogućava nesmetan prijenos podataka unutar EENC sustava svojom propusnošću. Svaka lokacija dizajnom mreže omogućava visoku raspoloživost odabirom opreme te njezinim redovitim održavanjem u režimu 24x7x365 i redundanciju sustava alternativnim putem (backup veze). Za ostvarivanje alternativnih putova (backup veza) koristi se drugi pravac telekomunikacijske infrastrukture poput iznajmljenih veza, vlastite infrastrukture položene sa suprotne strane kolnika, kriptiranih bežičnih veza i slično.
Računalno komunikacijska mreža kojom se odvija prijenos podataka unutar EENC sustava zatvorenog je tipa što znači da pristup podacima nije moguć iz drugih mreža koje se koriste za druge namjene, poput poslovnih sustava, telefonije i drugih.
Pristup računalno komunikacijskoj mreži sustava EENC kontroliran je i moguć samo osobama s posebnim dopuštenjem. Udaljen pristup (VPN) je kriptiran i koristi se IPsec protokolom ili jednakovrijednim.
f) Poslužitelj za prihvat podataka od pružatelja usluge EENC-a, odnosno za obradu i razmjenu podataka prikupljenih s ulaznih i izlaznih ENC staza prema pružatelju usluge EENC-a
Poslužitelj naplatne postaje prihvaća sve transakcije koje nastaju na izlaznim i ulaznim stazama, proslijeđene od upravljačko-procesne jedinice te iste pohranjuje u bazu podataka. Istovremeno neobrađene transakcije šalje prema centralnom poslužitelju. U normalnom režimu rada informacije sa upravljačko-procesnih jedinica se automatski i neovisno šalju na poslužitelj naplatne postaje i centralni poslužitelj. U degradiranom režimu rada podaci se pohranjuju na izlaznu ili ulaznu upravljačko-procesnu jedinicu gdje se čuvaju do povratka u normalni režim rada, odnosno uspostave komunikacije sa poslužiteljem kada će automatski poslati neprenesene podatke. Na oba poslužitelja transakcije se obrađuju neovisno jedna o drugoj. Pomoću radnih stanica na kojima su instalirane aplikacije za pristup bazama podataka pregledavaju se razni tipovi izvješća. Transakcije koje se razmjenjuju između pružatelja usluge EENC-a šalju se sa centralnog poslužitelja na poslužitelj za razmjenu kako bi ih druga strana mogla preuzeti i obraditi u svom sustavu.
g) Sustav za pohranu i arhivu podataka s rokom čuvanja podataka na period od najmanje 3 (tri) godine od dana nastanka transakcije iz usluge EENC-a
Pohrana i arhiva transakcija i slika prolaza vozila
Svaka pojedina transakcija i slika prolaza vozila nastala u sustavu za naplatu cestarine šalje se na poslužitelj sustava za pohranu i arhivu podataka na naplatnoj postaji. Ista se prosljeđuje na centralni arhivski sustav gdje se uvozi u sustav za upravljanje dokumentima i obrađuje. Sustav za pohranu i arhivu podataka omogućuje jednostavni i trenutni dostup podacima s naplatnih postaja vezanih uz kontrolu prolaza vozila kroz naplatne postaje.
Glavne funkcionalnosti sustava za pohranu i arhivu podataka su:
- Osiguravanje i zaštita podataka automatiziranim backup i arhivskim sustavom
- Unaprijed definirano vrijeme retencije i zadržavanja podataka
- Osiguranje od brisanja podataka prije isteka vremena čuvanja podataka
- On-line pristup arhiviranim podacima
- Brzo i efikasno pretraživanje
- Automatiziran proces
- Obavješćivanje sustava o potencijalnim i novonastalim problemima
Centralni arhivski sustav ima minimalno sljedeće karakteristike:
- sustav za upravljanje dokumentima omogućava automatiziran uvoz velikog broja dokumenata na dnevnoj razini (>30 000 dokumenata dnevno)
- sustav podržava automatsko, dugotrajno i sigurno arhiviranje velike količine podataka
- sustav omogućava pretragu svih uvezenih dokumenata na osnovi metapodataka definiranih na dokumentima prilikom njihovog uvoza
- sustav omogućava uvid u sadržaj (sliku dokumenta) za sve uvezene dokumente
- sustav omogućava kvalitetan pristup spremljenim dokumentima za barem 15 korisnika sustava
- sustav omogućava siguran pristup dokumentima tj. samo korisnici s potrebnim dozvolama smiju pretraživati i pregledavati dokumente uvezene u sustav
- Sustav osigurava dohvat podataka za manje od 1 sekunde.
Pohrana i arhiva centralne baze podataka
Centralna baza podataka arhivira se min. 3 god na pouzdan način (npr. trake, storage).
h) Prateća oprema i infrastruktura koja mora osigurati odgovarajući stupanj zaštite opreme i aplikacija koje se koriste u sustavu pružanja usluge EENC-a
Prateća oprema ENC antenskog sustava smještena je u posebno dizajniranim ormarima u naplatnim kućicama ili na prometnim otocima između naplatnih staza, dok se poslužitelji nalaze u server salama u pratećem objektu na naplatnoj postaji.
Ormar za smještaj opreme izrađen je od obojenog čelika visoko otpornog na teške uvjete radne okoline, kemijske čestice, prašinu, vrućinu i vlagu. U ormaru je instalirana oprema ulazne ili izlazne staze te upravljačko procesna jedinica. Uređaj za ventilaciju osigurava reguliranu temperaturu i vlagu u ormaru, a projektiran je tako da unutar ormara osigurava viši tlak zraka od vanjskog te sprječava ulazak prašine u ormar.
U pratećem objektu na naplatnoj postaji nalazi se prostorija za smještaj informatičke opreme (server sala) u kojoj su smješteni poslužitelji sustava za naplatu cestarine. U prostorijama su instalirani klima uređaji koji osiguravaju optimalnu temperaturu za rad informatičke opreme. Poslužitelji sustava za naplatu cestarine smješteni su u server ormare.
Kako bi se izbjegla opasnost od nestanka električne energije, a samim time i prestanak rada sustava za naplatu cestarine, na svakoj naplatnoj postaji nalazi se uređaj za besprekidno napajanje (UPS uređaj) koji osigurava autonomiju rada sustava od minimalno 30 minuta. Isto tako na svakoj naplatnoj postaji nalazi se agregat ili sličan rezervni izvor el. energije koji se automatski pokreće nakon nestanka električne energije.
74 19.06.2013 Pravilnik o posebnim uvjetima i tehničkim zahtjevima za Europsku elektroničku naplatu cestarine i elementima interoperabilnosti 74 19.06.2013 Pravilnik o posebnim uvjetima i tehničkim zahtjevima za Europsku elektroničku naplatu cestarine i elementima interoperabilnosti
