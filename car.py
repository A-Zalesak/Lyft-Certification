from engine import Engine
from battery import Battery
from serviceable import Serviceable
from tire import Tire


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        super().__init__()
        self.engine: Engine = engine
        self.battery: Battery = battery
        self.tire: Tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
