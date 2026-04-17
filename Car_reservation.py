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
        for r in self._reservations:
            print(f"{r.vehicle.get_info()} | {r.days} days | {r.total}€")

from abc import ABC, abstractmethod

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
        print("Registered")

    def login(self, email, password):
        for u in self.users:
            if u.check_login(email, password):
                print("Login success")
                return u
        print("Wrong login")
        return None
    
    def add_vehicle(self, v):
        self.vehicles.append(v)

    def show_vehicles(self):
        for i, v in enumerate(self.vehicles):
            print(f"{i}, {v.get_info()}")

    def save(self):
        with open("data.txt", "w") as f:
            for r in self.reservations:
                f.write(f"{r.user._name},{r.vehicle.get_info()},{r.days},{r.total}\n")

    def load(self):
        try:
            with open("data.txt", "r") as f:
                for line in f:
                    print(line.strip())
        except:
            pass

system = System()

system.add_vehicle(Car("BMW", "320", 50))
system.add_vehicle(LuxuryCar("Mercedes", "S", 120))
system.add_vehicle(Car("Toyota", "corolla", 45))
system.add_vehicle(Car("Toyota", "Prius", 54))
system.add_vehicle(LuxuryCar("BMW", "X5", 75))
system.add_vehicle(LuxuryCar("Audi", "A8", 110))

current_user = None

while True:
    print("\n1 Register")
    print("2 Login")
    print("3 Cars")
    print("4 Rent")
    print("5 My reservations")
    print("6 Save")
    print("7 Exit")

    c = input("Choose: ")

    if c == "1":
        system.register(input("Name: "), input("Email: "), input("Pass: "))

    elif c == "2":
        current_user = system.login(input("Email: "), input("Pass: "))

    elif c == "3":
        system.show_vehicles()

    elif c == "4":
        if current_user:
            system.show_vehicles()
            i = int(input("Car: "))
            d = int(input("Days: "))
            r = current_user.reserve(system.vehicles[i], d)
            system.reservations.append(r)
            print("Reserved:", r.total, "€")
        else:
            print("Login first")

    elif c == "5":
        if current_user:
            current_user.show_reservations()

    elif c == "6":
        system.save()

    elif c == "7":
        break
