from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str) -> None:
        pass

class Vehicle(ABC):
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def get_speed(self) -> int:
        pass

    def request_analysis(self):
        print(f"[{self.name}] (Speed: {self.get_speed()} km/h) yêu cầu phân tích")
        self.mediator.notify(self, "analysis")

    def receive(self, msg: str):
        print(f"[{self.name}] -> {msg}")

class ControlTower(Mediator):
    def __init__(self):
        self.vehicles = []

    def add(self, v: Vehicle):
        self.vehicles.append(v)

    def notify(self, sender, event: str):
        if event == "analysis":
            faster = [v.name for v in self.vehicles if v != sender and v.get_speed() > sender.get_speed()]
            msg = f"Đối thủ nhanh hơn: {', '.join(faster)}" if faster else "Bạn nhanh nhất!"
            sender.receive(msg)

class RacingCar(Vehicle):
    def get_speed(self): return 300

class RacingBicycle(Vehicle):
    def get_speed(self): return 30

if __name__ == '__main__':
    tower = ControlTower()
    car = RacingCar("F1", tower)
    bike = RacingBicycle("Xe đạp", tower)

    tower.add(car)
    tower.add(bike)

    bike.request_analysis()
    car.request_analysis()
