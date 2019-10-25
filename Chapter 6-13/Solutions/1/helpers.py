"""
Helper functions for solution for 6.1/13.1 (and perhaps 6.2/13.2)
"""


# will read & return a float, negative sign will simply be ignored...
# thus returning only positive floats
def read_positive_float(msg="Enter a real number: "):
    f = input(msg)
    f = f[1:] if f != "" and f[0] == '-' else f  # ignore negative sign if present
    while f == "" or not f.replace('.', '', 1).isdigit():
        print("Invalid number was given, please try again...")
        f = input(msg)
    return float(f)


# will read & return a positive integer
def read_positive_integer(msg="Enter a positive integer: "):
    integer = input(msg)
    while not integer.isdigit():
        print("The given input is invalid, please try again...")
        integer = input(msg)
    return int(integer)
