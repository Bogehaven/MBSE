
class Vehicle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
        # TODO


class TrafficManager:
    def __init__(self):
        self.vehicles = []

    def addVehicle(self, x, y):
        self.vehicles.append(Vehicle(x, y, 1.0))