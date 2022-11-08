from engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car


class CarFactory:
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        engine = Engine(CapuletEngine)
        battery = Battery(SpindlerBattery)
        return Car(self.last_service_date, engine, battery)

    def create_glissade(self):
        engine = Engine(WilloughbyEngine)
        battery = Battery(SpindlerBattery)
        return Car(self.last_service_date, engine, battery)

    def create_palindrome(self):
        engine = Engine(SternmanEngine)
        battery = Battery(SpindlerBattery)
        return Car(self.last_service_date, engine, battery)

    def create_rorschach(self):
        engine = Engine(WilloughbyEngine)
        battery = Battery(NubbinBattery)
        return Car(self.last_service_date, engine, battery)

    def create_thovex(self):
        engine = Engine(CapuletEngine)
        battery = Battery(NubbinBattery)
        return Car(self.last_service_date, engine, battery)
