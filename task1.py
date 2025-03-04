from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

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
        self.car = Motorcycle(make, model)
        self.spec = "US_spec"
        
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):   
        return Car(make, model), "EU_spec" 

    def create_motorcycle(self, make, model):
        self.motorcycle = Motorcycle(make, model)
        self.spec = "EU_spec"



# Використання
US_factory = USVehicleFactory()
t = US_factory.create_car("Toyota", "Corolla")
print(t[0], t[1])
t[0].start_engine()
EU_factory = EUVehicleFactory()
EU_factory.create_car("Toyota", "Camry")
# USVehicleFactory.create_car()
# vehicle1.start_engine()

# vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
# vehicle2.start_engine()