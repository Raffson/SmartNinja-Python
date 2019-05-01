import b

varA = 123
_privateA = "Private variable A"

print("Hello from a.py, __name__ = %s" % __name__)


if __name__ == "__main__":
    print("Only gets executed if a.py was executed")
    try:
        print(b.varB)
        print(b._privateB)
    except Exception as e:
        print("Exception occurred:", e)
