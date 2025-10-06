# Polymorphism Example 🎭

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

class Bike(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Using polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    print(v.move())
