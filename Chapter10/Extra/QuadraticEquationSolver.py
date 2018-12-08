#This file will contain some functions to solve a quadratic equation
#Note that some functions will start with an underscore _
#These functions are considered private,
#i.e. when we import this file in some other file,
#we won't be able to use the functions that start with an underscore in that other file...
#IIRC same goes for variables declared in the global scope...
from math import sqrt


#No default values for a, b & c, thus they are mandatory...
def _get_discriminant(a, b, c):
    return b**2-4*a*c #return b^2 - 4ac

'''
#redundant in case we use the generic approach
def _real_solutions(a, b, D):
    return ((-b+sqrt(D))/(2*a), (-b-sqrt(D))/(2*a))
'''

def _complex_solutions(a, b, D):
    return (-b / (2*a), sqrt(abs(D)) / (2*a))

def _check_coefficients(coeffs):
    #check type/length of coeffs is valid
    if not (type(coeffs) == list and len(coeffs) == 3):
        return "Must provide a list with 3 coefficients..."
    #now we'll check if the list contains floats/integers...
    for c in coeffs:
        if type(c) != float and type(c) != int:
            return "One of the provided coefficients has a bad type.\nValid types are float & int..."
    return ""

#Mind how we declare the argument, i.e. 'coeffs=[1,2,3]'
#coeffs is obviously the name, followed by '=[1,2,3]'
#  which represents the default argument...
#This means 'solve_quadratic' can be called with no argument
#in such a case, coeffs recieves the default list [1,2,3]
def solve_quadratic(coeffs=[1,2,3]):
    result = _check_coefficients(coeffs)
    if result != "": return result
    #we will write our results to this string
    #the idea is to return the string at the end of the function...
    a, b, c, = (coeffs[0], coeffs[1], coeffs[2]) #make a tuple and unpack
    aa = str(a) if a > 0 else "({})".format(a)
    bb = str(b) if b > 0 else "({})".format(b)
    cc = str(c) if c > 0 else "({})".format(c)
    result += "Solving quadratic equation: {}x^2 + {}x + {}\n".format(aa,bb,cc)
    D = _get_discriminant(a,b,c)
    result += "D = b^2 - 4ac = {}\n".format(D)
    result += "Solution:\n" if D == 0 else "Solutions:\n"
    '''
    #The following approach seperates real solutions from complex ones,
    #though we can make our algorithm more generic...
    if D >= 0: # real solution(s) (-b +- sqrt(D)) / (2*a)
        x1, x2 = _real_solutions(a,b,D)
        result += "x1 = {}\n".format(x1)
        if D > 0: result += "x2 = {}\n".format(x2)
    else: # complex solutions (-b / (2*a)) +- (i * (sqrt(D) / (2*a)))
        # 2 parts, real and imaginary...
        real, imag = _complex_solutions(a,b,D)
        result += "x1 = {} + {}i\n".format(real, imag)
        result += "x2 = {} - {}i\n".format(real, imag)
    '''
    #Note that (-b +- sqrt(D)) / (2*a) = (-b / (2*a)) +- (sqrt(D) / (2*a))
    #thus, we can use '_complex_solutions',
    #in case we're dealing with a real solution,
    #simply add real and imaginary parts together,
    #otherwise we have to keep them seperate...
    real, imag = _complex_solutions(a,b,D)
    appendix = ("i", "i") if D < 0 \
                        else (" = "+str(real+imag), " = "+str(real-imag))
    result += "x1 = {} + {}{}\n".format(real, imag, appendix[0])
    if D != 0: result += "x2 = {} - {}{}\n".format(real, imag, appendix[1])
    return result

if __name__ == "__main__":
    #Writing the test-code in here...
    #so when running this file, it's basically a test...
    #You should run main.py in order to interact with the program...
    print("Testing QuadraticEquationSolver...")
    print("==================================")
    print("Testing _get_discriminant: "),
    #note the comma in the above statement, it will suppress the newline

    D = _get_discriminant(1,2,3)
    assert D == -8, "Test for _get_discriminant failed,\n" \
    "target = 2^2 - 4*1*3 = 4 - 12 = -8\nactual = {}".format(D)

    print("\t[PASS!]")
    print("Testing _complex_solutions:"),

    real, imag = _complex_solutions(1,2,4)
    assert real == -1 and imag == 1, "Test for _complex_solutions failed,\n" \
    "target 'real' = -1\nactual 'real'= {}"\
    "target 'imag' = 1\nactual 'imag'= {}".format(real, imag)

    print("\t[PASS!]")
    print("Testing _check_coefficients:"),

    result = _check_coefficients([1,2,3])
    assert result == "", "Test for _check_coefficients failed\n"\
    "A valid list of coefficients was given, "\
    "yet _check_coefficients returned a non-empty string...\n"

    assertmsg = "Test for _check_coefficients failed\n"\
        "An invalid list of coefficients was given "\
        "and _check_coefficients failed to return the correct string...\n"\
        "target = \"{}\"\nactual = \"{}\""

    target = "Must provide a list with 3 coefficients..."
    result = _check_coefficients([1,2])
    assert result == target,assertmsg.format(target, result)

    result = _check_coefficients((1,2,3)) #passing a tuple instead
    assert result == target,assertmsg.format(target, result)

    target = "One of the provided coefficients has a bad type.\nValid types are float & int..."
    result = _check_coefficients([1,2,"three"])
    assert result == target,assertmsg.format(target, result)

    print("\t[PASS!]")
    print("Testing solve_quadratic:"),

    assertmsg = "Test for solve_quadratic failed\n"\
        "Output is different from expected value\n"\
        "target = \"{}\"\nactual = \"{}\""

    target = "Solving quadratic equation: 1x^2 + 2x + 4\n"\
    "D = b^2 - 4ac = -12\nSolutions:\n"\
    "x1 = -1 + 1.73205080757i\n"\
    "x2 = -1 - 1.73205080757i\n"

    result = solve_quadratic([1,2,4])
    assert result == target, assertmsg.format(target, result)

    target = "Solving quadratic equation: 1x^2 + 2x + 1\n"\
    "D = b^2 - 4ac = 0\nSolution:\n"\
    "x1 = -1 + 0.0 = -1.0\n"

    result = solve_quadratic([1,2,1])
    assert result == target, assertmsg.format(target, result)

    print("\t[PASS!]")
    print("================================")
    print("All tests passed!")
