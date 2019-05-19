"""
Simple demonstration of an assert,
an assertion is basically something you claim that must be true,
if this claim is false, assert will raise an AssertionError,
not catching this exception will cause the program to abort...
this can be handy in particular when writing test code,
another scenario where assertions are needed is design by contract...
"""

try:
    a = int(input("Enter a number for a: "))  # possible ValueError
    b = int(input("Enter a number for b: "))  # possible ValueError
    assert a > b, "'a' must be bigger than 'b'."  # possible AssertionError
    # try inputting for 'a' a smaller (or equal) number than 'b'
    # this will trigger the AssertionError...
except AssertionError as ae:
    print("Assertion Error:", ae)
except ValueError as ve:
    print("Value Error:", ve)
except Exception as e:
    # if we get here, it means an Exception occurred which is different from
    # ValueError and AssertionError...
    # technically this can never occur because only 3 lines are used,
    # for which only a ValueError or an AssertionError can be raised
    print("Exception occurred:",  e)
