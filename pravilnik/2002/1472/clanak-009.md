## III. CERTIFIKAT
# Članak 9.
Struktura certifikata temelji se na obrascu ITU X.509 v3 i uključuje kao obvezne atribute:
- inačicu obrasca X.509
- serijski broj
- jednoznačni identifikacijski kod (Object Identifier prema ASN.1) Općih pravila davatelja usluga certificiranja (ako je prethodno pridobio OID)
- oznaku (ID) algoritma izrade elektroničkog potpisa (sha1/RSA, MD5/RSA)
- ime izdavatelja certifikata - po strukturi utvrđenoj u obrascu X.500
- razdoblje valjanosti certfikata
- ime potpisnika (korisnika certifikata) - po strukturi utvrđenoj u obrascu X.500
- podaci o javnom ključu potpisnika
- jedinstveni identifikator izdavatelja certifikata
- jedinstveni identifikator korisnika certifikata (potpisnika)
- dodatni atributi (proširenje osnovnog skupa atributa)
- elektronički potpisane prethodne podatke od strane izdavatelja certifikata.
