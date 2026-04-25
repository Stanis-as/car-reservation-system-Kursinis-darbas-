import unittest
from Car_reservation import User, Car, LuxuryCar, Reservation, System


class TestCar(unittest.TestCase):

    def test_car_price(self):
        car = Car("Toyota", "Corolla", 45)
        self.assertEqual(car.get_price(2), 90)

    def test_luxury_no_discount(self):
        car = LuxuryCar("Mercedes", "S", 100)
        self.assertEqual(car.get_price(2), 200)

    def test_luxury_with_discount(self):
        car = LuxuryCar("Mercedes", "S", 100)
        self.assertEqual(car.get_price(3), 270)


class TestUser(unittest.TestCase):

    def test_login_correct(self):
        user = User("Jonas", "jonas@mail.com", "1234")
        self.assertTrue(user.check_login("jonas@mail.com", "1234"))

    def test_login_wrong(self):
        user = User("Jonas", "jonas@mail.com", "1234")
        self.assertFalse(user.check_login("jonas@mail.com", "wrongpass"))

    def test_reservation_added(self):
        user = User("Jonas", "jonas@mail.com", "1234")
        car = Car("BMW", "320", 50)
        r = Reservation(user, car, 2)
        user.add_reservation(r)
        self.assertEqual(len(user._reservations), 1)


class TestSingleton(unittest.TestCase):

    def test_same_instance(self):
        s1 = System()
        s2 = System()
        self.assertIs(s1, s2)


if __name__ == "__main__":
    unittest.main()
