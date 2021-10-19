# Survival Game

## Opis igre

Survival game je 2D top-down shooter igra. 
Igrač se kreće po mapi i izbjegava čudovišta koja trče na njega. Igrač ima dva
oružja kojima ubija čudovišta. Čudovišta igrača napadaju u valovima (waves), u
svakom valu ima više čudovišta i imaju više healtha. Čudovišta oštećuju igrača
kada su u dodiru s njim i smanjuju mu health. Cilj igre je preživjeti što više
valova bez umiranja. Čudovišta dolaze izvan ekrana iz svih smjerova. Sva
čudovišta ne ulaze u ekran odjednom. 

Primjer slične igre je na linku: https://youtu.be/C6xqqz4WEn4?t=1540 (od
25:40). Dozvoljeno je koristiti iste slike koje su korištene u tom tutorijalu,
ali je preporuka naći svoje slike. Nije potrebno implementirati zvučne efekte,
ali je dozvoljeno.

Igra se sastoji od mape svijeta koja je cijela prikazana na ekranu (nema
scrollanja ekrana dok se igrač kreće).  Kada igrač umre, igra je gotova i pamti
se njegov score (broj vala na kojem je igrač poginuo). 

## Persone

### Igrač

Igrača upravlja korisnik preko miša i tipkovnice. Igrač želi preživjeti napade
čudovišta, za što koristi dva oružja za ubijanje čudovišta. Lijeva tipka miša
aktivira primarno oružje (pištolj ili puška) iz kojeg se metci ispucavaju u
smjeru gdje je igrač okrenut. Igrač se tipkama WASD kreće kroz svijet, bez
obzira u kojem smjeru je okrenut. Na lokaciji miša iscrtava se nišan. Desna
tipka miša aktivira bacanje granate. Granata pri aktivaciji leti od igrača do
mjesta gdje je bio nišan u trenutku aktivacije. Pri dolasku na to mjesto
granata eksplodira i radi štetu svima u određenom radiusu (uključujući i
igrača).  

### Čudovište

Čudovište želi ubiti igrača i trči na njega kroz svijet. Kada je u kontaktu s
igračem, čudovište nanosi štetu igraču. Čudovište ima Health i kada ga igrač
dovoljno ošteti svojim napadima, čudovište umire.


## Ekrani

Osnovni ekrani koji se koriste kroz igru:

- START ekran - ekran koji se otvara kada se igra pokrene. Sadrži izbornik s
  tipkama za start nove igre, za pregledavanje highscorea, te za izlaz.
- GAME ekran - ekran u kojem se odvija igra. Prikazuje health igrača, broj
  čudovišta u valu i cooldown granate.
- HIGHSCORE ekran - ekran u kojem se prikazuju ostvareni rezultati.

Pojedini ekran može imati više stanja.

## Tehnička ograničenja

- Dozvoljeno je koristiti klase iz laboratorijskih vježbi. U nekim slučajevima
  klasa na LV može imati drugo ime (recimo klasa Level iz LV bi se ovdje
  logičnije zvala Wave)
- Koristi se pygame, klase su razdvojene u različite datoteke kao na LV.

## Gameplay ograničenja

- Potrebno je optimizirati parametre brzine kretanja entiteta u
  igri tako da igra bude igriva (brzina kretanja igrača, brzina metka, brzina
  čudovišta, brzina leta granate, cooldown primarnog oružja, cooldown granate)
- Valovi napada čudovišta trebaju biti progresivno teži sa svakim novim valom.
- Brzine kretanja igrača i čudovišta se ne mijenjaju kroz valove, ali se
  mijenja broj čudovišta, njihov health i brzina udaraca igrača kada su u
  kontaktu.
- Kada je čudovište pogođeno primarnim oružjem, postoji animacija da je
  pogođeno. 


# User stories

