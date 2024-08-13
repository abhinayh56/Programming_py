# modules in standard library
# search on internet for python x module index

import random

for i in range(3):
    print(random.random())

print('---')
for i in range(3):
    print(random.randint(10, 20))

print('---')
for i in range(3):
    print(random.randrange(10, 200))

print('---')
for i in range(3):
    print(random.random())

members = ['Abhinay', 'Ramesh', 'Rohit', 'ABC', 'DEF', 'GHI']
m1 = random.choice(members)
random.shuffle(members)
print(members)

class Dice:
    def __init__(self):
        self.val = [1, 2, 3, 4, 5, 6]

    def roll(self):
        return random.choice(self.val)
    
    def roll_2(self):
        return (random.randint(1,6), random.randint(1,6))
    

dice = Dice()

mode = '1'

while(True):
    a = input()
    if(a == 'q'):
        break
    elif(a=='1'):
        mode = '1'
    elif(a=='2'):
        mode = '2'
    else:
        pass

    if(mode=='1'):
        val = dice.roll()
        print(val)
    elif(mode=='2'):
        val=dice.roll_2()
        print(val)
    else:
        break