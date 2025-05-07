from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def get_max_speed(self) -> int:
        pass

class Car(Vehicle):
    def get_max_speed(self) -> int:
        return 200

class Bicycle(Vehicle):
    def get_max_speed(self) -> int:
        return 30

vehicles = [Car(), Bicycle(), Car() ]
for vehicle in vehicles:
    print(vehicle.get_max_speed())

