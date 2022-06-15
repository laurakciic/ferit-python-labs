# Pismeni ispit 15.06.2022.


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

### 1. Pokrenuti projekt (2boda)

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
- dodati bazu (db.sqlite3) u commit

### 2. Premjestiti image metadata (2boda) 

- Izmjeniti izgled podataka o pojedinom imageu na index stranici da bude kao
  na slici:

![slika](https://imgur.com/vtEraDy.png)


### 3. Prebaciti 'Submit new image' u navbar (2 boda)

- Na `index` stranici treba maknuti 'Submit new image' link i treba ga
  prebaciti u navigaciju s lijeve strane, pored 'Home'


### 4. Random image (4 boda)

- U navbar dodati tipku `Random` koja će usmjeravati na `/images/random`
- dodati rutu za `/images/random` i usmjeriti ju u *view*
- View treba uzeti random sliku iz baze i napraviti `HttpResponseRedirect` na tu
  sliku
- random sliku iz baze možete najlakše povući sa: 
  - `image = random.choice( Image.objects.all() )`


### 5. Dodaj cijenu na pojedinu sliku (3 boda)

- Omogući dodavanje cijene za svaku sliku
- Cijenu je dozvoljeno dodati u adminu, nije potrebno sučelje za cijenu
- Prikaži cijenu slike u zagradi nakon naslova slike na svim stranicama gdje se prikazuju slike


### 6. Dodaj mogućnost kupovine slike (7 bodova)

- Nije potrebno stvarno omogućiti kupovinu slike već samo postaviti vizualne elemente potrebne za tu funkcionalnost:
  - Dodaj tipku "Kupi sliku (CIJENA)" na svako mjesto gdje se na stranici pojavljuje slika
  - Klik na kupi sliku vodi na novu stranicu sličnu `detail` stranici, koja osim podataka o slici ima i formu za unos podataka o kupcu (ime, prezime adresa), te tipku KUPI
  - Klik na tipku kupi okida POST request na novi view koji redirecta na novu stranicu na kojoj samo piše tekst: vaša narudžba je uspješno obavljena i link za vraćanje na homepage.
  - Nije potrebno spremati u bazu detalje o narudžbi


