'''
Some basic examples of functions
'''

# useless function that does nothing, just like the name suggests
# mind that None is returned if nothing is explicitly returned...
def do_nothing():
    pass


# function that takes an arbitrary number of parameters and prints them one by one
# on separate lines
def print_parameters(*args):
    print("Start of print_parameters:")
    for arg in args:
        print(arg)
    print("End of print_parameters.")


c2f = lambda c : c*1.8+32 # lambda function equivalent to 'celsius2fahrenheit'

# function which converts degrees celsius to degrees fahrenheit,
# c: temp in celsius, type is supposed to be 'int' or 'float'
# returns temp in fahrenheit
def celsius2fahrenheit(c):
    return c*1.8+32


f2c = lambda f : (f-32)/1.8 # lambda function equivalent to 'fahrenheit2celsius'

# function which converts degrees celsius to degrees fahrenheit,
# f: temp in fahrenheit, type is supposed to be 'int' or 'float'
# return temp celsius
def fahrenheit2celsius(f):
    return (f-32)/1.8


# function that returns the minimum of the two given parameters,
# mind that 'a' and 'b' must be comparable
# a: the first number
# b: the second number
# returns 'a' if a < b, else 'b'
def minimum(a, b):
    if a < b:
        print("'a' is smaller than 'b'")
        return a
    else:
        print("'b' is smaller that 'a'")
        return b


# function that returns the maximum of the two given parameters,
# mind that 'a' and 'b' must be comparable
# a: the first number (optional), default value is 1
# b: the second number (optional), default value is 2
# returns 'a' if a > b, else 'b'
def maximum(a=1, b=2):
    if a > b:
        print("'a' is bigger than 'b'")
        return a
    else:
        print("'b' is bigger than 'a'")
        return b


print(f"Hello from basics.py, __name__ is currently {__name__}")
if __name__ == "__main__":
    # examples of how to call functions
    print(f"do_nothing() = {do_nothing()}")
    print_parameters(1, 2, 3, "Hello", celsius2fahrenheit(15))
    print(f"celsius2fahrenheit(20) = {celsius2fahrenheit(20)}")
    print(f"farenheit2celsius(20) = {fahrenheit2celsius(20)}")
    print(f"c2f(20) = {c2f(20)}")
    print(f"f2c(20) = {f2c(20)}")
    print(f"minimum(3, 2) = {minimum(3, 2)}")

    # in the following examples, mind the how we pass arguments,
    # the order matters, unless we specify the name of the parameters
    # also note how default arguments arguments get passed
    print(f"maximum(7, 5) = {maximum(7, 5)}") # a=7, b=5
    print(f"maximum(b=7, a=5) = {maximum(b=7, a=5)}") # a=5, b=7
    print(f"maximum() = {maximum()}") # uses both default arguments
    print(f"maximum(3) = {maximum(3)}") # a=3, b=default
    print(f"maximum(b=-1) = {maximum(b=-1)}") # a=default, b=-1


