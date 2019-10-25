"""
Basic solution for 5.1/12.1
"""


# takes 2 parameters 'a' and 'b'
# returns the sum of 'a' and 'b'
def numsum(a, b):
    return a+b


# takes 2 parameters 'a' and 'b'
# returns the difference of 'a' and 'b'
def numdiff(a, b):
    return a-b


print("Hello from sum.py with __name__ = %s" % __name__)

if __name__ == "__main__":
    print("sum.py is the 'entry-point'...")
    print(numsum(2, 3))
    print(numdiff(2, 3))
