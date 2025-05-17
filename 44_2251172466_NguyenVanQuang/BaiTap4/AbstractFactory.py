from __future__ import annotations
from abc import ABC, abstractmethod

from arrow.api import factory


class Car(ABC):
    @abstractmethod
    def get_max_speed(self) -> int:
        pass

class Bicycle(ABC):
    @abstractmethod
    def get_max_speed(self) -> int:
        pass

class RacingCar(Car):
    def get_max_speed(self) -> int:
        return 300


class RacingBicycle(Bicycle):
    def get_max_speed(self) -> int:
        return 30

class VehicleFactory(ABC):
    def create_car(self) -> Car:
        pass
    def create_bicycle(self) -> Bicycle:
        pass

class RacingVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return RacingCar()
    def create_bicycle(self) -> Bicycle:
        return RacingBicycle()

def client_code(factory: VehicleFactory):
    car = factory.create_car()
    bicycle = factory.create_bicycle()
    print(f"Created Car with max speed: {car.get_max_speed()} km/h")
    print(f"Created Bicycle with max speed: {bicycle.get_max_speed()} km/h")

if __name__ == "__main__":
    factory = RacingVehicleFactory()
    client_code(factory)
