from car_factory import CarFactory
from datetime import datetime

my_factory = CarFactory()
today = datetime.today().date()
three_years_ago = today.replace(year=today.year - 1)
my_calliope = my_factory.create_calliope(current_date=today,
                                         last_service_date=three_years_ago,
                                         current_mileage=20001,
                                         last_service_mileage=0)

if __name__ == '__main__':
    assert my_calliope.needs_service()
