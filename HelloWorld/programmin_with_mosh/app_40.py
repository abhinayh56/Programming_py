# generators

def top_ten():
    yield 1
    yield 2
    yield 3
    yield 4

values = top_ten()

print(values)
print(values.__next__())
print(next(values))

print('---')

for i in values:
    print(i)
