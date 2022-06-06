from car_factory.car_factory import CarFactory
from car.volkswagen_car import VolkswagenCar

class VolkswagenFactory(CarFactory):
    def __init__(self):
        super().__init__(VolkswagenCar)
