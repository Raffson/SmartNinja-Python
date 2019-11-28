"""
Basic solution for the calculator
"""

# robust solutions for reading floats will be discussed later in the course
# read a first number
x = float(input("Enter a first number:  "))
# read a second number
y = float(input("Enter a second number:  "))
# read an operation
operation = input("Enter your operation: *  /  +  -  ^  %  //       ")

if operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
elif operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "^":
    print(x**y)
elif operation == "%":
    print(x % y)
elif operation == "//":
    print(x//y)
else:
    print("The given operator is not defined...")
