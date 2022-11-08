from abc import abstractmethod


class Engine:
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
