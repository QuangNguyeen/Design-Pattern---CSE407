from abc import ABC, abstractmethod
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

vehicles = [Car(), Bicycle()]
for vehicle in vehicles:
    print(vehicle.get_max_speed())

