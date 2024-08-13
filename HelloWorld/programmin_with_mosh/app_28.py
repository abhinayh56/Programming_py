class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()
    
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Abhinay", 2)
s2 = Student("Rohit", 3)

s1.show()

lap1 = Student.Laptop()
lap2 = Student.Laptop()

print(id(lap1), id(lap2))

print()