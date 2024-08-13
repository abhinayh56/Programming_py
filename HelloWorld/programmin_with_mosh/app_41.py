def top_ten():
    n = 1
    while n<= 10:
        sq = n**2
        yield sq
        n += 1

values = top_ten()

print(values)

for i in values:
    print(i)