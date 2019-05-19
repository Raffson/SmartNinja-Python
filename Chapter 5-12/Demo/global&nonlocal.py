"""
Simple example of global & nonlocal
"""


globalvar = 1  # our global variable


def function1():
    globalvar = 5  # creates a local variable = 5, instead of adjusting globalvar
    print(f"globalvar in function1 = {globalvar}")


def function2():
    global globalvar  # indicates we're using a global variable
    globalvar = 5  # adjusts the value of globalvar (not a local variable)
    print(f"globalvar in function2 = {globalvar}")


def function3():
    localvar = 1  # local variable, i.e. local to function3
    print(f"localvar in function3 before function4 = {localvar}")  # localvar=1

    def function4():  # <-- nested function
        localvar = 2  # local variable, i.e. local to function4
        print(f"localvar in function4 = {localvar}")  # localvar=2
    function4()  # execute the nested function...
    print(f"localvar in function3 after function4 = {localvar}")  # localvar=1


def function5():
    localvar = 1  # local variable, i.e. local to function5
    print(f"localvar in function5 before function6 = {localvar}")  # localvar=1

    def function6():  # <-- nested function
        nonlocal localvar  # indicates we're using a nonlocal variable
        localvar = 2  # adjusts the nonlocal variable
        # mind that nonlocal is not the same as global,
        # nonlocal basically means not local to the current function,
        # but local to (one of) the parent function(s),
        print(f"localvar in function6 = {localvar}")  # localvar=2
    function6()
    print(f"localvar in function5 after function6 = {localvar}")  # localvar=2


if __name__ == "__main__":
    print(f"globalvar in global scope = {globalvar}")
    function1()
    print(f"globalvar in global scope after function1 = {globalvar}")
    function2()
    print(f"globalvar in global scope after function2 = {globalvar}")

    function3()
    function5()
