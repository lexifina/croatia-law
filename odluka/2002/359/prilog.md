Prilog 1
OPERATVNI POSTUPCI HSVP-a
Operativnim postupcima HSVP-a uređuju se:
- platne poruke u HSVP-u
- tehnička valjanost platnih poruka u HSVP-u
- način upisivanja pojedinih elemenata s naloga za plaćanje u platnu poruku
- ostale poruke u HSVP-u
- način zadavanja plaćanja između Hrvatske narodne banke i ostalih sudionika HSVP-a
- način zadavanja direktnih transfera
- sudjelovanje u obračunu preko HSVP-a banaka koje nisu osposobljene za razmjenu poruka SWIFT telekomunikacijskom mrežom.
1. PLATNE PORUKE U HSVP-u
Platne poruke su odgovarajuće vrste SWIFT poruka kojima sudionik zadaje plaćanja na teret svog računa za namiru u HSVP-u.
1.1. Vrste platnih poruka
Platne su poruke u HSVP-u sljedeće vrste SWIFT poruka:
- MT103 (MT100)
- MT102
- MT202
- MT205
Opis i način upotrebe platnih poruka odgovaraju propisanim SWIFT standardima.
1.2. Tehnička valjanost platne poruke
Uvjet je za namirenje platne poruke na računu za namiru sudionika njezina tehnička valjanost. Tehnički valjana platna poruka mora:
- u zaglavlju, u polju 103 (FIN Copy Service Code), kao oznaku servisnoga identifikacijskoga koda, imati upisanu oznaku »HRK«;
- u tekstualnom dijelu, u polju 32A, kao oznaku valute, imati upisanu oznaku »HRK«;
- u tekstualnom dijelu, u polju 32A, kao oznaku datuma valute, imati upisan datum koji odgovara datumu tekućega obračunskog dana;
- zadovoljavati sve ostale propisane SWIFT standarde.
Platna poruka koja ne zadovoljava navedene uvjete, neće biti namirena.
1.3. Platne poruke s budućim datumom valute
Sudionik može zadavati platne poruke sedam dana unaprijed u odnosu na upisani datum valute u polju 32A tekstualnog dijela poruke. Platne poruke s budućim datumom valute bit će namirene na računu za namiru sudionika na obračunski dan koji odgovara upisanom datumu valute.
1.4. Prioritet izvršenja platne poruke
Oznaka prioriteta izvršenja platne transakcije upisuje se, u zaglavlju platne poruke, u polje 113.
2. NAČIN UPISIVANJA POJEDINIH ELEMENATA S NALOGA ZA PLAĆANJE U PLATNE PORUKE
Platne poruke moraju biti popunjene na način koji odgovara svim propisanim SWIFT standardima.
2.1. Broj računa platitelja
Broj računa platitelja, u banci platitelju, upisuje se u platnu poruku MT103 (MT100) i MT102, u tekstualnom dijelu, u prvi red polja 50K (u platnim porukama MT100 i MT102 polje 50).
Upisuje se brojčana oznaka računa u skladu s Odlukom o konstrukciji računa u banci (VBDI-partija računa u banci). Između VBDI-a i partije računa upisuje se crtica (»-«), bez razmaka.
2.2. Naziv računa platitelja
Naziv računa platitelja, u banci platitelju, upisuje se u platnu poruku MT103 (MT100) i MT102, u tekstualnom dijelu, u drugi red polja 50K (u platnim porukama MT100 i MT102 polje 50).
2.3. Broj računa primatelja
Broj računa primatelja, u banci primatelju, upisuje se u platnu poruku MT103 (MT100) i MT102, u tekstualnom dijelu, u prvi red polja 59.
Upisuje se brojčana oznaka računa u skladu s Odlukom o konstrukciji računa u banci (VBDI-partija računa u banci). Između VBDI-a i partije računa upisuje se crtica (»-«), bez razmaka.
2.4. Naziv računa primatelja
Naziv računa primatelja, u banci primatelju, upisuje se u platnu poruku MT103 (MT100) i MT102, u tekstualnom dijelu, u drugi red polja 59.
2.5. Vrsta posla, poziv na broj odobrenja/poziv na broj zaduženja
U sve platne poruke poziv na broj odobrenja/poziv na broj zaduženja upisuju se, u tekstualnom dijelu poruke, u polje 72, i to:
- u prvi se red upisuje brojčana oznaka vrste posla. Upisuje se oznaka »/VPO/« i brojčana oznaka vrste posla. Brojčanu oznaku vrste posla i način upisa dogovaraju banke međusobno;
- u drugi se red upisuje poziv na broj zaduženja. Upisuje se oznaka »/ZAD/« i brojčana oznaka poziva na broj zaduženja. Između modela poziva na broj (M) i pojedinih elemenata poziva na broj (P1, P2, P3, P4) upisuje se crtica (»-«) bez razmaka (M-P1-P2-P3-P4);
- u treći se red upisuje poziv na broj odobrenja. Upisuje se oznaka »/ODO/« i brojčana oznaka poziva na broj odobrenja. Između modela poziva na broj (M) i pojedinih elemenata poziva na broj (P1, P2, P3, P4) upisuje se crtica (»-«) bez razmaka (M-P1-P2-P3-P4).
Oznake »/VPO/«, »/ZAD/« i »/ODO/« upisuju se bez obzira na to postoji li podatak o vrsti posla, pozivu na broj zaduženja ili pozivu na broj odobrenja.
2.6. Opis plaćanja
a) Platne poruke MT103 (MT100) i MT102
U platne poruke MT103 (MT100) i MT102 opis plaćanja upisuje se, u tekstualnom dijelu poruke, u polje 70.
b) Platne poruke MT202 i MT205
U platne poruke MT202 i MT205 opis plaćanja upisuje se, u tekstualnom dijelu poruke, u četvrti i peti red polja 72 (prvi, drugi i treći red popunjavaju se kako je navedeno u točki 2.3.).
3. OSTALE PORUKE U HSVP-u
Ostale su poruke SWIFT poruke (u daljnjem tekstu: servisne poruke) kojima sudionici dobivaju obavijesti o platnim transakcijama zadanim preko HSVP-a, o stanju i promjenama na računu za namiru sudionika, i druge obavijesti vezane uz sudjelovanje u obračunu preko HSVP-a.
3.1. Važnije servisne poruke
Potvrdu o izvršenom namirenju platne transakcije na njegovu računu za namiru sudionik dobiva putem poruke MT012.
Obavijest o odbijenim platnim transakcijama sudionik dobiva putem poruke MT019.
Izvješće o promjenama i stanju na računu za namiru na kraju dana sudionik dobiva putem poruke MT950.
Obavijest o izvršenom direktnom transferu na teret računa za namiru sudionik dobiva putem poruke MT900.
Obavijest o izvršenom direktnom transferu u korist računa za namiru sudionik dobiva putem poruke MT910.
3.2. Ostale servisne poruke
Pregled ostalih servisnih poruka, njihov opis i način upotrebe dani su u Funkcionalnim specifikacijama HSVP-a, koje svakom sudioniku dostavlja Hrvatska narodna banka prilikom samostalnog uključenja u obračun preko HSVP-a.
4. ZADAVANJE PLATNIH TRANSAKCIJA IZMEĐU HRVATSKE NARODNE BANKE I BANAKA
Platne poruke u korist računa za namiru Hrvatske narodne banke upućuje banka na SWIFT adresu Hrvatske narodne banke za domaći platni promet NBHRHR2D.
Za zadavanje platnih transakcija između Hrvatske narodne banke i ostalih banaka u HSVP-u upotrebljavaju se odgovarajuće vrste platnih poruka. Navedene platne poruke moraju zadovoljavati sve uvjete propisane SWIFT standardima i ovim dokumentom.
4.1. Platna poruka MT202
4.1.1. Upotreba platne poruke MT202 prema vrstama posla
Hrvatska narodna banka zadaje platnu poruku MT202 u korist računa za namiru banaka kad se obavljaju sljedeće vrste poslova:
- odobrenje lombardnog kredita;
- odobrenje sredstava po repo aranžmanu;
- ispis blagajničkih zapisa HNB-a u kunama;
- prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u kunama;
- odobrenje kratkoročnog kredita za likvidnost;
- kupnja deviza;
- kupnja deviza po ugovoru o obvezi reotkupa;
- prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u stranoj valuti;
- povrat obvezne pričuve po obračunu.
Banka zadaje platnu poruku u korist računa za namiru Hrvatske narodne banke kad se obavljaju sljedeće vrste poslova:
- povrat lombardnog kredita;
- povrat sredstava po repo aranžmanu;
- upis blagajničkih zapisa HNB-a u kunama;
- povrat kratkoročnog kredita za likvidnost;
- prodaja deviza;
- prodaja efektivnog stranog novca;
- prodaja deviza po ugovoru o obvezi reotkupa;
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
DDDDDDD vodeći broj banke - VBDI
a) Brojčane oznake vrste posla
Prema pojedinim vrstama poslova na mjestu označenom s AA u strukturi polja 21, upisuju se sljedeće oznake:
Vrsta posla
Oznaka
lombardni kredit (odobrenje i povrat)
01
sredstva po repu aranžmanu (odobrenje i povrat)
02
ispis / upis blagajničkih zapisa HNB-a u kunama
04
prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u kunama
05
kratkoročni kredit za likvidnost (odobrenje i povrat)
06
kupnja/prodaja deviza
31
prodaja efektivnog stranog novca
32
kupnja/prodaja deviza po ugovoru o obvezi reotkupa
33
prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u stranoj valuti
35
povrat / izdvajanje sredstava za pokriće obračuna iz NKS-a
51
povrat / izdvajanje obvezne pričuve po obračunu
71
b) Brojčane oznake karaktera platne transakcije
Prema karakteru platne transakcije na mjestu označenom s BB u strukturi polja 21 upisuju se sljedeće oznake:
Karakter platne transakcije
Oznaka
transakcije emitiranja sredstava od strane Hrvatske narodne banke
01
transakcije prijenosa sredstava na račun Hrvatske narodne banke
02
c) Brojčane oznake specifične karakteristike pojedinog posla
Prema specifičnim karakteristikama pojedinih vrsta poslova, kod određenih vrsta poslova, na mjestu označenom s CCCC u strukturi polja 21 upisuju se sljedeće oznake:
Vrsta posla
Specifične karakteristike
Oznaka
ispis / upis blagajničkih zapisa u kunama
blagajnički zapisi s rokom dospijeća od 35 dana
0035
blagajnički zapisi s rokom dospijeća od 70 dan
0070
blagajnički zapisi s rokom dospijeća od 105 dana
0105
Kod ostalih vrsta poslova, kod kojih nisu propisane specifične karakteristike, na mjestu označenom s CCCC u strukturi polja 21 upisuju se nule.
d) Vodeći broj banke - VBDI
Na mjestu označenom s DDDDDDD u strukturi polja 21 upisuje se pripadajući VBDI banke zadavatelja platne transakcije.
Kada platnu transakciju zadaje Hrvatska narodna banka, upisuje se VBDI banke primatelja platne transakcije.
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
sredstva po repu aranžmanu (odobrenje i povrat)
odobrenje
02010000DDDDDDD
povrat
02020000DDDDDDD
ispis / upis blagajničkih zapisa HNB-a u kunama
ispis
35 dana
04010035DDDDDDD
70 dan
04010070DDDDDDD
105 dana
04010105DDDDDDD
upis
35 dana
04020035DDDDDDD
70 dan
04020070DDDDDDD
105 dana
04020105DDDDDDD
prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u kunama
iskup
05010000DDDDDDD
kratkoročni kredit za likvidnost
(odobrenje i povrat)
odobrenje
06010000DDDDDDD
povrat
06020000DDDDDDD
kupnja / prodaja deviza
kupnja
31010000DDDDDDD
prodaja
31020000DDDDDDD
prodaja efektivnog stranog novca
prodaja
32020000DDDDDDD
kupnja / prodaja deviza po ugovoru o obvezi reotkupa
kupnja
33010000DDDDDDD
prodaja
33020000DDDDDDD
prijevremeni iskup blagajničkih zapisa HNB-a nominiranih u stranoj valuti
iskup
35010000DDDDDDD
izdvajanje sredstava za pokriće obračuna iz NKS-a
izdvajanje
sredstava za pokriće obračuna iz NKS-a
51020000DDDDDDD
povrat / izdvajanje obvezne pričuve po obračunu
povrat
71010000DDDDDDD
izdvajanje
71020000DDDDDDD
4.1.2.2. Polje 72 - tekstualni opis vrste plaćanja
Radi označivanja vrste plaćanja platna poruka MT 202, kojom banka zadaje platnu transakciju u korist računa za namiru Hrvatske narodne banke, mora uz popunjeno polje 21 (točka 4.1.2. pod a)) na propisani način imati popunjeno i polje 72 u tekstualnom dijelu poruke.
Polje 72 sadrži tekstualni opis plaćanja u korist Hrvatske narodne banke u skladu sa stupcima 1 i 2 iz tablice s primjerima popunjavanja polja 21 prema vrstama posla.
5. ZADAVANJE DIREKTNOG TRANSFERA
Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru sudionika:
- na temelju naloga banke
- na temelju zakonskih propisa.
5.1. Direktni transfer na temelju naloga banke
Hrvatska narodna banka zadaje direktni transfer na temelju naloga primljenog od sudionika. Nalog za zadavanje direktnog transfera sudionik podnosi na obrascu Nalog HSVP/DT. Obrazac Nalog HSVP/DT kreira Hrvatska narodna banka, i primjerak obrasca dostavlja svim bankama.
Popunjeni Nalog HSVP/DT (u daljnjem tekstu: Nalog) banka dostavlja telefaksom Hrvatskoj narodnoj banci. Hrvatska narodna banka dostavlja svim bankama broj telefaksa za dostavu Naloga.
Nakon što je primila popunjeni Nalog, Hrvatska narodna banka telefonski usklađuje vjerodostojnost podataka iz Naloga s bankom pošiljateljem Naloga.
Kako bi omogućila usklađivanje vjerodostojnosti podataka iz Naloga, Hrvatska narodna banka dostavlja svim bankama šifru za usklađivanje.
Usklađivanje vjerodostojnosti podataka iz Naloga provodi se, nakon što ga Hrvatska narodna banka primi telefaksom, na sljedeći način:
- Hrvatska narodna banka telefonski zove banku pošiljatelja Naloga;
- banka pošiljatelj Naloga priopćuje šifru za usklađivanje;
- banka pošiljatelj Naloga čita podatke s Naloga koji je dostavljen Hrvatskoj narodnoj banci, a Hrvatska narodna banka ih uparuje s podacima na primljenom Nalogu.
Nakon što je usklađivanje provedeno, Hrvatska narodna banka zadaje direktni transfer u skladu s podacima na Nalogu.
Banka dostavlja Hrvatskoj narodnoj banci broj telefona i imena osoba za kontakt koje će provoditi usklađivanje.
5.2. Direktni transfer na temelju propisa
a) Namirenje neto pozicije iz NKS-a
Namirenje neto pozicije iz NKS-a obavlja Hrvatska narodna banka na temelju podataka dobivenih od NKS-a o konačnim neto pozicijama na obračunskim računima banaka i Hrvatske narodne banke u NKS-u na kraju obračunskog dana.
Namirenje neto pozicije iz NKS-a obavlja se na sljedeći način:
- ako je neto pozicija iz NKS-a pozitivna, Hrvatska narodna banka zadaje direktni transfer u korist računa za namiru sudionika;
- ako je neto pozicija iz NKS-a negativna, Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru sudionika.
b) Povrat sredstava banke prethodno izdvojenih za osiguranje pokrića u obračunu preko NKS-a
Hrvatska narodna banka zadaje direktni transfer u korist računa za namiru banke radi povrata sredstava koje je banka izdvojila tijekom dana na poseban račun za osiguranje pokrića obračuna iz NKS-a u Hrvatskoj narodnoj banci.
c) Izvršenje osnova za naplatu
Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru banke po osnovi izvršenja zaprimljenih osnova za naplatu izdanih na teret računa banke u Hrvatskoj narodnoj banci.
6. NAČIN SUDJELOVANJA U OBRAČUNU PREKO HSVP-A BANAKA KOJE NISU TEHNIČKI OSPOSOBLJENE ZA RAZMJENU PORUKA SWIFT TELEKOMUNIKACIJSKOM MREŽOM
Sve operativne poslove vezane uz sudjelovanje u obračunu preko HSVP-a za banke koje nisu osposobljene za razmjenu poruka SWIFT telekomunikacijskom mrežom (u daljnjem tekstu: posredni sudionici) obavlja Hrvatska narodna banka.
Sve platne transakcije na teret računa za namiru posrednih sudionika zadaje Hrvatska narodna banka direktnim transferima.
Hrvatska narodna banka zadaje direktni transfer na teret računa za namiru posrednog sudionika u uvjetima i na način propisan u točki 5. ovoga dokumenta.
Nalog HSVP/DT kojim posredni sudionik podnosi Hrvatskoj narodnoj banci nalog za zadavanje direktnog transfera na teret svog računa za namiru, mora sadržavati sve podatke propisane u točki 4.1.2. ovoga dokumenta.
Obavijest o stanju na računu za namiru posrednog sudionika tijekom dana Hrvatska narodna banka daje telefonski na upit posrednog sudionika, telefaksom, ili na drugi način dogovoren između posrednog sudionika i Hrvatske narodne banke.
Izvješće o stanju i izvršenim platnim transakcijama na računu za namiru posrednog sudionika na kraju dana daje Hrvatska narodna banka. Izvješće se dostavlja posrednom sudioniku preporučenom pošiljkom, prvog radnog dana u tjednu, za protekli tjedan.
