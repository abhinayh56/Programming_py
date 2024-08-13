# 2 types of methods in a class
# 1. instance methods: 1.1. Accessors method, 1.2. Mutator method
# 2. class methods
# 2. static methods

class Student:
    school = "RKMVD"

    def __init__(self, m1, m2, m3):
        self.m1 = m1 # instance variable
        self.m2 = m2
        self.m3 = m3
    
    def avg(self): # it is an instance method because it works on the object
        return (self.m1 + self.m2 + self.m3) / 3.0
    
    def get_m1(self): # accessor instance method
        self.m1
    
    def set_m1(self, val): # mutator instance method
        self.m1 = val
    
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class. Practice.")
    
s1 = Student(34, 45, 55)
s2 = Student(78, 56, 71)

print(s1.m1)
print(s1.m2)
print(s2.school)

print(s1.avg())
print(s2.avg())

print(s1.getSchool())
print(Student.getSchool())

s1.info()
Student.info()
