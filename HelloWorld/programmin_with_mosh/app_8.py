# dictionaries
# key value pair

customer = {
    "name": "Ramesh Mishra",
    "age": 45,
    "height": 170.5,
    "working": True,
    "daily expences": [12.5, 448.6, 98]
}

print(customer)
print(customer["name"])
print(customer["age"])
print(customer["height"])
print(customer["working"])
print(customer["daily expences"])
print(customer["daily expences"][1])
# print(customer.["village"])
print(customer.get("village"))
print(customer.get("name"))

customer["name"] = "Rohit Shetty"
customer["birthday"] = "16.10.1996"
print(customer)
customer.pop("name")
print(customer)

phone_number = input("Enter yout phone number: ")
num_dict = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

w = ""
for n in phone_number:
    w = w + num_dict[n] + " "

print(w)

print(num_dict)
a = num_dict.copy()
print(a)

a.pop("2")
print(a)
print(num_dict)