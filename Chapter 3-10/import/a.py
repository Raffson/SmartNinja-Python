'''
Simple example that demonstrates how __name__ behaves when importing,
and how it relates to __main__
This also demonstrates how variables (and eventually functions and classes)
can be used from an external module
'''

import b # and thus b.py gets executed
# mind that python will not get stuck in a loop when there's a cyclic dependency

varA = 123 # create a public variable
_privateA = "Private variable A" # create a private variable
# mind that you can still access this  private variable from outside,
# though the underscore indicates to other users that this variable
# is considered private and thus should be left alone

print("Hello from a.py, __name__ = %s" % __name__)
# print __name__ to show how it behaves

if __name__ == "__main__":
    print("Only gets executed if a.py was executed (entry-point)")
    # another print-statement to show how __name__ relates to __main__

    try:
        print(b.varB) # prints varB from b.py
        print(b._privateB) # print _privateB from b.py
        print(b.doesNotExist) # exception because there's no variable with that name
    except Exception as e: # <- catch any exception
        print("Exception occurred:", e)
