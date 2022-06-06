
class Car():
    def __init__(self, car_name):
        self.car_name = car_name
        self.wheel_count = 0
        self.door_count = 0
        self.hood_count = 0
        self.trunk_lid_type = ""

    def add_wheels(self, wheel_count):
        self.wheel_count = wheel_count

    def add_doors(self, door_count):
        self.door_count = door_count

    def add_hood(self):
        self.hood_count = 1

    def add_trunk_lid(self, trunk_lid_type):
        self.trunk_lid_type = trunk_lid_type

    def list_parts(self):
        print(f"Car name: {self.car_name}, wheel_count: {self.wheel_count}, door_count: {self.door_count}, hood_count: {self.hood_count}, trunk_lid_type: '{self.trunk_lid_type}'")
