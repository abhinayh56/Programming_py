# https://www.youtube.com/watch?v=rfscVS0vtbw
# Learn Python - Full Course for Beginners [Tutorial]

# r  : read
# w  : write
# a  : append
# r+ : read and write

my_file = open("employees.txt",'r')
print(my_file)

print(my_file.readable())
# print(my_file.read()) # read entire file

print(my_file.readline())
my_file.close()
print("---")
my_file = open("employees.txt",'r')
print(my_file.read())
my_file.close()
print("---")

my_file = open("employees.txt",'r')
f = my_file.readline()
f = my_file.readlines()
print(f, len(f))
my_file.close()


my_file = open("employees.txt",'r')
for employee in my_file.readlines():
    print(employee)
my_file.close()
