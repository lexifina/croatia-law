Prilog 1
NAČIN IZRAČUNA KONTROLNOG BROJA HRVATSKOG IBAN-A
Za izračun kontrolnog broja IBAN-a primjenjuje se međunarodna norma ISO 7064, MOD 97-10, na sljedeći način:
1. Vodeći broj banke i broj računa klijenta treba upisati u slijedu bez razmaka i posebnih znakova, što rezultira nizom:
AAAAAAABBBBBBBBBB
gdje slova A označuju vodeći broj banke (7n), a slova B broj (partiju) računa (10n);
2. Oznaku za Hrvatsku (HR) i dvije nule (00) potrebno je dodati s desne strane niza navedenog u točki 1.:
AAAAAAABBBBBBBBBBHR00.
3. U tako dobivenom nizu slova (HR) treba pretvoriti u brojčane znakove u skladu s međunarodnom normom ISO 13616 prema kojoj H=17, R=27, što ukupno daje broj od 23 znamenke:
AAAAAAABBBBBBBBBB172700.
4. Dobiveni broj od 23 znamenke dijeli se sa 97, pri čemu se dobiva ostatak (NN).
5. Ostatak (NN), dobiven dijeljenjem, treba oduzeti od (97 + 1), što konačno čini kontrolni broj (CC):
CC = (97 = 1) - NN.
Ako je rezultat manji od 10, dobivenom će broju prethoditi 0.
Prilog 2
PROVJERA KONTROLNOG BROJA
1. Treba izostaviti sve znakove koji nisu alfanumerički i razmake te premjestiti prva četiri znaka koji čine oznaku države (npr. HR) i kontrolni broj (CC) na desni kraj niza, tako da se na kraju dobije sljedeći niz:
primjerice: AAAAAAABBBBBBBBBBHRCC.
2. Potom je potrebno pretvoriti slova u znamenke u skladu s tablicom prema međunarodnoj normi ISO 13616:
A=10 F=15 K=20 P=25 U=30
B=11 G=16 L=21 Q=26 V=31
C=12 H=17 M=22 R=27 W=32
D=13 I=18 N=23 S=28 X=33
E=14 J=19 O=24 T=29 Y=34 Z=35
primjerice: AAAAAAABBBBBBBBBB1727CC.
3. Prema međunarodnoj normi ISO 7064, MOD 97-10, dobiveni broj od 23 znamenke dijeli se brojem 97, pri čemu se dobiva ostatak dijeljenja (NN).
4. Ako je ostatak dijeljenja (NN)=1, IBAN je točan.
