## Usmjeravanje komunikacijskog prometa prema prenesenim brojevima
# Članak 10.
(1) Operatori su obvezni odmah po isteku vremenskog okvira prenosivosti broja ispravno usmjeravati poziv prema prenesenom broju.
(2) Za ispravno usmjeravanje poziva prema prenesenim brojevima operator je u zahtjevu za uspostavu poziva (eng.: IAM - Initial Address Message) obvezan ispred nacionalnog broja dodati predbroj za usmjeravanje poziva (eng.: NRN - Network Routing Number).
(3) Predbroj za usmjeravanje poziva je mrežni broj koji označava elektroničku komunikacijsku mrežu (eng.: NetID - Network Identifier) i čvor (eng.: NodeID) na kojima se nalazi preneseni broj.
(4) Veza između pretplatničkog broja i predbroja za usmjeravanje poziva (NRN) pohranjena je u CABP. Predbroj za usmjeravanje poziva sastoji se od 5 znamenaka sljedeće strukture:
Predbroj za usmjeravanje poziva (eng.: NRN - Network Routing Number)
5 znamenaka
Heksadecimalna
vrijednost broja 14
1 znamenka
Kôd za oznaku mreže
(00-99)
2 znamenke
Kôd za oznaku centrale
(00-99)
2 znamenke
E
NetID
NodeID
(5) Prva znamenka predbroja za usmjeravanje iz tablice iz stavka 4. ima heksadecimalnu vrijednost broja 14 koja označava da se pozivajući broj sastoji od predbroja za usmjeravanje na koji se nastavlja nacionalni broj.
(6) Vrijednost polja Kôd za oznaku mreže (NetID) iz tablice iz stavka 4. određuje Agencija sukladno Pravilniku o dodjeli adresa i brojeva.
(7) Vrijednost polja Kôd za oznaku čvora (NodID) iz tablice iz stavka 4. određuje operator.
