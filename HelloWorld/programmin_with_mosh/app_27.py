class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.roll_no)
    
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

s1 = Student("Abhinay", 2)
s2 = Student("Rohit", 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1), id(lap2))