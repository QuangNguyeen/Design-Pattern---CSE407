from abc import ABC, abstractmethod

# Implementor
class VehicleImpl(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_max_speed(self) -> int:
        pass

# ConcreteImplementors
class RacingCarImpl(VehicleImpl):
    def get_type(self) -> str:
        return "RacingCar"

    def get_max_speed(self) -> int:
        return 300

class RacingBicycleImpl(VehicleImpl):
    def get_type(self) -> str:
        return "RacingBicycle"

    def get_max_speed(self) -> int:
        return 30

# Abstraction
class Vehicle:
    def __init__(self, impl: VehicleImpl):
        self._impl = impl

    def __str__(self):
        return f"{self._impl.get_type()} {self._impl.get_max_speed()}"

# RefinedAbstraction (optional - in this case, can be used for extension)
class RacingVehicle(Vehicle):
    pass

# Client function
def show_vehicle(vehicle: Vehicle):
    print(vehicle)

if __name__ == '__main__':
    car = RacingVehicle(RacingCarImpl())
    bike = RacingVehicle(RacingBicycleImpl())

    show_vehicle(car)
    show_vehicle(bike)
