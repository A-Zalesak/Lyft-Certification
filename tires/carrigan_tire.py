from tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear) -> None:
        super().__init__(tire_wear)
    
    def needs_service(self):
        result = any(wear >= 0.9 for wear in self.tire_wear)
        return result
    
