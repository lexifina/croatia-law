# Članak 4.
Podaci za izradu elektroničkog potpisa moraju se u potpunosti razlikovati od podataka za ovjeru elektroničkog potpisa.
Postupak izrade elektroničkog potpisa ne smije izmijeniti podatke koji se potpisuju niti spriječiti prikaz tih podataka potpisniku prije čina potpisivanja.
Potpisnik u elektronički potpis ugrađuje osnovne podatke o postupku, algoritmu i sadržaju potpisa kako bi primatelj (korisnik elektroničkog potpisa) mogao ovjeriti potpis temeljem iste ili sukladne tehnologije i postupaka.
Napredni elektronički potpis mora se izrađivati primjenom standardiziranih algoritama iz grupe RSA (rsagen1) odnosno DSA (dsagen1).
Kod izrade naprednog elektroničkog potpisa obvezno se ugrađuje i funkcija kriptiranja sadržaja koji se potpisuje (hash funkcija). Algoritmi koji se primjenjuju u provedbi hash funkcije moraju biti iz skupine SHA-1 (Secure Hash Algorithm) odnosno RIPEMD 160.
