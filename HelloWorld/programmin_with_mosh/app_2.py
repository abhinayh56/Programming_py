a = 'This is a tree'

print(a, len(a))
print(a[0], a[1], a[8], a[13])
print(a[-1], a[-2], a[-6], a[-14])
print(a[0:3])
print(a[0:])
print(a[:3])
print(a[:])
print(a[3:-2])

first = 'Harry'
last = 'Porter'
msg = first + ' [' + last + '] ' 'is a programmer'
print(msg)

msg2 = f'{first} \'[{last}] is a coder'
print(msg2)