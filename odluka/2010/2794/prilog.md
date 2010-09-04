PROVEDBENA PRAVILA ZA METAPODATKE
DIO A.
Tumačenje
1. Primjenjuju se sljedeće definicije:
- »niz znakova« označava polje vrijednosti elemenata metapodataka izraženih kao skup znakova koji se tretiraju kao cjelina,
- »slobodan tekst« označava polje vrijednosti elemenata metapodataka izraženo na jednom ili više živih jezika,
- »podrijetlo« označava povijest skupa podataka i životni ciklus od prikupljanja i dobivanja do sastavljanja zbirke i izdvajanja u njegov trenutni oblik, sukladno EN ISO 19101,
- »element metapodatka« označava zasebnu jedinicu metapodataka sukladno EN ISO 19115,
- »prostor imena« označava zbirku imena, utvrđenu poveznicom na jedinstven označivač izvora (unique resource identifier - URI), koja se koriste u dokumentima formata XML (extensible markup language) kao imena elemenata i imena atributa,
- »kvaliteta« označava sveukupnost značajki nekog proizvoda koji imaju utjecaja na njegovu sposobnost zadovoljavanja izraženih ili impliciranih potreba, sukladno EN ISO 19101,
- »izvor« označava informacijski izvor (resurs) koji ima izravnu ili neizravno poveznicu s određenim mjestom ili geografskim područjem,
- »nizovi skupova prostornih podataka« označava zbirku skupova prostornih podataka koji dijele iste specifikacije proizvoda.
2. Smatrat će se da se poveznice na valjanosti skupova prostornih podataka mogu odnositi na bilo koji od sljedećih navoda:
- raspon prostora i vremena koji je važan za podatak,
- jesu li podaci provjereni prema mjernom standardu ili normi radnog učinka,
- mjeru u kojoj podaci odgovaraju namijeni,
- gdje je to prikladno, pravovaljanost skupa prostornih podataka.
DIO B.
Elementi metapodataka
1. IDENTIFIKACIJA
Osiguravaju se sljedeći elementi metapodataka.
1.1. Naziv izvora
Ovo je karakteristično, a često i jedinstveno ime po kojem je izvor poznat.
Polje vrijednosti ovog elementa metapodataka je slobodni tekst.
1.2. Sažetak izvora
Ovo je kratki narativni sažetak sadržaja izvora.
Polje vrijednosti ovog elementa metapodataka je slobodni tekst.
1.3 Vrsta izvora
Ovo je vrsta izvora koju opisuju metapodaci.
Polje vrijednosti ovog elementa metapodataka definirano je u Dijelu D.1.
1.4. Adresa izvora podataka
Adresa izvora podataka definira veze prema izvoru i/ili link na dodatne informacije o izvoru.
Polje vrijednosti ovog elementa metapodataka je niz znakova koji se obično izražava kao jedinstvena adresa izvora (URL).
1.5. Jedinstveni označivač izvora
Vrijednost kojom se jedinstveno utvrđuje izvor.
Polje vrijednosti ovog elementa metapodataka je obvezan kod niza znakova, kojeg obično dodjeljuje vlasnik podataka, i prostor imena niza znakova koji jedinstveno utvrđuje kontekst identifikacijskog koda (primjerice: vlasnik podataka).
1.6. Upareni izvori
Ukoliko je izvor neka usluga prostornih podataka, ovaj element metapodataka utvrđuje, tamo gdje je to važno, ciljni/ciljne skup(ove) prostornih podataka ove usluge putem njihovih jedinstvenih označivača izvora (URI).
Polje vrijednosti ovog elemenata metapodataka je obvezan kod niza znakova kojeg obično dodjeljuje vlasnik podataka, i prostor imena niza znakova koji jedinstveno utvrđuje kontekst identifikacijskog koda (primjerice, vlasnik podataka).
1.7. Jezik izvora
Jezik/jezici korišteni unutar izvora.
Polje vrijednosti ovog elemenata metapodataka je ograničeno na jezike definirane u ISO 639-2.
2. KLASIFIKACIJA PROSTORNIH PODATAKA I USLUGA
2.1. Tematska kategorija
Tematska kategorija je shema klasifikacije visoke razine koja pomaže u grupiranju i pretraživanju po temama dostupnih izvora prostornih podataka.
Polje vrijednosti ovog elemenata metapodataka je definirano u Dodatku D.2.
2.2. Vrste usluga prostornih podataka
Ovo je klasifikacija koja pomaže u pretraživanju dostupnih usluga prostornih podataka. Dotična usluga svrstava se samo u jednu kategoriju.
Polje vrijednosti ovog elemenata metapodataka definirano je u Dijelu D.3.
3. KLJUČNE RIJEČI
Ukoliko je izvor neka usluga prostornih podatka, treba se osigurati barem jedna ključna riječ iz Dijela D.4.
Za svaku od ključnih riječi osiguravaju se sljedeći elementi metapodataka:
3.1. Vrijednost ključne riječi
Vrijednost ključne riječi je riječ koja se uobičajeno koristi, formaliziran pojam ili fraza koja se koristi da bi se opisao subjekt. Budući da je tematska kategorija previše gruba za detaljno pretraživanje, ključne riječi pomažu suziti pretraživanje cjelokupnog teksta i dozvoljavaju strukturiranu pretragu po ključnim riječima.
Polje vrijednosti ovog elemenata metapodataka je slobodan tekst.
3.2. Stvaranje kontroliranog rječnika
Ukoliko je vrijednost ključne riječi stvorena iz kontroliranog rječnika (rječnik pojmovima, ontologija), primjerice opći višejezični rječnik pojmova u svezi okoliša (GEMET), mora se navesti kontrolirani rječnik iz kojeg je ista nastala.
Ovo navođenje obuhvaća barem naslov i referentni datum (datum publikacije, datum zadnje revizije ili izrade) kontroliranog rječnika iz kojeg je ista nastala.
4. GEOGRAFSKA LOKACIJA
Uvjet geografske lokacije bit će izražen elementom metapodatka geografski granični pravokutnik.
4.1. Geografski granični pravokutnik
Ovo je prostiranje izvora u zemljopisnom prostoru, koje je prikazano kao granični pravokutnik.
Granični pravokutnik izražen je krajnjom zapadnom i istočnom zemljopisnom dužinom te južnom i sjevernom zemljopisnom širinom, u decimalnim stupnjevima s preciznošću od barem dvije decimale.
5. VREMENSKA REFERENCA
Ovaj element metapodataka bavi se uvjetom o posjedovanju informacija o vremenskoj dimenziji podataka. Treba se osigurati barem jedan od elemenata metapodataka koji su navedeni u točkama 5.1. do 5.4.
Polje vrijednosti ovog elemenata metapodataka koji se spominje u točkama 5.1 do 5.4 je skup datuma. Svaki datum odnosi se na sustav vremenske reference te se izražava u obliku koji je kompatibilan s tim sustavom. Predodređeni referentni sustav bit će gregorijanski kalendar s datumima izraženim u skladu s normom ISO 8601.
5.1. Vremenski obuhvat
Vremenski obuhvat određuje vremenski period obuhvaćen sadržajem izvora. Ovaj period može se izraziti kao
- pojedinačni datum
- interval datuma izraženim početnim i završnim datumom intervala
- mješavina pojedinačnih datuma i intervala datuma
5.2. Datum objave
Ovo je datum objave izvora kada je poznat ili datum stupanja na snagu. Može postojati više od jednog datuma objave.
5.3 Datum zadnje izmjene
Ovo je datum zadnje izmjene izvora, ukoliko je izvor mijenjan. Ne smije biti više od jednog datuma revizije.
5.4 Datum stvaranja
Ovo je datum stvaranja izvora. Ne smije biti više od jednog datuma stvaranja.
6. KAKVOĆA I VALJANOST
Zahtjevi spomenuti u Zakonu o državnoj izmjeri i katastru nekretnina (»Narodne novine« 16/07), čl. 87. st. 2. i čl. 89. st. 2. u svezi kvalitete i valjanosti prostornih podataka bit će obrađeni sljedećim elementima metapodataka:
6.1 Podrijetlo
Ovo je izjava o povijesti postupka i/ili općenito kvaliteti skupa prostornih podataka. Gdje je to prikladno, ona može sadržavati izjavu o tome je li valjanost skupa podataka potvrđena ili mu je kvaliteta osigurana, je li ovo službena verzija (ukoliko postoji više verzija) te je li pravovaljan.
Polje vrijednosti ovog elementa metapodatka je slobodan tekst.
6.2 Prostorna rezolucija
Prostorna rezolucija odnosi se na razinu detalja skupa podataka. Izražava se kao skup od nula do više rezolucijskih udaljenosti (obično za rasterske podatke i proizvode izvedene temeljem slika) ili odgovarajućih mjerila (obično za karte i proizvode izvedene iz karata).
Odgovarajuće mjerilo obično se izražava kao cjelobrojna vrijednost koja izražava nazivnik mjerila.
Rezolucijska udaljenost izražava se kao brojčana vrijednost kojoj je pridružena jedinica duljine.
7. SUKLADNOST
Zahtjevi spomenuti u čl. 87. st. 2. točka 2. i čl. 89. st. 2., točka 4. ZDIKN u svezi sukladnosti i stupnja sukladnosti s provedbenim pravilima usvojenima temeljem članka 87. st. 2., točka 2. ZDIKN bit će obrađeni sljedećim elementima metapodataka:
7.1 Specifikacija
Ovo je navođenje provedbenih pravila usvojenih temeljem čl. 88. i čl. 90. st. 2 ZDIKN ili druge specifikacije kojoj je određen izvor sukladan.
Izvor može biti sukladan više nego jednom provedbenom pravilu usvojenom temeljem čl. 88. i čl. 90. st. 2. ZDIKN ili drugoj specifikaciji.
Ovo će navođenje uključivati barem naziv i referentni datum (datum objave, datum zadnje izmjene ili datum stvaranja) provedbenih pravila usvojenih temeljem čl. 88. i čl. 90. st. 2. ZDIKN ili specifikacije.
7.2. Stupanj
Ovo je stupanj sukladnosti izvora s provedbenim pravilima usvojenima temeljem čl. 88. i čl. 90., st. 2. ZDIKN ili drugom specifikacijom.
Polje vrijednosti ovog elementa metapodatke definirano je u Dijelu D.
8. OGRANIČENJE KOJE SE ODNOSI NA PRISTUP I KORIŠTENJE
Ograničenje koje se odnosi na pristup i korištenje mora biti jedna ili obje od niže navedenih stavki:
- skup uvjeta koji se primjenjuju na pristup i korištenje (8.1)
- skup ograničenja javnog pristupa (8.2).
8.1 Uvjeti koji se odnose na pristup i korištenje
Ovaj element metapodataka definira uvjete za pristupanje i korištenje skupova i usluga prostornih podataka te, tamo gdje je to primjenljivo, odgovarajuće naknade kao što je to određeno, čl. 87., st. 2. t. 3., čl. 89., st. 2. t. 6., čl. 90., st. 3. ZDIKN.
Polje vrijednosti ovog elementa metapodataka je slobodni tekst.
Element mora imati vrijednosti. Ukoliko nema uvjeta koji se primjenjuju na pristup i korištenje izvora, koristi se »ne podliježe uvjetima«. Ukoliko su uvjeti nepoznati, koristi se »uvjeti nepoznati«.
Ovaj element pruža i informacije o svim naknadama koje su potrebne za pristupanje i korištenje izvora, ukoliko je to primjenljivo, ili se odnosi na jedinstvenu adresu izvora podataka (URL) gdje su informacije o naknadama dostupne.
8.2 Ograničenja javnog pristupa
Kada je ograničen javni pristup skupovima prostornih podataka i uslugama prostornih podataka temeljem čl. 90., st. 5. ZDIKN,, ovaj element metapodataka pruža informacije o ograničenjima i razlozima istih.
Ukoliko ne postoje ograničenja javnog pristupa, ovaj element metapodataka naznačava tu činjenicu.
Polje vrijednosti ovog elementa metapodataka je slobodni tekst.
9. ORGANIZACIJE ODGOVORNE ZA USPOSTAVU, UPRAVLJANJE, ODRŽAVANJE I DISTRIBUCIJU SKUPOVA I USLUGA PROSTORNIH PDOATAKA
U svrhu čl. 87. st. 2., točka 5. i čl. 89., st. 2., točka. 7. ZDIKN, trebaju se osigurati sljedeća dva elementa metapodataka:
9.1 Odgovorna strana
Ovo je opis organizacije odgovorne za uspostavu, upravljanje, održavanje i distribuciju izvora.
Ovaj opis obuhvaća:
- ime organizacije kao slobodan tekst,
- kontaktnu e-mail adresu kao niz znakova.
9.2 Uloga odgovorne strane
Ovo je uloga odgovorne organizacije.
Polje vrijednosti ovog elementa metapodataka definirano je u Dijelu D.
10. METAPODACI O METAPODACIMA
U svrhu članka 87. st. 4. ZDIKN, trebaju se osigurati sljedeći elementi metapodataka:
10.1 Kontaktna točka metapodataka
Ovo je opis organizacije odgovorne za stvaranje i održavanje metapodataka.
Ovaj opis obuhvaća:
- ime organizacije kao slobodan tekst,
- kontaktnu e-mail adresu kao niz znakova.
10.2 Datum metapodataka
Datum koji pobliže određuje kada je zapis o metapodacima stvoren ili ažuriran.
Ovaj datum izražava se sukladno normi ISO 8601.
10.3 Jezik metapodataka
Ovo je jezik u kojem su izraženi elementi metapodatka.
Polje vrijednosti ovog elementa metapodataka ograničen je na hrvatski jezik izražen sukladno normi ISO 639-2.
DIO C
Upute o mnogostrukosti i uvjetima elemenata metapodataka
Metapodaci koji opisuju izvor sastoje se, vezano za skup prostornih podataka ili niz skupova prostornih podataka, od elemenata metapodataka ili skupina elemenata metapodataka navedenih u tablici 1. te, vezano uz uslugu skupa prostornih podataka, elemenata metapodataka ili skupina elemenata metapodataka navedenih u tablici 2.
Ovi elementi metapodataka ili skupine elemenata metapodataka sukladni su očekivanoj mnogostrukosti i povezanim uvjetima izloženima u tablicama 1. i 2.
Ukoliko nije izražen niti jedan uvjet vezan uz određeni element metapodataka, taj je element obvezan.
Tablice daju sljedeće informacije:
- prvi stupac sadrži poveznice na odjeljak u Dijelu B Dodatka koji definira element metapodataka ili skupine elemenata metapodataka,
- drugi stupac sadrži ime elementa metapodatka ili skupine elemenata metapodataka,
- treći stupac pobliže utvrđuje mnogostrukost elementa metapodataka. Izražavanje mnogostrukosti slijedi notaciju Unified Modelling Languagea (UML) za mnogostrukost u kojoj:
- 1 označava da postoji samo jedan slučaj ovog elementa metapodataka unutar nekog skupu rezultata;
- 1..* označava da postoji barem jedan slučaj ovog elementa metapodataka unutar nekog skupu rezultata;
- 0..1 označava da je postojanje elementa metapodataka unutar nekog skupu rezultata uvjetno, ali da se može pojaviti samo jednom;
- 0..* označava da je postojanje elementa metapodataka unutar nekog skupu rezultata uvjetno, ali da se taj element metapodataka može pojaviti i više od jednom;
Kada je mnogostrukost 0..1 ili 0..*, uvjet definira kad su elementi metapodataka uvjetovani
Četvrti stupac sadrži uvjetnu izjavu u slučaju da se mnogostrukost elementa ne odnosi na sve vrste izvora. Svi su elementi obvezni u ostalim okolnostima.
Tablica 1.
METAPODACI ZA SKUPOVE PROSTORNIH PODATAKA ILI NIZ SKUPOVA PROSTORNIH PODATAKA
Poveznica
Elementi metapodataka
Mnogostrukost
Uvjet
1.1
Naziv izvora
1
1.2
Sažetak o izvoru
1
1.3
Vrsta izvora
1
1.4
Adresa izvora podataka
0..*
Obvezan ukoliko je URL dostupan kako bi se dobilo više informacija o izvoru, i/ili pristupilo povezanim uslugama.
1.5
Jedinstveni označivač izvora
1..*
1.7
Jezik izvora
0..*
Obvezan ukoliko izvor obuhvaća tekstualne informacije.
2.1
Tematska kategorija
1..*
3
Ključna riječ
1..*
4.1
Geografski granični pravokutnik
1..*
5
Vremenska referenca
1..*
6.1
Podrijetlo
1
6.2
Prostorna rezolucija
0..*
Obvezno za skupove podataka i serije skupova podataka ukoliko odgovarajuće mjerilo ili rezolucijska udaljenost mogu biti pobliže određeni.
7
Sukladnost
1..*
8.1
Uvjeti za pristup i korištenje
1..*
8.2
Ograničenja javnog pristupa
1..*
9
Odgovorna organizacija
1..*
10.1
Kontaktna točka za metapodatke
1..*
10.2
Datum metapodataka
1
10.3
Jezik metapodataka
1
Tablica 2.
METAPODACI ZA USLUGE PROSTORNIH PODATAKA
Poveznica
Elementi metapodataka
Mnogostrukost
Uvjet
1.1
Naziv izvora
1
1.2
Sažetak o izvoru
1
1.3
Vrsta izvora
1
1.4
Adresa izvora podataka
0..*
Obvezna ukoliko je dostupno povezivanje na uslugu.
1.6
Upareni izvor
0..*
Obvezan ukoliko je dostupno povezivanje na skupove podataka temeljem kojih usluga funkcionira
2.2
Vrsta usluga prostornih podataka
1
.
3
Ključna riječ
1..*
4.1
Geografski granični pravokutnik
0…*
Obvezan za usluge s izričitim geografskim prostiranjem.
5
Vremenska poveznica
1..*
6.2
Prostorna rezolucija
0..*
Obvezno kada postoji ograničenje prostorne rezolucije za ovu uslugu.
7
Sukladnost
1..*
8.1
Uvjeti za pristup i korištenje
1..*
8.2
Ograničenje javnog pristupa
1..*
9
Odgovorna organizacija
1..*
10.1
Kontaktna točka za metapodatke
1..*
10.2
Datum metapodataka
1
10.3
Jezik metapodataka
1
DIO D
POLJA VRIJEDNOSTI
Ukoliko je ovo pobliže naznačeno u opisu elemenata metapodataka u Dijelu B, polja vrijednosti opisana u Dijelovima D.1. to D.6 koriste se u kombinaciji s mnogostrukošću izraženom u tablicama 1. i 2. u Dijelu C.
Vezano za određeno polje, svaka je vrijednost definirana:
- brojčanim označiteljem,
- tekstualnim imenom za ljude na hrvatskom jeziku,
- ime koje je jezično neutralno za računala (vrijednost izražena u zagradi),
- fakultativan opis ili definicija.
1. VRSTA IZVORA
1.1. serija skupova prostornih podataka (serija)
1.2. skup prostornih podataka (skup podataka)
1.3. usluge prostornih podataka (usluge)
2. TEMATSKE KATEGORIJE SUKLADNO NORMI EN ISO 19115
2.1. Uzgoj (farming)
Uzgoj životinja i/ili kultiviranje bilja.
Ova se kategorija primjenjuje na temu prostornih podataka:
- Poljoprivredna i vodoprivredna postrojenja koja se definiraju kao oprema za poljodjelstvo i proizvodni objekti i strojevi (uključujući sustave navodnjavanja, staklenike i štale),
u skladu s kategorijom iz čl. 86. st. 3. t. 8. ZDIKN.
2.2. Živi svijet (biota)
Flora i/ili fauna u prirodnom okruženju.
Ova se kategorija odnosi na sljedeće teme prostornih podataka:
- Bio-zemljopisna područja, koja se definiraju kao područja s relativno homogenim ekološkim uvjetima koja imaju zajedničke osobine,
- Staništa i biotopi koji se definiraju kao geografska područja za koja su svojstveni posebni ekološki uvjeti, procesi, strukture i funkcije (za održavanje života) koje fizički pomažu organizmima da žive na njima. Uključujući kopnena i vodena područja koja se razlikuju po geografskim, abiotičkim i biotičkim značajkama, bilo da su u potpunosti prirodna ili polu-prirodna, te
- Raspodjela vrsta koja se definira kao geografska raširenost životinjskih i biljnih vrsta, razvrstana po mreži, regiji, upravnoj jedinici ili drugoj analitičkoj jedinici,
u skladu s kategorijom iz čl. 86. st. 3. t. 8. ZDIKN.
2.3. Granice (boundaries)
Pravni opisi zemljišta.
Ova se kategorija primjenjuje na teme prostornih podataka:
- Upravne jedinice koje se definiraju kao upravne jedinice za lokalnu, regionalnu ili državnu upravu, koje razdjeljuju područja na kojima države članice imaju i/ili primjenjuju jurisdikcijska prava i koje su razdvojene upravnim granicama.
- Statističke jedinice koje se definiraju kao jedinice za širenje i korištenje statističkih informacija,
u skladu s s kategorijoma iz čl. 86. st. 2 i st. 3. t. 7. ZDIKN.
2.4. Klimatologija /Meteorologija/Atmosfera (climatologyMeteorologyAtmosphere)
Atmosferski procesi i fenomeni.
Ova se kategorija primjenjuje na teme prostornih podataka:
- Atmosferski uvjeti koji se definiraju kao fizikalni uvjeti u atmosferi. Uključujući prostorne podatke koji se temelje na mjerenjima, uzorcima ili na njihovom spoju i uključuju lokacije za mjerenje.
- Meteorološke geografske značajke koje se definiraju kao vremenski uvjeti i njihova mjerenja; padaline, temperature, ishlapljivanje, brzina i smjer vjetra,
u skladu s kategorijom iz čl. 86. st. 3. t. 8. ZDIKN.
2.5. Ekonomija (economy)
Gospodarske aktivnosti, uvjeti i zapošljavanje.
Ova se kategorija primjenjuje na teme prostornih podataka:
- Izvori energije koji se definiraju kao izvori energije, uključujući ugljikovodike, vodenu energiju, bioenergiju, solarnu energiju, vjetar itd., uključujući dubinske/visinske informacije o veličini izvora tamo gdje je potrebno,
- Izvori minerala koji se definiraju kao Izvori minerala, uključujući kovinske rude, industrijske minerale itd., uključujući dubinske/visinske informacije o veličini izvora tamo gdje je potrebno,
u skladu s kategorijom iz čl. 86. st. 3. t. 8. ZDIKN.
2.6. Visine (elevation)
Visina iznad ili ispod razine mora.
Ova se kategorija primjenjuje na teme prostornih podataka
- Visine koja se definira kao digitalni modeli visina za površinu kopna, leda i oceana. Uključuju nadmorske visine, dubine mora i obalne linije,
u skladu s kategorijom iz čl. 86. St. 2 ZDIKN.
2.7. Okoliš (environment)
Izvori, zaštita i očuvanje okoliša.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Zaštićena područja koja se definiraju kao područje koje je određeno ili kojime se upravlja u okviru međunarodnog prava, prava Europske zajednice i Hrvatske, kako bi se postigli posebni ciljevi očuvanja,
u skladu s kategorijom iz čl. 86. St.3.t. 5 ZDIKN.
2.8. Geo-znanstvene informacije (geoscientificInformation)
Informacije koje se odnose na znanosti o Zemlji (geo-znanosti).
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Tlo koje se definira kao tla i slojevi zemlje ispod površine, opisani prema debljini, teksturi, strukturi i sadržaju čestica i organske tvari, kamenitosti, eroziji, tamo gdje je primjereno prema postotku nagiba i prema predviđenom opsegu zaliha vode,
- Geologija koja se je opisana u skladu sa sastavom i strukturom. Uključuje stjenovito tlo, podzemne vode i geomorfologiju,
- Zone prirodnih rizika koje se definiraju kao osjetljiva područja koja su obilježena u skladu s prirodnim opasnostima (svim atmosferskim, hidrološkim, seizmološkim, vulkanskim pojavama i požarima, koji zbog svojeg položaja, težine i učestalosti imaju potencijal da ozbiljno utječu na društvo), npr. poplave, odroni zemlje i slijeganje tla, snježne lavine, šumski požari, potresi, vulkanske erupcije,
u skladu s kategorijom iz čl. 86. st. 3. t. 8 ZDIKN.
2.9. Zdravlje (health)
Zdravlje, zdravstvene usluge, ljudska ekologija i sigurnost.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Ljudsko zdravlje i sigurnost koja se definira kao geografska raširenost prevladavajućih patoloških pojava (alergije, tumori, bolesti dišnih putova, itd.), informacije koje pokazuju učinak na zdravlje (biomarkeri, smanjenje plodnosti, epidemije), ili dobrobit ljudi (umor, stres, itd.), koji su direktno (onečišćenje zraka, kemikalije, prorijeđenost ozonskog omotača, buka, itd.) ili indirektno povezani (hrana, genetski izmijenjeni organizmi, itd.) s kakvoćom okoliša,
u skladu s kategorijom iz čl. 86. st. 3. t. 8 ZDIKN.
2.10. Slike / Osnovne karte / Zemljin pokrov (imageryBaseMapsEarthCover)
Osnovne karte.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Ortosnimci koji se definiraju kao georeferencirani slikovni podaci Zemljine površine nastali snimanjem sa satelita ili aero snimanjem,
- Pokrov zemljišta, koji se definira kao fizički ili biološki pokrov Zemljine površine, uključujući umjetne površine, poljoprivredna područja, šume, (polu-) prirodna područja, močvare, vodena tijela,
u skladu s kategorijom iz čl. 86. st. 2. ZDIKN.
2.11. Obavještajni / Vojni podaci (intelligenceMilitary)
Vojne baze, objekti, aktivnosti.
Ova se kategorija ne primjenjuje izravno ni na koju od tema prostornih podataka definiranih u ZDIKN.
2.12. Kontinentalne vode (inlandWaters)
Značajke kontinentalnih voda, sustavi odvodnje i njihova svojstva.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Hidrografija koja se definira kao hidrografski elementi, uključujući morska područja i sva druga vodena tijela i s njima povezane jedinice, uključujući riječne bazene i pod-bazene.,
u skladu s kategorijom iz čl. 86. st. 3. t. 1. ZDIKN.
2.13. Lokacija (location)
Položajne informacije i usluge.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Zemljopisna imena koja se definiraju kao imena područja, regija, mjesta, velikih gradova, predgrađa, gradova ili naselja, ili bilo koje geografskog ili topografskog obilježja od državnog ili povijesnog značenja,
- Adrese, koje se definiraju kao položaj nekretnina koji se temelji na identifikatoru adresa, najčešće s imenom ulice, kućnim brojem i poštanskim brojem,
u skladu s kategorijom iz čl. 86. st. 2. ZDIKN.
2.14. Oceani (oceans)
Značajke i karakteristike slanih vodenih tijela (bez kontinentalnih voda).
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Morska područja koja se definiraju kao fizikalni uvjeti mora i slanih vodenih tijela koja su podijeljena u regije i podregije sa zajedničkim osobinama,
- Oceanografske zemljopisne značajke, koje se definiraju kao fizikalni uvjeti oceana (struje, slanost, visina valova, itd.),
u skladu s kategorijom iz čl. 86. st. 3. t. 1. ZDIKN.
2.15. Planiranje / Katastar (planningCadastre)
Informacije koje se koriste za primjerene aktivnosti budućeg korištenja zemlje.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Katastarske čestice koje se definiraju kao područja koja određuju katastarski registri ili njihovi ekvivalenti,
u skladu s kategorijom iz čl. 86. st. 2. ZDIKN,
- Namjena zemljišta koja se definira kao Područje opisano u skladu s njegovom sadašnjom i ubuduće planiranom funkcionalnom veličinom ili u skladu s njegovom društveno-gospodarskom namjenom (npr. stambenom, industrijskom, poslovnom, poljoprivrednom, za šumarstvo i sportsko-rekreacijskom),
u skladu s kategorijom iz čl. 86. st. 3. t. 4. ZDIKN,
- Upravljanje određenim područjima /ograničenja/zone regulacije & izvještajne jedinice, koje se definiraju kao područja kojima se upravlja, koja se uređuje ili koristi za izvještavanje na međunarodnoj, europskoj, državnoj ili regionalnoj razini. Uključuju odlagališta smeća, zaštićena područja oko izvora pitke vode, područja osjetljiva na nitrate, uređeni plovni putovi na moru ili na velikim kopnenim vodama, područja za odlaganje otpada, područja zaštićena od buke, područja s dozvolom za istraživanje ruda i rudarenje, područja riječnih bazena, odgovarajuće jedinice za izvještavanje i područja za upravljanje obalnim pojasom,
u skladu s kategorijom iz s čl. 86. st. 3. ZDIKN.
2.16. Društvo (society)
Značajke društva i kultura.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Raspodjela stanovništva-demografija koja se definira kao Geografska raširenost stanovništva, uključujući obilježja stanovništva i razine aktivnosti, razvrstana po mreži, regiji, administrativnoj jedinici ili drugoj analitičkoj jedinici,
u skladu s kategorijom iz čl. 86. st. 3, t. 7. ZDIKN.
2.17. Struktura (structure)
Ljudska tvorevina.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Zgrade koje se definiraju kao geografski položaj zgrada,
u skladu s kategorijom iz čl. 86. st. 2. ZDIKN,
- Proizvodna i industrijska postrojenja koja se definiraju kao područja industrijske proizvodnje te postrojenja za izvlačenje vode, rudnici i skladišta,
u skladu s kategorijom iz čl. 86. st. 2. ZDIKN,
- Postrojenja za praćenje okoliša koja se definiraju kao lokacija i djelovanje sustava za nadzor okoliša koji uključuju promatranje i mjerenje emisija, stanje okoliša, kao i drugih parametara ekosustava (biološka raznolikost, ekološko stanje vegetacije, itd.) putem ili u ime državnih tijela,
u skladu s kategorijom iz čl. 86. st. 3. t. 5. ZDIKN
2.18. Promet (transportation)
Sredstva i pomagala za prijevoz osoba i/ili roba.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Prometne mreže koje se definiraju kao mreže cestovnog, željezničkog i vodenog prijevoza i pripadajuća infrastruktura. Uključuje veze između različitih mreža,
u skladu s kategorijom iz čl. 86. st. 3. t. 2. ZDIKN.
2.19. Vodovi / Komunikacije (utilitiesCommunication)
Infrastruktura i usluge sustava energije, vodoopskrbe i odvodnje, zbrinjavanja otpada i komunikacija.
Ova se kategorija primjenjuje na sljedeće teme prostornih podataka:
- Vodovi i usluge javne uprave koja uključuje komunalne sustave kao što su kanalizacija, zbrinjavanje otpada, opskrba energijom i opskrba vodom, upravne i socijalne državne usluge kao što su javna uprava, sjedišta civilne zaštite, škole i bolnice,
u skladu s kategorijom iz čl. 86. st. 3. t. 6. ZDIKN.
3. VRSTE USLUGA PROSTORNIH PODATAKA
3.1. Usluga pronalaženja (discovery)
Usluga koja omogućava pretraživanje skupova i usluga prostornih podataka na temelju sadržaja odgovarajućih metapodataka i prikaz sadržaja metapodataka.
3.2. Usluga pregleda (view)
Usluga koja, kao minimum, omogućava prikaz, snalaženje, uvećavanje i smanjivanje, pomicanje ili preklapanje skupova prostornih podataka koji se mogu pregledavati te prikaz informacija iz kazala i bilo kakvog relevantnog sadržaja metapodataka.
3.3. Usluga preuzimanja (download)
Usluga koja omogućava učitavanje skupova prostornih podataka ili dijelova tih skupova te, tamo gdje je to izvedivo, izravan pristup.
3.4. Usluga preobrazbe (transformation)
Usluga koja omogućava preobrazbu skupova prostornih podataka u cilju postizanja interoperabilnosti.
3.5. Usluga pozivanja prostornih podataka (invoke)
Usluga koja dopušta definiranje ulaznih podataka kao i izlaznih podataka koji se očekuju od prostorne usluge te radni tijek ili lanac usluga koji obuhvaća više usluga. Također dozvoljava definiranje vanjskog sučelja web usluga radnog tijeka ili lanca usluga.
3.6. Ostale usluge (other)
4. KLASIFIKACIJA USLUGA PROSTORNIH PODATAKA
Ključne riječi temelje se na taksonomiji geografskih usluga EN ISO 19119. Ova je taksonomija organizirana po kategorijama dok podkategorije definiraju polje vrijednosti klasifikacije usluga prostornih podataka.
100 Geografske usluge ljudskih interakcija (humanInteractionService)
Ova se kategorija sastoji od sljedećih podkategorija:
101 Preglednik kataloga (humanCatalogueViewer)
Klijentska usluga koja omogućava interakciju korisnika s katalogom u cilju pronalaženja, pregleda i upravljanja metapodacima o geografskim podacima ili geografskim uslugama.
102 Geografski preglednik (humanGeographicViewer)
Klijentska usluga koja omogućava korisniku pregledati jednu ili više zbirki značajki ili slojeva.
103 Preglednik radnih listova kataloga (humanGeographicSpreadsheetViewer)
Klijentska usluga koja korisniku omogućava interakciju s više podatkovnih objekata te mu omogućava da zatraži izračune koji su slični aritmetičkim radnim listovima, ali su prošireni na geografske podatke.
104 Uređivač usluge (humanServiceEditor)
Klijentska usluga koja omogućava korisniku da kontrolira usluge geografske obrade podataka.
105 Urednik definicije lanca (humanChainDefinitionEditor)
Pruža korisničku interakciju s uslugom definicije lanca.
106 Upravitelj provedbe radnog tijeka (humanWorkflowEnactmentManager)
Pruža korisničku interakciju s uslugom provedbe radnog tijeka.
107 Uređivač geografskih značajki (humanGeographicFeatureEditor)
Geografski preglednik koji omogućava korisničku interakciju s podacima o značajkama.
108 Uređivač zemljopisnih simbola (humanGeographicSymbolEditor)
Klijentska usluga koja omogućava čovjeku da izabere i upravlja knjižnicama simbola.
109 Uređivač generalizacije značajki (humanFeatureGeneralizationEditor)
Klijentska usluga koja omogućava korisniku da promijeni kartografske karakteristike određene značajke ili zbirke značajki pojednostavljujući njezinu vizualizaciju te istovremeno održavajući njene složene elemente - prostorni ekvivalent pojednostavljenja.
110 Preglednik strukture geografskih podataka (humanGeographicDataStructureViewer)
Klijentska usluga koja omogućava korisniku da pristupi dijelu skupa podataka kako bi vidio njegovu unutrašnju strukturu.
200 Geografski model/usluge upravljanja informacijama (infoManagementService)
Ova se kategorija sastoji od sljedećih potkategorija:
201 Usluga pristupa značajkama (infoFeatureAccessService)
Usluga koja omogućava klijentski pristup i upravljanje pohranom značajki.
202 Usluga pristupa kartama (infoMapAccessService)
Usluga koja omogućava klijentski pristup geografskoj grafici tj. slikama geografskih podataka.
203 Usluga pristupa pokrovu (infoCoverageAccessService)
Usluga koja omogućava klijentski pristup i upravljanje pohranom pokrova (coverage).
204 Usluga opisa senzora (infoSensorDescriptionService)
Usluga koja pruža opis senzora pokrova zajedno s položajem i orijentacijom senzora, kao i geometriju, dinamiku i radiometrijske karakteristike senzora u svrhu obrade geografskih podataka.
205 Usluga pristupa proizvodima (infoProductAccessService)
Usluga koja omogućava pristup i upravljanje pohranom geografskih proizvoda.
206 Usluga vrste značajki (infoFeatureTypeService)
Usluga koja korisniku omogućava pristup i upravljanje pohranom definicija vrsti značajki.
207 Usluga kataloga (infoCatalogueService)
Usluga koja omogućava usluge otkrivanja i upravljanja pohranom metapodataka o primjerima.
208 Usluga registra (infoRegistryService)
Usluga koja omogućava pristup pohrani metapodataka o vrstama.
209 Usluga geografskog leksikona (infoGazetteerService)
Usluga koja omogućava pristup imeniku primjera klasu ili klasa fenomena u stvarnom svijetu koji sadržavaju neke informacije u svezi položaja.
210 Usluga obrade narudžbi (infoOrderHandlingService)
Usluga koja omogućava korisniku mogućnost naručivanja proizvoda od dobavljača.
211 Usluga trajnog naloga (infoStandingOrderService)
Usluga obrade narudžbi koja omogućava korisniku da zatraži isporuku (diseminaciju) proizvoda unutar određenog geografskog područja kada isti postane dostupan.
300 Geografske usluge upravljanja tijekom rada/zadacima (taskManagementService)
Ova se kategorija sastoji od sljedećih potkategorija:
301 Usluga definiranja lanca (chainDefinitionService)
Usluga definiranja lanca i njegovog osposobljavanja da ga pokrene usluga izvođenja radnog tijeka.
302 Usluga izvođenja radnog tijeka (workflowEnactmentService)
Usluga izvođenja radnog tijeka tumači lanac i kontrolira trenutak nastanka usluga te slijed aktivnosti.
303 Usluga pretplate (subscriptionService)
Usluga koja omogućava klijentima prijavu za dobivanje obavijesti o događajima.
400 Usluge obrade geografskih podataka - prostorno (spatialProcessingService)
Ova se kategorija sastoji od sljedećih potkategorija:
401 Usluga konverzije koordinata (spatialCoordinateConversionService)
Usluga promjene koordinata iz jednog koordinatnog sustava u drugi koordinatni sustav koji se odnosi na isti datum.
402 Usluga transformacije koordinata (spatialCoordinateTransformationService)
Usluga promjene iz jednog koordinatnog referentnog sustava temeljenog na jednom datumu u koordinatni referentni sustav temeljen na drugom datumu.
403 Usluga konverzije pokrova/vektora (spatialCoverageVectorConversionService)
Usluga promjene prostornog predstavljanja iz sheme pokrivenosti u vektorsku shemu i obratno.
404 Usluga konverzije slikovnih koordinata (spatialImageCoordinateConversionService)
Usluga preobrazbe ili konverzije koordinata kako bi se promijenio koordinatni referentni sustav za određenu sliku.
405 Usluga ispravljanja (spatialRectificationService)
Usluga za pretvaranje slike u pravokutnu paralelnu projekciju te time i stalno mjerilo.
406 Usluga orto-ispravljanja (spatialOrthorectificationService)
Usluga ispravljanja koja uklanja iskrivljenost slike i premještanje uslijed visine terena.
407 Usluga podešavanja geometrijskog modela senzora (spatialSensorGeometryModelAdjustmentService)
Usluga koja podešava geometrijske modele senzora kako bi se poboljšalo poklapanje slike s ostalim slikama i/ili poznatim položajima na terenu.
408 Usluga pretvorbe geometrijskog modela slika (spatialImageGeometryModelConversionService)
Usluga koja pretvara geometrijske modele senzora u različit, ali ekvivalentan geometrijski model senzora.
409 Usluga izdvajanja (spatialSubsettingService)
Usluga koja izdvaja podskup iz ulaznih podataka u neprekinutom prostornom području bilo prema geografskoj lokaciji ili rasterskim koordinatama.
410 Usluga uzorkovanja (spatialSamplingService)
Usluga koja izdvaja podatke iz ulaznih podataka korištenjem dosljedne sheme uzimanja uzoraka bilo prema geografskoj lokaciji ili rasterskim koordinatama.
411 Usluga promjene podjele na listove (spatialTilingChangeService)
Usluga koja mijenja podjelu na listove geografskih podataka.
412 Usluga mjerenja dimenzija (spatialDimensionMeasurementService)
Usluga izračuna dimenzija objekata koji su vidljivi na slici ili drugom geografskom podatku.
413 Usluga manipulacije značajki (spatialFeatureManipulationService)
Registrira jednu značajku u drugu značajku, sliku, ili drugi skup podataka ili skup koordinata; ispravlja relativni translacijski pomak, rotacijske razlike, razlike mjerila i razlike perspektive. Ovjerava da su sve značajke u Zbirci značajki topološki dosljedne sukladno topološkim pravilima Zbirke značajki, te utvrđuje i/ili ispravlja bilo kakve otkrivene nedosljednosti.
414 Usluga uparivanja značajki (spatialFeatureMatchingService)
Usluga koja određuje koja značajka ili dio značajki predstavlja istu stvarnu cjelinu iz više izvora podataka npr. spajanje na rubovima i ograničena konflacija.
415 Usluga generalizacije značajki (spatialFeatureGeneralizationService)
Usluga koja smanjuje prostorne varijacije u zbirci značajki kako bi se povećala djelotvornost komuniciranja suzbijanjem neželjenih učinaka redukcije podataka.
416 Usluga određivanja rute (spatialRouteDeterminationService)
Usluga koja određuje optimalan put između dviju određenih točaka temeljem ulaznih parametara i svojstava koja su sadržana u Zbirci značajki.
417 Usluga pozicioniranja (spatialPositioningService)
Usluga koju osigurava uređaj za određivanje položaja kako bi se koristile, dobile i jednoznačno tumačile informacije te određuje ispunjavaju li rezultati zahtjeve za korištenjem.
418 Usluga analize blizine (spatialProximityAnalysisService)
S obzirom na položaj ili zemljopisnu značajku, pronalazi sve objekte s određenim skupom atributa koji se nalaze unutar razdaljine, koju odredi korisnik, od nekog položaja ili značajke.
500 Usluge obrade geografskih podataka - tematsko (thematicProcessingService)
Ova se kategorija sastoji od sljedećih potkategorija:
501 Usluga izračuna geo-parametara (thematicGoparameterCalculationService)
Usluga kojom se dobivaju kvantitativni rezultati orijentirani na primjenu koji nisu dostupni u samim sirovim podacima.
502 Usluga tematske klasifikacije (thematicClassificationService)
Usluga kojom se klasificiraju područja geografskih podataka temeljem tematskih atributa.
503 Usluga generalizacije značajki (thematicFeatureGeneralizationService)
Usluga koja generalizira vrste značajki u zbirci značajki kako bi se povećala djelotvornost komunikacije suzbijanjem neželjenih učinaka redukcije podataka.
504 Usluga izdvajanja (thematicSubsettingService)
Usluga koja izdvaja podatke iz ulaza temeljem vrijednosti parametara.
505 Usluga prostornog brojanja (thematicSpatialCountingService)
Usluga koja broji geografske značajke.
506 Usluga otkrivanja promjena (thematicChangeDetectionService)
Usluga pronalaženja razlika između dva skupa podataka koji predstavljanju isto geografsko područje u različitim trenucima.
507 Usluge izdvajanja geografskih informacija (thematicGeographicInformationExtractionService)
Usluge koje podržavaju izdvajanje značajki i informacija o terenu iz slika dobivenih daljinskim istraživanjem i skeniranjem.
508 Usluga obrade slika (thematicImageProcessingService)
Usluga kojom se mijenja vrijednost tematskih atributa slike uporabom matematičke funkcije.
509 Usluga generiranja smanjene razlučivosti (thematicReducedResolutionGenerationService)
Usluga koja smanjuje razlučivost slike.
510 Usluge slikovne manipulacije (thematicImageManipulationService)
Usluge za manipuliranje vrijednostima podataka u slikama: promjena vrijednosti boje i kontrasta, primjena različitih filtara, manipulacija razlučivošću slike, otklanjanje šumova, »striping«, sistematsko-radiometrijska korekcija, atmosfersko ublažavanje, promjena osvjetljenja scene, itd.
511 Usluge razumijevanja slike (thematicImageUnderstandingService)
Usluge koje automatski otkrivaju promjenu na slici, registrirano slikovno diferenciranje, analizu značaja razlika i njihov prikaz te diferencijaciju po području i modelu.
512 Usluge slikovne sinteze (thematicImageSynthesisService)
Usluga za izradu ili preobrazbu slika korištenjem računalnih prostornih modela, perspektivnih transformacija i manipulacija karakteristika slika kako bi se poboljšala vidljivost, izoštrila rezolucija i/ili smanjili učinci oblačnog pokrova ili maglice.
513 Manipulacija višekanalne slike (thematicMultibandImageManipulationService)
Usluge koje mijenjaju sliku koristeći više kanala slike.
514 Usluga otkrivanja objekata (thematicObjectDetectionService)
Usluga otkrivanja stvarnih objekata na nekoj slici.
515 Usluga geoparsinga (thematicGeoparsingService)
Usluga skeniranja tekstualnih dokumenata za poveznice na lokacije kao što su imena mjesta, adrese, poštanski brojevi itd. kao priprema za prijelaz na uslugu geokodiranja.
516 Usluga geokodiranja (thematicGeocodingService)
Usluga proširenja tekstualnih poveznica na lokacije geografskim koordinatama (ili nekom drugom prostornom poveznicom).
600 Usluge obrade geografskih podataka - vremensko (temporalProcessingService)
Ova se kategorija sastoji od sljedećih potkategorija:
601 Usluga preobrazbe vremenskog referentnog sustava (temporalReferenceSystemTransformationService)
Usluga promjene vrijednosti vremenskih primjera iz jednog vremenskog referentnog sustava u drugi vremenski referentni sustav.
602 Usluga izdvajanja (temporalSubsettingService)
Usluga izdvajanja podataka iz nekog ulaza u neprekinutom intervalu temeljem vremenskih položajnih vrijednosti.
603 Usluga uzorkovanja (temporalSamplingService)
Usluga koja izdvaja podskup iz ulaznih podataka korištenjem dosljedne sheme uzimanja uzoraka temeljeno na vremenskim položajnim vrijednostima.
604 Usluga analiza vremenske blizine (temporalProximityAnalysisService)
S obzirom na neki vremenski interval ili događaj, pronalazi sve objekte s danim skupom atributa koji se nalaze unutar intervala koji odredi korisnik od zadanog intervala ili događaja.
700 Usluge obrade geografskih podataka - metapodaci (metadataProcessingService)
Ova se kategorija sastoji od sljedećih potkategorija:
701 Usluga statističkog izračuna (metadataStatisticalCalculationService)
Usluga izračuna statistike skupa podataka.
702 Usluga geografskog bilježenja (metadataGeographicAnnotationService)
Usluge dodavanja pomoćnih informacija slici ili značajki u Zbirci značajki.
800 Geografske komunikacijske usluge (comService)
Ova se kategorija sastoji od sljedećih potkategorija:
801 Usluga kodiranja (comEncodingService)
Usluga koja osigurava provedbu pravila o kodiranju i pruža sučelje prema funkciji kodiranja i dekodiranja.
802 Usluga prijenosa (comTransferService)
Usluga koja osigurava primjenu jednog ili više protokola prijenosa, što dopušta prijenos podataka između sustava distribuiranih informacija putem komunikacijskih medija bez ili putem interneta.
803 Usluga geografske kompresije (comGeographicCompressionService)
Usluga koja pretvara prostorne dijelove zbirke značajki u ili iz komprimiranog oblika.
804 Usluga konverzije geografskog formata (comGeographicFormatConversionService)
Usluga koja pretvara jedan format geografskih podataka u drugi.
805 Usluga prijenosa poruka (comMessagingService)
Usluga koja omogućava da više korisnika istovremeno pregledava, komentira i zatraži uređivanje zbirki značajki
806 Daljinsko upravljanje datotekama podataka i izvršnih programa (comRemoteFileAndExecutableManagement)
Usluga koja daje pristup sekundarnoj pohrani geografskih značajki kao da je na strani klijenta.
5. STUPANJ SUKLADNOSTI
5.1. Sukladno (conformant)
Izvor se u potpunosti poklapa s navedenom specifikacijom.
5.2. Nesukladno (notConformant)
Izvor se ne poklapa s navedenom specifikacijom.
5.3. Neocijenjeno (notEvaluated)
Poklapanje nije ocijenjeno.
6. ULOGA ODGOVORNE STRANE
6.1. Dobavljač izvora (resourceProvider)
Strana koja nabavlja izvor.
6.2. Skrbnik (custodian)
Strana koja prihvaća odgovornost za podatke i osigurava primjerenu brigu i održavanje izvora.
6.3. Vlasnik (owner)
Strana koja je vlasnik izvora.
6.4. Korisnik (user)
Strana koja koristi izvor.
6.5. Distributer (distributor)
Strana koja distribuira izvor.
6.6. Tvorac (originator)
Strana koja je stvorila izvor.
6.7. Točka kontakata (pointOfContact)
Strana koju se može kontaktirati kako bi se saznalo više o izvoru ili nabavilo izvor.
6.8. Glavni istraživač (principalInvestigator)
Ključna strana odgovorna za prikupljanje informacija i vođenje istraživanja.
6.9. Obradnik (processor)
Strana koja je obradila podatke na način da je izvor bio promijenjen.
6.10. Izdavač (publisher)
Strana koja je objavila izvor.
6.11. Autor (author)
Strana koja je autor izvora.
