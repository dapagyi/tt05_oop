import math

class Vehicle:
    # attributes (tagváltozók)
    speed = 0
    maxSpeed = 0
    # methods (függvények)
    def __init__(self, x, y):
        self.speed = x
        self.maxSpeed = y
        print("You have just created a vehicle.")
    def accelerate(self, x):
        self.speed = min(self.speed + x, self.maxSpeed)
    def brake(self, x):
        self.speed = max(self.speed - x, 0)
    def status(self):
        print("The speed of the vehicle is",self.speed)

class Motorcycle(Vehicle):
    frontTire = 95
    rearTire = 95
    def setWidthTires(self, x, y):
        self.frontTire = x
        self.rearTire = y
        print("You have just put on some tires.")
    def printTireInfo(self):
        print("Width of front tire:",self.frontTire)
        print("Width of front tire:",self.rearTire)

v = Vehicle(50,200)
v.status()
v.accelerate(120)
v.status()
v.accelerate(100)
v.status()
v.brake(80)
v.status()
v.brake(70)
v.status()
v.brake(60)
v.status()

m = Motorcycle(0, 70)
m.accelerate(50)
m.status()
m.accelerate(30)
m.status()
m.brake(80)
m.status()
m.printTireInfo()
m.setWidthTires(92, 108)
m.printTireInfo()