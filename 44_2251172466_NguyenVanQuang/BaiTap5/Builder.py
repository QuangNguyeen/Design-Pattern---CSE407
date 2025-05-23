from __future__ import annotations
from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self):
        self.type = None
        self.max_speed = 0

    def __str__(self):
        return f"{self.type} with max speed: {self.max_speed} km/h"

# Inter
class VehicleBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_type(self) -> None:
        pass

    @abstractmethod
    def set_max_speed(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> Vehicle:
        pass

# Concrete builder Racing Car
class RacingCarBuilder(VehicleBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._vehicle = Vehicle()

    def set_type(self):
        self._vehicle.type = "RacingCar"

    def set_max_speed(self) -> None:
        self._vehicle.max_speed = 300

    def get_result(self) -> Vehicle:
        return self._vehicle

# Concrete builder Racing Bicycle
class RacingBicycleBuilder(VehicleBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._vehicle = Vehicle()

    def set_type(self):
        self._vehicle.type = "Racing Bicycle"

    def set_max_speed(self):
        self._vehicle.max_speed = 30

    def get_result(self) -> Vehicle:
        return self._vehicle

class VehicleDirector:
    def __init__(self, builder: VehicleBuilder):
        self._builder = builder

    def construct(self) -> Vehicle:
        self._builder.reset()
        self._builder.set_type()
        self._builder.set_max_speed()
        return self._builder.get_result()

if __name__ == "__main__":
    car_builder = RacingCarBuilder()
    bike_builder = RacingBicycleBuilder()

    car_director = VehicleDirector(car_builder)
    bicycle_director = VehicleDirector(bike_builder)

    racing_car = car_director.construct()
    racing_bike = bicycle_director.construct()

    print(racing_car)
    print(racing_bike)
