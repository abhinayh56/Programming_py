import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=rfscVS0vtbw
# Learn Python - Full Course for Beginners [Tutorial]

my_current_file = open("employees.txt",'a')

my_current_file.write("\nAbhinay, New joining, 8741440525")

my_current_file.close()


my_current_file = open("employee.txt",'w')

content = '''Michael,Rogers,14,123234877
Anand,Manikutty,14,152934485
Carol,Smith,37,222364883
Joe,Stevens,37,326587417
Mary-Anne,Foster,14,332154719
George,ODonnell,77,332569843
John,Doe,59,546523478
David,Smith,77,631231482
Zacary,Efron,59,654873219
Eric,Goldsmith,59,745685214
Elizabeth,Doe,14,845657245
Kumar,Swamy,14,845657246'''

my_current_file.write(content)

my_current_file.close()