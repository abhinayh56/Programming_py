# inheritance

# single level inheritence
# multi level inheritance
# multiple inheritace


# A is super class
#     parent class

# B is sub class
#     child class

class A:
    def feature_1(self):
        print("feature 1 working")
    
    def feature_2(self):
        print("feature 2 working")

class B(A): # B is the child class / sub class of A. B is inheriting all the features of A
    def feature_3(self):
        print("feature 3 working")
    
    def feature_4(self):
        print("feature 4 working")

class C(B): # B is the child class / sub class of A. B is inheriting all the features of A
    def feature_5(self):
        print("feature 5 working")

print('---')
a1 = A()
a1.feature_1()
a1.feature_2()

print('---')
b1 = B()
b1.feature_1()
b1.feature_2()
b1.feature_3()
b1.feature_4()

print('---')
c1 = C()
c1.feature_1()
c1.feature_2()
c1.feature_3()
c1.feature_4()
c1.feature_5()