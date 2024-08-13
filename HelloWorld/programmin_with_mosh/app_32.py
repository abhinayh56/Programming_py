# inheritance
# constructor in inheritance

class A:
    def __init__(self):
        print("in A init")

    def feature_1(self):
        print("feature 1A working")
    
    def feature_2(self):
        print("feature 2A working")

class B():
    def __init__(self):
        print("in B init")
        super().__init__()
        
    def feature_1(self):
        print("feature 1B working")
    
    def feature_2(self):
        print("feature 2B working")

class C(A, B):
    def __init__(self): # method resolution order (MRO) (always from left to right)
        super().__init__()
        super().__init__()
        print("in C init")
    
    def feat(self):
        super().feature_2()

print('---')
a1 = A()

print('---')
b1 = B()

print('---')
c1 = C()

print('---')
c1.feature_1()
c1.feat()