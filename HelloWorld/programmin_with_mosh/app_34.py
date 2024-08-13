# operator overloading

a = 5
b = 6

print(a+b)
print(int.__add__(a,b))

a = '5'
b = '6'
c = '7'
print(a+b)
print(str.__add__(str.__add__(a,b), c))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other): # operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if(r1>r2):
            return True
        else:
            return False
    
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(10, 11)
s2 = Student(21, 41)

s3 = s1 + s2 # Student.__add__(s1, s2)
print(s3.m1, s3.m2)

print(s1>s2)
print(s1<s2)

print('---')
a = 5
print(a)
print(a.__str__())
print(s1.__str__())
print(s1)

print('---')
print(s1)
print(s2)
print(s3)
print(s1 + s2 + s3)
