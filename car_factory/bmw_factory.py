from car_factory.car_factory import CarFactory
from car.bmw_car import BmwCar

class BmwFactory(CarFactory):
    def __init__(self):
        super().__init__(BmwCar)
