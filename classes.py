# Base class representing a generic Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vehicle is moving")

# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, wheels=4):
        super().__init__(brand, model)
        self.wheels = wheels

    def move(self):
        print(f"{self.brand} {self.model} is Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def __init__(self, brand, model, wingspan):
        super().__init__(brand, model)
        self.wingspan = wingspan

    def move(self):
        print(f"{self.brand} {self.model} is Flying ✈️")

# Smartphone class to demonstrate encapsulation and constructors
class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.__os = os  # Private attribute (encapsulation)

    def get_os(self):
        return self.__os

    def set_os(self, new_os):
        self.__os = new_os

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, OS: {self.__os}")
