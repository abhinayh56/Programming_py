print('---')
n = [5, 2, 5, 2, 2]
for i in n:
    print('x'*i)

n = [10, 3, 6, 22, 8, 14]
max = n[0]
for num in n:
    if(num>max):
        max = num
    print(num, max)

print('---')
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(matrix[1])
print(matrix[1][:])
print(matrix[1][1:3])

for i in matrix:
    for j in i:
        print(j, i)

print('---')

n = [1, 6, 12, 34, 889, 23]
print(n)
n.append(247)
print(n)
n.insert(0,17)
print(n)
n.insert(1,111)
print(n)
n.insert(len(n),1144851)
print(n)
n.insert(-1,-78)
print(n)

print('---')
print(n)
n.remove(889)
print(n)
n.pop()
print(n)
print(n.index(12))
print(n)

print(34 in n)
print(type(333 in n))

print('---')
print(n)
n.append(12)
print(n.count(12))
n.reverse()
print(n)

n.sort()
print(n)
n.reverse()
print(n)
n2 = n
n.reverse()
print('n2: ', n2)
print('n:  ', n)

print('---')
n.clear()
print(n)

numbers = [2, 2, 4, 6, 3, 6, 1]
uniques = []
print(numbers)
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        print(uniques)