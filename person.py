class Person:
    # attributes (tagváltozók)
    name = "No name yet"
    age = 0
    # methods (függvények)
    def setName(self, x):
        self.name = x 
    def setAge(self, x):
        self.age = x
    def talk(self):
        print("Hi! My name is", self.name, "and I am", self.age, "years old.")

class Person2:
    # attributes (tagváltozók)
    __name = "No name yet"
    __age = 0
    # methods (függvények)
    def __init__(self, x, y):
        self.__name = x
        self.age = y
    def setName(self, x):
        self.__name = x 
    def setAge(self, x):
        self.age = x
    def talk(self):
        print("Hi! My name is", self.__name, "and I am", self.age, "years old.")

class Car:
    # attributes (tagváltozók)
    brand = "No name yet"
    maxSpeed = 0
    # methods (függvények)
    def setBrand(self, x):
        self.brand = x 
    def setMaxSpeed(self, x):
        self.maxSpeed = x
    def printData(self):
        print("Hi! My brand is", self.brand, "and my max speed is", self.maxSpeed, "km/h.")

p = Person2("Sandy",34)
p.__name = "Bill"
p.talk()