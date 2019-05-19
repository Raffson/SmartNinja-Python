"""
A small collection of mathematical functions
"""


def _is_iteratable(i):
    try:
        iter(i)
    except TypeError:
        return False
    else:
        return True


def sum_of_iteratable(iteratable):
    total = 0
    iteratable = iteratable.values() if type(iteratable) == dict else iteratable
    for i in iteratable:
        if type(i) == str:
            continue  # skip strings
        elif _is_iteratable(i):
            total += sum_of_iteratable(i)  # recursive call
        else:  # must be numeric or complex type...
            try:  # try to add, if exception occurs, just continue
                total += iteratable[i]
            except TypeError:
                continue
    return total


def factorial(n):
    assert type(n) == int, "Type of 'n' must be integer."
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def factorial_recursive(n):
    assert type(n) == int, "Type of 'n' must be integer."
    return 1 if n <= 1 else n*factorial_recursive(n-1)


def sum_of_first_n(n):
    assert type(n) == int, "Type of 'n' must be integer."
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def sum_of_first_n_recursive(n):
    assert type(n) == int, "Type of 'n' must be integer."
    return 0 if n <= 0 else n+sum_of_first_n_recursive(n-1)


def _pascal_recursive(n=10, prev=None):
    prev = list() if prev is None else prev
    if n >= 0:
        nextt = [1]
        for i in range(len(prev)-1):
            nextt.append(prev[i]+prev[i+1])
        nextt.append(1)
        return prev + (_pascal_recursive(n-1, nextt))
    else:
        return []


def pascals_triangle(n=10):
    assert type(n) == int, "Type of 'n' must be integer."
    res = _pascal_recursive(n)
    last = 0
    rows = [[1]]
    for i in range(n):
        rows.append(res[last:last+len(rows[-1])+1])
        # indexing[from:to] with 'to' excluded, result is sub-list
        # index -1 means the last element
        last += len(rows[-1])
    return rows


if __name__ == "__main__":
    for row in pascals_triangle():
        print(row)
