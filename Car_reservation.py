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

    