from abc import ABC, abstractmethod
from car_factory.car_builder import CarBuilder

class CarFactory(ABC):
    def __init__(self, car_prototype):
        self._car_prototype = car_prototype
        self._car_builder = CarBuilder(self._car_prototype)

    @property
    def car_builder(self):
        return self._car_builder

    def build_sedan(self):
        self.car_builder.produce_doors(4)
        self.car_builder.produce_wheels(4)
        self.car_builder.produce_hood()
        self.car_builder.produce_lid("bagazhnik")
        sedan_car = self.car_builder.product
        return sedan_car

    def build_cabri(self):
        self.car_builder.produce_doors(2)
        self.car_builder.produce_wheels(4)
        self.car_builder.produce_hood()
        self.car_builder.produce_lid("bagazhnik")
        cabri_car = self.car_builder.product
        return cabri_car

    def build_crossover(self):
        self.car_builder.produce_doors(4)
        self.car_builder.produce_wheels(6)
        self.car_builder.produce_hood()
        self.car_builder.produce_lid("lyada")
        crossover_car = self.car_builder.product
        return crossover_car
