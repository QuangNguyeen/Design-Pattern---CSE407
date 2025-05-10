from __future__  import annotations
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_max_speed(self) -> int:
        pass

class Car(Vehicle):
    def get_max_speed(self) -> int:
        return 200

class Bicycle(Vehicle):
    def get_max_speed(self) -> int:
        return 30

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass
    def show_vehicle_info(self):
        vehicle = self.create_vehicle()
        if vehicle.get_max_speed() == 200:
            print('Factory created: Car')
        if vehicle.get_max_speed() == 30:
            print('Factory created: Bicycle')


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Car:
        return Car()

class BicycleFactory(VehicleFactory):
    def create_vehicle(self) -> Bicycle:
        return Bicycle()

def client_code(factory: VehicleFactory):
    factory.show_vehicle_info()

if __name__ == '__main__':
    client_code(CarFactory())
    client_code(BicycleFactory())



