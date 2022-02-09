# Pismeni ispit 29.01.2022.


## NAPOMENE

### Pazite na `git config`, postavite svoje ime i email prije commitanja

- Svaki zadatak riješiti i spremiti u vlastiti commit, nakon
rješavanja ispita pushati sve na svoj repozitorij

- Ne miješati fileove različitih zadataka u isti commit. U commitu za pojedini
  zadatak trebaju biti samo oni fileovi koji direktno utječu na taj zadatak.

- U slučaju greške pri commitu, napraviti novi commit s ispravkom i nazvati ga
  "Fix za N. zadatak", gdje je N broj zadatka za koji se radi ispravak

- U commitovima ignorirati virtual environment i pycache fileove.



## Zadaci

### 1. Pokrenuti projekt (3boda)

- kreirati virtualno okruženje
- aktivirati ga
- instalirati potrebne pakete pomoću `requirements.txt` datoteke koja se nalazi
  u `se_labs/ispiti/racunarstvo/20220209/requirements.txt`
  - podsjetimo se, instalacija paketa radi se iz odgovarajućeg direktorija
    pomoću `pip install -r requirements.txt` naredbe
- pokrenuti aplikaciju
- dodati sliku kao *admin*
  - username: `admin`
  - password: `admin`
- dodati sliku kao *student* (običan user)
  - username: `student`
  - password: `asdfasdf.1A`


### 2. Premjestiti image metadata (3boda) 

- Izmjeniti izgleda podataka o pojedinom imageu na index stranici da bude kao
  na slici:

![slika](https://imgur.com/vtEraDy.png)


### 3. Prebaciti 'Submit new image' u navbar (4 boda)

- Na `index` stranici treba maknuti 'Submit new image' link i treba ga
  prebaciti u navigaciju s lijeve strane, pored 'Home'

### 4. Promijeni boju za naziv slike za superusera (4 boda)

- Na oba pagea (i na `index` i na `detail`) potrebno je staviti naslov slike u 
   `#ffa801` boji, ako je sliku objavio superuser, a ostaviti kakva je ako ju
    je objavio običan user
- Koristiti css klase

### 5. Dodaj 'Moje slike' stranicu (6 bodova)

- Dodati u navigaciju pored tipke za Logout link 'My images'
- Link će voditi na novi view koji treba prikazati sve slike ulogiranog
  korisnika
  - potrebno je postaviti novu rutu za usmjeravanje u view
  - nije potrebno kreirati novi template, možete jednostavno renderirati index
    template, ali je potrebno uzeti slike samo od ulogiranog korisnika
- Ako nije ulogiran korisnik, 'My images' link se ne prikazuje


