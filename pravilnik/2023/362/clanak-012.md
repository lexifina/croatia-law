## Zaštitni kod brodara
# Članak 12.
(1) ZKB stvara Operator linije te ga dostavlja u SEOP u sklopu zahtjeva za evidentiranje prodaje putne karte.
(2) ZKB Operatoru linije služi da po potrebi u postupku nadzora dokazuje da je on izdavatelj određene putne karte.
(3) ZKB omogućava provjeru:
- jedinstvenosti, izvornosti i nepromjenjivost podataka o putnoj karti, te
- autentičnosti Operatora linije koji izdaje i elektronički potpisuje podatke o putnoj karti.
(4) Oznaka ZKB je 32-znamenkasti broj zapisan u heksadecimalnom formatu (brojevi i mala slova: 0-9, a-f).
(5) Pri računanju ZKB koristi se UTF-8 (Unicode Transformation Format 8) kodiranje. Kao decimalni separator kod podatka »ukupni iznos« koristi se točka.
(6) Za potrebe izrade ZKB, Operatori linije su dužni osigurati digitalni certifikat u skladu s člankom 15. ovoga Pravilnika.
(7) Elektroničko potpisivanje podataka o putnoj karti vrši se koristeći RSA-SHA265 algoritma.
(8) ZKB se izračunava korištenjem MD5 kriptografske hash funkcije (po standardu RFC 1321 The MD5 Message-DigestAlgorithm) koja se primjenjuje na izračunati elektronički potpis.
