from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear) -> None:
        super().__init__(tire_wear)
    
    def needs_service(self):
        result = sum(self.tire_wear) >= 3
        return result