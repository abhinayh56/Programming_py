# inheritance
# constructor in inheritance

class A:
    def __init__(self):
        print("in A init")

    def feature_1(self):
        print("feature 1 working")
    
    def feature_2(self):
        print("feature 2 working")

class B(A):
    def __init__(self):
        print("in B init")
        super().__init__()
        
    def feature_3(self):
        print("feature 3 working")
    
    def feature_4(self):
        print("feature 4 working")

print('---')
a1 = A()
print('---')
b1 = B()
