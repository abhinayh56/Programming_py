# if(condition 1):
#     statement 1
# elif(condition 2):
#     statement 2
# elif(condition 3):
#     statement 3
# else:
#     statement 4

# while(True):
#     statement

# for iterates an items over collection
for item in 'Python':
    print(item)

a = [1, 3, 34, "aslfkj", 3.445]
print(a)

for i in a:
    print(i, type(i))

print('\n')

for a in a:
    print(a, type(a))

for i in range(7):
    print(i)
print("---")
for i in range(4,7):
    print(i)
print("---")
for i in range(4,13,3):
    print(i)
# break: terminates the entire the entire loop iteration
# continue: skips the current iteration

print('---')
prices = [10, 20, 40, 2]
sum = 0.0
for price in prices:
    sum += price

print(f'total price of items list is {sum}, the input list \nwas      {prices}')

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')