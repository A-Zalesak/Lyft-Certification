from car_factory import CarFactory
from datetime import datetime
from tires.carrigan_tire import CarriganTire

my_factory = CarFactory()
tw = [0, 0.9, 0, 0]
my_tire = CarriganTire(tw)
"""
today = datetime.today().date()
three_years_ago = today.replace(year=today.year - 1)
my_calliope = my_factory.create_calliope(current_date=today,
                                         last_service_date=three_years_ago,
                                         current_mileage=20001,
                                         last_service_mileage=0)
"""


if __name__ == '__main__':
    assert my_tire.needs_service()
