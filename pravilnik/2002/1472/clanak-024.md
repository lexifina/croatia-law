# Članak 24.
Postupak povezivanja sustava certificiranja temelji se na primjeni dogovorenih obrazaca za sljedeća područja:
- certifikati
- poruke
- razmjena certifikata i poruka
- prijenos certifikata i poruka.
Certifikat ima dogovoreni obvezni format utvrđen putem obrasca X.509v3:1997.
Poruke uključuju:
- upite za izdavanje certifikata koji se iskazuju putem obrasca PKCS#10
- nepotpisane/potpisane/kritpirane poruke koje se iskazuju putem obrasca PKCS#7
- skupne podatke o potpisniku koji se iskazuju putem obrasca PKCS#12 (Personal Information Exchange Syntax).
Razmjena certifikata i poruka ima dogovoreni obvezni obrazac CMC (Certificate Management Messages over CMS), pri čemu se upit za izdavanje certifikata temelji na potpisanoj PKCS#109 oblikovanoj poruci, a odgovor (certifikat) na PKCS#7 nepotpisanoj ili CMS potpisanoj poruci. Sustavi certificiranja koji imaju mogućnost tehnološke podrške mogu koristiti i CMP (Certificate Management Protocols).
Prijenos certifikata i poruka provodi se putem telekomunikacijskih sustava uz obveznu uporabu obrasca S/MIME (Secure Multipurpose Internet Mail Extensions) odnosno obrasca SSL (Secure Socket Layer).