[Više o Epic user stories](https://www.agilealliance.org/glossary/epic)

Svaki Epic user story podjeljen je u više user storyja, kojima su definirane
funkcionalnosti aplikacije iz perspektive pojedine persone. Svaki User story
ima definiran acceptance criteria koji potvrđuje ispunjavanje tog User storija.
Epic user story je ispunjen kada su ispunjeni svi acceptance kriteriji svih
storija unutra tog Epica. U slučaju kada je sam story jasno definiran, može se
preskočiti acceptance criteria. Primjer: Kao igrač, kada me čudovište ubije,
prikazuje mi se START ekran.

NAPOMENA: Neki user storiji imaju i polje Need. U tom polju su eksplicitno navedeni
zahtjevi za funkcionalnost koji se ne mogu zaključiti iz teksta storyja. Tamo
gdje nema polja Need, potrebni resursi za ispunjenje storyja mogu se
zdravo-razumski zaključiti. 

## Epic 1: Ekrani

- S1.1
  Kao igrač, kada pokrenem igru, trebam moći pokrenuti GAME ekran, pogledati
  highscoreove ili izaći iz igre

  Acceptance criteria:
  - klik na START GAME pokreće igru
  - klik na HIGHSCORE prikazuje ekran sa high scoreovima
  - klik na EXIT zatvara igru

- S1.2
  Kao igrač, kada sam na GAME ekranu, trebam moći izići iz aktivne igre
  pritiskom ESC tipke

  Acceptance criteria:
  - pritisak ESC na tipkovnici vraća igrača na START ekran

- S1.3
  Kao igrač, kada sam na HIGHSCORE ekranu, trebam moći izići iz ekrana
  pritiskom ESC tipke

  Acceptance criteria:
  - pritisak ESC na tipkovnici vraća igrača na START ekran

## Epic 2: Igrač i neprijatelji (GAME ekran)

- S2.1
  Kao igrač, kada sam u aktivnoj igri, trebam moći pomicati ikonu igrača po
  ekranu korištenjem WASD tipaka

  Acceptance criteria:
  - W pomiče igrača gore za proizvoljno određeni broj piksela
  - A pomiče igrača lijevo za proizvoljno određeni broj piksela
  - S pomiče igrača dolje za proizvoljno određeni broj piksela
  - D pomiče igrača desno za proizvoljno određeni broj piksela

- S2.2
  Kao igrač, kada sam u aktivnoj igri, trebam moći pucati iz primarnog oružja

  Acceptance criteria:
  - Lijevi klik miša ispaljuje metak sa lokacije igrača prema lokaciji miša

- S2.3
  Kao igrač, kada sam u aktivnoj igri, trebam vidjeti nišan na lokaciji miša

  Acceptance criteria:
  - Ikonica nišana (proizvoljno odabrana) iscrtava se na ekranu na lokaciji
    miša

- S2.4
  Kao igrač, kada ispalim metak, metak treba nestati kad iziđe izvan okvira
  ekrana

  Acceptance criteria:
  - Metak se briše iz liste metaka

- S2.5
  Kao igrač, kada sam u aktivnoj igri, neprijatelji se kreću prema meni

  Acceptance criteria:
  - čudovišta se stvore na random lokacijama
  - čudovišta se kreću prema igraču

- S2.6
  Kao igrač, kada sam u aktivnoj igri, trebam moći pucati na čudovišta,
  oštetiti ih i ubiti

  Acceptance criteria:
  - Kada metak pogodi čudovište, nestaje i oštećuje čudovište
  - Čudovište umire kada mu je health <= 0
  - Čudovište se briše iz liste neprijatelja nakon što je ubijeno

- S2.7
  Kao igrač, kada sam u aktivnoj igri, čudovišta se stvaraju izvan ekrana i
  kreću se prema meni  

  Acceptance criteria:
  - Sva čudovišta nisu vidljiva odjednom na početku igre
  - Sva čudovišta eventualno uđu u ekran

  Napomena: Ako se čudovištima postave slučajne koordinate na kojima se
  stvaraju na koordinatama daleko od igrača, budući da se kreću prema igraču u
  nekom trenutku će ući u ekran. 

- S2.8
  Kao igrač, kada sam u aktivnoj igri, čudovište me može oštetiti i ubiti kada
  mi se približi

  Acceptance criteria:
  - Čudovište umanjuje health igrača nakon što dođe do njega
  - Igrač umire ako mu health padne na 0 ili manje

- S2.9
  Kao igrač, kada me čudovište ubije, trebam se vratiti na START ekran 

- S2.10
  Kao igrač, kada pogodim čudovište, trebam vidjeti animaciju da je metak
  pogodio čudovište

- S2.11
  Kao igrač, kada čudovište ošteti mene, trebam vidjeti animaciju da me je
  oštetilo


## Epic 3: GAME UI

- S3.1
  Kao igrač, želim vidjeti koliko čudovišta ima u igri i koliko sam ih ubio

  Acceptance criteria:
  - Broj čudovišta prikazan je na ekranu u formatu (BROJ_UBIJEN/UKUPAN_BROJ)

- S3.2
  Kao igrač, želim vidjeti koliko healtha imam

## Epic 4: Waves

- S3.1
  Kao igrač, čudovišta me trebaju napadati u valovima

  Acceptance criteria:
  - kada igrač ubije sva čudovišta, pokreće se novi val sa više čudovišta
  - sa svakim valom čudovištima raste health i brzina udaranja igrača
  - nema ograničenja na broj valova

- S3.2 
  Kao igrač, želim vidjeti na kojem sam trenutno valu

  Acceptance criteria:
  - Na ekranu je ispisano na kojem je igrač trenutno valu

- S3.3 
  Kao igrač, želim da između valova bude odbrojavanje od 3 sekunde

- S3.4
  Kao igrač, kada me čudovišta ubiju, moj rezultat se treba upisati u
  HIGHSCORES i treba biti dostupan i nakon restarta igre

  Acceptance criteria:
  - Nakon što čudovišta ubiju igrača, treba mu se prikazati START ekran
  - Kada ode na HIGHSCORE ekran, treba mu se prikazati rezultat ostvaren u 
    zadnjem igranju u formatu (TIMESTAMP - Wave BROJ_VALA)
  - Rezultat treba ostati vidljiv u  HIGHSCORES i nakon restarta igre

  Note: Snimanje highscoreova može se obaviti u datoteku, pri otvaranju
  HIGHSCORE ekrana rezultati se mogu pročitati iz datoteke


## Epic 4: Granate

- S4.1 
  Kao igrač, tijekom igre trebam moći baciti granatu lijevim klikom miša

  Acceptance criteria:
  - Klik na lijevu tipku miša baca granatu na mjesto gdje se nalazi pokazivač
    miša
  - Granata putuje sporije od metka
  - Kada dođe na mjesto gdje je bio pokazivač, eksplodira (animacija)

- S4.2
  Kao igrač, kada bacim granatu i ona eksplodira, treba oštetiti čudovišta u
  određenom radijusu

  Acceptance criteria:
  - Eksplozija granate smanjuje health čudovištima u radijusu eksplozije
  
- S4.3
  Kao igrač, kada bacim granatu i ona eksplodira, treba oštetiti i mene ako sam u
  radijusu eksplozije

  Acceptance criteria:
  - Eksplozija granate smanjuje health igrača ako je u radijusu eksplozije

  
  

  
