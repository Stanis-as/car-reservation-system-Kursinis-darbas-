import os
from abc import ABC, abstractmethod

class Vehicle(ABC): # Abstraction - Vehicle is an abstract class
    def __init__(self, brand, model, price):
        self._brand = brand   # Encapsulation - protected attributes
        self._model = model
        self._price = price

    @abstractmethod
    def get_price(self, days):
        pass

    def get_info(self):
        return f"{self._brand} {self._model} ({self._price}€/day)"


class Car(Vehicle): # Inheritance - Car inherits from Vehicle
    def get_price(self, days):
        return self._price * days


class LuxuryCar(Vehicle): # Inheritance + Polymorphism - LuxuryCar overrides get_price
    def get_price(self, days):
        total = self._price * days
        if days >= 3:
            total = total * 0.9  # 10% discount
        return total


class User:
    def __init__(self, name, email, password):
        self._name = name        # Encapsulation
        self._email = email
        self._password = password
        self._reservations = []  # Aggregation - user has reservations

    def check_login(self, email, password):
        return self._email == email and self._password == password

    def get_name(self):
        return self._name

    def add_reservation(self, reservation): 
        self._reservations.append(reservation)

    def show_reservations(self):
        print("\n=== MY RESERVATIONS ===")
        if len(self._reservations) == 0:
            print("No reservations yet.")
            return
        for r in self._reservations:
            print(f"  {r.vehicle.get_info()} | {r.days} days | Total: {r.total}€")


class Reservation: # Composition
    def __init__(self, user, vehicle, days):
        self.user = user
        self.vehicle = vehicle
        self.days = days
        self.total = vehicle.get_price(days)


class System: # Singleton pattern - only one System can exist
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = []
            cls._instance.vehicles = []
            cls._instance.reservations = []
        return cls._instance

    def add_user(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)
        print("Registered successfully!")

    def login(self, email, password):
        for user in self.users:
            if user.check_login(email, password):
                print("Login successful!")
                return user
        print("Wrong email or password.")
        return None

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_vehicles(self):
        print("\n=== AVAILABLE CARS ===")
        for i, vehicle in enumerate(self.vehicles, start=1):
            print(f"  {i}. {vehicle.get_info()}")

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def save_to_file(self):
        with open("data.txt", "w") as f:
            if len(self.reservations) == 0:
                f.write("No reservations\n")
            else:
                for r in self.reservations:
                    f.write(f"{r.user.get_name()},{r.vehicle.get_info()},{r.days},{r.total}\n")
        print("Data saved to data.txt")

    def load_from_file(self):
        if not os.path.exists("data.txt"):
            print("No saved file found.")
            return
        print("\n=== SAVED RESERVATIONS ===")
        with open("data.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            print(" ", line.strip())


system = System()
system.add_vehicle(Car("Toyota", "Corolla", 45))
system.add_vehicle(Car("BMW", "320", 50))
system.add_vehicle(LuxuryCar("Mercedes", "S", 120))
system.add_vehicle(LuxuryCar("Audi", "A8", 110))

current_user = None

# --- Main menu ---
while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n=== CAR RENTAL SYSTEM ===")
    print("1. Register")
    print("2. Login")
    print("3. Show cars")
    print("4. Rent a car")
    print("5. My reservations")
    print("6. Save")
    print("7. Load saved data")
    print("8. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")
        system.add_user(name, email, password)
        input("Press Enter to continue...")

    elif choice == "2":
        email = input("Email: ")
        password = input("Password: ")
        current_user = system.login(email, password)
        input("Press Enter to continue...")

    elif choice == "3":
        system.show_vehicles()
        input("Press Enter to continue...")

    elif choice == "4":
        if current_user is None:
            print("Please login first.")
            input("Press Enter to continue...")
        else:
            system.show_vehicles()
            pick = int(input("Pick a car (number): ")) - 1
            days = int(input("How many days: "))
            vehicle = system.vehicles[pick]
            r = Reservation(current_user, vehicle, days)
            current_user.add_reservation(r)
            system.add_reservation(r)
            print(f"Booked! Total cost: {r.total}€")
            input("Press Enter to continue...")

    elif choice == "5":
        if current_user is None:
            print("Please login first.")
            input("Press Enter to continue...")
        else:
            current_user.show_reservations()
            input("Press Enter to continue...")

    elif choice == "6":
        system.save_to_file()
        input("Press Enter to continue...")

    elif choice == "7":
        system.load_from_file()
        input("Press Enter to continue...")

    elif choice == "8":
        print("Goodbye!")
        break
