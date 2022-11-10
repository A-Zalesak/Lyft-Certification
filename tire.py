from abc import abstractmethod


class Tire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    @abstractmethod
    def needs_service(self):
        pass