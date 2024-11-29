
# Class definition
class Car:
    def __init__(self, name):
        self.name = name  # Attribute

    def brand(self):  # Method
        print(f"{self.name} makes a sound.")

class Red(Car):
    def brand(self):  # Method Overriding
        print(f"{self.name} red.")

# Object creation
car = Car("red")
car.brand()  # Output: Car Brand.

print("I have  learned how to merge")




