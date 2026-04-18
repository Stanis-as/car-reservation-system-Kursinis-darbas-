import os
from abc import ABC, abstractmethod

class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
        self._reservations = []

    def check_login(self, email, password):
        return self._email == email and self._password == password

    def reserve(self, vehicle, days):
        reservation = Reservation(self, vehicle, days)
        self._reservations.append(reservation)
        return reservation

    def show_reservations(self):
        print("\n=== MY RESERVATIONS ===")
        print("-" * 45)

        if not self._reservations:
            print("No reservations")
            return

        for r in self._reservations:
            print(f"{r.vehicle.get_info():<20} | {r.days} days | {r.total}€")

        print("-" * 45)

    def get_name(self):
        return self._name

class Vehicle(ABC):
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price

    @abstractmethod
    def get_price(self, days):
        pass

    def get_info(self):
        return f"{self._brand} {self._model}"


class Car(Vehicle):
    def get_price(self, days):
        return self._price * days


class LuxuryCar(Vehicle):
    def get_price(self, days):
        total = self._price * days
        if days >= 3:
            total *= 0.9
        return total

class Reservation:
    def __init__(self, user, vehicle, days):
        self.user = user
        self.vehicle = vehicle
        self.days = days
        self.total = vehicle.get_price(days)

class System:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = []
            cls._instance.vehicles = []
            cls._instance.reservations = []
        return cls._instance

    def register(self, name, email, password):
        self.users.append(User(name, email, password))
        print("!!!Registered successfully!!!")

    def login(self, email, password):
        for u in self.users:
            if u.check_login(email, password):
                print("!!!Login successful!!!")
                return u
        print("!!!Wrong login!!!")
        return None

    def add_vehicle(self, v):
        self.vehicles.append(v)

    def show_vehicles(self):
        print("\n=== AVAILABLE CARS ===")
        print("-" * 40)

        for i, v in enumerate(self.vehicles, start=1):
            print(f"{i}. {v.get_info():<20}")

        print("-" * 40)

    def save(self):
        path = os.path.join(os.path.dirname(__file__), "data.txt")

        with open(path, "w") as f:
            if not self.reservations:
                f.write("No reservations\n")
            else:
                for r in self.reservations:
                    f.write(f"{r.user.get_name()},{r.vehicle.get_info()},{r.days},{r.total}\n")

        print(f"FILE Saved to: {path}")

system = System()

# Cars
system.add_vehicle(Car("BMW", "320", 50))
system.add_vehicle(LuxuryCar("Mercedes", "S", 120))
system.add_vehicle(Car("Toyota", "Corolla", 45))
system.add_vehicle(Car("Toyota", "Prius", 54))
system.add_vehicle(LuxuryCar("BMW", "X5", 75))
system.add_vehicle(LuxuryCar("Audi", "A8", 110))

current_user = None

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 35)
    print("CAR RENTAL SYSTEM")
    print("=" * 35)
    print("1. Register")
    print("2. Login")
    print("3. Show cars")
    print("4. Rent car")
    print("5. My reservations")
    print("6. Save")
    print("7. Exit")
    print("=" * 35)

    c = input("Choose: ")

    if c == "1":
        system.register(input("Name: "), input("Email: "), input("Pass: "))
        input("Press Enter...")

    elif c == "2":
        current_user = system.login(input("Email: "), input("Pass: "))
        input("Press Enter...")

    elif c == "3":
        system.show_vehicles()
        input("Press Enter...")

    elif c == "4":
        if current_user:
            system.show_vehicles()
            i = int(input("Choose car: ")) - 1
            d = int(input("Days: "))
            r = current_user.reserve(system.vehicles[i], d)
            system.reservations.append(r)
            print(f"Reserved! Total: {r.total}€")
        else:
            print("!!!Login first!!!")
        input("Press Enter...")

    elif c == "5":  
        if current_user:
            current_user.show_reservations()
        else:
            print("!!!Login first!!!")
        input("Press Enter...")

    elif c == "6":
        system.save()
        input("Press Enter...")

    elif c == "7":
        break
