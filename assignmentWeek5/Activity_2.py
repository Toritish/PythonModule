# Parent class: Vehicle
class Vehicle:
    def move(self):
        return "The vehicle moves."

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road "

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky "

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on water "

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on the road "

# Function to demonstrate polymorphism
def show_movement(vehicle):
    print(vehicle.move())

# Example usage
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    show_movement(v)

