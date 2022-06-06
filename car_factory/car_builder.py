
class CarBuilder():
    def __init__(self, car_prototype):
        self._car_prototype = car_prototype
        self.reset()

    def reset(self):
        self._product = self._car_prototype()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_wheels(self, wheel_count):
        self._product.add_wheels(wheel_count)

    def produce_doors(self, door_count):
        self._product.add_doors(door_count)

    def produce_hood(self):
        self._product.add_hood()

    def produce_lid(self, lid_type):
        self._product.add_trunk_lid(lid_type)
