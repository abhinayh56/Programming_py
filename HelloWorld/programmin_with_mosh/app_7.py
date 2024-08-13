# tuples

numbers = (1, 2, 3, 2, 2, 2, 12, 34, 1)

for n in numbers:
    print(n)

print('---')
print(numbers)
print('---')
print(numbers.count(2))
print('---')
print(numbers.index(12))
print(numbers[2])

print('---')
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x, y, z, x*y*z)
x = y
print(x, y, z, x*y*z)

print(coordinates)
x, y, x = coordinates
print(x, y, z, type(coordinates), type(x))

print('---')

aa = [1,3,4]
d = 445

a,b,c = aa
print(a,b,c)