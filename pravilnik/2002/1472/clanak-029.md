# Članak 29.
Pristup sadržajima elektroničkih imenika mora biti oblikovan u skladu s okružjem X.500 i primjenom obrasca DAP (Directory Access Protocol).
Sustavi certificiranja mogu radi jednostavnijeg pružanja usluga elektroničkih imenika koristiti LDAPv3/RFC 2251 (Lightweight Directory Access Protocol) obrazac oblikovanja i pristupa elektroničkim imenicima.
LDAP elektronički imenici mogu biti sadržajno ograničeni za jedan sustav certificiranja.
Svaki sustav certificiranja mora osigurati prosljeđivanje upita u elektroničke imenike drugih sustava certificiranja. Prosljeđivanje upita može se provoditi uporabom vlastitog elektroničkog imenika ili usmjeravanjem upita davatelju imeničkih usluga koji za njega vodi elektronički imenik.
Povezivanje elektroničkih imenika koji koriste obrazac LDAP mora se provoditi primjenom obrasca LDUP (LDAP Duplication/Replication/Update Protocol) putem dva temeljna modula:
- Replication Information Model:2001
- Replication Update Protocol:2001.
Povezivanje elektroničkih imenika koji koriste obrazac X.500 mora se provoditi primjenom obrasca DISP (Directory Information Shadowing Protocol) putem primjene dogovorene strukture DIT (Directory Information Tree) objedinjene obrascima ISO 9594 odnosno X.520:1988 (Selected Attribute Types) i X.521:1988 (Selected Object Classes).
Povezivanje računalnih sustava koji pružaju usluge elektroničkih imenika mora se provoditi primjenom obrasca X.518:1993 kojim se definira obrazac povezivanje DSP (Directory System Protocol).
