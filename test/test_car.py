import unittest
from datetime import datetime
from car_factory import CarFactory
from tires.octoprime_tire import OctoprimeTire
from tires.carrigan_tire import CarriganTire


car_factory = CarFactory()

# The better method, which test components
class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0.75, 0.75, 0.75, 0.75]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0, 0, 0, 0]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0, 0, 0.9, 0]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0, 0, 0, 0]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

# The worse method, which tests cars with combinations of many components
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_calliope(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_glissade(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_palindrome(self, today, last_service_date, warning_light_is_on, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_palindrome(self, today, last_service_date, warning_light_is_on, tire_type, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_palindrome(self, today, last_service_date, warning_light_is_on, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_palindrome(self, today, last_service_date, warning_light_is_on, tire_type, tire_wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_rorschach(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "octoprime_tire"
        tire_wear = [0, 0, 0, 0]

        car = car_factory.create_thovex(self, today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
