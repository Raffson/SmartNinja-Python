'''
Basic solution for the calculator
'''
xs
#read a first number
x = int(input("Enter a first number:  "))
#read a second number
y = int(input("Enter a second number:  "))
#read an opeation
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
    print(x%y)
elif operation == "//":
    print(x//y)
else:
    print("The given operator is not defined...")

