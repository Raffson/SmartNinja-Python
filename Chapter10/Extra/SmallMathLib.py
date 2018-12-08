import QuadraticEquationSolver as qes

def read_coefficient(c):
    inp = raw_input("Enter a coefficient for '%s': " % c)
    neg = True if inp != "" and inp[0] == '-' else False #check for negative sign...
    while not inp.replace('.', '', 1).replace('-', '', 1).isdigit(): #while invalid input...
        print("You must enter an integer or a real number...")
        inp = raw_input("Enter a coefficient for '%s': " % c)
        if inp == "": return 0 #if empty string, return 0
        neg = True if inp[0] == '-' else False
        #mind how we only check for '-' and no longer for empty string
        #because if inp was empty, we would've returned 0...
    return -float(inp) if neg else float(inp)

def main():
    stop = ""
    while stop != "y" or stop != "yes":
        coefficients = [] #empty list where we'll put our coefficients
        labels = ["a", "b", "c"] #labels to be passed on to 'read_coefficient()'
        for i in range(3): #read the 3 coefficients...
            coefficients.append(read_coefficient(labels[i]))
        print(qes.solve_quadratic(coefficients))
        stop = raw_input("Do you want to solve another equation? (y/n) ")

if __name__ == "__main__":
    main()
