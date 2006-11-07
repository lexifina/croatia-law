# Članak 5.
Prilog 3. - FORMAT ZA DOSTAVLJANJE OBRASCA R-Sm NA MAGNETNOM NOSITELJU (»MN OBRAZAC R-Sm«), mijenja se i glasi:
PRILOG 3.
FORMAT SLOGA ZA DOSTAVLJANJE OBRASCA R-Sm U ELEKTRONSKOM ZAPISU(FORMAT »EZ OBRAZAC R-Sm«)
Ovaj format služi za predaju podataka s Obrasca R-Sm u elektronskom obliku. Koristi se za sve vrste obračuna/ispravka, osim za vrstu 88 (ispravak podataka na stranici A) za koju se obrazac predaje isključivo u papirnom obliku.
OPIS, SADRŽAJ I STRUKTURA FORMATA »EZ OBRAZAC R-Sm«:
Svaki format »EZ OBRAZAC R-Sm« sastoji se od sljedećih tipova slogova:
- Tip sloga »0« - POČETNI SLOG FORMATA
- Tip sloga »3« - POČETNI SLOG JEDNOG OBRASCA R-Sm U FORMATU
- Tip sloga »5« - SLOG POJEDINAČNE TRANSAKCIJE OBRASCA R-Sm
- Tip sloga »7« - ZAVRŠNI SLOG JEDNOG OBRASCA R-Sm U FORMATU
- Tip sloga »9« - ZAVRŠNI SLOG FORMATA.
U daljnjem tekstu dan je opis, sadržaj i struktura svakog od navedenih tipova slogova prema zahtjevanim poljima u slogu. Sva polja tipa N poravnavaju se desno i upisuju s vodećim nulama. Sva polja tipa C poravnavaju se lijevo. Ako pravila za popunjavanje pojedinog Obrasca R-Sm ne zahtjevaju popunjenost nekih polja, takva polja tipa N treba popuniti s nulama, a polja tipa C s prazninama (blankovima)
KONTROLNI BROJ FORMATA »EZ OBRAZAC R-Sm«:
U slučaju kada se obrazac predaje na magnetnom nositelju za cijeli format »EZ OBRAZAC R-Sm« (sadržaj svih slogova) potrebno je generirati kontrolni broj (HASH) i ovaj broj treba upisati na stranicu A Obrasca R-Sm koja se predaje na papiru (ili više stranica A, ako format sadrži više Obrazaca R-Sm). Upute za generiranje kontrolnog broja dane su u prilogu 2 ovog pravilnika.
ZAHTJEVANA OBILJEŽJA FORMATA »EZ OBRAZAC R-Sm«:
n Format »EZ OBRAZAC R-Sm«, kada se predaje na magnetnom nositelju, podnosi se na DISKETI 3.5'' u obliku ASCII (tekst) datoteke. Ako je predajno mjesto opremljeno čitačem CD medija, podaci se mogu predati i na CD-u.
n Svaki redak u datoteci treba zaključiti s kodnom sekvencom Hex(0D)+Hex(0A) = CR+LF. Ovaj zapis treba dodati iza zadnjeg polja u svakom retku (iza polja: Tip sloga).
n Preporuka je zapis ostvariti u kodnoj stranici (CP = 1250). Za obradni sustav ovo je predodređena kodna stranica kojom se osigurava ispravno interpretiranje svih znakova tijekom faza obrade i u izvještajima. Ako je zapis u datoteci pripremljen pod nekom drugom kodnom stranicom, tada će postupak formalne kontrole podataka zamjeniti znakom »#« dijakritičke znakove (ŠĐČĆŽšđčćž) koji se ne mogu kvalitetno interpretirati.
IME DATOTEKE KOJA SADRŽI FORMAT »EZ OBRAZAC R-Sm«:
Ime datotke treba biti u obliku REGOS.RMx, gdje je:
REGOS = konstanta
RM = konstanta;
x = redni broj datoteke (0 - 9)
1. POČETNI SLOG FORMATA - tip sloga 0
Ovaj tip sloga određuje početak nekog formata. Pojavljuje se samo jednom u formatu, uvijek kao prvi slog u formatu.
Podatak u polju RS0MBOO - MB obveznika/ovlaštene osobe, odnosno podatak u polju RS0MBGO - MBG obveznika/ovlaštene osobe je jedinstveno obilježje kojim je određen obveznik/ovlaštena osoba podnošenja OBRASCA R-Sm. To je identifikator pravne, odnosno fizičke osobe koja je formirala format (identifikator obveznika - ako sam formira i podnosi obrazac, odnosno identifikator ovlaštene pravne ili fizičke osoba - ako formira i podnosi obrazac za jednog ili više svojih komintenata). Obvezno se popunjava ili jedan ili drugi podatak, a u nekim slučajevima dozvoljeno je popuniti i oba ova podatka, ovisno o tipu obveznika/ovlaštene osobe.
- Ako se popunjava polje RS0MBOO, kontrolna znamenka nalazi se na 8. mjestu. Ako matični broj ima manje od 8 znamenka, upisuju se vodeće nule. Ako se radi o središnjem poslovnom subjektu, mjesta od 9 do 12 popunjavaju se nulama. Ako se radi o jedinici u sastavu središnjeg poslovnog subjekta, mjesta od 9 do 12 popunjavaju se rednim brojem te jedinice u sastavu s vodećim nulama.
- Ako se popunjava polje RS0MBGO kontrolna znamenka nalazi se na 13. mjestu.
|  |  |  | r. br. polja
|  |  |  | naziv polja
|  |  |  | opis polja
|  |  |  | tip polja
|  |  |  | od
|  |  |  | do
|  |  |  | broj mjesta
|  | 1.
|  | RS0MBOO
|  | MB obveznika/ovlaštene osobe
|  | N
|  | 1
|  | 12
|  | 12
|  | 2.
|  | RS0MBGO
|  | MBG obveznika/ovlaštene osobe
|  | N
|  | 13
|  | 25
|  | 13
|  | 3.
|  | RS0NAOB
|  | Naziv/prezime i ime obveznika/ovlaštene |  | osobe
|  | C
|  | 26
|  | 75
|  | 50
|  | 4.
|  | RS0ADOB
|  | Adresa obveznika/ovlaštene osobe
|  | C
|  | 76
|  | 125
|  | 50
|  | 5.
|  | RS0OSOB
|  | Ime i prezime osobe za kontakt
|  | C
|  | 126
|  | 175
|  | 50
|  | 6.
|  | RS0TELE
|  | Broj telefona za kontakt
|  | C
|  | 176
|  | 185
|  | 10
|  | 7.
|  | RS0MAIL
|  | Adresa elektronske pošte za kontakt
|  | C
|  | 186
|  | 215
|  | 30
|  | 8.
|  | RS0DTMN
|  | Datum formiranja formata (DMMGGGG)
|  | N
|  | 216
|  | 223
|  | 8
|  | 9.
|  | RS0OFOR
|  | Oznaka formata ("RM
|  | 500")
|  | C
|  | 224
|  | 228
|  | 5
|  | 10.
|  | RS0REZE
|  | Rezerva (prazno)
|  | C
|  | 229
|  | 249
|  | 21
|  | 11.
|  | RS0TIPS
|  | Tip sloga ("0")
|  | N
|  | 250
|  | 250
|  | 1
2. POČETNI SLOG JEDNOG OBRASCA R-Sm U FORMATU - tip sloga 3
Ovaj tip sloga određuje početak jednog OBRASCA R-Sm u formatu. Pojavljuje se onoliko puta u formatu koliko je različitih OBRAZACA R-Sm u formatu, uvijek kao prvi slog svakog OBRASCA R-Sm u formatu.
Podaci u poljima: RS3MBOO i RS3MBGO popunjavaju se prema prethodno navedenim pravilima za popunjavanje podataka u poljima: RS0MBOO i RS0MBGO kod sloga tipa 0, s time da se u slogu tipa 3 uvijek popunjavaju podaci obveznika.
Podaci u poljima za iznose popunjavaju se u kunama s lipama, u duljini od 15 znakova i zaokruženi na dvije decimale. Decimalni zarez se ne upisuje (zadnje dvije znamenke označavaju decimalne vrijednosti, odnosno lipe). Svi iznosi se obvezno upisuju s vodećim nulama, s time da prvi znak u svakom polju za iznos može biti i znak »+«.
|  | r. br. polja
|  | naziv polja
|  | opis polja
|  | tip polja
|  | od
|  | do
|  | broj
|  | mjesta
|  | 1.
RS3MBOO
MB obveznika
|  | N
|  | 1
|  | 12
|  | 12
|  | 2.
RS3MBGO
MBG obveznika
|  | N
|  | 13
|  | 25
|  | 13
|  | 3.
RS3RBSU
Identifikator |  | obrasca
|  | N
|  | 26
|  | 29
|  | 4
|  | 4.
RS3NAOB
Naziv/Prezime i ime |  | obveznika
|  | C
|  | 30
|  | 79
|  | 50
|  | 5.
RS3ADOB
Adresa obveznika
|  | C
|  | 80
|  | 129
|  | 50
|  | 6.
RS3VROB
Vrsta obveznika
|  | N
|  | 130
|  | 131
|  | 2
|  | 7.
RS3MMGG
Mjesec i godina za |  | koje se podnose podaci
(MMGGGG)
|  | N
|  | 132
|  | 137
|  | 6
|  | 8.
RS3VROI
Vrsta |  | obračuna/ispravka
|  | N
|  | 138
|  | 139
|  | 2
|  | 9.
RS3BROS
Broj osiguranika za |  | koje se podnosi Obrazac R-Sm
|  | (broj različitih MBG osiguranika)
|  | N
|  | 140
|  | 144
|  | 5
|  | 10.
RS3IBRT
|  | Iznos obračunane |  | plaće/naknade/drugog dohotka
|  | N
|  | 145
|  | 159
|  | 15
|  | 11.
RS3IOSN
Iznos osnovice za |  | obračun doprinosa za MO
|  | N
|  | 160
|  | 174
|  | 15
|  | 12.
RS3IST1
Iznos obračunanog |  | doprinosa za I. stup MO
|  | N
|  | 175
|  | 189
|  | 15
|  | 13.
RS3IST2
Iznos obračunanog |  | doprinosa za II. stup MO
|  | N
|  | 190
|  | 204
|  | 15
|  | 14.
RS3INET
Iznos isplaćene |  | plaće/naknade/drugog dohotka
|  | N
|  | 205
|  | 219
|  | 15
|  | 15.
RS3IGMM
Godina i mjesec |  | isplate plaće/naknade/drugog dohotka (GGGGMM)
|  | N
|  | 220
|  | 225
|  | 6
|  | 16.
RS3REZE
Rezerva (prazno)
|  | C
|  | 226
|  | 249
|  | 24
|  | 17.
RS3TIPS
Tip sloga (»3«)
|  | N
|  | 250
|  | 250
|  | 1
3. SLOG POJEDINAČNE TRANSAKCIJE OBRASCAR-Sm - tip sloga 5
Ovaj tip sloga određuje pojedinačne podatke nekog osiguranika u nekom razdoblju s istom osnovom obračuna. Pojavljuje se barem onoliko puta u formatu koliko je različitih OBRAZACA R-Sm u formatu koji sadržavaju podatke za tog osiguranika, odnosno onoliko puta u jednom OBRASCU R-Sm koliko je različitih kombinacija osnova obračuna i razdoblja s istom osnovom obračuna za tog osiguranika u razdoblju za koje se podnosi taj OBRAZAC R-Sm.
Ako se podaci za nekog osiguranika na istom Obrascu R-Sm javljaju u više slogova ovog tipa (više redova), polje za redni broj osiguranika (RS5RBRO) ima isti sadržaj u svakom slogu s podacima za tog osiguranika (isti osiguranik tj. isti MBG ima uvijek isti redni broj na jednom obrascu i taj isti redni broj se obvezatno upisuje u svakom od slogova za taj MBG).
Podaci trebaju biti sortirani uzlazno prema rednom broju, a unutar istog rednog broja prema razdoblju. Zadnji redni broj mora odgovarati sadržaju polja RS3BROS u slogu tipa 3.
Podaci u poljima za iznose popunjavaju se prema prethodno navedenim pravilima za popunjavanje iznosa kod sloga tipa 3.
|  | r. br. polja
|  | naziv polja
|  | opis polja
|  | tip polja
|  | od
|  | do
|  | broj mjesta
|  | 1.
|  | RS5RBRO
Redni broj |  | osiguranika na Obrascu R-Sm
|  | N
|  | 1
|  | 5
|  | 5
|  | 2.
|  | RS5MBGO
MBG osiguranika
|  | N
|  | 6
|  | 18
|  | 13
|  | 3.
|  | RS5PRIM
|  | Prezime i ime |  | osiguranika
|  | C
|  | 19
|  | 48
|  | 30
|  | 4.
|  | RS5GROP
Šifra općine/grada |  | rada
|  | N
|  | 49
|  | 52
|  | 4
|  | 5.
|  | RS5OSOB
Osnova obračuna: |  | OO(2)
|  | +B(1)
|  | N
|  | 53
|  | 55
|  | 3
|  | 6.
|  | RS5RAZD
Razdoblje s istom |  | osnovom obračuna (ddDD)
|  | N
|  | 56
|  | 59
|  | 4
|  | 7.
|  | RS5IBRT
Iznos obračunane |  | plaće/naknade/drugog dohotka
|  | N
|  | 60
|  | 74
|  | 15
|  | 8.
|  | RS5IOSN
Iznos osnovice za |  | obračun doprinosa za MO
|  | N
|  | 75
|  | 89
|  | 15
|  | 9.
|  | RS5IST1
Iznos obračunanog |  | doprinosa za I. stup MO
|  | N
|  | 90
|  | 104
|  | 15
|  | 10.
|  | RS5IST2
Iznos obračunanog |  | doprinosa za II. stup MO
|  | N
|  | 105
|  | 119
|  | 15
|  | 11.
|  | RS5INET
Iznos isplaćene |  | plaće/naknade/drugog dohotka
|  | N
|  | 120
|  | 134
|  | 15
|  | 12.
|  | RS5REZE
Rezerva (prazno)
|  | C
|  | 135
|  | 249
|  | 115
|  | 13.
|  | RS5TIPS
Tip sloga (»5«)
|  | N
|  | 250
|  | 250
|  | 1
4. ZAVRŠNI SLOG JEDNOG OBRASCA R-Sm U FORMATU - tip sloga 7
Ovaj tip sloga određuje kraj jednog OBRASCA R-Sm u formatu. Pojavljuje se onoliko puta u formatu koliko je različitih OBRAZACA R-Sm u formatu, uvijek kao zadnji slog svakog OBRASCA R-Sm u formatu.
Podaci u poljima: RS7MBOO, RS7MBGO i RS7RBSU moraju odgovarati podacima u poljima RS3MBOO, RS3MBGO i RS3RBSU kod sloga tipa 3.
|  | r. br. polja
|  | naziv polja
|  | opis polja
|  | tip polja
|  | od
|  | do
|  | broj mjesta
|  | 1.
|  | RS7MBOO
MB obveznika
|  | N
|  | 1
|  | 12
|  | 12
|  | 2.
|  | RS7MBGO
MBG obveznika
|  | N
|  | 13
|  | 25
|  | 13
|  | 3.
|  | RS7RBSU
Identifikator |  | obrasca
|  | N
|  | 26
|  | 29
|  | 4
|  | 4.
|  | RS7BRSL
Broj slogova tipa 5 |  | koji se pojavljuju u obrascu čiji je ovo zadnji slog
|  | N
|  | 30
|  | 34
|  | 5
|  | 5.
|  | RS7DTRS
Datum formiranja |  | obrasca R-Sm (DDMMGGGG)
|  | N
|  | 35
|  | 42
|  | 8
|  | 6.
|  | RS7REZE
Rezerva (prazno)
|  | C
|  | 43
|  | 249
|  | 207
|  | 7.
|  | RS7TIPS
Tip sloga (»7«)
|  | N
|  | 250
|  | 250
|  | 1
5. ZAVRŠNI SLOG FORMATA - tip sloga 9
Ovaj tip sloga određuje kraj nekog formata. Pojavljuje se samo jednom u svakom formatu, uvijek kao zadnji slog u formatu.
Podaci u poljima: RS9MBOO, RS9MBGO i RS9DTMN moraju odgovarati podacima u poljima RS0MBOO, RS0MBGO i RS0DTMN kod sloga tipa 0.
Podatak u polju RS9BROJ mora odgovarati broju pojavljivanja slogova tipa 3, odnosno broju pojavljivanja slogova tipa 7 u tom formatu.
|  | r. br. polja
|  | naziv polja
|  | opis polja
|  | tip polja
|  | od
|  | do
|  | broj mjesta
|  | 1.
|  | RS9MBOO
MB |  | obveznika/ovlaštene osobe
|  | N
|  | 1
|  | 12
|  | 12
|  | 2.
|  | RS9MBGO
MBG |  | obveznika/ovlaštene osobe
|  | N
|  | 13
|  | 25
|  | 13
|  | 3.
|  | RS9DTMN
Datum formiranja |  | formata (DDMMGGGG)
|  | N
|  | 26
|  | 33
|  | 8
|  | 4.
|  | RS9BROJ
Broj Obrazaca R-Sm |  | u formatu
|  | N
|  | 34
|  | 39
|  | 6
|  | 5.
|  | RS9REZE
Rezerva 1 (prazno)
|  | C
|  | 40
|  | 121
|  | 82
|  | 6.
|  | RS9DIGP
Rezerva 2 (prazno)
|  | C
|  | 122
|  | 249
|  | 128
|  | 7.
|  | RS9TIPS
Tip sloga ("9")
|  | N
|  | 250
|  | 250
|  | 1
