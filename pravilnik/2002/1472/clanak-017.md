# Članak 17.
Kod uporabe opreme u okružju računala nužna je upotreba API (Application Program Interface) programskih sklopova kojima se mora osigurati korištenje bilo koje vrste smart kartica, PCMCIA (Personal Computer Memory Card International Association) modula, tokena i drugih uređaja.
Oprema s ugrađenim API programskim sklopovima mora izvršavati:
- izradu elektroničkog potpisa
- ovjeru elektroničkog potpisa
- oblikovanje podataka
- komuniciranje uređaja i podataka.
API programski sklopovi moraju se temeljiti na sljedećim kriptografskim obrascima:
- CRYPTOKI - BSAFE/PKCS (RSA) za ugradnju u uređaje i programe
- IDUP-API (Independent Data Unit Protection) za ugradnju u uređaje
- GSS-API (General Security Services) za ugradnju u programe.
Kod uporabe kartica Fortezza nužna je primjena RFC 2876 (Use of the KEA and SKIPJACK Algorithms in CMS) obrasca povezivanja procesa kriptiranja i procesa potpisivanja.
