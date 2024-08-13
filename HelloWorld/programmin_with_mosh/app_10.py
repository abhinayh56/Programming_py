# functions

def greet_user_1():
    print(f'Hello Rohan!\nWelcome to the party!!!')
def greet_user_2(name):
    print(f'Hello {name}!\nWelcome to the party!!!')
def greet_user_3(name = "XYZ"):
    print(f'Hello {name}!\nWelcome to the party!!!')
def greet_user_4(name_1 = "XYZ", name_2 = "ABC"):
    print(f'Hello {name_1} & {name_2}!\nWelcome to the party!!!')

greet_user_1()
greet_user_2("Abhinay")
greet_user_3("Ram")
greet_user_3()
greet_user_3("Ramesh")
greet_user_4(name_2="XYZbbb", name_1 = "ABCaaa654654")

def square(n):
    return n*n

print(square(12))
print(square(4))

def cube(n):
    print(n*n*n)

result = cube(2)
print(result)
print(cube(3))