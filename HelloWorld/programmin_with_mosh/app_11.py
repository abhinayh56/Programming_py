age = input("Enter your age: ")
age = int(float(age))
print(age)
try:
    age = int(input("Enter your age: "))
    temp = 1/age
    print(age)
except ZeroDivisionError:
    print("Age can not be zero")
except ValueError:
    print('Invalid value')


# comments
# 1
# this is a line comment

# 2
# this is a multiline comment
# this is second line of multiline comment
# this is third line of multiline comment
#
# and so on

# 3 (python ignores string literal that is not assigned to any value.
# So multiline comment can also be written using string)
'''
this is a paragraph comment
this is second line of paragraph comment
this is third

and so on
'''