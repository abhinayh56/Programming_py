from app_20 import Class1

class Class2(Class1):
    def __init__(self):
        self.fruit_2 = "mango"
        self.veg_2 = "cabbage"
        self.var_2 = 2.123
        super().__init__()
    
    def fun_2(self):
        print("this is fun2 from class 2")
    
    # def fun_1(self):
    #     print("this is fun1 from class 2")

a = Class2()

print(a.var_2)
print(a.fruit_2)
print(a.veg_2)
a.fun_2()

a.fun_1()
print(a.var_1)
