from __future__ import annotations
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.type = None
        self.max_speed = 0

    def __str__(self):
        return f"{self.type} {self.max_speed}"

class RacingCarBuilder:
    def build(self) -> Vehicle:
        vehicle = Vehicle()
        vehicle.type = "RacingCar"
        vehicle.max_speed = 300
        return vehicle

class RacingBicycleBuilder:
    def build(self) -> Vehicle:
        vehicle = Vehicle()
        vehicle.type = "RacingBicycle"
        vehicle.max_speed = 30
        return vehicle

class VehicleAdapter(ABC):
    @abstractmethod
    def get_vehicle(self) -> Vehicle:
        pass

class RacingCarAdapter(VehicleAdapter):
    def __init__(self, builder: RacingCarBuilder):
        self._builder = builder
    def get_vehicle(self) -> Vehicle:
        return self._builder.build()

class RacingBicycleAdapter(VehicleAdapter):
    def __init__(self, builder: RacingBicycleBuilder):
        self._builder = builder
    def get_vehicle(self) -> Vehicle:
        return self._builder.build()

def show_vehicle(vehicle_adapter: VehicleAdapter):
    vehicle = vehicle_adapter.get_vehicle()
    print(vehicle)

if __name__ == '__main__':
    car_builder = RacingCarBuilder()
    bike_builder = RacingBicycleBuilder()

    car_adapter = RacingCarAdapter(car_builder)
    bike_adapter = RacingBicycleAdapter(bike_builder)

    show_vehicle(car_adapter)
    show_vehicle(bike_adapter)


