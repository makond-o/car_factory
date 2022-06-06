from car_factory.ford_factory import FordFactory
from car_factory.bmw_factory import BmwFactory
from car_factory.volkswagen_factory import VolkswagenFactory

if __name__ == "__main__":

    ford_factory = FordFactory()
    ford_sedan = ford_factory.build_sedan()
    ford_sedan.list_parts()
    ford_cabri = ford_factory.build_cabri()
    ford_cabri.list_parts()
    ford_crossover = ford_factory.build_crossover()
    ford_crossover.list_parts()

    bmw_factory = BmwFactory()
    bmw_sedan = bmw_factory.build_sedan()
    bmw_sedan.list_parts()
    bmw_cabri = bmw_factory.build_cabri()
    bmw_cabri.list_parts()
    bmw_crossover = bmw_factory.build_crossover()
    bmw_crossover.list_parts()

    volkswagen_factory = VolkswagenFactory()
    volkswagen_sedan = volkswagen_factory.build_sedan()
    volkswagen_sedan.list_parts()
    volkswagen_cabri = volkswagen_factory.build_cabri()
    volkswagen_cabri.list_parts()
    volkswagen_crossover = volkswagen_factory.build_crossover()
    volkswagen_crossover.list_parts()
