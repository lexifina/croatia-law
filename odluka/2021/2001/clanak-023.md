# Članak 23.
U poglavlju 4.3. STRtočka 20. mijenja se i glasi:
»4.3. ER3
20. Pregled pogrešaka nastalih na osnovi vertikalnih kontrola za određeni datum/oznaku izvješća. Kreira se nakon svake obrade. Datoteka ER3 odnosi se na vertikalne kontrole (tip »VW« - Vertical Warning).«
Iza točke 20. dodaje se novo poglavlje 4.4. STR, a točka 21. mijenja se i glasi:
»4.4. STR
21. Datoteka STR, slogovi za storniranje, kreira se iz slogova koji imaju samo pogreške tipa warning (W) pa su prihvaćeni kao ispravni, sadržajem je ista kao ulazni slog sa separatorima (#) polja, s iznimkom podatka o identifikatoru protustranke koji je maskiran, a na kraju je sloga šifra pogreške; datoteka sadržava informaciju o vremenu zaprimanja i obrade poslanih podataka.«
Iza točke 21. dodaje se nova točka 22. i glasi:
»22. Napomena: to je predložak u kojem treba promijeniti sadržaj polja 3 u »S« i predznak u suprotni od originala te uz to kreirati novi, ispravni slog s oznakom »P«.
Primjer:
Obrada podataka banke 12345678 zaprimljenih 21.01.2020. 10:28:42 počela je 21.01.2020. 10:39:38.
Popis redaka za storniranje:
MK#20191231#R#00056798#FZ#***********#HR#21#10008 #20190325#20190501#20291001#A0232#HRK#N000#F1000#NRS03#EUR#A1#01#18#+#000000023000000#A#01#01#01#01#02#02#NE#03#XXX#HR#335576#HR#335568#674W#
Obrada podataka završila 21.01.2020. 10:46:30«
