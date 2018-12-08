from sum import numsum #only import 'numsum' from 'sum.py'
#if you want to import all functions from 'sum.py', use 'from sum import *'
#alternatively you can use 'import sum',
#but then you'd have to call 'sum.numsum(...)' instead
#shorten the module's name with 'import sum as s',
#which would allow you to call 's.numsum(...)'

print("Hello from main.py with __name__ = %s" % __name__)

if __name__ == "__main__":
    print("main.py is the 'entry-point'...")
    print("Evaluating numsum(5,38) : %d" % numsum(5, 38))
    print("Evaluating numsum(22,3) : %d" % numsum(22, 3))
    print("Evaluating numsum(4,4) : %d" % numsum(4, 4))
    print("Evaluating numsum(13,87) : %d" % numsum(13, 87))
