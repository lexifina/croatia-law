PRIVITAK 1.
1.1.1 Podatkovni skup zahtjeva za račun
U tablici u nastavku opisan je podatkovni skup poruke zahtjeva za račun.
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
Datum i vrijeme slanja poruke zahtjeva.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Račun
OIB | OIB obveznika fiskalizacije. | DA | Char(11)
U sustavu PDV
Oznaka je li obveznik u sustavu PDV-a ili nije.
True ako je obveznik u sustavu PDV-a, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Datum i vrijeme izdavanja
Datum i vrijeme izdavanja koji se ispisuju na računu.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Oznaka slijednosti
Oznaka slijednosti brojeva računa.
Oznaka koja govori gdje se određuje dodjela broja računa tj. dodjeljuje li se broj računa centralno na razini poslovnog prostora ili pojedinačno na svakom naplatnom uređaju.
Dodjela brojeva računa može biti na razini poslovnog prostora ili naplatnog uređaja:
P - na nivou poslovnog prostora
N - na nivou naplatnog uređaja
| DA | Char(1)
Broj računa
Propisat će se izgled broja računa kako se treba ispisivati na fizičkom računu u sljedećem obliku:
brojčana oznaka računa/oznaka poslovnog prostora/oznaka naplatnog uređaja
Primjer: 1234567890/POSL1/12
Podaci će se Poreznoj upravi dostavljati odvojeni u XML-u radi kasnije lakše manipulacije u izvještajima i analizama.
| DA
Brojčana oznaka računa | Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule. | DA | Varchar(20)
Oznaka poslovnog prostora
Može sadržavati samo znamenke i slova 0-9, a-z, A-Z.
Mora biti jedinstvena na razini OIB-a obveznika.
| DA | Varchar(20)
Oznaka naplatnog uređaja
Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule.
Mora biti jedinstvena na razini jednog poslovnog prostora obveznika.
| DA | Varchar(20)
PDV
Porez na dodanu vrijednost.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji PDV.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 25,00% se dostavlja kao 25.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
PNP
Porez na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji porez na potrošnju.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 3,00% se dostavlja kao 3.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Ostali porezi
Ostali porezi koji se mogu pojaviti na računu osim PDV-a i poreza na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje ostali porezi.
Podatak se sastoji od naziva poreza, porezne stope, osnovice i iznosa poreza.
Može postojati lista poreza.
| NE
Naziv poreza | Naziv poreza za koji se šalju podaci. Npr. Porez na luksuz. | DA, ako postoji porez | Varchar(100)
Porezna stopa | Iznos porezne stope. Npr. stopa od 15,00% se dostavlja kao 15.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Iznos oslobođenja
Ukupni iznos oslobođenja na računu.
Oslobođenja u slučajevima kada se isporučuju dobra ili obavljaju usluge koje su oslobođene od plaćanja PDV-a.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji oslobođenje.
| NE | Decimal(15,2)
Iznos na koji se odnosi poseban postupak oporezivanja marže
Ukupni iznos na koji se odnosi poseban postupak oporezivanja marže na računu.
Marža za rabljena dobra, umjetnička djela, kolekcionarske ili antikne predmete.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji poseban postupak oporezivanja marže.
| NE | Decimal(15,2)
Iznos koji ne podliježe oporezivanju
Ukupni iznos koji ne podliježe oporezivanju na računu.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji iznos koji ne podliježe oporezivanju.
| NE | Decimal(15,2)
Naknade
Naknade koje se mogu pojaviti na računu tipa povratne naknade za ambalažu i sl.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje naknade.
Podatak se sastoji od naziva naknade i iznosa naknade.
Može postojati lista naknada.
| NE
Naziv naknade | Opisno naziv naknade. | DA, ako postoji naknada | Varchar(100)
Iznos naknade |  | DA, ako postoji naknada | Decimal(15,2)
Ukupan iznos | Ukupan iznos iskazan na računu. | DA | Decimal(15,2)
Način plaćanja
G - gotovina
K - kartice
C - ček
T - transakcijski račun
O - ostalo
U slučaju više načina plaćanja po jednom računu, isto je potrebno prijaviti pod 'Ostalo'.
Za sve načine plaćanja koji nisu prije navedeni koristiti će se oznaka 1397967985Ostalo’.
| DA | Char(1)
OIB operatera na naplatnom uređaju
OIB operatera na naplatnom uređaju koji izdaje račun.
U slučaju samouslužnih naplatnih uređaja i automata potrebno je dostaviti OIB izdavatelja (OIB s računa).
| DA | Char(11)
Zaštitni kod izdavatelja
Zaštitni kod izdavatelja obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i izdanog računa.
Zaštitni kod generira obveznik fiskalizacije sukladno algoritmu opisanom u poglavlju 12 ovog dokumenta i ispisuje na računu.
32-znamenkasti broj zapisan u heksadecimalnom formatu.
Može sadržavati znamenke 0-9 i mala slova a-f.
Primjer:
e4d909c290d0fb1ca068ffaddf22cbd0
| DA | Char(32)
Oznaka naknadne dostave računa
Pod naknadnom dostavom računa Poreznoj upravi smatra se situacija kad je isti prethodno izdan kupcu bez JIR-a (npr. prekid Internet veze ili potpuni prestanak rada naplatnog uređaja).
True ako je riječ o naknadnoj dostavi računa, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Oznaka paragon računa | Dostavlja se samo u slučaju potpunog prestanka rada naplatnog uređaja kada obveznik fiskalizacije mora prepisati izdane paragon račune i prijaviti ih putem poruke Poreznoj upravi. | NE | Varchar(100)
Specifična namjena | Predviđeno za slučaj da se naknadno pojavi potreba za dostavom podataka koji nisu prepoznati tokom analize. | NE | Varchar(1000)
1.1.1. Podatkovni skup odgovora za račun
U tablici u nastavku opisan je podatkovni skup poruke odgovora za račun.
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
Jedinstveni identifikator računa
JIR
Jedinstveni identifikator računa.
U slučaju greške, JIR se ne šalje u odgovoru.
| NE | Char(36)
Greške
Šifra greške
Šifra greške je u formatu sXXX gdje je XXX troznamenkasti prirodni broj.
Šifre grešaka sukladno šifarniku grešaka.
| DA, ako ima grešaka | Varchar(4)
Poruka | Poruka greške je tekstualni opis greške sukladno šifarniku grešaka. | DA, ako ima grešaka | Varchar(500)
U nastavku je šifarnik grešaka koji je jedinstven za sve tipove poruka.
Šifra greške | Poruka greške
s001 | 'Poruka nije u skladu s XML shemom : #element ili lista elemenata koji nisu ispravni po shemi#'
s002 | 'Certifikat nije izdan od strane Fina RDC CA ili je istekao ili je ukinut.'
s003 | 'Certifikat ne sadrži naziv 'Fiskal' .'
s004 | 'Neispravan digitalni potpis.'
s005 | 'OIB iz poruke zahtjeva nije jednak OIB-u iz certifikata.'
s006 | 'Sistemska pogreška prilikom obrade zahtjeva.'
PRIVITAK 2.
Obrazac prijave podataka u sustavu fiskalizacije
OBRAZAC PRIJAVE PODATAKA U SUSTAVU FISKALIZACIJE
Podaci o obvezniku fiskalizacije:
OIB
Ime i prezime/Naziv
Adresa
Oznaka poslovnog prostora
Adresa poslovnog prostora
Tip poslovnog prostora
Vrsta djelatnosti koja se obavlja u poslovnom prostoru
Radno vrijeme i radni dani
Datum otvaranja poslovnog prostora
Datum zatvaranja poslovnog prostora
Status poslovnog prostora
Oznaka o izdavanju dokumenta iz članka 27.b Zakona
Podaci o proizvođaču programskog rješenja:
OIB
Ime i prezime/Naziv
Adresa
Podaci o održavatelju programskog rješenja:
OIB
Ime i prezime/Naziv
Adresa
NAPOMENA*/**/***:
______________________________________________________________________________________________________________________________________________________________________________________________________________
* Kod prijave adrese samoposlužnog uređaja, obveznik fiskalizacije obavezno popunjava dodatno polje u kojem se pobliže opisno opisuje lokaciju samoposlužnog uređaja
** Kod polja »Oznaka o izdavanju dokumenta iz članka 27. b Zakona« obveznik fiskalizacije upisuje DA ako u poslovnom prostoru izdaje prateći dokument iz članka 27.b Zakona.
*** Ako je proizvođač i/ili održavatelj programskog rješenja strana fizička ili pravna osoba koja u Republici Hrvatskoj nema dodijeljen OIB, upisuju se podaci te osobe koji obavezno moraju sadržavati ime i prezime/naziv, adresu, oznaku države i identifikacijski broj strane fizičke ili pravne osobe iz države u kojoj ista ima poslovni nastan.
PRIVITAK 3.
1.1.3 Podatkovni skup zahtjeva za fiskalizaciju prodaje putem samoposlužnog uređaja
U tablici u nastavku opisan je podatkovni skup poruke zahtjeva za fiskalizaciju prodaje putem samoposlužnog uređaja.
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
Datum i vrijeme slanja poruke zahtjeva.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Račun
OIB | OIB obveznika fiskalizacije. | DA | Char(11)
U sustavu PDV
Oznaka je li obveznik u sustavu PDV-a ili nije.
True ako je obveznik u sustavu PDV-a, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Datum i vrijeme izdavanja
Datum i vrijeme transakcije.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Oznaka slijednosti
Oznaka slijednosti brojeva transakcije kod fiskalizacije prodaje.
Oznaka koja govori da se dodjela broja transakcije kod fiskalizacije prodaje dodjeljuje centralno na razini poslovnog prostora.
Dodjela brojeva transakcije kod fiskalizacije prodaje može biti na razini poslovnog prostora:
P - na nivou poslovnog prostora
| DA | Char(1)
Broj računa
Izgled broja transakcije u sljedećem obliku:
brojčana oznaka transakcije/oznaka poslovnog prostora/ISU
Primjer: 1234567890/POSL1/123456789
Podaci će se Poreznoj upravi dostavljati odvojeni u XML-u radi kasnije lakše manipulacije u izvještajima i analizama.
| DA
Brojčana oznaka računa | Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule. | DA | Varchar(20)
Oznaka poslovnog prostora
Može sadržavati samo znamenke i slova 0-9, a-z, A-Z.
Mora biti jedinstvena na razini OIB-a obveznika.
| DA | Varchar(20)
Oznaka naplatnog uređaja | Može sadržavati samo znamenke 0-9. Mora biti jedinstvena na razini jednog samoposlužnog uređaja. Dostavlja se ISU. | DA | Varchar(20)
PDV
Porez na dodanu vrijednost.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji PDV.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 25,00% se dostavlja kao 25.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
PNP
Porez na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji porez na potrošnju.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 3,00% se dostavlja kao 3.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Ostali porezi
Ostali porezi koji se mogu pojaviti na računu osim PDV-a i poreza na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje ostali porezi.
Podatak se sastoji od naziva poreza, porezne stope, osnovice i iznosa poreza.
Može postojati lista poreza.
| NE
Naziv poreza | Naziv poreza za koji se šalju podaci. Npr. Porez na luksuz. | DA, ako postoji porez | Varchar(100)
Porezna stopa | Iznos porezne stope. Npr. stopa od 15,00% se dostavlja kao 15.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Iznos oslobođenja
Ukupni iznos oslobođenja na računu.
Oslobođenja u slučajevima kada se isporučuju dobra ili obavljaju usluge koje su oslobođene od plaćanja PDV-a.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji oslobođenje.
| NE | Decimal(15,2)
Iznos na koji se odnosi poseban postupak oporezivanja marže
Ukupni iznos na koji se odnosi poseban postupak oporezivanja marže na računu.
Marža za rabljena dobra, umjetnička djela, kolekcionarske ili antikne predmete.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji poseban postupak oporezivanja marže.
| NE | Decimal(15,2)
Iznos koji ne podliježe oporezivanju
Ukupni iznos koji ne podliježe oporezivanju na računu.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji iznos koji ne podliježe oporezivanju.
| NE | Decimal(15,2)
Naknade
Naknade koje se mogu pojaviti na računu tipa povratne naknade za ambalažu i sl.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje naknade.
Podatak se sastoji od naziva naknade i iznosa naknade.
Može postojati lista naknada.
| NE
Naziv naknade | Opisno naziv naknade. | DA, ako postoji naknada | Varchar(100)
Iznos naknade |  | DA, ako postoji naknada | Decimal(15,2)
Ukupan iznos | Ukupan iznos transakcije. | DA | Decimal(15,2)
Način plaćanja
G - gotovina
K - kartice
O - ostalo (plaćanje putem sms poruka, mobilne aplikacije i slično).
U slučaju više načina plaćanja po jednoj prodaji, isto je potrebno prijaviti pod 'Ostalo'.
Za sve načine plaćanja koji nisu prije navedeni koristiti će se oznaka 1397967985Ostalo’.
| DA | Char(1)
OIB operatera na naplatnom uređaju | OIB obveznika fiskalizacije | DA | Char(11)
Zaštitni kod izdavatelja
Zaštitni kod izdavatelja obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i fiskalizacije transakcije.
Zaštitni kod generira obveznik fiskalizacije sukladno algoritmu opisanom u poglavlju 12 ovog dokumenta.
32-znamenkasti broj zapisan u heksadecimalnom formatu.
Može sadržavati znamenke 0-9 i mala slova a-f.
Primjer:
e4d909c290d0fb1ca068ffaddf22cbd0
| DA | Char(32)
Oznaka naknadne dostave računa
Pod naknadnom dostavom transakcije Poreznoj upravi smatra se situacija kad je došlo do prestanka internet veze.
True ako je riječ o naknadnoj dostavi transakcije, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Oznaka paragon računa | Oznaka paragon računa se ne dostavlja kod fiskalizacije prodaje putem samoposlužnih uređaja. | NE | Varchar(100)
Specifična namjena | Predviđeno za slučaj da se naknadno pojavi potreba za dostavom podataka koji nisu prepoznati tokom analize. | NE | Varchar(1000)
1.1.3. Podatkovni skup odgovora za fiskalizaciju prodaje putem samoposlužnih uređaja
U tablici u nastavku opisan je podatkovni skup poruke odgovora za fiskalizaciju prodaje putem samoposlužnih uređaja.
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
Jedinstveni identifikator računa
JIR
Oznaka JIR se odnosi na uredno zaprimljene elemente transakcije.
U slučaju greške, JIR se ne šalje u odgovoru.
| NE | Char(36)
Greške
Šifra greške
Šifra greške je u formatu sXXX gdje je XXX troznamenkasti prirodni broj.
Šifre grešaka sukladno šifarniku grešaka.
| DA, ako ima grešaka | Varchar(4)
Poruka | Poruka greške je tekstualni opis greške sukladno šifarniku grešaka. | DA, ako ima grešaka | Varchar(500)
U nastavku je šifarnik grešaka koji je jedinstven za sve tipove poruka.
Šifra greške | Poruka greške
s001 | 'Poruka nije u skladu s XML shemom : #element ili lista elemenata koji nisu ispravni po shemi#'
s002 | 'Certifikat nije izdan od strane Fina RDC CA ili je istekao ili je ukinut.'
s003 | 'Certifikat ne sadrži naziv 'Fiskal' .'
s004 | 'Neispravan digitalni potpis.'
s005 | 'OIB iz poruke zahtjeva nije jednak OIB-u iz certifikata.'
s006 | 'Sistemska pogreška prilikom obrade zahtjeva.'
PRIVITAK 4.
1.1.4. Podatkovni skup zahtjeva za prateći dokument
U tablici u nastavku opisan je podatkovni skup poruke zahtjeva za prateći dokument.
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
Datum i vrijeme slanja poruke zahtjeva.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Prateći dokument
OIB | OIB obveznika fiskalizacije. | DA | Char(11)
Datum i vrijeme izdavanja
Datum i vrijeme izdavanja koji se ispisuju na pratećem dokumentu.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Broj pratećeg dokument
Izgled broja pratećeg dokumenta u sljedećem obliku:
brojčana oznaka pratećeg dokumenta/oznaka poslovnog prostora/oznaka naplatnog uređaja
Primjer: 1234567890/POSL1/12
Podaci će se Poreznoj upravi dostavljati odvojeni u XML-u radi kasnije lakše manipulacije u izvještajima i analizama.
| DA
Brojčana oznaka pratećeg dokumenta | Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule. | DA | Varchar(20)
Oznaka poslovnog prostora
Može sadržavati samo znamenke i slova 0-9, a-z, A-Z.
Mora biti jedinstvena na razini OIB-a obveznika.
| DA | Varchar(20)
Oznaka naplatnog uređaja
Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule.
Mora biti jedinstvena na razini jednog poslovnog prostora obveznika.
| DA | Varchar(20)
Ukupan iznos | Ukupan iznos iskazan na pratećem dokumentu. | DA | Decimal(15,2)
Zaštitni kod izdavatelja
Zaštitni kod izdavatelja obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i pratećeg dokumenta.
Zaštitni kod generira obveznik fiskalizacije sukladno algoritmu opisanom u poglavlju 12 ovog dokumenta i ispisuje na pratećem dokumentu.
32-znamenkasti broj zapisan u heksadecimalnom formatu.
Može sadržavati znamenke 0-9 i mala slova a-f.
Primjer:
e4d909c290d0fb1ca068ffaddf22cbd0
| DA | Char(32)
Oznaka naknadne dostave pratećeg dokumenta
Pod naknadnom dostavom pratećeg dokumenta Poreznoj upravi smatra se situacija kad je isti prethodno izdan kupcu bez JIR-a (npr. prekid Internet veze).
True ako je riječ o naknadnoj dostavi pratećeg dokumenta, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
1.1.4. Podatkovni skup odgovora za prateći dokument
U tablici u nastavku opisan je podatkovni skup poruke odgovora za prateći dokument.
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
Jedinstveni identifikator računa
JIR
Jedinstveni identifikator pratećeg dokumenta.
U slučaju greške, JIR se ne šalje u odgovoru.
| NE | Char(36)
Greške
Šifra greške
Šifra greške je u formatu sXXX gdje je XXX troznamenkasti prirodni broj.
Šifre grešaka sukladno šifarniku grešaka.
| DA, ako ima grešaka | Varchar(4)
Poruka | Poruka greške je tekstualni opis greške sukladno šifarniku grešaka. | DA, ako ima grešaka | Varchar(500)
U nastavku je šifarnik grešaka koji je jedinstven za sve tipove poruka.
Šifra greške | Poruka greške
s001 | 'Poruka nije u skladu s XML shemom : #element ili lista elemenata koji nisu ispravni po shemi#'
s002 | 'Certifikat nije izdan od strane Fina RDC CA ili je istekao ili je ukinut.'
s003 | 'Certifikat ne sadrži naziv 'Fiskal' .'
s004 | 'Neispravan digitalni potpis.'
s005 | 'OIB iz poruke zahtjeva nije jednak OIB-u iz certifikata.'
s006 | 'Sistemska pogreška prilikom obrade zahtjeva.'
PRIVITAK 5.
1.1.5. Podatkovni skup zahtjeva i odgovora za račun nakon pratećeg dokumenta
U tablici u nastavku opisan je podatkovni skup poruke zahtjeva za račun-veza prateći dokument
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
Datum i vrijeme slanja poruke zahtjeva.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Račun
OIB | OIB obveznika fiskalizacije. | DA | Char(11)
U sustavu PDV
Oznaka je li obveznik u sustavu PDV-a ili nije.
True ako je obveznik u sustavu PDV-a, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Datum i vrijeme izdavanja
Datum i vrijeme izdavanja koji se ispisuju na računu.
dd.mm.ggggThh:mm:ss
| DA | Date & Time
Oznaka slijednosti
Oznaka slijednosti brojeva računa.
Oznaka koja govori gdje se određuje dodjela broja računa tj. dodjeljuje li se broj računa centralno na razini poslovnog prostora ili pojedinačno na svakom naplatnom uređaju.
Dodjela brojeva računa može biti na razini poslovnog prostora ili naplatnog uređaja:
P - na nivou poslovnog prostora
N - na nivou naplatnog uređaja
| DA | Char(1)
Broj računa
Propisat će se izgled broja računa kako se treba ispisivati na fizičkom računu u sljedećem obliku:
brojčana oznaka računa/oznaka poslovnog prostora/oznaka naplatnog uređaja
Primjer: 1234567890/POSL1/12
Podaci će se Poreznoj upravi dostavljati odvojeni u XML-u radi kasnije lakše manipulacije u izvještajima i analizama.
| DA
Brojčana oznaka računa | Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule. | DA | Varchar(20)
Oznaka poslovnog prostora
Može sadržavati samo znamenke i slova 0-9, a-z, A-Z.
Mora biti jedinstvena na razini OIB-a obveznika.
| DA | Varchar(20)
Oznaka naplatnog uređaja
Može sadržavati samo znamenke 0-9. Nisu dozvoljene vodeće nule.
Mora biti jedinstvena na razini jednog poslovnog prostora obveznika.
| DA | Varchar(20)
PDV
Porez na dodanu vrijednost.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji PDV.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 25,00% se dostavlja kao 25.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
PNP
Porez na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji porez na potrošnju.
Podatak se sastoji od porezne stope, osnovice i iznosa poreza.
Može postojati lista poreznih stopa.
| NE
Porezna stopa | Iznos porezne stope. Npr. stopa od 3,00% se dostavlja kao 3.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Ostali porezi
Ostali porezi koji se mogu pojaviti na računu osim PDV-a i poreza na potrošnju.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje ostali porezi.
Podatak se sastoji od naziva poreza, porezne stope, osnovice i iznosa poreza.
Može postojati lista poreza.
| NE
Naziv poreza | Naziv poreza za koji se šalju podaci. Npr. Porez na luksuz. | DA, ako postoji porez | Varchar(100)
Porezna stopa | Iznos porezne stope. Npr. stopa od 15,00% se dostavlja kao 15.00. | DA, ako postoji porez | Decimal(3,2)
Osnovica | Iznos osnovice. | DA, ako postoji porez | Decimal(15,2)
Iznos poreza |  | DA, ako postoji porez | Decimal(15,2)
Iznos oslobođenja
Ukupni iznos oslobođenja na računu.
Oslobođenja u slučajevima kada se isporučuju dobra ili obavljaju usluge koje su oslobođene od plaćanja PDV-a.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji oslobođenje.
| NE | Decimal(15,2)
Iznos na koji se odnosi poseban postupak oporezivanja marže
Ukupni iznos na koji se odnosi poseban postupak oporezivanja marže na računu.
Marža za rabljena dobra, umjetnička djela, kolekcionarske ili antikne predmete.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji poseban postupak oporezivanja marže.
| NE | Decimal(15,2)
Iznos koji ne podliježe oporezivanju
Ukupni iznos koji ne podliježe oporezivanju na računu.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoji iznos koji ne podliježe oporezivanju.
| NE | Decimal(15,2)
Naknade
Naknade koje se mogu pojaviti na računu tipa povratne naknade za ambalažu i sl.
Podatak se dostavlja Poreznoj upravi samo ako na računu postoje naknade.
Podatak se sastoji od naziva naknade i iznosa naknade.
Može postojati lista naknada.
| NE
Naziv naknade | Opisno naziv naknade. | DA, ako postoji naknada | Varchar(100)
Iznos naknade |  | DA, ako postoji naknada | Decimal(15,2)
Ukupan iznos | Ukupan iznos iskazan na računu. | DA | Decimal(15,2)
Način plaćanja
G - gotovina
K - kartice
C - ček
T - transakcijski račun
O - ostalo
U slučaju više načina plaćanja po jednom računu, isto je potrebno prijaviti pod 'Ostalo'.
Za sve načine plaćanja koji nisu prije navedeni koristiti će se oznaka 1397967985Ostalo’.
| DA | Char(1)
OIB operatera na naplatnom uređaju
OIB operatera na naplatnom uređaju koji izdaje račun.
U slučaju samouslužnih naplatnih uređaja i automata potrebno je dostaviti OIB izdavatelja (OIB s računa).
| DA | Char(11)
Zaštitni kod izdavatelja
Zaštitni kod izdavatelja obveznika fiskalizacije je alfanumerički zapis kojim se potvrđuje veza između obveznika fiskalizacije i izdanog računa.
Zaštitni kod generira obveznik fiskalizacije sukladno algoritmu opisanom u poglavlju 12 ovog dokumenta i ispisuje na računu.
32-znamenkasti broj zapisan u heksadecimalnom formatu.
Može sadržavati znamenke 0-9 i mala slova a-f.
Primjer:
e4d909c290d0fb1ca068ffaddf22cbd0
| DA | Char(32)
Oznaka naknadne dostave računa
Pod naknadnom dostavom računa Poreznoj upravi smatra se situacija kad je isti prethodno izdan kupcu bez JIR-a (npr. prekid Internet veze ili potpuni prestanak rada naplatnog uređaja).
True ako je riječ o naknadnoj dostavi računa, u suprotnom false.
Boolean (1-true/0-false)
| DA | Boolean
Oznaka paragon računa | Dostavlja se samo u slučaju potpunog prestanka rada naplatnog uređaja kada obveznik fiskalizacije mora prepisati izdane paragon račune i prijaviti ih putem poruke Poreznoj upravi. | NE | Varchar(100)
Specifična namjena | Predviđeno za slučaj da se naknadno pojavi potreba za dostavom podataka koji nisu prepoznati tokom analize. | NE | Varchar(1000)
JIR PD | Jedinstveni identifikator pratećeg dokumenta. U slučaju kada postoji više pratećih dokumenta potrebno je dostaviti podatak o JIR PD jednog od pratećih dokumenata. | Da, ako ne postoji JIR PD, obvezan je ZKI PD
Zaštitni kod izdavatelja PD | Zaštitni kod izdavatelja obveznika fiskalizacije za prateći dokument. U slučaju kada postoji više pratećih dokumenta, potrebno je dostaviti Zaštitni kod izdavatelja obveznika fiskalizacije za isti prateći dokument za koji se dostavlja JIR PD. | Da, ako ne postoji JIR PD
1.1.5. Podatkovni skup odgovora za račun
U tablici u nastavku opisan je podatkovni skup poruke odgovora za račun.
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
Jedinstveni identifikator računa
JIR
Jedinstveni identifikator računa.
U slučaju greške, JIR se ne šalje u odgovoru.
| NE | Char(36)
Greške
Šifra greške
Šifra greške je u formatu sXXX gdje je XXX troznamenkasti prirodni broj.
Šifre grešaka sukladno šifarniku grešaka.
| DA, ako ima grešaka | Varchar(4)
Poruka | Poruka greške je tekstualni opis greške sukladno šifarniku grešaka. | DA, ako ima grešaka | Varchar(500)
U nastavku je šifarnik grešaka koji je jedinstven za sve tipove poruka.
Šifra greške | Poruka greške
s001 | 'Poruka nije u skladu s XML shemom : #element ili lista elemenata koji nisu ispravni po shemi#'
s002 | 'Certifikat nije izdan od strane Fina RDC CA ili je istekao ili je ukinut.'
s003 | 'Certifikat ne sadrži naziv 'Fiskal' .'
s004 | 'Neispravan digitalni potpis.'
s005 | 'OIB iz poruke zahtjeva nije jednak OIB-u iz certifikata.'
s006 | 'Sistemska pogreška prilikom obrade zahtjeva.'
