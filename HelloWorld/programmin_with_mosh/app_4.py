a = 10
print(a, type(a))
b = 3
print(b, type(b))
c = 2.3
print(c,type(c))
d = a/b
print(d, type(d), type(10/3))
print(d, type(d), type(10/2))
print(10/3)
print(10/2)

x = 12
x += 3
print(x)

x = 12
x -= 3
print(x)

x = 12
x /= 3
print(x)

x = 12
x *= 3
print(x)

x = 12
x **= 2
print(x)

# precedence of operation
# exponentian
# division
# multiplication or division
# addition or substraction

a = 10 + 3 - 7**2
print(a)
a = 2*15/3/3**2
print(a)

a = 10/10*10
print(a)
a = 10*10/10
print(10.347%3)

# operators
# arithmetic: +, -, *, /, %
# assignment: =, +=, -=, *=, /=, %=, **=
# logical   : and, or, not
# relational: <, <=, >, >=, ==, !=
# bitwise   : &, |, ^, ~, <<, >>
# identity  : is, is not
# membership: in, not in


a = True
b = False
print(a and b)

a = 2
b = 6
print(a and b)
print(b and a)
print(a or b)
print(b or a)
print(not a)

a = 0
print(not a)

a = 0.0
print(not a)

print("membership operator")
a = "Abhi\\nay"
print("Abh" in a)
print("h" in a)
print("hi\\n" in a)
print("hi" not in a)
print("hi" in a)

print("identity operator")
a = 12
b = 15
print(a is 12)
print(b is a)
print(a is 15)
print(a is not b)
print(a is not 15)