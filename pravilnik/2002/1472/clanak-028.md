## Elektronički imenici
# Članak 28.
Svi potpisnici i subjekti sustava certificiranja upisuju se u elektroničke imenike.
Usluge elektroničkih imenika temelje se na primjeni obrasca ITU-T X.500:2001 (Directory Service) - ISO/IEC 9594:2001 putem jedinstvene strukture (DIT-Directory Information Tree).
Nazivi subjekata u elektroničkom imeniku (DN) kodiraju se po obrascu ASN.1 i moraju biti izraženi sa sljedećom minimalnom listom atributa:
- ime subjekta u imeniku (fizička, pravna osoba) - CommonName
- naziv organizacijske jedinice - OrganizationalUnitName
- naziv pravne osobe - OrganizationName
- mjesto/adresa - LocalityName
- država - CountryName (Nazivi i oznake u skladu s obrascem ISO 3166-1:1997+Alpha 2).
Sadržaj elektroničkog imenika mora biti izrađen primjenom obrasca kodiranja ISO/IEC 10646 - 1:2000 Universal Multiple Octet Coded Character Set (UCS) - Basic Multiple Plane (BMP), odnosno u skladu s obrascem UTF-8 o okruženju Unix, Linux i srodnih operacijskih sustava.
