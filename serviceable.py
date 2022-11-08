from abc import abstractmethod


# Not really sure how I'm supposed to use this... Does it just make it easier to extend in the future?
class Serviceable:
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
