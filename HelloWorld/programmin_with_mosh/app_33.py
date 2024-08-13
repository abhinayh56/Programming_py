# polymorphism
# 4 ways of implementing polymorphism
#   1. duck typing
#   2. operator overloading
#   3. method overloading
#   4. method overwriting

# duck typing in python

x = 5
# dynamic typing in python
x = "Abhinay" 

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide1 = PyCharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide1)
print('---')
lap1.code(ide2)
