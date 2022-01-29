# Pismeni ispit 29.01.2022.

## Zadaci

**NAPOMENA: Svaki zadatak riješiti i spremiti u vlastiti commit, nakon
rješavanja ispita pushati sve na svoj repozitorij**

### 1. Pokrenuti projekt

- kreirati virtualno okruženje
- aktivirati ga
- instalirati potrebne pakete pomoću `requirements.txt` datoteke koja se nalazi
  u `se_labs/ispiti/racunarstvo/20220129a/requirements.txt`
  - podsjetimo se, instalacija paketa radi se iz odgovarajućeg direktorija
    pomoću `pip install -r requirements.txt` naredbe
- pokrenuti aplikaciju
- dodati sliku kao *admin*
  - username: `admin`
  - password: `admin`
- dodati sliku kao *student* (običan user)
  - username: `student`
  - password: `asdfasdf.1A`


### 2. Dodati ime korisnika na index

- Svaka slika povezana je na korisnika pomoću `foreign key` polja u modelu
- Na `index` stranici potrebno je za svaku sliku dodati *username* korisnika
  koji je objavio sliku
- Format crvenog teksta iznad naslova slike treba biti:
  - `Published: DATUM; By: USERNAME; Comments: BROJ_KOMENTARA`


### 3. Obojati grupe korisnika drugačije

- Na `index` stranici treba promijeniti stil teksta za `username` korisnika
  koji je objavio sliku, i to na način:
  - `username` običnog korisnika treba biti crne boje
  - `username` superusera treba biti *bold* i *plave boje*


### 4. Tko vidi Edit i Delete

- Tipke `Edit` i `Delete` na *index* stranici trebaju vidjeti samo korisnik koji
  je objavio sliku i superuser


### 5. Random image

- U navbar dodati tipku `Random` koja će usmjeravati na `/images/random`
- dodati rutu za `/images/random` i usmjeriti ju u *view*
- View treba uzeti random sliku iz baze i napraviti `HttpResponseRedirect` na tu
  sliku
- random sliku iz baze možete najlakše povući sa: 
  - `image = random.choice( Image.objects.all() )`


