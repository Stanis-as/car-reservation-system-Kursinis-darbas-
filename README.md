# Car Reservation System

Automobilių nuomos programa parašyta Python kalba kaip OOP kursinis darbas.

---

## 1. Įvadas

### Apie programą
Ši programa leidžia vartotojams registruotis, prisijungti, peržiūrėti automobilius ir juos rezervuoti. Rezervacijų duomenys išsaugomi į tekstinį failą.

### Kaip paleisti?
1. Įsitikinkite kad įdiegtas **Python 3.x**
2. Atsisiųskite failus į vieną aplanką
3. Terminale paleiskite:
```bash
python Car_reservation.py
```

### Kaip naudotis?
- Pirmiausia **užsiregistruokite** (1) ir **prisijunkite** (2)
- Peržiūrėkite automobilius (3)
- Rezervuokite pasirinktą automobilį (4) ir nurodykite dienų skaičių
- Išsaugokite duomenis (6) — jie bus įrašyti į `data.txt`
- Galite peržiūrėti išsaugotus duomenis pasirinkę (7)

---

## 2. OOP Principų Įgyvendinimas

### Enkapsuliacija
Duomenys slepiami klasės viduje naudojant apsaugotus atributus su `_` ženklu. Tiesiogiai iš išorės jų pasiekti negalima.

```python
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
```

### Paveldėjimas
`Car` ir `LuxuryCar` klasės paveldi iš `Vehicle` klasės — perima jos atributus ir metodus.

```python
class Car(Vehicle):
    def get_price(self, days):
        return self._price * days
```

### Abstrakcija
`Vehicle` yra abstrakti klasė. Ji apibrėžia metodą `get_price()` bet neįgyvendina jo — tai palieka klasėms `Car` ir `LuxuryCar`.

```python
class Vehicle(ABC):
    @abstractmethod
    def get_price(self, days):
        pass
```

### Polimorfizmas
Tas pats metodas `get_price()` veikia skirtingai priklausomai nuo klasės:
- `Car` — kaina × dienos
- `LuxuryCar` — ta pati formulė bet su 10% nuolaida nuo 3 dienų

```python
class LuxuryCar(Vehicle):
    def get_price(self, days):
        total = self._price * days
        if days >= 3:
            total = total * 0.9
        return total
```

---

### Projektavimo Šablonas — Singleton
`System` klasė naudoja Singleton šabloną. Tai reiškia kad visoje programoje egzistuoja tik vienas `System` objektas su visais duomenimis.

```python
class System:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Šis šablonas tinkamas nes sistema turi turėti vieną bendrą vartotojų, automobilių ir rezervacijų sąrašą.

---

### Kompozicija ir Agregacija
- **Kompozicija** — `Reservation` objektas negali egzistuoti be `User` ir `Vehicle`. Jis juos naudoja kainai apskaičiuoti.
- **Agregacija** — `System` laiko `users` ir `vehicles` sąrašus, tačiau šie objektai gali egzistuoti nepriklausomai.

---

### Darbas su Failais
Duomenys išsaugomi į `data.txt` failą ir gali būti vėliau nuskaitomi atgal.

Išsaugoma: vartotojo vardas, automobilis, dienų skaičius, bendra suma.

---

### Testavimas
Naudojamas `unittest` framework'as. Testuojamos pagrindinės funkcijos:

1. Prisijungimas su teisingais ir neteisingais duomenimis
2. `Car` kainos skaičiavimas
3. `LuxuryCar` nuolaidos skaičiavimas
4. Rezervacijos sukūrimas
5. Singleton šablono veikimas

```bash
python -m unittest test_system.py
```

---

## 3. Rezultatai ir Išvados

### Rezultatai
- Programa veikia — vartotojai gali registruotis, prisijungti ir rezervuoti automobilius
- Singleton šablonas užtikrina vieną sistemos instanciją per visą programos veikimą
- Failų skaitymas ir rašymas veikia su `data.txt`
- Visi `unittest` testai sėkmingai praeina

### Išvados
Kursiniam darbui pavyko sukurti veikiančią automobilių nuomos sistemą naudojant OOP principus. Įgyvendinti visi keturi principai, Singleton šablonas ir failų valdymas.

Ateityje sistemą būtų galima patobulinti:
- Naudoti duomenų bazę vietoje tekstinio failo
- Pridėti slaptažodžių šifravimą
- Sukurti administratoriaus funkciją
- Panauduoti dar viena Projektavimo šablona

---

## 4. Šaltiniai
- Python dokumentacija — https://docs.python.org
- unittest dokumentacija — https://docs.python.org/3/library/unittest.html
- Paskaitų medžiaga
