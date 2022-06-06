from car_factory.car_factory import CarFactory
from car.ford_car import FordCar

class FordFactory(CarFactory):
    def __init__(self):
        super().__init__(FordCar)
