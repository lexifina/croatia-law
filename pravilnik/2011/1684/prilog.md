PRILOG 1
POJAŠNJENJE O PODNOŠENJU PROVOZNIH DEKLARACIJA PUTEM ELEKTRONIČKE RAZMJENE STANDARDNIH PORUKA
(ELEKTRONIČKA PROVOZNA DEKLARACIJA)
Glava I.
OPĆENITO
Provozna deklaracija se podnosi elektroničkim putem, osim kada Carinski zakon i Uredba za provedbu Carinskog zakona predviđaju drukčije.
Elektronička provozna deklaracija temelji se na pojedinostima vezanim za različita polja jedinstvene carinske deklaracije (JCD-a) u smislu Pravilnika o uporabi obrazaca pri provedbi Carinskog zakona, kojima se dodaju ili koja se zamjenjuju oznakama i šiframa sukladno ovom Prilogu i Prilogu 2 ovoga Pravilnika, ako je to prikladno.
Ovaj Prilog sadrži isključivo osnovne posebne zahtjeve koji se primjenjuju kada se formalnosti provoza obavljaju elektroničkom razmjenom standardnih poruka. Nadalje, dodatne šifre koje se primjenjuju navedene su u Prilogu 2 ovoga Pravilnika.
Pobliža struktura poruka i sadržaj elektroničke provozne deklaracije slijede tehničke specifikacije koje nadležna tijela priopćavaju glavnom obvezniku kako bi se osiguralo ispravno funkcioniranje sustava. Te specifikacije se temelje na zahtjevima propisanim ovim Prilogom.
Ovaj Prilog opisuje strukturu razmjene podataka. Provozna deklaracija je strukturirana u grupama podataka koje sadrže dodatne podatke (atribute). Podaci (atributi) su grupirani tako da tvore jednstvene logičke blokove u okviru poruke. Uvučenost odlomka s grupom podataka znači da grupa podataka ovisi o grupi podataka donjeg odlomka.
Ako postoji, upisuje se odgovarajući broj polja na JCD-u.
Izraz »broj« u objašnjenju grupe podataka označava koliko se puta grupa podataka može koristiti u provoznoj deklaraciji.
Izraz »tip/duljina«" u objašnjenju podataka (atributa) označava zahtjeve za tip podataka i duljinu podataka. Šifre za tipove podataka su sljedeće:
a slovna (alfa)
n brojčana (numerička)
an slovno-brojčana (alfanumerička)
Broj nakon šifre označava dopuštenu duljinu podataka. Primjenjuje se sljedeće:
Opcionalne dvije točke prije pokazivača duljine znače da podaci nemaju utvrđenu duljinu, ali mogu imati do određenog broja znamenaka, koji određuje pokazivač duljine. Zarez u duljini podataka znači da podatak (atribut) može sadržavati decimale, znamenka prije zareza označava ukupnu duljinu podatka (atributa), a znamenka nakon zareza označava najveći mogući broj znamenki nakon decimalne točke.
Glava II.
PODACI KOJI SE UPISUJU U PROVOZNU DEKLARACIJU I STRUKTURA ELEKTRONIČKE PROVOZNE DEKLARACIJE
Poglavlje I.
POTREBNI PODACI
Ovaj Prilog sadrži potrebne podatke za postupak provoza koji su utemeljeni na podacima koji se koriste pri popunjavanju JCD-a.
Poglavlje II.
STRUKTURA
A. Tablica grupa podataka
PROVOZNA OPERACIJA
GOSPODARSKI SUBJEKT pošiljatelj
GOSPODARSKI SUBJEKT primatelj
ROBNA STAVKA
- GOSPODARSKI SUBJEKT pošiljatelj
- GOSPODARSKI SUBJEKT primatelj
- KONTEJNERI
- OZNAKE ZA OSJETLJIVU ROBU (SGI)
- PAKIRANJA
- PRETHODNE ISPRAVE
- PREDOČENE ISPRAVE/POTVRDE
- POSEBNE NAPOMENE
Otpremna CARINARNICA
GOSPODARSKI SUBJEKT glavni obveznik
ZASTUPNIK
Provozna CARINARNICA
Odredišna CARINARNICA
GOSPODARSKI SUBJEKT ovlašteni primatelj
REZULTAT KONTROLE
PODACI O PLOMBAMA
- OZNAKA (ID) PLOMBI
JAMSTVO
- OZNAKA JAMSTVA
B. Pojedinosti o podacima provozne deklaracije
PROVOZNA OPERACIJA
Broj: 1
Grupa podataka je obvezna.
LRN
Tip/duljina: an..22
Koristi se lokalni referentni broj (LRN). Dodjeljuje ga korisnik prema sljedećoj strukturi kako bi se mogla identificirati svaka pojedinačna deklaracija:
Polje
Sadržaj
Vrsta polja
Primjeri
1
Osobni identifikacijski broj (OIB)
Brojčano 11
12378945612
3
Posljednje dvije znamenke godine u kojoj je deklaracija podnesena (GG)
Brojčano 2
11
4
Jedinstvena identifikacijska oznaka za provoznu pošiljku po godini i gospodarstveniku
Brojčano 9
000123456
Vrsta deklaracije
(polje 1)
Tip/duljina: an..5
Podatak (atribut) je obvezan.
Obvezno se unosi sljedeće:
(1) ako je zahtijevano kretanje domaće robe u sklopu postupka T2: T2;
(2) ako je zahtjevano kretanje strane robe u sklopu postupka T1: T1;
(3) za mješovite pošiljke koje sadrže domaću i stranu robu: T-.
Podatak (atribut) je obvezan.
Ukupan broj stavki
(polje 5)
Tip/duljina: n..5
Podatak (atribut) je obvezan.
Ukupan broj paketa
(polje 6)
Tip/duljina: n..7
Korištenje ovog podatka (atributa) nije obvezno. Ukupni broj paketa jednak je zbroju svih paketa navedenih u poljima »Broj paketa«, »Broj komada« plus vrijednost od »1« za svako deklarirano pakiranje robe »u rasutom stanju«.
Otpremna zemlja
(polje 15a)
Tip/duljina: a2
Zemlja iz koje se roba otprema/izvozi
Podatak (atribut) se koristi ako je deklarirana samo jedna otpremna zemlja. Koriste se šifre zemalja navedene u Prilogu 2. U tom slučaju ne može se koristiti podatak (atribut) »Otpremna zemlja« grupe podataka »ROBNA STAVKA«. Ako je deklarirano više od jedne otpremne zemlje, ta se oznaka (atribut) grupe podataka »PROVOZNA OPERACIJA« ne može koristiti. U tom slučaju koristi se oznaka (atribut) »Otpremna zemlja« grupe podataka »ROBNA STAVKA«.
Odredišna zemlja
(polje 17)
Tip/duljina: a2
Podatak (atribut) se koristi ako je deklarirana samo jedna odredišna zemlja. Koriste se šifre zemlje navedene u Prilogu 2. U tom slučaju ne može se koristiti podatak (atribut) »Odredišna zemlja« grupe podataka »ROBNA STAVKA«. Ako je deklarirano više od jedne odredišne zemlje, ta se oznaka (atribut) grupe podataka »PROVOZNA OPERACIJA« ne može koristiti. U tom slučaju koristi se oznaka (atribut) »Odredišna zemlja« grupe podataka »ROBNA STAVKA«.
Identitet na mjestu otpreme (polaska)
(polje 18)
Tip/duljina: an..27
Upisuju se identifikacijske oznake, npr. registracijski broj/brojevi ili naziv prijevoznog sredstva (kamiona, broda, željezničkog vagona, zrakoplova) u koje je roba izravno utovarena prilikom podnošenja otpremnoj carinarnici, koristeći šifre određene za tu svrhu. Na primjer, ako se koriste tegljač i prikolica s različitim registracijskim brojevima, upisuju se registracijski brojevi obaju vozila.
Međutim, ako se roba prevozi u kontejnerima predviđenima za prijevoz na cestovnim vozilima, nadležna tijela mogu dopustiti glavnom obvezniku da ostavi ovo polje prazno kada logistika na mjestu otpreme nije u mogućnosti pribaviti identitet prijevoznog sredstva u trenutku sastavljanja provozne deklaracije i ako mogu osigurati da će odgovarajuće informacije o prijevoznom sredstvu nakon toga biti upisane u polje 55.
Ako se roba prevozi nepokretnim prijevoznim instalacijama (cjevovodi,..), registracijski broj se ne upisuje.
Identitet na mjestu otpreme LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se odgovarajuće slobodno polje koristi za unos teksta.
Nacionalnost na mjestu otpreme
(polje 18)
Tip/duljina: a2
Koristi se šifra zemlje navedena u Prilogu 2.
Upisuje se nacionalna pripadnost prijevoznog sredstva (broda, kamiona, željezničkog vagona, zrakoplova) na koje je roba izravno utovarena prilikom podnošenja otpremnoj carinarnici (ili nacionalna pripadnost prijevoznog sredstva koje osigurava pogon za cjelinu ako se ona sastoji od nekoliko prijevoznih sredstava), koristeći šifre određene za tu svrhu. Na primjer, ako se koriste tegljač i prikolica s različitim registracijskim brojevima, upisuju se registracijski brojevi obaju vozila i nacionalnost tegljača.
Međutim, ako se roba prevozi u kontejnerima predviđenima za prijevoz na cestovnim vozilima, nadležna tijela mogu dopustiti glavnom obvezniku da ostavi ovo polje prazno kada logistika na mjestu otpreme nije u mogućnosti pribaviti podatke o nacinalnosti prijevoznog sredstva u trenutku sastavljanja provozne deklaracije i ako mogu osigurati da će odgovarajuće informacije o prijevoznom sredstvu biti naknadno upisane u polje 55.
Ako se roba prevozi nepokretnim prijevoznim instalacijama ili željeznicom, ne upisuje se podaci o nacinalnosti prijevoznog sredstva.
U drugim slučajevima, deklariranje nacionalnosti nije obvezno.
Kontejner
(polje 19)
Tip/duljina: n1
Koriste se šifre predviđene za potrebe unošenja pojedinosti o pretpostavljenom stanju na granici, utemeljene na informacijama raspoloživim u vrijeme stavljanja robe u provozni postupak.
Koriste se sljedeće šifre:
0: ne.
1: da.
Nacionalnost pri prelasku granice
(polje 21)
Tip/duljina: a2
Obvezno se upisuje nacionalnost prijevoznog sredstva.
Međutim, kada se roba prevozi željeznicom ili nepokretnim instalacijama, ništa se ne upisuje pod registracijski broj ili nacinalnost.
Koristi se šifra zemlje navedena u Prilogu 2.
Identitet pri prelasku granice
(polje 21)
Tip/duljina: an..27
Koristeći odgovarajuću šifru, unosi se vrsta (brod, kamion, željeznički vagon, zrakoplov, itd.) i sredstvo identifikacije (npr. registracijski broj ili ime) aktivnog prijevoznog sredstva (tj. prijevoznog sredstva koje osigurava pogon) za koje se pretpostavlja da će se koristiti pri prelasku granice, nakon čega slijedi šifra nacionalnosti prijevoznog sredstva u vrijeme stavljanja robe u zajednički provozni postupak.
Ako se koristi kombinirani prijevoz ili nekoliko prijevoznih sredstava, aktivno prijevozno sredstvo predstavlja jedinicu koja osigurava pogon za cijelu prijevoznu kombinaciju. Na primjer, kada se kamion nalazi na brodu morske plovidbe, aktivno je prijevozno sredstvo brod, a kada se koristi kombinacija tegljača i prikolice, aktivno prijevozno sredstvo je tegljač.
Ako se roba prevozi željeznicom ili nepokretnim instalacijama, ne upisuju se podaci o registracijskom broju.
Identitet pri prelasku granice LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se odgovarajuće slobodno polje koristi za unos teksta.
Vrsta prijevoza pri prelasku granice
(polje 21)
Tip/duljina: n..2
Vrsta prijevoza na granici
(polje 25)
Tip/duljina: n..2
Koriste se šifre predviđene za vrstu prijevoza kojima se označava vrstu aktivnog prijevoznog sredstva za koji se pretpostavlja da će na njemu roba napustiti carinsko područje.
Korištenje ovog podatka (atributa) nije obvezno.
Vrsta unutarnjeg prijevoza
(polje 26)
Tip/duljina: n..2
Korištenje ovog podatka (atributa) nije obvezno. Mora se koristiti u skladu s pojašnjenjem u vezi s poljem 25 navedenim u Prilogu 2.
Mjesto utovara
(polje 27)
Tip/duljina: an..17
Korištenje ovog podatka (atributa) nije obvezno.
Šifra dogovorenog mjesta robe
(polje 30)
Tip/duljina: an..17
Podatak (atribut) se ne može koristiti ako se koristi grupa podataka »REZULTAT KONTROLE«. Ako se ne koristi ta grupa podataka, korištenje podatka (atributa) nije obvezno. Ako se podatak (atribut) koristi, potrebno je u šifriranom obliku točno naznačiti mjesto na kojem se roba može pregledati. Podaci (atributi) »Dogovoreno mjesto robe«/»Šifra dogovorenog mjesta«, »Odobreno mjesto robe« i »Drugo carinsko mjesto« ne mogu se koristiti istovremeno.
Dogovoreno mjesto robe
(polje 30)
Tip/duljina: an..35
Podatak (atribut) se ne može koristiti ako se koristi grupa podataka »REZULTAT KONTROLE«. Ako se ta grupa podataka ne koristi, korištenje podatka (atributa) nije obvezno. Ako se podatak (atribut) koristi potrebno je točno naznačiti mjesto na kojem se roba može pregledati. Podaci (atributi) »Dogovorena mjesto robe«/»Šifra dogovorenog mjesta«, »Odobreno mjesto robe« i »Drugo carinsko mjesto« ne mogu se koristiti istovremeno.
Dogovoreno mjesto robe LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se odgovarajuće slobodno polje koristi za unos teksta.
Odobreno mjesto robe
(polje 30)
Tip/duljina: an..17
Uporaba podatka (atributa) nije obvezna ako se koristi grupa podataka »REZULTAT KONTROLE«. Ako se podatak (atribut) koristi, potrebno je točno naznačiti mjesto na kojem se roba može pregledati. Ako se grupa podataka »REZULTAT KONTROLE« ne koristi, ni podatak (atribut) se ne može koristiti. Podaci (atribut) i »Dogovorena mjesto robe«/»Šifra dogovorenog mjesta«, »Odobreno mjesto robe« i »Drugo carinsko mjesto« ne mogu se koristiti istovremeno.
Drugo carinsko mjesto
(polje 30)
Tip/duljina: an..17
Podatak (atribut) se ne može koristiti ako se koristi grupa podataka »REZULTAT KONTROLE«. Ako se ta grupa podataka ne koristi, korištenje podatka (atributa) nije obvezno. Ako se (podatak) atribut koristi, potrebno je točno naznačiti mjesto na kojem se roba može pregledavati. Podaci (atributi) »Dogovorena mjesto robe«/»Šifra dogovorenog mjesta«, »Odobreno mjesto robe« i »Drugo carinsko mjesto« ne mogu se koristiti istovremeno.
Ukupna bruto-masa
(polje 35)
Tip/duljina: n..11,3
Podatak (atribut) je obvezan.
Šifra jezika NCTS Prateće provozne isprave.
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika Prateće provozne isprave
Pokazatelj govornog jezika na mjestu otpreme
Tip/duljina: a2
Korištenje šifre jezika navedene u Prilogu 2 nije obvezno.
Datum deklaracije
(polje 50)
Tip/duljina: n8
Podatak (atribut) je obvezan.
Mjesto deklaracije
(polje 50)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Mjesto deklaracije LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) pripadajućeg slobodnog polja za unos teksta.
GOSPODARSKI SUBJEKT pošiljatelj (polje 2)
Broj: 1
Ova grupa podataka koristi se kada je deklariran samo jedan pošiljatelj. U tom slučaju ne može se koristiti grupa podataka »GOSPODARSKI SUBJEKT pošiljatelj« grupe podataka »ROBNA STAVKA«.
Naziv
(polje 2)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Ulica i broj
(polje 2)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Zemlja
(polje 2)
Tip/duljina: a2
Koristi se šifra zemlje navedena u Prilogu 2.
Poštanski broj
(polje 2)
Tip/duljina: an..9
Podatak (atribut) je obvezan.
Grad
(polje 2)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
NAD LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika naziva i adrese (NAD LNG).
IDENTIFIKACIJSKI BROJ GOSPODARSKOG
SUBJEKTA (TIN)
(polje 2)
Tip/duljina: an..17
Korištenje ovog podatka (atributa) za upisivanje identifikacijskog broja gospodarskog subjekta (TIN-a) nije obvezno. Kada je gospodarski subjekt domaća osoba koristi se OIB.
GOSPODARSKI SUBJEKT Primatelj
(polje 8)
Broj: 1
Grupa podataka koristi se kada je deklariran samo jedan primatelj i kada podatak (atribut) »Odredišna zemlja« grupe podataka »PROVOZNA OPERACIJA« sadrži navedenu »zemlju«. U tom slučaju ne može se koristiti grupa podataka »GOSPODARSKI SUBJEKT Primatelj« grupe podataka »ROBNA STAVKA«.
Naziv
(polje 8)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Ulica i broj
(polje 8)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Zemlja
(polje 8)
Tip/duljina: a2
Koristi se šifra zemlje navedena u Prilogu 2.
Poštanski broj
(polje 8)
Tip/duljina: an..9
Podatak (atribut) je obvezan.
Grad
(polje 8)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
NAD LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika naziva i adrese (NAD LNG).
IDENTIFIKACIJSKI BROJ GOSPODARSKOG
SUBJEKTA (TIN)
(polje 8)
Tip/duljina: an..17
Upisuje se identifikacijski broj gospodarskog subjekta (TIN-a). Korištenje ovog podatka (atributa) za upisivanje identifikacijskog broja gospodarskog subjekta (TIN-a) nije obvezno. Kada je gospodarski subjekt domaća osoba koristi se OIB.
ROBNA STAVKA
Broj: 999
Grupa podataka je obvezna.
Vrsta deklaracije
(ex polje 1)
Tip/duljina: an..5
Podatak (atribut) je obvezan ako je šifra »T-« korištena za podatak (atribut) »Vrsta deklaracije« grupe podataka »PROVOZNA OPERACIJA«. U drugim slučajevima ovaj se podatak (atribut) ne može koristiti.
Otpremna zemlja
(ex polje 15a)
Tip/duljina: a2
Zemlja iz koje se roba otprema/izvozi.
Podatak (atribut) je obvezan ako je deklarirano više od jedne otpremne zemlje. Koriste se šifre zemlje navedene u Prilogu 2. Podatak (atribut) »Otpremna zemlja« grupe podataka »PROVOZNA OPERACIJA« ne može se koristiti. Ako je deklarirana samo jedna otpremna zemlja, koristi se pripadajući podatak (atribut) grupe podataka »PROVOZNA OPERACIJA«.
Odredišna zemlja
(ex polje 17a)
Tip/duljina: a2
Podatak (atribut) je obvezan ako je deklarirano više od jedne odredišne zemlje. Koriste se šifre zemlje navedene u Prilogu 2. Podatak (atribut) »Odredišna zemlja« grupe podataka »PROVOZNA OPERACIJA« ne može se koristiti. Ako je deklarirana samo jedna odredišna zemlja, koristi se pripadajući podatak (atribut) grupe podataka »PROVOZNA OPERACIJA«.
Tekstualni opis
(polje 31)
Tip/duljina: an..140
Podatak (atribut) je obvezan.
Uobičajeni trgovački opis robe unosi se u svim slučajevima. Ovaj opis mora uključivati sve detalje potrebne za identifikaciju robe. Kada je potrebno popuniti podatak (atribut) »Šifra robe«, opis mora biti izražen dovoljno preciznim izrazima da bi se omogućilo razvrstavanje robe. Ovaj podatak (atribut) također mora prikazivati pojedinosti određene bilo kojim posebnim propisima (npr. o trošarinama). Ako se koriste kontejneri, identifikacijske oznake kontejnera također se unose u ovo polje.
Tekstualni opis LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) pripadajućeg slobodnog polja za unos teksta.
Broj stavke
(polje 32)
Tip/duljina: n..5
Navodi se broj stavke prikazan na popisu stavki deklariranih u podatku (atributu) »Ukupni broj stavki«.
Podatak (atribut) se koristi, čak i ako je broj »1« već korišten za podatak (atribut) »Ukupni broj stavki« grupe podataka »PROVOZNA OPERACIJA«. U tom slučaju, broj »1« koristi se za taj podatak (atribut). Broj stavke jedinstven je za cijelu deklaraciju.
Šifra robe
(polje 33)
Tip/duljina: n..8
Koristi se podatak (atribut) s najmanje 4 i najviše do 8 znamenki.
Ovo polje se mora popuniti kada:
- ista osoba sastavlja provoznu deklaraciju u isto vrijeme ili nakon carinske deklaracije na kojoj se nalazi tarifna oznaka robe; ili
- se provozna deklaracija odnosi za robu navedenu na popisu osjetljivih roba - Prilog 31A Uredbe za provedbu Carinskog zakona.
Unosi se oznaka robe.
U provoznim deklaracijama T2 ovo se polje ne popunjava, osim ako prethodna provozna deklaracija sadrži oznaku robe.
U tom slučaju potrebno je navesti oznaku upisanu u odgovarajućoj deklaraciji.
U svim ostalim slučajevima popunjavanje navedenog polja nije obvezno.
Bruto-masa
(polje 35)
Tip/duljina: n..11,3
Upisuje se bruto-masu, izražena u kilogramima, robe koja je opisana u odgovarajućem polju 31. Bruto-masa je ukupna masa robe s cjelokupnim pakiranjem, isključujući kontejnere i ostalu prijevoznu opremu.
Ovaj podatak (atribut) nije obvezan kada su različite vrste robe koje su obuhvaćene istom deklaracijom zajedno zapakirane tako da je nemoguće utvrditi bruto-masu pojedine vrste robe.
Neto-masa
(polje 38)
Tip/duljina: n..11,3
Upisuje se neto masa, izražena u kilogramima, robe opisane u pripadajućoj oznaci (atributu). Neto-masa je masa robe bez ikakvog pakiranja.
Korištenje ovog podatka (atributa) nije obvezno.
GOSPODARSKI SUBJEKT Pošiljatelj
(ex polje 2)
Broj: 1
Grupa podataka »GOSPODARSKI SUBJEKT Pošiljatelj« ne može se koristiti kada je deklariran samo jedan pošiljatelj. U tom slučaju koristi se grupa podataka »GOSPODARSKI SUBJEKT Pošiljatelj« grupe podataka »PROVOZNA OPERACIJA«.
Naziv
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 2)
Ulica i broj
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 2)
Zemlja
Tip/duljina: a2
Koristi se šifra zemlje navedena u Prilogu 2.
(ex polje 2)
Poštanski broj
Tip/duljina: an..9
Podatak (atribut) je obvezan.
(ex polje 2)
Grad
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 2)
NAD LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika naziva i adrese (NAD LNG).
IDENTIFIKACIJSKI BROJ GOSPODARSKOG SUBJEKTA (TIN)
Tip/duljina: an..17
(ex polje 2)
Korištenje ovog podatka (atributa) za upisivanje identifikacijskog broja gospodarskog subjekta (TIN-a) nije obvezno. Kada je gospodarski subjekt domaća osoba koristi se OIB.
GOSPODARSKI SUBJEKT Primatelj
(ex polje 8)
Broj: 1
Grupa podataka koristi se kada je deklarirano više od jednog primatelja i kada podatak (atribut) »Odredišna zemlja« grupe podataka »ROBNA STAVKA« sadrži »zemlju«. Kada je deklariran samo jedan primatelj, ne može se koristiti grupa podataka »GOSPODARSKI SUBJEKT Primatelj« grupe podataka »ROBNA STAVKA«.
Naziv
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 8)
Ulica i broj
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 8)
Zemlja
Tip/duljina: a2
Koristi se šifra zemlje navedena u Prilogu 2.
(ex polje 8)
Poštanski broj
Tip/duljina: an..9
Podatak (atribut) je obvezan.
(ex polje 8)
Grad
Tip/duljina: an..35
Podatak (atribut) je obvezan.
(ex polje 8)
NAD LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika naziva i adrese (NAD LNG).
IDENTIFIKACIJSKI BROJ GOSPODARSKOG SUBJEKTA (TIN)
Tip/duljina: an..17
(ex polje 8)
Korištenje ovog podatka (atributa) za upisivanje identifikacijskog broja gospodarskog subjekta (TIN-a) nije obvezno. Kada je gospodarski subjekt domaća osoba koristi se OIB.
KONTEJNERI
(polje 31)
Broj: 99
Grupa podataka koristi se ako podatak (atribut) »Kontejner« grupe podataka »PROVOZNA OPERACIJA« sadrži šifru »1«.
Brojevi kontejnera
(polje 31)
Tip/duljina: an..11
Podatak (atribut) je obvezan.
Oznake osjetljive robe (SGI)
(polje 31)
Broj: 9
Grupa podataka koristi se za upisivanje identifikacije osjetljive robe (SGI) ako se provozna deklaracija odnosi na robu navedenu na popisu roba iz Priloga 31A Uredbe za provedbu Carinskog zakona.
Šifra osjetljive robe
(polje 31)
Tip/duljina: n..2
Šifra navedena u Prilogu 2 koristi se ako šifra (tarifna oznaka) robe nije dovoljna za jedinstvenu identifikaciju robe s popisa Priloga 31A Uredbe za provedbu Carinskog zakona.
Količina osjetljive robe
(polje 31)
Tip/duljina: n..11,3
Podatak (atribut) se koristi kada provozna deklaracija sadrži robu navedenu na popisu Priloga 31A Uredbe za provedbu Carinskog zakona.
PAKIRANJA
(polje 31)
Broj: 99
Koristi se grupa podataka.
Oznake i brojevi paketa
(polje 31)
Tip/duljina: an..42
Podatak (atribut) se koristi ako podatak (atribut) »Vrsta pakiranja« sadrži drugačije šifre navedene u Prilogu 2 od onih za rasuto stanje (VQ, VG, VL, VY, VR ili VO) ili za »nepakirano« (NE, NF, NG). Nije obvezan ako podatak (atribut) »Vrsta pakiranja« sadrži jednu od prethodno spomenutih šifara.
Oznake i brojevi paketa LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
Vrsta paketa
(polje 31)
Tip/duljina: a2
Koriste se šifre pakiranja navedene u Prilogu 2.
Broj paketa
(polje 31)
Tip/duljina: n..5
Podatak (atribut) se koristi ako podatak (atribut) »Vrsta pakiranja« sadrži šifre navedene u Prilogu 2 drugačije od onih za rasuto stanje (VQ, VG, VL, VY, VR ili VO) ili za »nepakirano« (NE, NF, NG). Ne može se koristiti ako podatak (atribut) »Vrsta pakiranja« sadrži jednu od prethodno spomenutih šifara.
Broj komada
(polje 31)
Tip/duljina: n..5
Podatak (atribut) se koristi ako podatak (atribut) »Vrsta pakiranja« sadrži šifru navedenu u Prilogu 2 za »nepakirano« (NE). Ovaj podatak (atribut) se ne može koristiti u drugim slučajevima.
PRETHODNE ISPRAVE
(polje 40)
Broj: 9
Upisuje se poziv na prethodni carinski dopušten postupak ili uporabu ili na bilo koje odgovarajuće carinske isprave.
Grupa podataka koristi se ako podatak (atribut) »Vrsta deklaracije« grupa podataka »PROVOZNA OPERACIJA« ili »ROBNI STAVAK« sadrži šifru T2.
Vrsta prethodne isprave
(polje 40)
Tip/duljina: an..6
Ako se koristi grupa podataka, koristi se barem jedna šifra prethodne isprave navedene u Prilogu 2.
Oznaka prethodne isprave
(polje 40)
Tip/duljina: an..20
Koristi se oznaka prethodne isprave.
Oznaka prethodne isprave LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) odgovarajućeg slobodnog polja za unos teksta.
Dodatni podaci
(polje 40)
Tip/duljina: an..26
Korištenje ovog podatka (atributa) nije obvezno.
Nadopunjavanje podataka LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
PREDOČENE ISPRAVE/POTVRDE
(polje 44)
Broj: 99
Upisuju se pojedinosti propisane bilo kojim posebnim propisima primjenjivim u Republici Hrvatskoj zajedno s referentnim brojevima isprava podnesenih kao prilog carinskoj deklaraciji (npr. broj izvozne dozvole ili izvoznog dopuštenja, podatke koje zahtijevaju veterinarski i fitosanitarni propisi ili broj teretnice).
Ako se koristi grupa podataka, koristi se barem jedan od sljedećih podataka (atributa).
Vrsta isprave
(polje 44)
Tip/duljina: an..3
Koristi se šifra navedena u Prilogu 2.
Oznaka isprave
(polje 44)
Tip/duljina: an..20
Oznaka isprave LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
Dodatni podaci
(polje 44)
Tip/duljina: an..26
Dodatni podaci LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
POSEBNE NAPOMENE
(polje 44)
Broj: 99
Korištenje ove grupe podataka nije obvezno. Ako se koristi grupa podataka, koristi se ili podatak (atribut) »Dodatni podaci id« ili »Tekst«.
Dodatni podaci id
(polje 44)
Tip/duljina: an..3
Šifra navedena u Prilogu 2 koristi se za unošenje identifikacije (id) dodatnih informacija.
Izvoz iz zemlje
(polje 44)
Tip/duljina: a2
Ako podatak (atribut) »Dodatne informacije id« sadrži šifru »DG0« ili »DG1«, koristi se podatak (atribut) »Izvoz iz zemlje«. Nije moguće koristiti oba podatka (atributa) istovremeno. U drugim slučajevima podatak (atribut) se ne može koristiti. Ako se koristi ovaj podatak (atribut), mora se koristiti šifra zemlje navedena u Prilogu 2.
Tekst
(polje 44)
Tip/duljina: an..70
Tekst LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
Otpremna CARINARNICA
(polje C)
Broj: 1
Koristi se grupa podataka.
Referentni broj
(polje C)
Tip/duljina: an8
Koristi se šifra navedena u Prilogu 2.
GOSPODARSKI SUBJEKT GLAVNI OBVEZNIK
(polje 50)
Broj: 1
Koristi se grupa podataka.
IDENTIFIKACIJSKI BROJ GLAVNOG
OBVEZNIKA (TIN)
(polje 50)
Tip/duljina: an..17
Podatak (atribut) se koristi kada grupa podataka »REZULTAT KONTROLE« sadrži šifru A3 ili kada se koristi oznaka (atribut) »GRN«. Kao podatak koristi se OIB.
Naziv
(polje 50)
Tip/duljina: an..35
Podatak (atribut) se koristi ako se koristi atribut »TIN« i ako drugi podaci (atributi) ove grupe podataka još nisu poznati sustavu.
Ulica i broj
(polje 50)
Tip/duljina: an..35
Podatak (atribut) se koristi ako se koristi oznaka (atribut) »TIN« i ako drugi podaci (atributi) ove grupe podataka još nisu poznati sustavu.
Zemlja
(polje 50)
Tip/duljina: a2
Šifra zemlje navedena u Prilogu 2 koristi se ako se koristi oznaka (atribut) »TIN« i ako drugi podaci (atributi) ove grupe podataka još nisu poznati sustavu.
Poštanski broj
(polje 50)
Tip/duljina: an..9
Podatak (atribut) se koristi ako se koristi oznaka (atribut) »TIN« i ako drugi podaci (atributi) ove grupe podataka još nisu poznati sustavu.
Grad
(polje 50)
Tip/duljina: an..35
Podatak (atribut) se koristi ako se koristi oznaka (atribut) »TIN« i ako drugi podaci (atributi) ove grupe podataka još nisu poznati sustavu.
NAD LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika naziva i adrese (NAD LNG) ako se koriste odgovarajuća slobodna polja za unos teksta.
ZASTUPNIK
(polje 50)
Broj: 1
Grupa podataka koristi se ako glavni obveznik ima ovlaštenog zastupnika.
Naziv
(polje 50)
Tip/duljina: an..35
Podatak (atribut) je obvezan.
Svojstvo zastupnika
(polje 50)
Tip/duljina: a..35
Korištenje ovog podatka (atributa) nije obvezno.
Svojstvo zastupnika LNG
Tip/duljina: a2
Šifra jezika navedena u Prilogu 2 koristi se za određivanje jezika (LNG) ako se koristi odgovarajuće slobodno polje za unos teksta.
Provozna CARINARNICA
(polje 51)
Broj: 9
Upisuje se predviđenu carinarnicu izlaza i ponovnog ulaza kada roba u postupku provoza prelazi preko stranog carinskog područja (pri kretanju roba u postupku provoza preko koridora Neum).
Referentni broj
(polje 51)
Tip/duljina: an8
Koristi se šifra navedena u Prilogu 2.
Odredišna CARINARNICA
(polje 53)
Broj: 1
Koristi se grupa podataka.
Referentni broj
(polje 53)
Tip/duljina: an8
U Prilogu 2 naznačena je samo struktura šifre; odredišne carinarnice navedene su na popisu nadležnih carinarnica za provozne postupke.
Koristi se šifra navedena u Prilogu 2.
GOSPODARSKI SUBJEKT OVLAŠTENI
PRIMATELJ
(polje 53)
Broj: 1
Grupa podataka koristi se za označavanje da će roba biti dostavljena ovlaštenom primatelju.
TIN ovlaštenog primatelja
(polje 53)
Tip/duljina: an..17
Podatak (atribut) se koristi za upisivanje identifikacijskog broja gospodarskog subjekta (TIN-a). Kao podatak koristi se OIB.
REZULTAT KONTROLE
(polje D)
Broj: 1
Grupa podataka se koristi ako ovlašteni pošiljatelj podnosi deklaraciju.
Šifra rezultata kontrole
(polje D)
Tip/duljina: an2
Koristi se šifra A3.
Rok predaje robe
(polje D)
Tip/duljina: n8
Podatak (atribut) je obvezan.
PODACI O PLOMBAMA
(polje D)
Broj: 1
Grupa podataka koristi se ako ovlašteni pošiljatelj podnosi deklaraciju za koju se u njegovom odobrenju zahtijeva korištenje plombi ili ako je glavnom obvezniku odobrena uporaba posebne vrste plombi.
Broj plombi
(polje D)
Tip/duljina: n..4
Podatak (atribut) je obvezan.
OZNAKA PLOMBI
(polje D)
Broj: 99
Grupa podataka koristi se za identifikaciju (id) plombi.
Identitet plombi
(polje D)
Tip/duljina: an..20
Podatak (atribut) je obvezan.
Identitet plombi LNG
Tip/duljina: a2
Koristi se šifra jezika (LNG) navedena u Prilogu 2.
JAMSTVO
Broj: 9
Koristi se grupa podataka.
Vrsta jamstva
(polje 52)
Tip/duljina: an1
Koristi se šifra navedena u Prilogu 2.
OZNAKA JAMSTVA
Broj: 99
Grupa podataka koristi se ako podatak (atribut) »Vrsta jamstva« sadrži šifru »0«, »1«, »2«, »4« ili »9«.
REFERENTNI BROJ JAMSTVA (GRN)
(polje 52)
Tip/duljina: an..24
Podatak (atribut) se koristi za upisivanje referentnog broja jamstva (GRN-a) ako podatak (atribut) »Vrsta jamstva« sadrži šifru »0«, »1«, »2«, »4« ili »9«. U tom slučaju ne može se koristiti podatak (atribut) »Druga oznaka jamstva«.
»Referentni broj jamstva« (GRN) dodjeljuje jamstvena carinarnica za identifikaciju svakog pojedinačnog jamstva i strukturiran je na sljedeći način:
Polje
Sadržaj
Vrsta polja
Primjeri
1
Posljednje dvije znamenke godine u kojoj je jamstvo prihvaćeno (YY)
Brojčano 2
11
2
Oznaka zemlje u kojoj je jamstvo podneseno (ISO alfa 2 šifra zemlje)
Slovno 2
HR
3
Jedinstvena identifikacijska oznaka za godinu i zemlju, određena od strane jamstvene carinarnice
Slovno-brojčano 12
011009788966
4
Kontrolni broj
Slovno-brojčano 1
8
5
Oznaka pojedinačnog jamstva u obliku kupona (1 slovo + 6 znamenki) ili NULA za druge vrste jamstva
Slovno-brojčano 7
A001017
Polje 1 i 2 popunjavaju se kako je gore navedeno.
U polje 3 potrebno je upisati identifikacijsku oznaku prihvaćenog jamstva koju dodjeljuje jamstvena carinarnica, jedinstvenu za godinu i zemlju. Prvih šest znakova rezervirano je za šifru jamstvene carinarnice.
U polje 4 potrebno je upisati vrijednost koja predstavlja kontrolni broj za polja 1 do 3 GRN-a. Ovo polje omogućava otkrivanje bilo kakvih pogreški pri određivanju prva četiri polja GRN-a.
Polje 5 koristi se samo kada se GRN odnosi na pojedinačno jamstvo u obliku kupona registriranih u računalnom sustavu provoza. U tom slučaju ovo polje je potrebno popuniti identifikacijskom oznakom kupona.
Druga oznaka jamstva
(polje 52)
Tip/duljina: an..35
Podatak (atribut) se koristi ako podatak (atribut) »Vrsta jamstva« sadrži druge šifre osim »0«, »1«, »2«, »4« ili »9«. U tom slučaju ne može se koristiti podatak (atribut) »GRN«.
Pristupna šifra
Tip/duljina: an4
Podatak (atribut) se koristi kada se koristi podatak (atribut) »GRN«; u drugim slučajevima ovaj podatak (atribut) nije obvezan. Ovisno o vrsti jamstva, izdaje ga jamstvena carinarnica, jamac ili glavni obveznik, a koristi se za zaštitu posebnog jamstva.
PRILOG 2
DODATNE ŠIFRE ZA RAČUNALNI SUSTAV PROVOZA
1. ŠIFRE ZEMALJA (CNT)
Polje
Sadržaj
Vrsta polja
Primjer
1
ISO alfa 2 šifra zemlje.
Slovno 2
HR
Primjenjuje se »ISO alfa-2 šifra zemlje« navedena u standardu ISO - 3166 - 1 iz 1997. i naknadne izmjene.
2. ŠIFRA JEZIKA
Primjenjuje se označavanje ISO alfa 2 navedeno u standardu ISO - 639: 1988.
Popunjava se šifrom HR.
3. ŠIFRA ROBE (COM)
Polje
Sadržaj
Vrsta polja
Primjeri
1
HS6
Brojčano 6
(poravnano lijevo)
010290
Potrebno je upisati šest znamenki Harmoniziranog sustava (HS6). Prema potrebi šifra robe može se proširiti na 8 znamenki.
4. ŠIFRA OSJETLJIVE ROBE
Polje
Sadržaj
Vrsta polja
Primjeri
1
Dodatna oznaka za osjetljivu robu
Brojčano..2
2
Šifra se koristi kao proširenje HS6, ako je ista navedena u Prilogu 31A Uredbe za provedbu Carinskog zakona, kada se osjetljiva roba ne može dovoljno identificirati putem HS6.
5. ŠIFRA PAKIRANJA
(Preporuka UNECE-a br. 21/Rev. 4 od svibnja 2002)
Aerosol (Sprej)
AE
Ampula, nezaštićena
AM
Ampula, zaštićena
AP
Raspršivač
AT
Vreća
BG
Vreća, fleksibilna ambalaža
FX
Vreća, velika
ZB
Vreća, višedjelna
MB
Vreća, papirnata
5M
Vreća, papirnata, višeslojna
XJ
Vreća, papirnata, višeslojna, vodonepropusna
XK
Vreća, plastična
EC
Vreća, plastični film
XD
Vreća, velika za rasute terete
43
Vreća, tekstilna
5L
Vreća, tekstilna, nepropusna
XG
Vreća, tekstilna, vodonepropusna
XH
Vreća, tekstilna, bez unutarnje presvlake/podstave
XF
Vreća, tkana plastika
5H
Vreća, tkana plastika, nepropusna
XB
Vreća, tkana plastika, vodonepropusna
XC
Vreća, tkana plastika, bez unutarnje presvlake/podstave
XA
Bala, komprimirana
BL
Bala, nekomprimirana
BN
Balon, nezaštićeni
BF
Balon, zaštićeni
BP
Šipka
BR
Bačva
BA
Bačva, drvena
2C
Bačva, drvena, s čepom
QH
Bačva, drvena, s odvojivim poklopcem
QJ
Šipke, u snopu/svežnju/smotku
BZ
Bazen
BM
Košara
BK
Košara, s ručkom, kartonska
HC
Košara, s ručkom, plastična
HA
Košara, s ručkom, drvena
HB
Koš
BI
Ploča
BD
Ploča, u snopu/svežnju/smotku
BY
Svitak (kalem)
BB
Bala (tkanina)
BT
Boca, plinska
GB
Boca, nezaštićena, konveksna
BS
Boca, nezaštićena, cilindrična
BO
Boca, zaštićena, konveksna
BV
Boca, zaštićena, cilindrična
BQ
Sanduk za boce / stalak za boce
BC
Kutija
BX
Kutija, aluminijska
4B
Kutija, Commonwealth Handling Equipment Pool (CHEP), Eurobox
DH
Kutija, vlaknaste ploče
4G
Kutija, za tekućine
BW
Kutija, od prirodnog drva
4C
Kutija, plastična
4H
Kutija, plastična, proširiva
QR
Kutija, plastična, čvrsta
QS
Kutija, šperploča
4D
Kutija, rekonstituirano drvo
4F
Kutija, čelična
4A
Kutija, drvena, od prirodnog drva, obična
QP
Kutija, drvena, od prirodnog drva, s nepropusnim stjenkama
QQ
Kanta (vjedro)
BJ
Rasuto, plin (pri 1 031 mbar i 15 °C)
VG
Rasuto, ukapljeni plin (pri abnormalnoj temperaturi/ tlaku)
VQ
Rasuto, tekućine
VL
Rasuto, krute tvari, fine čestice (praške)
VY
Rasuto, krute tvari, zrnaste čestice (zrna)
VR
Rasuto, krute tvari, krupnije čestice (grumeni)
VO
Svežanj
BH
Snop
BE
Bure (490,96 l)
BU
Kavez
CG
Kavez, Commonwealth Handling Equipment Pool (CHEP)
DG
Kavez, valjkasti
CW
Limenka, cilindrična
CX
Limenka, četvrtasta
CA
Limenka, s drškom i lijevkom
CD
Kanistar
CI
Platno
CZ
Kapsula
AV
Stakleni balon za držanje koroziva, nezaštićeni
CO
Stakleni balon za držanje koroziva, zaštićeni
CP
Tanki karton
CM
Karton
CT
Patrona
CQ
Sanduk
CS
Sanduk, izotermički
EI
Sanduk, kosturni
SK
Sanduk, čelični
SS
Sanduk, s paletnim dnom
ED
Sanduk, s paletnim dnom, karton
EF
Sanduk, s paletnim dnom, metal
EH
Sanduk, s paletnim dnom, plastika
EG
Sanduk, s paletnim dnom, drvo
EE
Bure
CK
Škrinja
CH
Posuda za mlijeko
CC
Kutija s poklopcem na pregib
AI
Kaseta
CF
Lijes
CJ
Spirala
CL
Kombinirano pakiranje, stakleni spremnik
6P
Kombinirano pakiranje, stakleni spremnik u aluminijskom sanduku
YR
Kombinirano pakiranje, stakleni spremnik u aluminijskom bubnju
YQ
Kombinirano pakiranje, stakleni spremnik u proširivom plastičnom pakiranju
YY
Kombinirano pakiranje, stakleni spremnik u vlaknastom bubnju
YW
Kombinirano pakiranje, stakleni spremnik u kutiji od vlaknastih ploča
YX
Kombinirano pakiranje, stakleni spremnik u bubnju od šperploče
YT
Kombinirano pakiranje, stakleni spremnik u čvrstom plastičnom pakiranju
YZ
Kombinirano pakiranje, stakleni spremnik u čeličnoj kutiji
YP
Kombinirano pakiranje, stakleni spremnik u čeličnom bubnju
YN
Kombinirano pakiranje, stakleni spremnik u košari od pruća
YV
Kombinirano pakiranje, stakleni spremnik u drvenoj kutiji
YS
Kombinirano pakiranje, plastični spremnik
6H
Kombinirano pakiranje, plastični spremnik u aluminijskom sanduku
YD
Kombinirano pakiranje, plastični spremnik u aluminijskom bubnju
YC
Kombinirano pakiranje, plastični spremnik u vlaknastom bubnju
YJ
Kombinirano pakiranje, plastični spremnik u kutiji od vlaknastih ploča
YK
Kombinirano pakiranje, plastični spremnik u plastičnom bubnju
YL
Kombinirano pakiranje, plastični spremnik u kutiji od šperploče
YH
Kombinirano pakiranje, plastični spremnik u bubnju od šperploče
YG
Kombinirano pakiranje, plastični spremnik u čvrstoj plastičnoj kutiji
YM
Kombinirano pakiranje, plastični spremnik u čeličnoj kutiji
YB
Kombinirano pakiranje, plastični spremnik u čeličnom bubnju
YA
Kombinirano pakiranje, plastični spremnik u drvenoj kutiji
YF
Stožac
AJ
Spremnik, koji nije drugačije označen kao prijevozna oprema
CN
Pokrov
CV
Sanduk
CR
Sanduk, pivski
CB
Sanduk, za rasuti teret, kartonski
DK
Sanduk, za rasuti teret, plastični
DL
Sanduk, za rasuti teret, drveni
DM
Sanduk, uokvireni
FD
Sanduk, voće
FC
Sanduk, mlijeko
MC
Sanduk, višeslojni, kartonski
DC
Sanduk, višeslojni, plastični
DA
Sanduk, višeslojni, drveni
DB
Sanduk, plitki
SC
Košara (pletena)
CE
Posuda
CU
Cilindar
CY
Opletena boca, nezaštićena
DJ
Opletena boca, zaštićena
DP
Dozator
DN
Bubanj
DR
Bubanj, aluminijski
1B
Bubanj, aluminijski, neuklonjivi poklopac
QC
Bubanj, aluminijski, uklonjivi poklopac
QD
Bubanj, vlaknasti
1G
Bubanj, željezni
DI
Bubanj, plastični
IH
Bubanj, plastični, neuklonjivi poklopac
QF
Bubanj, plastični, uklonjivi poklopac
QG
Bubanj, šperploča
1D
Bubanj, čelični
1A
Bubanj, čelični, neuklonjivi poklopac
QA
Bubanj, čelični, uklonjivi poklopac
QB
Bubanj, drveni
1W
Omot
EN
Omot, čelični
SV
Kutija za film
FP
Bačvica
FI
Čuturica
FL
Spremnik za hranu
FT
Kovčeg (vojnički)
FO
Okvir
FR
Nosač
GI
Nosači, u snopu/svežnju/smotku
GZ
Košara sa pokrovom (korpa)
HR
Posuda (238 l ili 286 l)
HG
Ingot
IN
Ingoti, u snopu/svežnju/smotku
IZ
Međuspremnik za teret
WA
Međuspremnik za teret, aluminijski
WD
Međuspremnik za teret, aluminijski, tekućina
WL
Međuspremnik za teret, aluminijski, pod tlakom > 10 kPa
WH
Međuspremnik za teret, kombiniran
ZS
Međuspremnik za teret, kombiniran, fleksibilna plastika, tekućine
ZR
Međuspremnik za teret, kombiniran, fleksibilna plastika, pod tlakom
ZP
Međuspremnik za teret, kombiniran, fleksibilna plastika, krute tvari
ZM
Međuspremnik za teret, kombiniran, kruta plastika, tekućine
ZQ
Međuspremnik za teret, kombiniran, kruta plastika, pod tlakom
ZN
Međuspremnik za teret, kombiniran, kruta plastika, krute tvari
ZL
Međuspremnik za teret, vlaknasta ploča
ZT
Međuspremnik za teret, fleksibilan
ZU
Međuspremnik za teret, metalni
WF
Međuspremnik za teret, metalni, tekućina
WM
Međuspremnik za teret, metalni, osim čelika
ZV
Međuspremnik za teret, metalni, pod tlakom 10 kPa
WJ
Međuspremnik za teret, prirodno drvo
ZW
Međuspremnik za teret, prirodno drvo, s unutarnjom presvlakom
WU
Međuspremnik za teret, papirni, višeslojni
ZA
Međuspremnik za teret, papirni, višeslojni, vodootporan
ZC
Međuspremnik za teret, plastični film
WS
Međuspremnik za teret, šperploča
ZX
Međuspremnik za teret, šperploča, s unutarnjom presvlakom
WY
Međuspremnik za teret, rekonstituirano drvo
ZY
Međuspremnik za teret, rekonstituirano drvo, s unutarnjom presvlakom
WZ
Međuspremnik za teret, kruta plastika
AA
Međuspremnik za teret, kruta plastika, samostojeći, tekućine
ZK
Međuspremnik za teret, kruta plastika, samostojeći, pod tlakom
ZH
Međuspremnik za teret, kruta plastika, samostojeći, krute tvari
ZF
Međuspremnik za teret, kruta plastika, sa strukturalnom opremom, krute tvari
ZD
Međuspremnik za teret, kruta plastika, sa strukturalnom opremom, tekućine
ZJ
Međuspremnik za teret, kruta plastika, sa strukturalnom opremom, pod tlakom tlakottlakotlakomtlakomiskom
ZG
Međuspremnik za teret, čelični
WC
Međuspremnik za teret, čelični, tekućina
WK
Međuspremnik za teret, čelični, pod pritiskom > 10 kPa
WG
Međuspremnik za teret, tekstilni bez presvlake/obruba
WT
Međuspremnik za teret, tekstilni, presvučen
WV
Međuspremnik za teret, tekstilni, presvučen i obrubljen
WX
Međuspremnik za teret, tekstilni, obrubljen
WW
Međuspremnik za teret, tkana plastika, presvučen
WP
Međuspremnik za teret, tkana plastika, presvučen i obrubljen
WR
Međuspremnik za teret, tkana plastika, obrubljen
WQ
Međuspremnik za teret, tkana plastika, nepresvučen/neobrubljen
WN
Staklenka
JR
Kanistar, cilindrični
JY
Kanistar, plastični
3H
Kanistar, plastični, neuklonjivi poklopac
QM
Kanistar, plastični, uklonjivi poklopac
QN
Kanistar, četvrtasti
JC
Kanistar, čelični
3A
Kanistar, čelični, neuklonjivi poklopac
QK
Kanistar, čelični, uklonjivi poklopac
QL
Vrč
JG
Jutena vreća
JT
Bačvica
KG
Pokretni kontejner drveni (»liftvan«)
LV
Klada
LG
Klade, u snopu/svežnju/smotku
LZ
Velika količina, gomila
LT
Vreća od hasure
MT
Kutijica, za šibice
MX
Uzajamno određeno
ZZ
Gnijezdo
NS
Mreža
NT
Mreža, cjevasta, plastična
NU
Mreža, cjevasta, tekstilna
NV
Nedostupno
NA
Pakiranje
PK
Pakiranje, kartonsko, s otvorima za držanje
IK
Pakiranje, izložbeno, kartonsko
IB
Pakiranje, izložbeno, metalno
ID
Pakiranje, izložbeno, plastično
IC
Pakiranje, izložbeno, drveno
IA
Pakiranje, protočno
IF
Pakiranje, umotano u papir
IG
Pakiranje, izložbeno
IE
Paket
PA
Kabao (vjedro)
PL
Paleta
PX
Paleta, 100 cm × 110 cm
AH
Paleta, kutija
PB
Paleta, modularna, prsteni 80 cm × 100 cm
PD
Paleta, modularna, prsteni 80 cm × 120 cm
PE
Paleta, modularna, prsteni 80 cm × 60 cm
AF
Paleta, u zaštitnom plastičnom omotu
AG
Paket
PC
Tor za životinje
PF
Cijev
PI
Cijevi, u snopu/svežnju/smotku
PV
Vrč (lončarski)
PH
Daska
PN
Daske, u snopu/svežnju/smotku
PZ
Ploča
PG
Ploče, u snopu/svežnju/smotku
PY
Lonac
PT
Torba
PO
Košarica od drvenih trakica (za voće)
PJ
Stalak
RK
Stalak, vješalica za odjeću
RJ
Spremnik, vlaknasti
AB
Spremnik, stakleni
GR
Spremnik, metalni
MR
Spremnik, papirnati
AC
Spremnik, plastični
PR
Spremnik, obložen plastikom
MW
Spremnik, drveni
AD
Rednet mreža (za voće)
RT
Namot
RL
Prsten
RG
Šipka
RD
Šipke, u snopu/svežnju/smotku
RZ
Rola
RO
Vrećica
SH
Vreća
SA
Vreća, višeslojna
MS
Mornarski sanduk
SE
Set
SX
Ploča
ST
Ploča, omotana plastikom
SP
Metalna ploča
SM
Ploče, u snopu/svežnju/smotku
SZ
U zaštitnom, plastičnom omotu
SW
Klizna šipka
SI
Ploča
SB
Naglavak
SY
Klizna ploha
SL
Vreteno
SD
Namotaj (špula)
SO
Kovčeg
SU
Cisterna, cilindrična
TY
Cisterna, četverokutna
TK
Sanduk za čaj
TC
Bačva
TI
Limenka
TN
Plitica
PU
Plitica, jednoslojna bez poklopca, kartonska
DV
Plitica, jednoslojna bez poklopca, plastična
DS
Plitica, jednoslojna bez poklopca, polistirenska
DU
Plitica, jednoslojna bez poklopca, drvena
DT
Plitica, dvoslojna bez poklopca, kartonska
DY
Plitica, dvoslojna bez poklopca, plastična
DW
Plitica, dvoslojna bez poklopca, drvena
DX
Sanduk
TR
Nosač
TS
Kada
TB
Kada, s poklopcem
TL
Cijev
TU
Cijev, sklopiva
TD
Cijev, s mlaznicom
TV
Cijevi, u snopu/svežnju/smotku
TZ
Bačva
TO
Nije u kavezu
UC
Nezapakirano
NE
Nezapakirano, više jedinica
NG
Nezapakirano, jedna jedinica
NF
Vakumirano
VP
Kontejner za prijevoz kombijem (»vanpack«)
VK
Bačva
VA
Bočica
VI
Pletena boca
WB
6. ŠIFRE PRETHODNE ISPRAVE
Šifre se primjenjuju kako slijedi:
T2 =
Deklaracija za postupak provoza koja obuhvaća robu koja ima status domaće robe.
T2CIM =
Roba koja ima status domaće robe a prevozi se uz uporabu teretnog lista CIM ili predajnog lista TR.
T2TIR=
Roba koja ima status domaće robe i prevozi se uz uporabu karneta TIR.
T2ATA=
Roba koja ima status domaće robe i prevozi se na temelju karneta ATA.
T2L=
Isprava kojom se dokazuje status domaće robe podnesena na obrascu jedinstvene carinske deklaracije.
T1=
Deklaracija za postupak provoza koja obuhvaća postupak provoza za robu koja nema status domaće robe (strana roba).
*...................................................................................................
* bilo kakva druga prethodna isprava (an..5)
7. ŠIFRE PODNESENIH ISPRAVA / POTVRDA
(Brojčane šifre preuzete su iz UN-ovih Adresara za elektroničku razmjenu podataka za administraciju, trgovinu i promet 1997b: Popis oznaka za element podataka 1001, Isprava/ime poruke, s oznakom.)
Potvrda o usklađenosti
2
Potvrda o kvaliteti
3
Potvrda o kretanju robe A.TR.1
18
Popis kontejnera
235
Paking lista
271
Proforma račun
325
Komercijalni račun
380
Interni tovarni list
703
Glavna teretnica
704
Teretnica
705
Interna teretnica
714
Teretni list CIM (željeznica)
720
Cestovni popis - SMGS
722
Cestovni tovarni list
730
Zračni tovarni list
740
Glavni zračni tovarni list
741
Poštanska otpremnica (poštanski paketi)
750
Isprava za multimodalni/mješoviti prijevoz (opća)
760
Robni manifest
785
Bordereau (specifikacija tovarnog lista)
787
Obrazac otpremnice T
820
Obrazac otpremnice T1
821
Obrazac otpremnice T2
822
Kontrolna isprava T5
823
Obrazac otpremnice T2L
825
Deklaracija za izvoz robe
830
Fitosanitarni certifikat
851
Sanitarni certifikat
852
Veterinarski certifikat
853
Potvrda o podrijetlu
861
Deklaracija o podrijetlu
862
Potvrda o povlaštenom podrijetlu
864
Potvrda o podrijetlu, obrazac GSP
865
Dozvola za uvoz
911
Prijava robe (dolazak)
933
Dozvola u slučaju embarga
941
Obrazac TIF
951
Karnet TIR
952
Potvrda o podrijetlu EUR 1
954
Karnet ATA
955
Ostalo
Zzz
8. ŠIFRE NAČINA PRIJEVOZA, POŠTANSKIH I DRUGIH POŠILJAKA
A. Jednoznamenkasta šifra (obvezno);
B. Dvoznamenkasta šifra (nije obvezno).
A
B
Značenje
1
10
Pomorski promet
12
Željeznički vagon na brodu morske plovidbe
16
Cestovno motorno vozilo na brodu morske plovidbe
17
Priključno vozilo ili poluprikolica na brodu morske plovidbe
18
Brod unutarnje plovidbe na brodu morske plovidbe
2
20
Željeznički prijevoz
23
Cestovno vozilo na željezničkom vagonu
3
30
Cestovni prijevoz
4
40
Zračni prijevoz
5
50
Poštanske pošiljke
7
70
Nepokretna prijevozna instalacija
8
80
Prijevoz unutarnjim plovnim putovima
9
90
Vlastiti pogon
9. DODATNI PODACI / POSEBNE ŠIFRE
Primjenjive šifre su sljedeće:
DG0 =
Izvoz koji podliježe ograničenjima.
DG1 =
Izvoz koji podliježe izvoznim davanjima.
DG2 =
Izvoz.
10. ŠIFRE JAMSTAVA
Primjenjive oznake su:
Situacija
Šifra
Dodatne informacije
Za oslobađanje od polaganja zajedničkog jamstva (čl. 106 st. 4 Carinskog zakona)
0
-
broj potvrde o oslobađanju od polaganja jamstva
Za zajedničko jamstvo
1
-
broj potvrde o zajedničkom jamstvu
-
jamstvena carinarnica
Za pojedinačno jamstvo koje polaže jamac
2
-
referenca za prihvat jamstva
-
jamstvena carinarnica
Za pojedinačno jamstvo u obliku gotovinskog pologa
3
Za pojedinačno jamstvo u obliku kupona
4
-
broj kupona za pojedinačno jamstvo
Za oslobađanje od polaganja jamstva (Članak 106.a Carinskog zakona)
6
Za pojedinačno jamstvo tipa navedenog u članku 337.b st. 6 i Prilogu 33K Uredbe za provedbu Carinskog zakona
9
-
referenca za prihvat jamstva
-
jamstvena carinarnica
Šifre zemalja
Primjenjuju se usvojene šifre za polje 51.
11. REFERENTNI BROJ CARINARNICE (COR)
Polje
Sadržaj
Tip polja
Primjer
1
Oznaka zemlje
Slovno 2
HR
2
Nacionalna oznaka carinarnice
Slovno-brojčano 6
041173
Polje 1, kako je objašnjeno iznad.
Polje 2, mora biti slobodno ispunjeno sa 6 slovno-brojčanih znakova. Tih šest znakova omogućuje, ako je potrebno, identifikaciju uključene ustrojstvene jedinice.
