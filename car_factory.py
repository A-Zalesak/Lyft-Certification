from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire
from car import Car


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        if tire_type == "carrigan_tire":
            tire = CarriganTire(tire_wear)
        elif tire_type == "octoprime_tire":
            tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        if tire_type == "carrigan_tire":
            tire = CarriganTire(tire_wear)
        elif tire_type == "octoprime_tire":
            tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, tire_type, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        if tire_type == "carrigan_tire":
            tire = CarriganTire(tire_wear)
        elif tire_type == "octoprime_tire":
            tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        if tire_type == "carrigan_tire":
            tire = CarriganTire(tire_wear)
        elif tire_type == "octoprime_tire":
            tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        if tire_type == "carrigan_tire":
            tire = CarriganTire(tire_wear)
        elif tire_type == "octoprime_tire":
            tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

