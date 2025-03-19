import logging

from abc import ABC, abstractmethod

logging.basicConfig(
    format="%(message)s", level=logging.DEBUG, handlers=[logging.StreamHandler()]
)


class Vehicle(ABC):

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.make} {self.model}"


class Car(Vehicle):

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model), "US_spec"

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model), "US_spec"


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model), "EU_spec"

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model), "EU_spec"


US_factory = USVehicleFactory()
car = US_factory.create_car("Toyota", "Corolla")

logging.info(f"{car[0]} {car[1]}")
car[0].start_engine()
moto = US_factory.create_motorcycle("Иж", "Планета")
logging.info(f"{moto[0]} {moto[1]}")
moto[0].start_engine()
EU_factory = EUVehicleFactory()
car = EU_factory.create_car("Renault", "Duster")
logging.info(f"{car[0]} {car[1]}")
car[0].start_engine()
moto = EU_factory.create_motorcycle("Jawa", "350")
logging.info(f"{moto[0]} {moto[1]}")
moto[0].start_engine()
