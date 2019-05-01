import a

varB = 321
_privateB = "Private variable B"

print("Hello from b.py, __name__ = %s" % __name__)

if __name__ == "__main__":
    print("Only gets executed if b.py was executed")
    try:
        print(a.varA)
        print(a._privateA)
    except Exception as e:
        print("Exception occurred:", e)
