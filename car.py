from engine import Engine
from battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__()
        self.engine: Engine = engine
        self.battery: Battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
