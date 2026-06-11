# Car Reservation System

🇱🇹 Lietuviška versija: [README_LT.md](README_LT.md)

A Python-based car rental application built as an OOP course project.

---

## 1. Overview

### About
This application allows users to register, log in, browse available vehicles, and make reservations. Reservation data is persisted to a text file between sessions.

### How to run
1. Make sure **Python 3.x** is installed
2. Download all files into the same folder
3. Run in terminal:
```bash
python Car_reservation.py
```

### How to use
- **Register** (1) and **log in** (2)
- Browse available vehicles (3)
- Reserve a vehicle (4) and specify the number of days
- Save your data (6) — written to `data.txt`
- View saved reservations (7)

---

## 2. OOP Design

### Encapsulation
Class data is hidden using protected attributes prefixed with `_`, preventing direct external access.

```python
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
```

### Inheritance
`Car` and `LuxuryCar` both inherit from the `Vehicle` base class, reusing its attributes and methods.

```python
class Car(Vehicle):
    def get_price(self, days):
        return self._price * days
```

### Abstraction
`Vehicle` is an abstract base class. It defines the `get_price()` interface without implementing it, delegating the logic to each subclass.

```python
class Vehicle(ABC):
    @abstractmethod
    def get_price(self, days):
        pass
```

### Polymorphism
The same `get_price()` method behaves differently depending on the class:
- `Car` — price × days
- `LuxuryCar` — same formula with a 10% discount applied for bookings of 3+ days

```python
class LuxuryCar(Vehicle):
    def get_price(self, days):
        total = self._price * days
        if days >= 3:
            total = total * 0.9
        return total
```

---

## 3. Design Pattern — Singleton

The `System` class uses the Singleton pattern, ensuring only one instance exists throughout the application's lifetime. This guarantees a single shared state for users, vehicles, and reservations.

```python
class System:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = []
            cls._instance.vehicles = []
            cls._instance.reservations = []
        return cls._instance
```

---

## 4. Composition and Aggregation

- **Composition** — a `Reservation` object depends on both a `User` and a `Vehicle` to calculate the total price; it cannot exist independently.
- **Aggregation** — the `System` holds lists of `users` and `vehicles`, but these objects can exist independently of the system.

---

## 5. File Persistence

Data is saved to `data.txt` and can be loaded back on the next run.

Saved fields: username, vehicle name, number of days, total price.

---

## 6. Testing

Unit tests are written with Python's `unittest` framework and cover all core business logic:

1. Login with valid and invalid credentials
2. `Car` price calculation
3. `LuxuryCar` discount logic
4. Reservation creation
5. Singleton pattern behaviour

```bash
python -m unittest test_system.py
```

---

## 7. Results

- Full rental workflow functional: registration, login, booking, and file persistence
- Singleton pattern enforces a single shared system state
- All `unittest` tests pass

### Potential future improvements
- Replace file storage with a database
- Add password hashing
- Implement an admin role
- Apply an additional design pattern

---

## 8. References
- Python documentation — https://docs.python.org
- unittest documentation — https://docs.python.org/3/library/unittest.html
- Course lecture materials
