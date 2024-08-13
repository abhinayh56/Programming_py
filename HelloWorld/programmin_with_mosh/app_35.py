# polymorphism
# 4 ways of implementing polymorphism
#   1. duck typing
#   2. operator overloading
#   3. method overloading
#   4. method overwriting

# method overloading: present in java, c# but not in python

# Example of method overloading in python using trick (actually python does not directly support method overloading)
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def sum(self, a=None, b=None, c=None):
        s = 0
        if(a !=None and b != None and c!=None):
            s = a + b + c
        elif(a !=None and b != None):
            s = a+ b
        else:
            s = a
        return s
    
s1 = Student(12, 25)
print(s1.sum(20, 9, 9))
print(s1.sum(20, 9))
print(s1.sum(20))

# method overriting:

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1 = A()
a1.show()

b1 = B()
b1.show()