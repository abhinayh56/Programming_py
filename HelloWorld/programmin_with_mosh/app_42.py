# Errors generally of three types
# 1. Compile time error: usually syntactical error. Easiest to find
# 2. Logical error: code compiles and works but output is incorrect. Testing team finds this error.
# 3. Runtime error: Error during runtime. Eg diving by zero. Detected by user side. Eg if input provided is 0, but is is going to be in denominator of division.

# Statement: normal statement: Does not give error (a=5, b=3), critical: (a/b, b = 0)

a = 5
b = 3

try:
    print(a/b)
except Exception:
    print("Divion by zero")

a = 5
b = 0

try:
    print(a/b)
except Exception:
    print("can't divide by zero")

a = 5
b = 0

try:
    print("resource open")
    print(a/b)
    print("resource closed")
except Exception as e:
    print("Error: ", e)
    print("resource closed")


a = 5
b = 3


try:
    print("resource open")
    print(a/b)
    k = int(input("enter a number: "))
    print(1/k)
except ZeroDivisionError as e:
    print("can't divide by zero, Error:", e)
except ValueError as e:
    print("Invalid input, Error:", e)
except Exception as e:
    print("Unknown error, Error:", e)
finally:
    print("resource closed")