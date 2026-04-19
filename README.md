# Car Reservation System

Tai Python kalba parašyta automobilių nuomos programa, sukurta kaip objektinio programavimo (OOP) kursinis darbas. Programa leidžia vartotojams registruotis, prisijungti, peržiūrėti automobilius bei atlikti jų rezervaciją, išsaugant duomenis faile.

---

## 1. Įvadas (Introduction)

### Projekto tikslas
Sukurti veikiančią automobilių nuomos valdymo sistemą, kuri pademonstruotų keturis pagrindinius OOP polarius, projektavimo šablonų naudojimą bei duomenų valdymą išoriniuose failuose.

### Kaip paleisti programą?
1. Įsitikinkite, kad kompiuteryje įdiegtas **Python 3.x**.
2. Atsisiųskite projekto failus į vieną aplanką.
3. Atidarykite terminalą tame aplanke ir paleiskite:
   ```bash
   python Car_reservation.py
   ```
### Kaip naudotis programa?
1. Registracija/Prisijungimas: Norėdami rezervuoti automobilį, pirmiausia turite užsiregistruoti (1) ir prisijungti (2).
2. Peržiūra: Galite peržiūreti visų galimų automobilių sąrašą (3).
3. Rezervacija: Prisijungę pasirinkite "Rent Car" (4), nurodykite automobilio numerį ir nuomos dienų skaičių.
4. Išsaugojimas: Pasirinkus "save" (6), visis rezervacijų duomenys bus įrašyti į `data.txt` failą.

## 2. Analizė ir Įgyvendinimas (Body/Analysis)

### 1. **Enkapsuliacija (Encapsulation)**
Reikšmė: Duomenų slėpimas klasės viduje, apsaugant juos nuo tiesioginio pasiekiamumo iš išorės.
   ```python
   class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
   ```
### 2. **Paveldėjimas (Inheritance)**
Reikšmė: Galimybė kurti naujas klases esamų klasių pagrindu, perimant jų savybes ir metodus.
 ```python
   class Car(Vehicle):
    def get_price(self, days):
        return self._price * days
```
### 3. **Abstrakcija (Abstraction)**
Reikšmė: Sudėtingos detalės paslepiamos apibrėžiant tik bendrą metodų struktūrą per abstrakčias klases.
 ```python
   class Vehicle(ABC):
    @abstractmethod
    def get_price(self, days):
        pass
```
### 4. **Polimorfizmas (Polymorphism)**
 Reikšmė: Skirtingos klasės gali turėti tą patį metodą, tačiau jį įgyvendinti skirtingai.

 Šiame projekte metodas `get_price()` realizuojamas skirtingai:

- `Car` klasėje kaina skaičiuojama paprastai (kaina × dienos)
- `LuxuryCar` klasėje taikoma 10% nuolaida, jei nuoma trunka 3 dienas ar ilgiau

Tai leidžia naudoti tą patį metodą skirtingiems objektams, nekeičiat programos logikos.

### **Projektavimo šablonas (Design Pattern)**
Projekte panaudotas Singleton (Vienis) šablonas klasėje `System`.
1. **Kodėl šis šablonas?** Sistemoje turi egzistuoti tik vienas centralizuotas objektas, atsakingas už vartotojų sąrašą, automobilių parką ir rezervacijas. Singleton užtikrina, kad visoje programoje veiktų tas pats duomenų srautas.
2. **Veikimas:** Perrašius `__new__` metodą, užtikrinama, kad sukūrus naują `System()` objektą, bus grąžinta ta pati jau egzistuojanti egzemplioriaus nuoroda.

### **Kompozicija ir Agregacija**
1. **Kompozicija:** `Reservation` objektas turi `Vehicle` ir `User` objektus. Rezervacija yra tiesiogiai priklausoma nuo šių dalių, kad apskaičiuotų galutinę kainą (total).
2. **Agregacija:** `System` klasė turi `users` ir `vehicles` sąrašus. Tai yra agregacija, nes automobiliai ir vartotojai gali egzistuoti nepriklausomai nuo pačios sistemos veikimo loginės sesijos.

### **Darbas su failais (File Handling)**
Programa naudoja Python funkcijas darbui su failais.
1. Duomenys rašomi į `data.txt`.
2. Išsaugoma: Vartotojo vardas, automobilis, nuomos trukmė ir bendra suma.

### Testavimas (Testing)
Programoje buvo naudojamas testavimas su Python standartine biblioteka `unittest`, siekiant patikrinti pagrindinį funkcionalumą ir užtikrinti programos patikimumą.

Testavimo metu buvo tikrinamos svarbiausios sistemos dalys:

1. **Prisijungimo funkcionalumas**  
Patikrinama, ar vartotojas gali sėkmingai prisijungti su teisingais duomenimis ir ar sistema atmeta neteisingus prisijungimus.

2. **Kainos skaičiavimas (Polimorfizmas)**  
   Testuojama, ar skirtingų klasių (`Car` ir `LuxuryCar`) metodas `get_price()` veikia teisingai:
   - `Car` klasėje kaina skaičiuojama paprastai (kaina × dienos)
   - `LuxuryCar` klasėje taikoma nuolaida, jei dienų skaičius ≥ 3

3. **Rezervacijos sukūrimas**  
   Tikrinama, ar sukuriant rezervaciją teisingai apskaičiuojama bendra kaina ir ar rezervacija priskiriama vartotojui.

4. **Singleton šablono veikimas**  
   Patikrinama, ar sukūrus kelis `System` objektus, jie visi nurodo į tą patį egzempliorių.


Testai buvo vykdomi naudojant komandą:

```bash
python -m unittest test_system.py
```
## 3. Results and Summary

### Results
- Programa sėkmingai įgyvendina automobilių nuomos funkcionalumą: vartotojai gali registruotis, prisijungti ir rezervuoti automobilius.
- Kilo problemų su failų išsaugojimu ir teisingo kelio (path) nustatymu.
- Įgyvendintas Singleton projektavimo šablonas, kuris užtikrina vieną sistemos instanciją.
- Testavimo metu teko koreguoti kai kurias funkcijas, kad jos veiktų stabiliai.
- Sukurti ir paleisti vienetiniai testai, kurie patvirtina pagrindinių funkcijų teisingą veikimą.

### Conclusions
Šio darbo metu buvo sukurta veikianti automobilių nuomos sistema, pritaikant objektinio programavimo principus praktikoje.

Buvo sėkmingai įgyvendinti visi keturi OOP principai: enkapsuliacija, paveldėjimas, abstrakcija ir polimorfizmas. Taip pat pritaikytas Singleton projektavimo šablonas.

Programa leidžia vartotojams registruotis, prisijungti, rezervuoti automobilius ir išsaugoti duomenis faile.

Papildomai buvo įgyvendintas testavimas naudojant `unittest`, kuris padėjo patikrinti pagrindinių funkcijų veikimą. 

Ateityje šią sistemą būtų galima tobulinti:
- naudojant duomenų bazę vietoje tekstinio failo
- įdiegiant saugesnį slaptažodžių saugojimą
- pridedant daugiau funkcionalumo, pvz., administratoriaus valdymo sistemą

## 4. References

- Python Documentation
- unittest documentation
- Lecture materials
