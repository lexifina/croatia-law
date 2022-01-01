PRIVITAK 6.
Podatkovni skup zahtjeva za promjenu podatka o načinu plaćanja računa
Privitak 6.
1.1.6. Podatkovni skup zahtjeva za promjenu podatka o načinu plaćanja računa/računa koji se odnosi na prateći dokument
U tablici u nastavku opisan je podatkovni skup poruke zahtjeva za fiskalizaciju promjene podatka o načinu plaćanja računa/računa koji se odnosi na prateći dokument.
Podatak | Opis/Napomena
Obavezan
DA/NE
| Tip/Duljina
Zaglavlje
Identifikator poruke
ID poruke (UUID).
Svaka poruka koja se šalje prema CIS-u mora sadržavati različiti ID poruke. Isto vrijedi i u slučaju kad se ponavlja slanje poruke zbog greške u razmjeni poruka.
| DA | Char(36)
Datum i vrijeme slanja
Datum i vrijeme slanja poruke zahtjeva za ispravak načina plaćanja.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Račun
OIB | OIB obveznika fiskalizacije s izdanog računa. | DA | Char(11)
U sustavu PDV
Oznaka je li obveznik u sustavu PDV-a ili nije s izdanog računa.
True ako je obveznik u sustavu PDV-a, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Datum i vrijeme izdavanja
Datum i vrijeme izdavanja koji se ispisuju na računu s izdanog računa.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Oznaka slijednosti
Oznaka slijednosti brojeva računa s izdanog računa.
Oznaka koja govori gdje se određuje dodjela broja računa tj. dodjeljuje li se broj računa centralno na razini poslovnog prostora ili pojedinačno na svakom naplatnom uređaju.
Dodjela brojeva računa može biti na razini poslovnog prostora ili naplatnog uređaja:
P - na nivou poslovnog prostora
N - na nivou naplatnog uređaja
| DA | Char(1)
Broj računa
Izgled broja računa kako se treba ispisivati na fizičkom računu u sljedećem obliku s izdanog računa:
brojčana oznaka računa/oznaka poslovnog prostora/oznaka naplatnog uređaja
Primjer: 1234567890/POSL1/12
Podaci će se Poreznoj upravi dostavljati odvojeni u XML-u radi kasnije lakše manipulacije u izvještajima i analizama.
| DA
Brojčana oznaka računa | Može sadržavati samo znamenke 0 - 9. Nisu dozvoljene vodeće nule. | DA | Varchar(20)
Oznaka poslovnog prostora
Može sadržavati samo znamenke i slova 0 - 9, a - z, A - Z.
Mora biti jedinstvena na razini OIB-a obveznika.
| DA | Varchar(20)
Oznaka naplatnog uređaja
Može sadržavati samo znamenke 0 - 9. Nisu dozvoljene vodeće nule.
Mora biti jedinstvena na razini jednog poslovnog prostora obveznika.
| DA | Varchar(20)
PDV
Porez na dodanu vrijednost s izdanog računa.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji PDV.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 25,00% se dostavlja kao 25.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
PNP
Porez na potrošnju s izdanog računa.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji porez na potrošnju.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 3,00% se dostavlja kao 3.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Ostali porezi
Ostali porezi koji se mogu pojaviti na računu osim PDV-a i poreza na potrošnju s izdanog računa.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje ostali porezi.
Podatak se sastoji od naziva poreza, porezne stope, osnovice i iznosa poreza.
Može postojati lista poreza.
|  | NE
Naziv poreza | Naziv poreza za koji se šalju podaci. Npr. Porez na luksuz. | DA, ako postoji porez | Varchar(100)
Porezna stopa | Iznos porezne stope. Npr. stopa od 15,00% se dostavlja kao 15.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Iznos oslobođenja
Ukupni iznos oslobođenja na računu s izdanog računa.
Oslobođenja u slučajevima kada se isporučuju dobra ili obavljaju usluge koje su oslobođene od plaćanja PDV-a.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji oslobođenje.
| NE | Decimal(15,2)
Iznos na koji se odnosi poseban postupak oporezivanja marže
Ukupni iznos na koji se odnosi poseban postupak oporezivanja marže na računu s izdanog računa.
Marža za rabljena dobra, umjetnička djela, kolekcionarske ili antikne predmete.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji poseban postupak oporezivanja marže.
| NE | Decimal(15,2)
Iznos koji ne podliježe oporezivanju
Ukupni iznos koji ne podliježe oporezivanju na računu s izdanog računa.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji iznos koji ne podliježe oporezivanju.
| NE | Decimal(15,2)
Naknade
Naknade koje se mogu pojaviti na računu tipa povratne naknade za ambalažu i sl. s izdanog računa.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje naknade.
Podatak se sastoji od naziva naknade i iznosa naknade.
Može postojati lista naknada.
| NE
Naziv naknade | Opisno naziv naknade. | DA, ako postoji naknada | Varchar(100)
Iznos naknade |  | DA, ako postoji naknada | Decimal(15,2)
Ukupan iznos | Ukupan iznos iskazan na računu s izdanog računa. | DA | Decimal(15,2)
Način plaćanja
Način plaćanja s izdanog računa
G - gotovina
K - kartice
C - ček
T - transakcijski račun
O - ostalo
U slučaju više načina plaćanja po jednom računu, isto je potrebno prijaviti pod ‘Ostalo’.
Za sve načine plaćanja koji nisu prije navedeni koristit će se oznaka ‘Ostalo’.
| DA | Char(1)
OIB operatera na naplatnom uređaju | OIB operatera na naplatnom uređaju koji izdaje račun s izdanog računa. | DA | Char(11)
Zaštitni kod izdavatelja
Zaštitni kod izdavatelja obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i izdanog računa s izdanog računa.
Zaštitni kod generira obveznik fiskalizacije sukladno algoritmu opisanom u poglavlju 12 ovog dokumenta i ispisuje na računu.
32-znamenkasti broj zapisan u heksadecimalnom formatu.
Može sadržavati znamenke 0 - 9 i mala slova a - f.
Primjer:
e4d909c290d0fb1ca068ffaddf22cbd0
| DA | Char(32)
Oznaka naknadne dostave računa
Pod naknadnom dostavom računa Poreznoj upravi smatra se situacija kad je isti prethodno izdan kupcu bez JIR-a (npr. prekid Internet veze ili potpuni prestanak rada naplatnog uređaja).
True ako je riječ o naknadnoj dostavi računa, u suprotnom false.
Boolean (1-true/0-false).
Podatak s izdanog računa.
| DA | Boolean
Oznaka paragon računa | Dostavlja se samo u slučaju potpunog prestanka rada naplatnog uređaja kada obveznik fiskalizacije mora prepisati izdane paragon račune i prijaviti ih putem poruke Poreznoj upravi. Podatak s izdanog računa. | NE | Varchar(100)
Specifična namjena | Predviđeno za slučaj da se naknadno pojavi potreba za dostavom podataka koji nisu prepoznati tokom analize. Podatak s izdanog računa. | NE | Varchar(1000)
Jedinstveni identifikator s pratećeg dokumenta | Obvezik fiskalizacije koji mijenja način plaćanja računa izdanog na temelju pratećeg dokumenta dostavlja jedinstveni identifikator pratećeg dokumenta ako je prethodio računu. Podatak s izdanog računa na temelju pratećeg dokumenta. | NE | Char(36)
Zaštitni kod izdavatelja s pratećeg dokumenta | Obvezik fiskalizacije koji mijenja način plaćanja računa izdanog na temelju pratećeg dokumenta dostavlja zaštitni kod izdavatelja pratećeg dokumenta s izdanog računa ako je prethodio računu u slučaju ako račun nema JIR s pratećeg dokumenta. | NE | Char(32)
Promijenjeni način plaćanja
Dostavlja se novi način plaćanja kojim se ispravlja način plaćanja s izdanog računa:
G - gotovina
K - kartice
C - ček
T - transakcijski račun
O - ostalo
U slučaju više načina plaćanja po jednom računu, isto je potrebno prijaviti pod ‘Ostalo’.
Za sve načine plaćanja koji nisu prije navedeni koristiti će se oznaka ‘Ostalo’.
| DA | Char(1)
1.1.6. Podatkovni skup odgovora za promjenu podatka o načinu plaćanja računa/računa koji se odnosi na prateći dokument
U tablici u nastavku opisan je podatkovni skup poruke odgovora za fiskalizaciju promjene podatka o načinu plaćanja računa/računa koji se odnosi na prateći dokument.
Podatak | Opis/Napomena
Obvezan
DA/NE
| Tip/Duljina
Zaglavlje
Identifikator poruke
ID poruke (UUID).
Kao identifikator poruke odgovora uzima se ID iz poruke zahtjeva.
| DA | Varchar(0-36)
Datum i vrijeme obrade
Datum i vrijeme obrade poruke zahtjeva.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Poruka odgovora
Šifra poruke | Ako je zahtjev uspješno obrađen vraća se poruka pod šifrom p001. | DA, ako je prijava uspješna | Varchar(4)
Poruka | Ako je zahtjev uspješno obrađen vraća se tekst poruke za šifru p001: »Uspješna prijava promjene načina plaćanja.«. | DA, ako je prijava uspješna | Varchar(500)
Greške
Šifra greške
Šifra greške je u formatu sXXX gdje je XXX troznamenkasti prirodni broj.
Šifre grešaka sukladno šifarniku grešaka.
| DA, ako ima grešaka | Varchar(4)
Poruka | Poruka greške je tekstualni opis greške sukladno šifarniku grešaka. | DA, ako ima grešaka | Varchar(500)
U nastavku su šifrarnici poruka odgovora i grešaka za fiskalizaciju promjene podatka o načinu plaćanja računa/računa koji se odnosi na prateći dokument.
Šifra poruke | Poruka uspješnosti
p001 | Uspješna prijava promjene načina plaćanja.
Šifra greške | Poruka greške
s001 | ‘Poruka nije u skladu s XML shemom : #element ili lista elemenata koji nisu ispravni po shemi#’
s002 | ‘Certifikat nije izdan od strane Fina RDC CA ili je istekao ili je ukinut.’
s003 | ‘Certifikat ne sadrži naziv ‘Fiskal’ .’
s004 | ‘Neispravan digitalni potpis.’
s005 | ‘OIB iz poruke zahtjeva nije jednak OIB-u iz certifikata.’
s006 | ‘Sistemska pogreška prilikom obrade zahtjeva.’
s007 | Datum izdavanja računa u poruci promjene načina plaćanja nije jednak trenutnom datumu.
s008 | Podaci za račun u poruci promjene načina plaćanja razlikuju se od podataka fiskaliziranog računa ili račun nije fiskaliziran.
