# 2 types of variables / attributes in a class
# 1. instance variable
# 2. static (class) variable

class Car:
    wheels = 4 # class variable static (common for all the objects), class namespace

    def __init__(self):
        self.mil = 10 # instance variable (inside the constructor) (different for different objects)
        self.com = "BMW" # instance namespace

c1 = Car()
c2 = Car()

c1.mil = 0

Car.wheels = 5
c1.mil = 44

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)