PRILOG 2.
UPUTA
O IZVRŠENJU PRIJENOSA NOVČANIH SREDSTAVA U SVRHU OPSKRBE BANAKA GOTOVIM NOVCEM EURA
Ovom Uputom uređuje se izvršenje prijenosa novčanih sredstava u svrhu opskrbe banaka gotovim novcem, i to:
- način prijenosa novčanih sredstava na račun banke za gotovinu u Hrvatskoj narodnoj banci
- način prijenosa novčanih sredstava s računa banke za gotovinu u Hrvatskoj narodnoj banci na račun banke u sustavu TARGET-HR
- vrste platnih poruka kojima se provode prijenosi novčanih sredstava
- način upisivanja pojedinih elemenata u poruke kojima se provodi prijenos novčanih sredstava u svrhu opskrbe banaka gotovim novcem eura
- postupanje u slučaju tehničkih problema na strani banke.
1. Uvod
Prijenosi novčanih sredstava u svrhu opskrbe banaka gotovim novcem eura provode se preko sustava TARGET-HR u RTGS usluzi. RTGS usluga nudi bruto namiru u realnom vremenu (RTGS) plaćanja velikih vrijednosti na RTGS namjenskim novčanim računima (u nastavku teksta: RTGS DCA).
U RTGS usluzi TARGET-HR namiruju se:
- prijenosi novčanih sredstava s RTGS DCA-a banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci i
- prijenosi novčanih sredstava s računa banke za gotovinu u Hrvatskoj narodnoj banci na njezin RTGS DCA.
Prijenosi novčanih sredstava provode se platnim porukama RTGS pacs.009.001.08 (u nastavku teksta: RTGS pacs.009) koje moraju biti zadane u skladu sa standardima Swifta, odlukom kojom se propisuje rad sustava TARGET-HR i ostalom tehničkom dokumentacijom sustava TARGET.
2. Način zadavanja platnih poruka u svrhu opskrbe banaka gotovim novcem eura
2.1. Prijenos novčanih sredstava s RTGS DCA-a banke na njezin račun za gotovinu u Hrvatskoj narodnoj banci
U svrhu prijenosa novčanih sredstava na račun banke za gotovinu, banka zadaje platnu poruku RTGS pacs.009 na teret svojeg RTGS DCA-a, a u korist RTGS DCA-a Hrvatske narodne banke i u elementu Creditor Account navodi broj svojeg računa za gotovinu u Hrvatskoj narodnoj banci. Platnu poruku RTGS pacs.009 banka upućuje na BIC NBHRHR2XXXX.
Platna poruka RTGS pacs.009 mora sadržavati najmanje sljedeće podatke (uz popunjavanje svih obveznih polja prema pravilima Swifta):
Naziv elementa | XML element | Pravilo korištenja
Credit Transfer Transaction Information
Interbank Settlement Amount | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmAmt | Iznos
Interbank Settlement Date | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmDt | Datum valute
Instructing Agent | /Document/FICdtTrf/CdtTrfTxInf/InstgAgt/FinInstnId/BICFI | BIC banke pošiljatelja vezan uz RTGS DCA banke pošiljatelja
Instructed Agent | /Document/FICdtTrf/CdtTrfTxInf/InstdAgt/FinInstnId/BICFI | BIC HNB-a vezan uz RTGS DCA HNB-a, NBHRHR2XXXX
Debtor Account | /Document/FICdtTrf/CdtTrfTxInf/DbtrAcct/Id/Othr/Id
Račun banke platitelja
Banka upisuje podatak o broju računa u skladu sa svojim potrebama.
Creditor Account | /Document/FICdtTrf/CdtTrfTxInf/CdtrAcct/Id/Othr/Id | Račun banke za gotovinu (vrsta računa 02)
U slučaju uspješne namire banka zaprima poruku RTGS pacs.002.001.10 sa statusom ACSC=namirena ako je na nju pretplaćena. U slučaju neuspješne namire banka zaprima poruku RTGS pacs.002.001.10 sa statusom RJCT=odbačena.
Ako banka pošalje platnu poruku RTGS pacs.009 s pogrešno popunjenim informacijama, Hrvatska narodna banka izvršava povrat pogrešno uplaćenih novčanih sredstava i banci dostavlja platnu poruku RTGS pacs.004.001.09 s kôdom razloga povrata novčanih sredstava.
2.2. Prijenos novčanih sredstava s računa banke za gotovinu u Hrvatskoj narodnoj banci na RTGS DCA banke
Nalog za prijenos novčanih sredstava s računa banke za gotovinu u Hrvatskoj narodnoj banci na RTGS DCA banke banka zadaje u skladu s odlukom kojom se propisuje opskrba banaka gotovim novcem eura.
Ako banka nalog za prijenos novčanih sredstava zadaje porukom CBPR+ pacs.009, poruku šalje na BIC NBHRHR2XXXX. Nalog za prijenos novčanih sredstava porukom CBPR+ pacs.009 banka može zadati do 17:40.
Poruka CBPR+ pacs.009 kojom banka zadaje prijenos novčanih sredstava s računa banke za gotovinu na RTGS DCA mora sadržavati najmanje sljedeće podatke (uz popunjavanje svih obveznih polja prema pravilima Swifta):
Naziv elementa | XML element | Pravilo korištenja
Business Application Header (head.001.001.02)
From | /AppHdr/Fr/FIId/FinInstnId/BICFI | BIC banke pošiljatelja
To | /AppHdr/To/FIId/FinInstnId/BICFI
BIC banke primatelja
BIC HNB-a, NBHRHR2XXXX
Credit Transfer Transaction Information
Interbank Settlement Amount | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmAmt/Ccy | Iznos i oznaka valute /EUR/
Interbank Settlement Date | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmDt | Tekući datum valute
Instructing Agent | /Document/FICdtTrf/CdtTrfTxInf/InstgAgt/FinInstnId/BICFI | BIC banke pošiljatelja
Instructed Agent | /Document/FICdtTrf/CdtTrfTxInf/InstdAgt/FinInstnId/BICFI
BIC banke primatelja
BIC HNB-a, NBHRHR2XXXX
Debtor | /Document/FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI | BIC banke platitelja
Debtor Account | /Document/FICdtTrf/CdtTrfTxInf/ DbtrAcct/Id/Othr/Id
Račun banke platitelja
Račun banke za gotovinu
Creditor | /Document/FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI | BIC banke primatelja
Creditor Account | /Document/FICdtTrf/CdtTrfTxInf/CdtrAcct/Id/Othr/Id | Račun banke primatelja. Banka upisuje podatak o broju računa u skladu sa svojim potrebama.
Ako banka pošalje poruku CBPR+ pacs.009 s pogrešno popunjenim informacijama, Hrvatska narodna banka neće izvršiti prijenos novčanih sredstava u korist RTGS DCA-a banke.
Na temelju zaprimljenog naloga za prijenos Hrvatska narodna banka zadaje platnu poruku RTGS pacs.009 kojom se prenose novčana sredstva u korist RTGS DCA-a banke koja je zadala nalog za prijenos novčanih sredstava.
Platnu poruku RTGS pacs.009 kojom se prenose novčana sredstva u korist RTGS DCA-a banke Hrvatska narodna banka upućuje na BIC banke koja je zadala nalog za prijenos novčanih sredstava.
Platna poruka RTGS pacs.009 kojom Hrvatska narodna banka prenosi novčana sredstva na RTGS DCA banke sadržava sljedeće informacije:
Naziv elementa | XML element | Pravilo korištenja
Credit Transfer Transaction Information
Interbank Settlement Amount | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmAmt | Iznos
Interbank Settlement Date | /Document/FICdtTrf/CdtTrfTxInf/IntrBkSttlmDt | Datum valute
Instructing Agent | /Document/FICdtTrf/CdtTrfTxInf/InstgAgt/FinInstnId/BICFI | BIC banke pošiljatelja, BIC HNB-a, NBHRHR2XXXX
Instructed Agent | /Document/FICdtTrf/CdtTrfTxInf/InstdAgt/FinInstnId/BICFI | BIC banke primatelja vezan uz RTGS DCA banke primatelja
Debtor Account | /Document/FICdtTrf/CdtTrfTxInf/DbtrAcct/Id/Othr/Id
Račun banke platitelja
Račun banke za gotovinu
Creditor Account | /Document/FICdtTrf/CdtTrfTxInf/CdtrAcct/Id/Othr/Id
Račun banke primatelja
Račun koji je banka navela u svojem zahtjevu za prijenos
Nakon uspješne namire platne transakcije banka će zaprimiti platnu poruku RTGS pacs.009.
3. Postupanje u slučaju tehničkih problema na strani banke
Kada banka ne može sama zadati poruku RTGS pacs.009 iz točke 2.1. ove Upute, banka može dostaviti Hrvatskoj narodnoj banci nalog za provođenje platne transakcije u skladu s Uputom za izvanredne situacije u sustavu TARGET2-HR koja je objavljena na internetskoj stranici Hrvatske narodne banke (https://www.hnb.hr/documents/20182/4531865/h-targer-hr_uputa-za-izvanredne-situacije.pdf/738f1b6b-cbeb-b46a-2824-fde4cdbab884?t=1679318115765).
Popunjeni nalog banka dostavlja Hrvatskoj narodnoj banci elektroničkom poštom na adresu: helpdesk.t2hr@hnb.hr.
Hrvatska narodna banka postupit će, ako je moguće, po nalogu banke samo kada banka to ne može sama provesti, odnosno u slučaju tehničkih problema na strani banke.
Nakon što je zaprimila popunjeni nalog, Hrvatska narodna banka telefonski usklađuje vjerodostojnost podataka iz naloga s bankom na sljedeći način:
- Hrvatska narodna banka telefonski zove banku
- banka Hrvatskoj narodnoj banci priopćuje šifru za usuglašenje
- banka čita podatke s naloga koji je dostavljen Hrvatskoj narodnoj banci, a Hrvatska narodna banka uparuje ih s podacima na primljenom nalogu.
Hrvatska narodna banka nastojat će nakon usklađivanja vjerodostojnosti podataka iz naloga, prema objektivnim mogućnostima, provesti takav nalog za plaćanje u najkraćem mogućem roku.
U slučaju tehničkih smetnji u radu sustava TARGET-HR i u slučaju pada sustava TARGET-HR postupa se u skladu s Pravilima rada sustava TARGET-HR.
