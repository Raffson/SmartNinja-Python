"""
This file will contain some functions to solve a quadratic equation
Note that some functions will start with an underscore _
These functions are considered private,
although python has practically no support for private variables/functions,
it indicates to other users they should leave that particular entity alone...
BUT! if you really want to hide a function, you can always use nested functions,
a nested function will only be accessible by the "parent" function...
but then again, mind that this can decrease readability...
"""
from math import sqrt


# No default values for a, b & c, thus they are mandatory...
def _get_discriminant(a, b, c):
    return b ** 2 - 4 * a * c  # return b^2 - 4ac


'''
#redundant in case we use the generic approach
def _real_solutions(a, b, d):
    return ((-b+sqrt(d))/(2*a), (-b-sqrt(d))/(2*a))
'''


# calculates complex solutions
# a: coefficient a from the equation ax^2 +bx + c
# b: coefficient b from the equation ax^2 +bx + c
# d: discriminant of the equation
# returns tuple (real, imaginary)
# note that if d > 0, only real solutions exist and thus we only have to
# add/subtract the imaginary part from the real part
def _complex_solutions(a, b, d):
    return -b / (2 * a), sqrt(abs(d)) / (2 * a)


# checks if the given coefficients are valid
# coeffs: a list with 3 elements, representing a, b & c from the equation
# retuns a string with a possible error message,
#   empty string implies everything is ok...
def _check_coefficients(coeffs):
    # check type/length of coeffs is valid
    if not (type(coeffs) == list and len(coeffs) == 3):
        return "Must provide a list with 3 coefficients..."
    # now we'll check if the list contains floats/integers...
    for c in coeffs:
        if type(c) != float and type(c) != int:
            return "One of the provided coefficients has a bad type.\nValid types are float & int..."
    return ""


# Mind how we declare the argument, i.e. 'coeffs=[1,2,3]'
# coeffs is obviously the name, followed by '=[1,2,3]'
#  which represents the default argument...
# This means 'solve_quadratic' can be called with no argument
# in such a case, coeffs receives the default list [1,2,3]
def solve_quadratic(coeffs=(1, 2, 3)):
    coeffs = list(coeffs) if type(coeffs) == tuple else coeffs
    res = _check_coefficients(coeffs)
    if res != "":
        return res
    # we will write our results to this string
    # the idea is to return the string at the end of the function...
    a, b, c, = (coeffs[0], coeffs[1], coeffs[2])  # make a tuple and unpack
    aa = str(a) if a > 0 else f"({a})"
    bb = str(b) if b > 0 else f"({b})"
    cc = str(c) if c > 0 else f"({c})"
    res += "Solving quadratic equation: {}x^2 + {}x + {}\n".format(aa, bb, cc)
    d = _get_discriminant(a, b, c)
    res += "D = b^2 - 4ac = {}\n".format(d)
    res += "Solution:\n" if d == 0 else "Solutions:\n"
    '''
    #The following approach separates real solutions from complex ones,
    #though we can make our algorithm more generic...
    if d >= 0: # real solution(s) (-b +- sqrt(d)) / (2*a)
        x1, x2 = _real_solutions(a,b,d)
        result += "x1 = {}\n".format(x1)
        if d > 0: result += "x2 = {}\n".format(x2)
    else: # complex solutions (-b / (2*a)) +- (i * (sqrt(d) / (2*a)))
        # 2 parts, real and imaginary...
        real, imag = _complex_solutions(a,b,d)
        result += "x1 = {} + {}i\n".format(real, imag)
        result += "x2 = {} - {}i\n".format(real, imag)
    '''
    # Note that (-b +- sqrt(d)) / (2*a) = (-b / (2*a)) +- (sqrt(d) / (2*a))
    # thus, we can use '_complex_solutions',
    # in case we're dealing with a real solution,
    # simply add real (r) and imaginary (i) parts together,
    # otherwise we have to keep them seperate...
    r, i = _complex_solutions(a, b, d)
    appendix = ("i", "i") if d < 0 \
        else (f" = {r + i}", f" = {r - i}")
    res += f"x1 = {r} + {i}{appendix[0]}\n"
    if d != 0:
        res += f"x2 = {r} - {i}{appendix[1]}\n"
    return res


if __name__ == "__main__":
    # Writing the test-code in here...
    # so when running this file, it's basically a test...
    # You should run main.py in order to interact with the program...
    print("Testing QuadraticEquationSolver...")
    print("==================================")
    print("Testing _get_discriminant:\t", end='')

    d = _get_discriminant(1, 2, 3)
    assert d == -8, "Test for _get_discriminant failed,\n" \
                    f"target = 2^2 - 4*1*3 = 4 - 12 = -8\nactual = {d}"

    print("\t[PASS!]")
    print("Testing _complex_solutions:\t", end='')

    real, imag = _complex_solutions(1, 2, 4)
    assert real == -1 and imag == 1, "Test for _complex_solutions failed,\n" \
                                     "target 'real' = -1\nactual 'real'= {}" \
                                     "target 'imag' = 1\nactual 'imag'= {}".format(real, imag)

    print("\t[PASS!]")
    print("Testing _check_coefficients:", end='')

    result = _check_coefficients([1, 2, 3])
    assert result == "", "Test for _check_coefficients failed\n" \
                         "A valid list of coefficients was given, " \
                         "yet _check_coefficients returned a non-empty string...\n"

    assertmsg = "Test for _check_coefficients failed\n" \
                "An invalid list of coefficients was given " \
                "and _check_coefficients failed to return the correct string...\n" \
                "target = \"{}\"\nactual = \"{}\""

    target = "Must provide a list with 3 coefficients..."
    result = _check_coefficients([1, 2])
    assert result == target, assertmsg.format(target, result)

    result = _check_coefficients((1, 2, 3))  # passing a tuple instead
    assert result == target, assertmsg.format(target, result)

    target = "One of the provided coefficients has a bad type.\nValid types are float & int..."
    result = _check_coefficients([1, 2, "three"])
    assert result == target, assertmsg.format(target, result)

    print("\t[PASS!]")
    print("Testing solve_quadratic:\t", end='')

    assertmsg = "Test for solve_quadratic failed\n" \
                "Output is different from expected value\n" \
                "target = \"{}\"\nactual = \"{}\""

    target = "Solving quadratic equation: 1x^2 + 2x + 4\n" \
             "D = b^2 - 4ac = -12\nSolutions:\n" \
             "x1 = -1.0 + 1.7320508075688772i\n" \
             "x2 = -1.0 - 1.7320508075688772i\n"

    result = solve_quadratic([1, 2, 4])
    assert result == target, assertmsg.format(target, result)

    target = "Solving quadratic equation: 1x^2 + 2x + 1\n" \
             "D = b^2 - 4ac = 0\nSolution:\n" \
             "x1 = -1.0 + 0.0 = -1.0\n"

    result = solve_quadratic([1, 2, 1])
    assert result == target, assertmsg.format(target, result)

    print("\t[PASS!]")
    print("================================")
    print("All tests passed!")
