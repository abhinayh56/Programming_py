class Computer:
    def __init__(self): # constructor
        self.name = "Abhinay"
        self.age = 10
    
    def update(self):
        self.age = 30
    
    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

print(id(c1)) # address of object in heap memory
print(id(c2))

c1.name = "Rohit"
c1.age = 23
c1.update()
# c2.update()

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")