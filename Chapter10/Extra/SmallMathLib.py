
def _is_iteratable(i):
    try:
        iter(i)
    except TypeError:
        return False
    else:
        return True

def sum_of_iteratable(iteratable):
    sum = 0
    if type(iteratable) == dict: iteratable = iteratable.values()
    for i in iteratable:
        if type(i) == str:
            continue #skip strings
        elif _is_iteratable(i):
            sum += sum_of_iteratable(i) #recursive call
        else: #must be numeric or complex type...
            try: #try to add, if exception occurs, just continue
                sum += iteratable[i]
            except TypeError:
                continue
    return sum

def factorial(n):
    assert type(n) == int, "Type of 'n' must be integer."
    result = 1
    for i in range(2, n+1):
        result *= i

def factorial_recursive(n):
    assert type(n) == int, "Type of 'n' must be integer."
    if n <= 1: return 1
    else: return n*factorial_recursive(n-1)

def sum_of_first_n(n):
    assert type(n) == int, "Type of 'n' must be integer."
    result = 0
    for i in range(1,n+1):
        result += i

def sum_of_first_n_recursive(n):
    assert type(n) == int, "Type of 'n' must be integer."
    if n <= 0: return 0
    else: return n+sum_of_first_n_recursive(n-1)
