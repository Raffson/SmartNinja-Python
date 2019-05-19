"""
Simple example that demonstrates how __name__ behaves when importing,
and how it relates to __main__
This also demonstrates how variables (and eventually functions and classes)
can be used from an external module
For comments, refer to a.py since the code is practically the same,
except for some values and names to distinguish from a.py
"""

import a

varB = 321
_privateB = "Private variable B"

print("Hello from b.py, __name__ = %s" % __name__)

if __name__ == "__main__":
    print("Only gets executed if b.py was executed (entry-point)")
    try:
        print(a.varA)
        print(a._privateA)
        print(a.doesNotExist)
    except Exception as e:
        print("Exception occurred:", e)
