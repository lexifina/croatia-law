UPUTA O TEHNIČKIM RJEŠENJIMA ZA DOSTAVU IZVJEŠTAJA
1. Ova je Uputa sastavni dio Odluke o informatičkim rješenjima za dostavu izvještaja kreditnih institucija u skladu s propisima Europske unije.
2. Uputa sadržava informatička rješenja za dostavljanje sadržaja izvještaja iz ove Odluke i Odluke o izvješćivanju o planovima financiranja, tehničke zahtjeve za dostavljanje izvještaja i sadržaj izvještajne datoteke.
3. Pojedini pojmovi koji se upotrebljavaju u ovoj Uputi imaju sljedeće značenje:
1) »tehnička definicija« jest definicija točaka podataka iz jedinstvenog obrasca s točkama podataka utvrđenog u prilogu XIV. Provedbene uredbe Komisije (EU) br. 680/2014 koje objavljuje i ažurira Europsko nadzorno tijelo za bankarstvo
2) »validacijska pravila iz tehničke definicije« jesu validacijska pravila utvrđena u Prilogu XV. Provedbene uredbe Komisije (EU) br. 680/2014 koje objavljuje i ažurira Europsko nadzorno tijelo za bankarstvo.
I. Tehnički zahtjevi za dostavljanje izvještajnog zahtjeva
4. U dijelu datoteke propisuje se način dostavljanja podataka u formatu XML za potrebe ispunjavanja izvještajnog zahtjeva.
5. Podaci se Hrvatskoj narodnoj banci dostavljaju u datotekama čija su obilježja i sadržaj opisani u ovom dijelu Upute.
I.1. Standardna obilježja datoteke
6. Pri dostavljanju izvještaja kreditna institucija primjenjuje format datoteke XML koji zadovoljava tehničke zahtjeve datoteke XSD koju objavljuje Hrvatska narodna banka na svojoj internetskoj stranici poštujući verziju tehničke definicije.
7. Hrvatska narodna banka može na svojoj internetskoj stranici objaviti neslužbene primjere datoteka XML kao prikaz tehničke logike, a ne ispravnih podataka koji vrijede za određeni izvještajni obuhvat ili tehničku definiciju.
8. Hrvatska narodna banka može na svojoj internetskoj stranici objaviti neslužbene dokumente koji povezuju format za dostavu podataka koji je odredila Hrvatska narodna banka i verziju tehničke definicije za određene izvještajne datume.
9. Kreditna institucija dužna je datoteku oblikovati u skladu s kodnom stranicom 8859 - 2 (CE).
10. Sadržaj izvještaja u obliku XML popunjava se prema prilozima iz Provedbene uredbe Komisije (EU) br. 680/2014, prilozima iz Provedbene uredbe Komisije (EU) 2016/2070 i Upute za jedinstvenu primjenu Odluke o izvješćivanju o planovima financiranja.
I.2. Sadržaj datoteke
11. Polja se popunjavaju onako kako je prikazano u Tablici 1. Ulazni slogovi u ovoj Uputi.
12. U dijelu datoteke XML koji se odnosi na izvještaje potrebno je slijedom navesti oznake izvještaja s vrijednostima, pozicijama (tagovima) i parametrima pojedinih polja prema pravilima iz Tablice 1. Ulazni slogovi.
13. Izvještajna institucija dužna je sadržaj datoteke XML prilagoditi izvještajima koji se sastavljaju za svaki referentni datum propisan Provedbenom uredbom Komisije (EU) br. 680/2014, Provedbenom uredbom Komisije (EU) 2016/2070 i Odlukom o izvješćivanju o planovima financiranja. Ako nije drugačije navedeno, kreditna institucija dužna je za određeni referentni datum dostaviti sve potrebne oznake izvještaja (u polju Izvjestaj) za određene oznake izvješća (iz polja OznakaIzvjesca). Izvještaji čija obveza dostave nije propisana za određeni datum ne trebaju biti sastavni dio sadržaja datoteke XML koja se šalje za određene oznake izvještaja. Na primjer, izvještaji oznake C 15.00 i F 46.00 ne trebaju biti predmet sadržaja datoteke XML za tromjesečno izvještavanje (31. ožujka ili 30. rujna).
14. Konceptualno rješenje izvještajne forme karakterizira osnovni podatak koji je predmet izvještavanja: vrijednost, koja predstavlja svaku stavku definiranih izvještaja koji su predmet dostave ovoga dijela Upute.
15. Za potrebe dostavljanja podataka iz izvještaja te prepoznavanja i formiranja kontrola u ovom dijelu Upute, svaka je vrijednost opisana jednoznačnim identifikatorom na razini svakog izvještaja, a dodatno, po potrebi, i oznakama parametara za koji se ti identifikatori (i/ili vrijednosti) dostavljaju.
16. Svako polje sloga datoteke ima ugrađenu kontrolu obvezne popunjenosti polja te kontrolu je li popunjeno vrijednošću s popisa dopuštenih vrijednosti u određenim kombinacijama koje se zasnivaju na tehničkoj definiciji.
17. Sivo označene pozicije iz izvještaja nemaju svoju jednoznačnu oznaku ili identifikator (tag) i ne dostavljaju se u datoteci XML.
18. Ako izvještajna institucija nema nijedan podatak za izvještaj koji je dužna dostaviti ili ne ispunjava uvjete za slanje izvještaja koji je predmet dostave za referentni datum, dužna je dostaviti oznaku izvještaja u polju (Izvještaj) koji se ne popunjava, bez dostavljanja ostalih njegovih slogova. Na primjer, ako je izvještaj oznake C 08.01 prazan, u datoteci XML dostavlja se zapis <Podaci izvjestaj="C 08.01"/>.
19. Ako izvještajna institucija nema dio podataka za neki izvještaj koji je dužna dostaviti, dužna je dostaviti sve pozicije (tagove) po tom izvještaju, pri čemu se u polje (Vrijednost) upisuje numerički iznos nula (0).
20. Izvještajna institucija dostavlja samo ona obilježja iz alfanumeričkih polja za koje ima podatke. Točnije, izvještajna institucija ne dostavlja oznake parametara za koje nema nijedan podatak u izvještaju koji je dužna dostaviti.
I.3. Zaglavlje
21. Prvi slog u datoteci jest Zaglavlje, u koje se upisuju podaci o datoteci: matični broj kreditne institucije koji dodjeljuje Državni zavod za statistiku, osobni identifikacijski broj kreditne institucije koji dodjeljuje Ministarstvo financija na temelju Zakona o osobnom identifikacijskom broju, posljednji dan izvještajnog razdoblja, oznaka izvještaja i ukupni broj slogova u datoteci. Osnovni podaci o odgovornoj osobi za kontakt (ime i prezime odgovorne osobe) unose se u polju (Ime osobe), o telefonu u polju (Telefon) i adresi elektroničke pošte u polju (Elektronička pošta). Polje (Napomena) neobavezno je polje u koje se može unijeti do 100 znakova proizvoljnog teksta.
22. U polju (Oznaka izvješća) navodi se jedna od sljedećih oznaka koja obuhvaća određeni izvještajni skup:
1) »NP« za nekonsolidirani privremeni izvještaj koji obuhvaća izvještaje iz poglavlja 3., 4., 5. i 6., članka 16. te poglavlja 7.a Provedbene uredbe Komisije (EU) br. 680/2014
2) »KP« za konsolidirani privremeni izvještaj koji obuhvaća izvještaje iz poglavlja 3., 4., 5. i 6., članka 16. te poglavlja 7.a Provedbene uredbe Komisije (EU) br. 680/2014
3) »NR« za nekonsolidirani revidirani izvještaj koji obuhvaća izvještaje iz poglavlja 3., 4., 5. i 6., članka 16. te poglavlja 7.a Provedbene uredbe Komisije (EU) br. 680/2014
4) »KR« za konsolidirani revidirani izvještaj koji obuhvaća izvještaje iz poglavlja 3., 4., 5. i 6., članka 16. te poglavlja 7.a Provedbene uredbe Komisije (EU) br. 680/2014
5) »MN« za mjesečni nekonsolidirani privremeni izvještaj koji obuhvaća izvještaje iz članka 15. Provedbene uredbe Komisije (EU) br. 680/2014
6) »MK« za mjesečni konsolidirani privremeni izvještaj koji obuhvaća izvještaje iz članka 15. Provedbene uredbe Komisije (EU) br. 680/2014
7) »FN« za godišnji nekonsolidirani izvještaj - planovi financiranja koji obuhvaćaju izvještaje iz članka 3. Odluke o izvješćivanju o planovima financiranja
8) »FK« za godišnji konsolidirani izvještaj - planovi financiranja koji obuhvaćaju izvještaje iz članka 3. Odluke o izvješćivanju o planovima financiranja
9) »AN« za nekonsolidirani izvještaj - dodatni likvidnosni nadzorni parametri koji obuhvaćaju izvještaje iz poglavlja 7.b Provedbene uredbe Komisije (EU) br. 680/2014
10) »AK« za konsolidirani izvještaj - dodatni likvidnosni nadzorni parametri koji obuhvaćaju izvještaje iz poglavlja 7.b Provedbene uredbe Komisije (EU) br. 680/2014
11) »BN« za godišnji nekonsolidirani izvještaj - referentni portfelj koji obuhvaća izvještaje iz članka 1. Provedbene uredbe Komisije (EU) 2016/2070
12) »BK« za godišnji konsolidirani izvještaj - referentni portfelj koji obuhvaća izvještaje iz članka 1. Provedbene uredbe Komisije (EU) 2016/2070
13) »IN« za godišnji nekonsolidirani izvještaj - referentni portfelj IMV koji obuhvaća izvještaje iz članka 1. Provedbene uredbe Komisije (EU) 2016/2070 i
14) »IK« za godišnji konsolidirani izvještaj - referentni portfelj IMV koji obuhvaća izvještaje iz članka 1. Provedbene uredbe Komisije (EU) 2016/2070.
23. Za oznake izvješća »NR« i »KR« u datotekama XML izvještajne institucije dostavljaju sve izvještaje kao i u obuhvatu oznaka »NP« i »KP«, što obuhvaća i revidirane izvještaje u skladu s Odlukom o sadržaju revizije u kreditnim institucijama i preostale izvještaje koji se dostavljaju sa stanjem na dan 31. prosinca, ali nisu predmet revizije. Razlog uključivanja nerevidiranih izvještaja u skup revidiranih izvještaja jest usklađivanje podataka zbog zadovoljavanja pravila za validaciju međusobno povezanih izvještaja.
24. Za oznake izvješća »NP« i »NR« u datotekama XML izvještajne institucije dostavljaju izvještaje oznake C 30.00, C 31.00, F 17.01, F 17.02, F 17.03, F 40.01 i F 40.02 na način definiran točkom 18. ove Upute.
25. U ostalim slogovima datoteke unose se podaci o izvještaju, parametrima, pozicijama (tagovima) i vrijednostima polja prema Uputi.
I.4. Ostali slogovi datoteke
26. Osnovni identifikator oznake izvještaja temelji se na tehničkoj definiciji i navodi se u polju (Izvjestaj).
27. Jednoznačna oznaka ili identifikator vrijednosti duljine osam znamenaka naziva se tag i navodi se u polju (Tag).
28. Oznake za tag prate logiku označavanja redaka i stupaca koji su propisani formama izvještaja iz priloga Provedbene uredbe Komisije (EU) br. 680/2014 i Provedbene uredbe Komisije (EU) 2016/2070, na način da je:
tag = abcdefgh, gdje je:
1) »abcd« - broj mjesta oznake za redni broj retka i
2) »efgh« - maksimalan broj mjesta oznake za redni broj stupca.
29. Oznake za tag prate logiku označavanja redaka i stupaca koji su propisani validacijskim pravilima iz tehničke definicije i koja vrijede za određeni izvještajni datum.
30. Oznaka za redni broj retka u tagu »abcd« sadržava četiri mjesta zato što broj oznaka redaka u nekim izvještajima prelazi 1000. Za sve takve izvještaje, čiji broj oznaka redaka prelazi 1000, vrijedi da je »a« = 1, dok za ostale vrijedi da je »a« = 0. Oznaka za redni broj stupca u tagu »efgh« može sadržavati najviše četiri mjesta zato što broj oznaka stupaca u nekim izvještajima sadržava i četiri znamenke. Za sve takve izvještaje, čiji broj oznaka stupca sadržava četiri znamenke, vrijedi da je »e« = 0, dok za sve ostale izvještaje redni broj stupca u tagu sadržava tri znamenke »fgh«.
31. Osnovni identifikator vrijednosti iz izvještaja koji su predmet dostave u ovom dijelu Upute navodi se u polju (Vrijednost), u koje je moguće unijeti do 1024 znaka.
32. Vrijednosti pojedinih polja uvijek se dostavljaju uz pripadajući tag. Na taj način omogućena je kontrola popunjavanja polja u samoj datoteci XML postavljanjem dodatnih ograničenja i pravila u datoteci XSD.
33. Popis mogućih vrijednosti iz izvještaja, koji se temelji na tehničkoj definiciji, obuhvaća sljedeće tipove vrijednosti:
1) monetarni iznos (engl. Monetary)
2) cijeli broj (engl. Integer)
3) postotak (engl. Percentage)
4) Booleova vrijednost (engl. Boolean)
5) šifra (engl. Code)
6) niz znakova (engl. String)
7) datum (engl. Date)
8) ključ (engl. Key value)
9) broj (decimalno) (engl. Number (decimal)).
34. Hrvatska narodna banka može objaviti neslužbeni popis mogućih vrijednosti te mogućih kombinacija oznaka redaka i stupaca propisanih izvještaja i njihovih pripadajućih tagova za sve tipove vrijednosti iz izvještaja, pri čemu će se isti mijenjati u skladu s dopunom i (ili) promjenom tehničke definicije.
35. Monetarni iznosi u novčanim jedinicama navode se u punom iznosu novčane jedinice u kojoj su izražene, uključujući decimalnu točku i dva decimalna mjesta. Na primjer: ako je vrijednost pozicije 100.000,60 kuna, u izvještaj se upisuje numerički iznos 100000.60, dakle, uključujući i iznos u lipama. Ako je vrijednost pozicije nula (0), u izvještaj se upisuje numerički iznos 0.
36. Svi monetarni iznosi izraženi u stranim valutama preračunavaju se u kune primjenom srednjeg tečaja Hrvatske narodne banke koji vrijedi na izvještajni datum. Iznosi izraženi u stranim valutama koje nisu iskazane na tečajnici Hrvatske narodne banke preračunavaju se u eure ili američke dolare primjenom srednjih tečajeva referentnih tržišta te ih se potom preračunava u kune primjenom srednjeg tečaja Hrvatske narodne banke koji vrijedi na izvještajni datum.
37. U dijelu izvještavanja prema prilozima XII., XIII., XXIV., XXV., XVIII., XIX., XX. i XXI. Provedbene uredbe Komisije (EU) br. 680/2014, stavke u kunama s ugovorenom valutnom klauzulom prema određenoj valuti tretiraju se kao pozicije u kunama.
38. Cijeli brojevi navode se u punom iznosu jedinice u kojoj su izražene, ali bez decimalne točke i decimalnih mjesta. Na primjer, ako je vrijednost pozicije 100 jedinica, u izvještaj se upisuje numerički iznos 100. Ako je vrijednost pozicije nula (0), u izvještaj se upisuje numerički iznos 0.
39. Postotak se navodi u postotnom iznosu u kojem je izražen, uključujući decimalnu točku i četiri decimalna mjesta. Na primjer, ako je vrijednost pozicije 9.6%, u XML datoteci se upisuje iznos 0.0960. Ako je vrijednost pozicije nula (0), u izvještaj se upisuje numerički iznos 0.
40. Brojevi (decimalno) navode se u punom iznosu jedinice u kojoj su izraženi, uključujući decimalnu točku i dva decimalna mjesta. Ako je vrijednost pozicije nula (0), u izvještaj se upisuje numerički iznos 0.
41. Booleova vrijednost navodi se prema znakovima iz tehničke definicije, a za potrebe izvještavanja istinite ili lažne vrijednosti. Za istinito je potrebno navesti oznaku »True«, dok je za lažno potrebno navesti oznaku »False«.
42. Šifra se navodi prema znakovima iz tehničke definicije. Ako vrijednost pozicije nije poznata, u izvještaj se upisuje »Null« ili alfanumerička oznaka » - « (minus).
43. Niz znakova se navodi do najviše 1024 znaka prema tehničkoj definiciji (npr. pri upisu oznake identifikacije, naziva, rejtinga, komentara ili druge oznake). Ako se u polje upisuje identifikacijska oznaka pravnog subjekta, prioritet pri navođenju ima unos OIB-a, a ako on nije poznat, upotrebljavaju se ostale identifikacijske oznake (matični broj koji dodjeljuje DZS ili interni evidencijski broj koji je dodijelila izvještajna institucija). Ako vrijednost pozicije nije poznata, u izvještaj se upisuje »Null« ili alfanumerička oznaka » - « (minus).
44. Datum se navodi prema znakovima iz tehničke definicije, a za potrebe izvještavanja o mjesecima i godinama u formatu »dd/mm/gggg«.
45. Ključ se navodi pri upisivanju oznake do najviše 1024 znaka koja je jedinstveni identifikator za svaki redak varijabilnog izvještaja prema tehničkoj definiciji. Ako se u polje upisuje identifikacijska oznaka pravnog subjekta, prioritet pri navođenju ima unos OIB-a, a ako on nije poznat, upotrebljavaju se ostale identifikacijske oznake (matični broj koji dodjeljuje DZS ili interni evidencijski broj koji je dodijelila izvještajna institucija).
46. Oznake parametara navode se prema vrijednosti znakova iz tehničke definicije u izvještajima koji se formom ponavljaju za različit sadržaj. Svaka oznaka parametra (predefinirana ili dio popisa otvorenih osi z) po kojemu se tip vrijednosti i tagovi iz izvještaja ponavljaju čini jedan list tog izvještaja.
Tablica 1. Ulazni slogovi
Broj | XML polje | Naziv polja | Tip polja | Duljina polja | Sadržaj polja
Zaglavlje (prvi slog)
1. | MBR | Kreditna institucija MBR | N | 8 | Matični broj koji dodjeljuje Državni zavod za statistiku
2. | DatumStanja | Datum stanja | D | 8 | gggg-mm-dd
3. | OznakaIzvjesca | Oznaka izvješća | AN | 2 | NP, NR, KP, KR, MN, MK, FN, FK, AN, AK, BN, BK, IN, IK
4. | OdgovornaOsoba | Ime osobe | AN | 50 | Ime odgovorne osobe
5. | Telefon | Telefon | AN | 30 | Telefon za kontakt
6. | E-mail | Elektronička pošta | AN | 50 | E-adresa za kontakt
7. | OIB | OIB kreditne institucije | N | 11 | OIB
8. | Napomena | Napomena | AN | 100 | Napomena
Izvještaj (ostali slogovi)
Broj | XML polje | Naziv polja | Tip polja | Duljina polja | Sadržaj polja
1. | Izvjestaj | Oznaka izvještaja | AN | 12 | Oznaka za izvještaj prema tehničkoj definiciji
2. | Parametar | Parametar | AN | 256 | Oznaka za parametar prema tehničkoj definiciji
3. | Tag | Tag | AN | 8 | Oznaka za tag prema Uputi
4. | Vrijednost | Vrijednost | AN | 1024 | Vrijednost prema Uputi
I.5. Kontrole
47. Sadržaj kontrola izvještaja iz Provedbene uredbe Komisije (EU) br. 680/2014, Provedbene uredbe Komisije (EU) 2016/2070 i izvještaja iz članka 3. točaka od 1. do 12. Odluke o izvješćivanju o planovima financiranja u skladu je s validacijskim pravilima iz tehničke definicije.
48. Za potrebe razumijevanja validacijskih pravila iz tehničke definicije opći zapis polja izvještaja definiran je kao: {izvještaj, redak, stupac, parametar}.
49. U dijelu zapisa »izvještaj« upisan je identifikator oznake izvještaja.
50. U dijelu zapisa »redak« upisana je oznaka »{rabcd}«, pri čemu je:
1) »r« - oznaka retka,
2) »abcd« - oznaka za redni broj retka (pritom se za potrebe validacijskih pravila oznaka »a« upotrebljava samo pri označavanju rednog broja retka koji prelazi 1000).
51. U dijelu zapisa »stupac« upisana je oznaka »{cefgh}«, pri čemu je:
1) »c« - oznaka stupca,
2) »efgh« - oznaka za redni broj stupca (pritom se za potrebe validacijskih pravila oznaka »e« upotrebljava samo pri označavanju rednog broja stupca koji prelazi četiri znamenke).
52. U dijelu zapisa »parametar« upisano je dodatno obilježje po kojem izvještaji variraju.
53. U slučaju provjere valjanosti unutar izvještaja, u kojoj se upotrebljavaju samo podaci iz tog izvještaja, zapisi validacijskih pravila ne navode oznaku izvještaja, već samo redak i stupac izvještaja: {rabcd, cefgh}. Ako izvještaj ima samo jedan stupac, u zapisu validacijskih pravila navode se samo oznaka i redci izvještaja {izvještaj; rabcd}.
II. Način dostave datoteka
54. Podaci se dostavljaju elektronički (SWIFT, internet), pri čemu načini dostavljanja podataka mogu biti utvrđeni posebnim uputama.
55. Datoteka može biti u izvornom formatu (XML) ili komprimirana (ZIP).
56. Za svaki datum stanja i oznaku izvještaja izvještajna institucija šalje posebnu datoteku, što znači da jedna datoteka smije sadržavati samo jedan datum stanja i oznaku izvješća.
57. Za elektroničku dostavu datoteka XML upotrebljava se naziv datoteke COFI_MBR_OZNAKAIZVJ_DATUMSTANJA.XML, gdje je:
1) MBR: matični broj kreditne institucije u duljini od osam znakova; ako je broj znakova manji od osam, znakovi se moraju nadopuniti vodećim nulama
2) OZNAKAIZVJ: oznaka izvješća u datoteci (oznake »NP« ili »KP« ili »MN« ili »MK« ili »NR ili »KR« ili »FN« ili »FK« ili »AN« ili »AK« ili »BN« ili »BK« ili »IN« ili »IK«)
3) DATUMSTANJA: referentni datum izvještaja u datoteci u obliku »GGGGMMDD«.
