UPUTA
za operativne postupke Hrvatskog sustava velikih plaćanja
Ovom uputom uređuju se operativni postupci Hrvatskog sustava velikih plaćanja (u nastavku teksta: HSVP), i to:
- vrste platnih poruka
- tehnička valjanost platnih poruka
- način upisivanja pojedinih elemenata s naloga za plaćanje u platne poruke
- ostale poruke
- način zadavanja platnih poruka između Hrvatske narodne banke i ostalih banaka u HSVP-u
- način zadavanja direktnih transfera
- sudjelovanje u obračunu preko HSVP-a banaka koje nisu osposobljene za razmjenu poruka SWIFT telekomunikacijskom mrežom.
1. PLATNE PORUKE
Platne poruke su odgovarajuće vrste SWIFT poruka kojima sudionik zadaje plaćanja na teret svog računa za namiru u HSVP-u.
1.1. Vrste platnih poruka
Platne su poruke u HSVP-u sljedeće vrste SWIFT poruka:
- MT103
- MT102
- MT202
- MT205.
Opis i način upotrebe platnih poruka odgovaraju propisanim SWIFT standardima.
1.2. Tehnička valjanost platne poruke
Uvjet je za namirenje platne poruke na računu za namiru sudionika njezina tehnička valjanost. Tehnički valjana platna poruka mora:
- u zaglavlju, u polju 103 (FIN Copy Service Code), kao oznaku servisnoga identifikacijskoga koda, imati upisanu oznaku »HRK«
- u tekstualnom dijelu, u polju 32A, kao oznaku valute, imati upisanu oznaku »HRK«
- u tekstualnom dijelu, u polju 32A, kao oznaku datuma valute, imati upisan datum koji odgovara datumu tekućega obračunskog dana
- zadovoljavati sve ostale propisane SWIFT standarde.
Platna poruka koja ne zadovoljava navedene uvjete, neće biti namirena.
1.3. Platne poruke s budućim datumom valute
Sudionik može zadavati platne poruke sedam dana unaprijed u odnosu na datum valute upisan u polje 32A tekstualnog dijela poruke. Platne poruke s budućim datumom valute bit će namirene na računu za namiru sudionika na obračunski dan koji odgovara upisanom datumu valute.
1.4. Prioritet izvršenja platne poruke
Oznaka prioriteta izvršenja platne transakcije upisuje se, u zaglavlju platne poruke, u polje 113.
2. NAČIN UPISIVANJA POJEDINIH ELEMENATA S NALOGA ZA PLAĆANJE U PLATNE PORUKE
Platne poruke moraju biti popunjene na način koji odgovara svim propisanim SWIFT standardima.
2.1. Broj računa platitelja
Broj računa platitelja, u banci platitelju, upisuje se u platnu poruku MT103 i MT102, u tekstualnom dijelu, u prvi red polja 50K.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa u banci.
2.2. Naziv računa platitelja
Naziv računa platitelja (naziv platitelja), u banci platitelju, upisuje se u platnu poruku MT103 i MT102, u tekstualnom dijelu, u drugi red i u ostale redove polja 50K.
2.3. Broj računa primatelja
Broj računa primatelja, u banci primatelju, upisuje se u platnu poruku MT103 i MT102, u tekstualnom dijelu, u prvi red polja 59.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa u banci.
2.4. Naziv računa primatelja
Naziv računa primatelja, u banci primatelju, upisuje se u platnu poruku MT103 i MT102, u tekstualnom dijelu, u drugi red i u ostale redove polja 59.
2.5. Vrsta posla, poziv na broj odobrenja/poziv na broj zaduženja
U sve platne poruke poziv na broj odobrenja/poziv na broj zaduženja upisuju se, u tekstualnom dijelu poruke, u polje 72, i to:
- U prvi se red upisuje brojčana oznaka vrste posla. Upisuje se oznaka »/VPO/« i brojčana oznaka vrste posla. Brojčanu oznaku vrste posla i način upisa dogovaraju banke međusobno.
- U drugi se red upisuje poziv na broj zaduženja. Upisuje se oznaka »/ZAD/« i brojčana oznaka poziva na broj zaduženja. Između modela poziva na broj (M) i pojedinih elemenata poziva na broj (P1, P2, P3, P4) upisuje se crtica (»-«) bez razmaka (M-P1-P2-P3-P4).
- U treći se red upisuje poziv na broj odobrenja. Upisuje se oznaka »/ODO/« i brojčana oznaka poziva na broj odobrenja. Između modela poziva na broj (M) i pojedinih elemenata poziva na broj (P1, P2, P3, P4) upisuje se crtica (»-«) bez razmaka (M-P1-P2-P3-P4).
Oznake »/VPO/«, »/ZAD/« i »/ODO/« upisuju se bez obzira na to postoji li podatak o vrsti posla, pozivu na broj zaduženja ili pozivu na broj odobrenja.
2.6. Opis plaćanja
a) Platne poruke MT103 i MT102
U platne poruke MT103 i MT102 opis plaćanja upisuje se, u tekstualnom dijelu poruke, u polje 70.
b) Platne poruke MT202 i MT205
U platne poruke MT202 i MT205 opis plaćanja upisuje se, u tekstualnom dijelu poruke, u četvrti i peti red polja 72 (prvi, drugi i treći red popunjavaju se kako je navedeno u točki 2.5.).
3. OSTALE PORUKE (SERVISNE PORUKE)
Ostale su poruke u HSVP-u SWIFT poruke (u nastavku teksta: servisne poruke) kojima sudionici dobivaju obavijesti o platnim transakcijama zadanim preko HSVP-a, o stanju i promjenama na računu za namiru sudionika i druge obavijesti vezane uz sudjelovanje u obračunu preko HSVP-a.
3.1. Važnije servisne poruke
Potvrdu o izvršenom namirenju platne transakcije na njegovu računu za namiru sudionik dobiva putem poruke MT012.
Obavijest o odbijenim platnim transakcijama sudionik dobiva putem poruke MT019.
Izvješće o promjenama i stanju na računu za namiru na kraju dana sudionik dobiva putem poruke MT950.
Obavijest o izvršenom direktnom transferu na teret računa za namiru sudionik dobiva putem poruke MT900.
Obavijest o izvršenom direktnom transferu u korist računa za namiru sudionik dobiva putem poruke MT910.
3.2. Ostale servisne poruke
Pregled ostalih servisnih poruka, njihov opis i način upotrebe dani su u Funkcionalnim specifikacijama HSVP-a, koje svakom sudioniku dostavlja Hrvatska narodna banka prilikom samostalnog uključenja u obračun preko HSVP-a.
4. NAČIN ZADAVANJA PLATNIH PORUKA IZMEĐU HRVATSKE NARODNE BANKE I OSTALIH BANAKA U HSVP-u
Platne poruke u korist računa za namiru Hrvatske narodne banke banka upućuje na SWIFT adresu NBHRHR2D.
Platne poruke u korist prolaznog računa za namiru trgovanja vrijednosnim papirima banka upućuje na SWIFT adresu SDAHHR22.
Banka upućuje na SWIFT adresu SDAHHR22 samo one platne poruke kojima provodi plaćanja na temelju naloga za plaćanje koji su, u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima, ispostavljeni u korist prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci.
Broj prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci jest 1001005-1310020013.
Za zadavanje platnih transakcija između Hrvatske narodne banke i ostalih banaka u HSVP-u upotrebljavaju se odgovarajuće vrste platnih poruka. Navedene platne poruke moraju zadovoljavati sve uvjete propisane SWIFT standardima i ovom uputom.
4.1. Platna poruka MT202
4.1.1. Upotreba platne poruke MT202 prema vrstama posla
Hrvatska narodna banka zadaje platnu poruku MT202 u korist računa za namiru banaka kad se obavljaju sljedeće vrste poslova:
- odobrenje lombardnoga kredita;
- odobrenje sredstava po obratnoj repo transakciji;
- povrat obveznih blagajničkih zapisa na temelju rasta plasmana u kunama;
- ispis blagajničkih zapisa HNB-a u kunama;
- prijevremeni iskup blagajničkih zapisa HNB-a u kunama;
- odobrenje kratkoročnoga kredita za likvidnost;
- povrat sredstava po repo transakciji;
- kupnja vrijednosnih papira;
- povrat prekonoćnoga depozita;
- kupnja deviza;
- kupnja deviza po ugovoru o obvezi reotkupa;
- povrat sredstava za pokriće obračuna iz NKS-a;
- povrat obvezne pričuve po obračunu.
Banka zadaje platnu poruku MT202 u korist računa za namiru Hrvatske narodne banke kad se obavljaju sljedeće vrste poslova:
- povrat lombardnoga kredita;
- povrat sredstava po obratnoj repo transakciji;
- upis obveznih blagajničkih zapisa na temelju rasta plasmana u kunama;
- upis blagajničkih zapisa HNB-a u kunama;
- povrat kratkoročnoga kredita za likvidnost;
- polog sredstava po repo transakciji;
- prodaja vrijednosnih papira;
- polog prekonoćnoga depozita;
- prodaja deviza;
- prodaja efektivnoga stranog novca;
- prodaja deviza po ugovoru o obvezi reotkupa;
- izdvajanje sredstava za pokriće obračuna iz NKS-a;
- izdvajanje obvezne pričuve po obračunu.
4.1.2. Način popunjavanja platne poruke MT202
4.1.2.1. Polje 21 - brojčana oznaka vrste plaćanja
Radi označivanja vrste plaćanja platna poruka MT202 mora imati popunjeno polje 21 u tekstualnom dijelu poruke, ovisno o vrsti plaćanja.
Struktura polja 21 (15 znakova) propisana je kako slijedi:
AABBCCCCDDDDDDD
pri čemu je:
AA brojčana oznaka vrste posla
BB brojčana oznaka karaktera transakcije
CCCC brojčana oznaka specifične karakteristike pojedinog posla
DDDDDDD vodeći broj banke - VBB.
a) Brojčane oznake vrste posla
Prema pojedinim vrstama poslova na mjestu označenom s AA u strukturi polja 21, upisuju se sljedeće oznake:
Vrsta posla
Oznaka
1
2
lombardni kredit (odobrenje i povrat)
01
sredstva po obratnoj repo transakciji (odobrenje i povrat)
02
povrat/upis obveznih blagajničkih zapisa na temelju rasta plasmana u kunama
03
ispis/upis blagajničkih zapisa HNB-a u kunama
04
prijevremeni iskup blagajničkih zapisa HNB-a u kunama
05
kratkoročni kredit za likvidnost (odobrenje i povrat)
06
sredstva po repo transakciji (povrat i polog)
07
kupnja/prodaja vrijednosnih papira
08
povrat/polog prekonoćnoga depozita
09
kupnja/prodaja deviza
31
prodaja efektivnoga stranog novca
32
kupnja/prodaja deviza po ugovoru o obvezi reotkupa
33
povrat/izdvajanje sredstava za pokriće obračuna iz NKS-a
51
povrat/izdvajanje obvezne pričuve po obračunu
71
b) Brojčane oznake karaktera platne transakcije
Prema karakteru platne transakcije na mjestu označenom s BB u strukturi polja 21 upisuju se sljedeće oznake:
Karakter platne transakcije
Oznaka
1
2
transakcije emitiranja sredstava od strane Hrvatske narodne banke
01
transakcije prijenosa sredstava na račun Hrvatske narodne banke
02
c) Brojčane oznake specifične karakteristike pojedinog posla
Prema specifičnim karakteristikama pojedinih vrsta poslova, kod određenih vrsta poslova, na mjestu označenom sa CCCC u strukturi polja 21 upisuju se sljedeće oznake:
Vrsta posla
Specifične karakteristike
Oznaka
1
2
3
ispis/upis blagajničkih zapisa HNB-a u kunama
blagajnički zapisi s rokom dospijeća od 35 dana
0035
povrat prekonoćnoga depozita
obustava mogućnosti polaganja
0001
Kod ostalih vrsta poslova, kod kojih nisu propisane specifične karakteristike, na mjestu označenom sa CCCC u strukturi polja 21 upisuju se nule.
d) Vodeći broj banke - VBB
Na mjestu označenom sa DDDDDDD u strukturi polja 21 upisuje se vodeći broj banke zadavatelja platne transakcije.
Kad platnu transakciju zadaje Hrvatska narodna banka, upisuje se vodeći broj banke primatelja platne transakcije.
e) Primjeri popunjavanja polja 21 prema vrstama posla
Vrsta posla
Karakter transakcije
Specifične karakteristike
Oznaka
vrste posla
1
2
3
4
lombardni kredit
(odobrenje i povrat)
odobrenje
01010000DDDDDDD
povrat
01020000DDDDDDD
sredstva po obratnoj repo transakciji (odobrenje i povrat)
odobrenje
02010000DDDDDDD
povrat
02020000DDDDDDD
povrat/upis obveznih blagajničkih zapisa na temelju rasta plasmana u kunama
povrat
03010000DDDDDDD
upis
03020000DDDDDDD
ispis/upis blagajničkih zapisa HNB-a u kunama
ispis
35 dana
04010035DDDDDDD
upis
35 dana
04020035DDDDDDD
prijevremeni iskup blagajničkih zapisa HNB-a u kunama
iskup
05010000DDDDDDD
kratkoročni kredit za likvidnost
(odobrenje i povrat)
odobrenje
06010000DDDDDDD
povrat
06020000DDDDDDD
sredstva po repo transakciji (povrat i polog)
povrat
07010000DDDDDDD
polog
07020000DDDDDDD
kupnja/prodaja vrijednosnih papira
kupnja
08010000DDDDDDD
prodaja
08020000DDDDDDD
povrat/polog prekonoćnoga depozita
povrat
09010000DDDDDDD
povrat
obustava mogućnosti polaganja
09010001DDDDDDD
polog
09020000DDDDDDD
kupnja/prodaja deviza
kupnja
31010000DDDDDDD
prodaja
31020000DDDDDDD
prodaja efektivnoga stranog novca
prodaja
32020000DDDDDDD
kupnja/prodaja deviza po ugovoru o obvezi reotkupa
kupnja
33010000DDDDDDD
prodaja
33020000DDDDDDD
povrat/izdvajanje sredstava za pokriće obračuna iz NKS-a
povrat
51010000DDDDDDD
izdvajanje
51020000DDDDDDD
povrat/izdvajanje obvezne pričuve po obračunu
povrat
71010000DDDDDDD
izdvajanje
71020000DDDDDDD
4.1.2.2. Polje 72 - tekstualni opis vrste plaćanja
Radi označivanja vrste plaćanja platna poruka MT 202, kojom banka zadaje platnu transakciju u korist računa za namiru Hrvatske narodne banke, mora uz popunjeno polje 21 (točka 4.1.2. pod a)) na propisani način imati popunjeno i polje 72 u tekstualnom dijelu poruke.
Polje 72 sadrži tekstualni opis plaćanja u korist Hrvatske narodne banke u skladu sa stupcima 1 i 2 iz tablice s primjerima popunjavanja polja 21 prema vrstama posla.
4.2. Platna poruka MT103
Uz uvjete propisane ovom točkom platna poruka MT103 kojom se izvršavaju plaćanja između Hrvatske narodne banke i banaka upotrebljava se i popunjava na način kako je to uređeno točkom 1. i 2. ove upute.
4.2.1. Upotreba platne poruke MT103
Pri izvršenju plaćanja između Hrvatske narodne banke i banaka platna poruka MT103 upotrebljava se:
- za prijenos sredstava u svrhu opskrbe banaka gotovim novcem s računa za namiru banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci, odnosno s računa banke za gotovinu u Hrvatskoj narodnoj banci na njezin račun za namiru
- za izvršenje međubankovnih plaćanja na teret/u korist transakcijskih računa koje vodi Hrvatska narodna banka, ako je izvršenje tih plaćanja preko HSVP-a u skladu s drugim propisima
- za izvršenje plaćanja u korist/na teret prolaznog računa za namiru trgovanja vrijednosnim papirima koje se provodi u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima.
Hrvatska narodna banka zadaje platnu poruku MT103 u korist računa za namiru banaka na osnovi:
- izvršenja naloga banke za prijenos sredstava s njezina računa za gotovinu u Hrvatskoj narodnoj banci na njezin račun za namiru
- izvršenja međubankovnih plaćanja na teret transakcijskih računa koje vodi Hrvatska narodna banka.
Središnja depozitarna agencija zadaje platnu poruku MT103 u korist računa za namiru banaka na osnovi:
- izvršenja plaćanja na teret prolaznog računa za namiru trgovanja vrijednosnim papirima koja se provode u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima.
Banka zadaje platnu poruku MT103 u korist računa za namiru Hrvatske narodne banke (SWIFT adresa NBHRHR2D) na osnovi:
- izvršenja prijenosa sredstava s računa za namiru banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci
- izvršenja međubankovnih plaćanja u korist transakcijskih računa koje vodi Hrvatske narodna banka, ako je izvršenje tih plaćanja preko HSVP-a u skladu s drugim propisima.
Banka zadaje platnu poruku MT103 u korist prolaznog računa za namiru trgovanja vrijednosnim papirima (SWIFT adresa SDAHHR22) na osnovi:
- izvršenja plaćanja koje provodi na temelju naloga za plaćanje ispostavljenog, u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima, u korist prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci broj: 1001005-1310020013.
4.2.2. Način popunjavanja platne poruke MT103 - prijenos sredstava na osnovi opskrbe banaka gotovim novcem
Prijenos sredstava na osnovi opskrbe banaka gotovim novcem obavlja se na način propisan Odlukom o opskrbi banaka gotovim novcem.
Platnu poruku MT103 kojom prenosi sredstva u korist računa banke za gotovinu u Hrvatskoj narodnoj banci banka upućuje na SWIFT adresu NBHRHR2D.
4.2.2.1. Polje 50K - Broj računa platitelja
U prvi red polja upisuje se broj računa platitelja, a u sljedeće redove polja naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa.
Kod prijenosa sredstava s računa za gotovinu banke u Hrvatskoj narodnoj banci na njezin račun za namiru Hrvatska narodna banka upisuje broj računa banke za gotovinu u Hrvatskoj narodnoj banci.
Kod prijenosa sredstava s računa za namiru banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci banka upisuje broj svog računa kojim se koristi za evidentiranje gotovog novca (interni račun banke za evidenciju gotovog novca).
4.2.2.2. Polje 59 - Broj računa primatelja
U prvi red polja upisuje se broj računa primatelja, a u sljedeće redove polja naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa.
Kod prijenosa sredstava s računa za gotovinu banke u Hrvatskoj narodnoj banci na njen račun za namiru Hrvatska narodna banka upisuje broj internog računa banke za evidentiranje gotovog novca koji je banka upisala u nalog za prijenos sredstava na račun za namiru.
Kod prijenosa sredstava s računa za namiru banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci banka upisuje broj računa banke za gotovinu u Hrvatskoj narodnoj banci.
4.2.3. Način popunjavanja platne poruke MT103 - izvršenje međubankovnih plaćanja na teret/u korist transakcijskih računa koje vodi Hrvatska narodna banka
Platnu poruku MT 103 kojom se izvršava plaćanje u korist transakcijskog računa koji vodi Hrvatska narodna banka, ako je izvršenje tog plaćanja preko HSVP-a u skladu s drugim propisima, banka upućuje na SWIFT adresu NBHRHR2D.
4.2.3.1. Polje 50K - Broj računa platitelja
U prvi red polja upisuje se broj računa platitelja, a u sljedeće redove polja naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa.
Hrvatska narodna banka upisuje broj transakcijskog računa u Hrvatskoj narodnoj banci koji se tereti na osnovi izvršenja platne poruke.
Banka upisuje broj transakcijskog računa u banci koji se tereti na osnovi izvršenja platne poruke.
4.2.3.2. Polje 59 - Broj računa primatelja
U prvi red polja upisuje se broj računa primatelja, a u sljedeće redove polja naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa.
Hrvatska narodna banka upisuje broj transakcijskog računa u banci koji se odobrava na osnovi izvršenja platne poruke.
Banka upisuje broj transakcijskog računa u Hrvatskoj narodnoj banci koji se odobrava na osnovi izvršenja platne poruke.
4.2.3.3. Polje 72 - Poziv na broj
Banka/Hrvatska narodna banka u polje 72 upisuje poziv na broj, u skladu s točkom 2.5. ove upute.
4.2.4. Način popunjavanja platne poruke MT103 - izvršenje plaćanja na teret/u korist prolaznog računa za namiru trgovanja vrijednosnim papirima
Prijenos sredstava po osnovi trgovanja vrijednosnim papirima obavlja se u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima.
Platnu poruku kojom provodi plaćanje u korist prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci (broj računa: 1001005-1310020013) banka upućuje na SWIFT adresu SDAHHR22.
4.2.4.1. Polje 50K - Broj računa platitelja
U prvi red polja upisuje se broj računa platitelja, a u sljedeće redove polja naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«), vodeći broj banke, crtica (»-«) i partija računa.
Središnja depozitarna agencija upisuje broj prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci, i to: 1001005-1310020013.
Banka, na temelju naloga za plaćanje koji je u skladu s propisima ispostavljen u korist prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci broj: 1001005-1310020013, upisuje broj transakcijskog računa u banci koji se tereti na osnovi izvršenja platne poruke.
4.2.4.2. Polje 59 - Broj računa primatelja
U prvi red upisuje se broj računa primatelja, a u sljedeće redove naziv računa.
Broj računa upisuje se u sljedećem formatu, bez razmaka: kosa crta (»/«) iza koje slijedi vodeći broj, crtica (»-«) i partija računa.
Središnja depozitarna agencija, u skladu s propisima kojima se uređuje trgovanje vrijednosnim papirima, upisuje broj transakcijskog računa u banci koji se odobrava po osnovi izvršenja platne poruke.
Banka, na temelju naloga za plaćanje koji je u skladu s propisima ispostavljen u korist prolaznog računa za namiru trgovanja vrijednosnim papirima otvorenog u Hrvatskoj narodnoj banci broj: 1001005-1310020013, upisuje taj broj računa.
4.2.4.3. Polje 72 - Poziv na broj odobrenja
Banka/Središnja depozitarna agencija u polje 72 upisuje poziv na broj odobrenja, u skladu s točkom 2.5. ove upute.
5. NAČIN ZADAVANJA DIREKTNIH TRANSFERA
Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru sudionika:
- na temelju naloga banke
- na temelju zakonskih propisa.
5.1. Direktni transfer na temelju naloga banke
Hrvatska narodna banka zadaje direktni transfer na temelju naloga primljenog od sudionika. Nalog za zadavanje direktnog transfera sudionik podnosi na obrascu Nalog HSVP/DT. Obrazac Nalog HSVP/DT kreira Hrvatska narodna banka i primjerak obrasca dostavlja svim bankama.
Popunjeni Nalog HSVP/DT (u nastavku teksta: Nalog) banka dostavlja telefaksom Hrvatskoj narodnoj banci. Hrvatska narodna banka dostavlja svim bankama broj telefaksa za dostavu Naloga.
Nakon što je primila popunjeni Nalog, Hrvatska narodna banka telefonski usklađuje vjerodostojnost podataka iz Naloga s bankom pošiljateljem Naloga.
Kako bi omogućila usklađivanje vjerodostojnosti podataka iz Naloga, Hrvatska narodna banka dostavlja svim bankama šifru za usklađivanje.
Usklađivanje vjerodostojnosti podataka iz Naloga provodi se, nakon što ga Hrvatska narodna banka primi telefaksom, na sljedeći način:
- Hrvatska narodna banka telefonski zove banku pošiljatelja Naloga
- banka pošiljatelj Naloga priopćuje šifru za usklađivanje
- banka pošiljatelj Naloga čita podatke s Naloga koji je dostavljen Hrvatskoj narodnoj banci, a Hrvatska narodna banka ih uparuje s podacima na primljenom Nalogu.
Nakon što je usklađivanje provedeno, Hrvatska narodna banka zadaje direktni transfer u skladu s podacima na Nalogu.
Banka dostavlja Hrvatskoj narodnoj banci broj telefona i imena osoba za kontakt koje će provoditi usklađivanje.
5.2. Direktni transfer na temelju propisa
a) Namirenje neto pozicije iz NKS-a
Namirenje neto pozicije iz NKS-a obavlja Hrvatska narodna banka na temelju podataka dobivenih od NKS-a o konačnim neto pozicijama na obračunskim računima banaka i Hrvatske narodne banke u NKS-u na kraju obračunskog dana.
Namirenje neto pozicije iz NKS-a obavlja se na sljedeći način:
- ako je neto pozicija iz NKS-a pozitivna, Hrvatska narodna banka zadaje direktni transfer u korist računa za namiru sudionika, a na teret obračunskog računa za NKS
- ako je neto pozicija iz NKS-a negativna, Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru sudionika, a u korist obračunskog računa za NKS.
b) Povrat sredstava banke prethodno izdvojenih za osiguranje pokrića u obračunu preko NKS-a
Hrvatska narodna banka zadaje direktni transfer u korist računa za namiru banke radi povrata sredstava koje je banka izdvojila tijekom dana na poseban račun za osiguranje pokrića obračuna iz NKS-a u Hrvatskoj narodnoj banci.
c) Izvršenje osnova za naplatu
Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru banke na osnovi izvršenja zaprimljenih osnova za naplatu izdanih na teret računa banke u Hrvatskoj narodnoj banci.
6. NAČIN SUDJELOVANJA U OBRAČUNU PREKO HSVP-a BANAKA KOJE NISU TEHNIČKI OSPOSOBLJENE ZA RAZMJENU PORUKA SWIFT TELEKOMUNIKACIJSKOM MREŽOM
Sve operativne poslove vezane uz sudjelovanje u obračunu preko HSVP-a za banke koje nisu osposobljene za razmjenu poruka SWIFT telekomunikacijskom mrežom (u nastavku teksta: sudionici koji nisu u SWIFT-u) obavlja Hrvatska narodna banka.
Platne transakcije na teret računa za namiru sudionika koji nije u SWIFT-u zadaje Hrvatska narodna banka direktnim transferima u uvjetima i na način propisan u točki 5. ove upute.
Obavijest o stanju na računu za namiru sudionika koji nije u SWIFT-u tijekom obračunskog dana Hrvatska narodna banka daje na način dogovoren između sudionika i Hrvatske narodne banke.
Hrvatska narodna banka dostavlja sudioniku koji nije u SWIFT-u Izvješće o stanju i izvršenim platnim transakcijama na njegovu računu za namiru preporučenom pošiljkom, prvoga radnog dana u tjednu, za protekli tjedan.
* * *
CJENIK
usluga Hrvatskog sustava velikih plaćanja
I.
(1) Cjenikom usluga HSVP-a određuje se naknada za plaćanja izvršena preko Hrvatskog sustava velikih plaćanja (u nastavku teksta: HSVP).
(2) Naknada za plaćanja izvršena preko HSVP-a podrazumijeva naknadu za usluge platnog prometa u Hrvatskoj narodnoj banci koje su vezane uz propisano sudjelovanje banaka u obračunu preko HSVP-a (u nastavku teksta: usluge HSVP-a).
II.
Banka - sudionik obračuna preko HSVP-a (u nastavku teksta: banka) naknadu za usluge HSVP-a plaća Hrvatskoj narodnoj banci.
III.
(1) Hrvatska narodna banka obavlja obračun učinjenih troškova po tarifnim stavkama u skladu s Cjenikom HSVP-a četiri puta godišnje, i to za sljedeća obračunska razdoblja:
- od 1. siječnja do 31. ožujka
- od 1. travnja do 30. lipnja
- od 1. srpnja do 30. rujna i
- od 1. listopada do 31. prosinca.
(2) Na temelju obračuna iz stavka 1. Hrvatska narodna banka ispostavlja banci račun za usluge HSVP-a, i to u roku od 15 dana od isteka obračunskog razdoblja na koje se račun odnosi.
(3) Iznimno, kada banka prestaje biti sudionik obračuna preko HSVP-a, Hrvatska narodna banka može banci ispostaviti račun za usluge HSVP-a prije isteka obračunskog razdoblja.
(4) Račun za usluge HSVP-a sadrži naznaku obračunskog razdoblja na koje se odnosi, pregled učinjenih troškova po tarifnim stavkama u skladu s Cjenikom HSVP-a i ukupan iznos za plaćanje, broj računa Hrvatske narodne banke u korist kojega se vrši uplata i datum dospijeća plaćanja.
IV.
(1) Banka je dužna izvršiti plaćanje u iznosu i na način kako je naznačeno na računu za usluge HSVP-a.
(2) Ako banka ne izvrši plaćanje po računu za usluge HSVP-a do datuma njegova dospijeća, ona je obvezna za razdoblje zakašnjenja platiti Hrvatskoj narodnoj banci i kamate u visini zakonske zatezne kamate.
V.
Cjenikom HSVP-a određuju se usluge HSVP-a prema tarifnim stavkama s pripadajućim naknadama, i to kako slijedi:
Tarifna stavka
Cijena u kunama
Napomena
Broj
Opis
1.
Održavanje i razvoj
1.1.
Mjesečna članarina
3.000,00
2.
SWIFT poruke
2.1.
Platna poruka (MT102, MT103, MT202 i MT205) - do 1000 platnih poruka mjesečno
8,00
platna poruka izvršena na teret računa za namiru
2.2.
Platna poruka (MT102, MT103, MT202 i MT205) - više od 1000 platnih poruka mjesečno
6,00
platna poruka izvršena na teret računa za namiru
2.3.
Izvješće o stanju i promjenama na računu za namiru (MT950)
10,00
2.4.
Upit (MT920, MT298 - SMT800, SMT801, SMT804, SMT200 i SMT202)
4,00
2.5.
Direktni transfer (MT900, MT910)
---
cijena je sastavni dio usluge na temelju koje se izvršava direktni transfer
3.
Plaćanja vezana uz funkcioniranje NKS-a
3.1.
Određivanje limita za 1. obračunski ciklus u NKS-u na temelju izvršenog plaćanja preko HSVP-a
10,00
3.2.
Određivanje limita za 2. i 3. obračunski ciklus u NKS-u na temelju izvršenog plaćanja preko HSVP-a
20,00
3.3.
Povrat izdvojenih sredstava za pokriće obračuna u NKS-u preko HSVP-a
10,00
cijena uključuje i izvršenje direktnog transfera u HSVP-u
3.4.
Namira neto pozicije na obračunskom računu banke u NKS-u preko HSVP-a
10,00
cijena uključuje i izvršenje direktnog transfera u HSVP-u
4.
Direktni transfer na zahtjev banke
4.1.
Zaprimanje, provjera i usklađivanje podataka s naloga za zadavanje direktnog transfera i izvršenje direktnog transfera u HSVP-u za banku koja je član SWIFT-a
50,00
4.2.
Zaprimanje, provjera i usklađivanje podataka s naloga za zadavanje direktnog transfera i izvršenje direktnog transfera u HSVP-u za banku koja nije član SWIFT-a
10,00
5.
Račun obvezne pričuve
5.1.
Platna transakcija na teret računa obvezne pričuve izvršena preko HSVP-a
10,00
5.2.
Izvješće o stanju i promjenama na računu obvezne pričuve
10,00
6.
Usluge na zahtjev banke
6.1.
Potvrda o vođenju računa banke u HNB-u
20,00
6.2.
Potvrda o evidentiranim nenamirenim obvezama na računu za namiru banke
20,00
6.3.
Potvrda o stanju na računu za namiru banke na dan
20,00
6.4.
Potvrda o prosječnom stanju na računu za namiru banke u određenom razdoblju
30,00
6.5.
Potvrda o izdvojenim sredstvima banke kod HNB-a po nalogu suda
20,00
6.6.
Potvrda o sredstvima banke na svim računima u HNB-u na dan
80,00
6.7.
Ovjerena preslika izvješća o stanju i promjenama na računu banke
20,00
7.
Osnove za plaćanje
7.1.
Zaprimanje, provjera podobnosti i izvršenje osnove za plaćanje
80,00
cijena uključuje i izvršenje direktnog transfera u HSVP-u
7.2.
Uvođenje osnove za plaćanje u evidenciju izdvojenih/zaplijenjenih sredstava po nalogu suda
50,00
naplaćuje se pri konačnom izvršenju osnove za plaćanje
