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

### 1. Pokrenuti projekt (2 boda)

- Preuzeti promjene sa repozitorija i spojiti ih u svoj repozitorij
- Pokrenuti igru
- Promjeniti boju svih tekstova u igri u narančastu


### 2. Brzina metaka (3 boda)

- Promjeniti brzinu metaka koje ispali Turret na 4, a onih koje ispali igrač na
  8

### 3. Brzina asteroida (4 boda)

- Pri kreiranju asteroida potrebno im je postaviti slučajnu brzinu između 1 i 4


### 4. Teleport (4 boda)

- Izmjeniti kod za teleportiranje igrača tako da više nema cooldowna, igrač se
  može teleportirati odmah bez čekanja, ali ima ukupno 3 teleportiranja po
  levelu. (2 boda)
- Umjesto cooldown timera staviti tekst koliko je igraču preostalo
  teleportiranja. (2 boda)

### 5. Freeze time (7 bodova)

- Dok igrač drži pritisnutu tipku T, svi asteroidi miruju. (3 boda)
- Kad igrač otpusti tipku T, asteroidima se vraćaju brzine koje su imali prije zamrzavanja. (4 boda)


