import unittest
from Car_reservation import User, Car, LuxuryCar, Reservation, System


class TestSystem(unittest.TestCase):

    def test_login(self):
        user = User("Jonas", "jonas@mail.com", "1234")
        self.assertTrue(user.check_login("jonas@mail.com", "1234"))
        self.assertFalse(user.check_login("wrong", "1234"))

    def test_car_price(self):
        car = Car("BMW", "320", 50)
        self.assertEqual(car.get_price(2), 100)

    def test_luxury_discount(self):
        car = LuxuryCar("Mercedes", "S", 100)
        self.assertEqual(car.get_price(3), 270)  # 10% discount

    def test_reservation(self):
        user = User("Jonas", "a", "b")
        car = Car("BMW", "320", 50)
        r = Reservation(user, car, 2)
        self.assertEqual(r.total, 100)

    def test_singleton(self):
        s1 = System()
        s2 = System()
        self.assertTrue(s1 is s2)


if __name__ == "__main__":
    unittest.main()