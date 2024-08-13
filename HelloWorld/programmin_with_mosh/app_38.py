# iterators
nums = [7, 8, 9, 10]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])

print('---')

for i in nums:
    print(i)

print('---')

it = iter(nums)

print(it)

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

print('---')
print(it.__next__())
print(next(it))
for i in nums:
    print(i)