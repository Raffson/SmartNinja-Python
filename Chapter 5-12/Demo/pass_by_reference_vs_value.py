"""
Quick example illustrating the difference between
pass by value & pass by reference
"""


class ExampleObject:
    def __init__(self):
        self.var1 = "Hello"
        self.var2 = 21

    def __str__(self):
        return f"{self.var1} - {self.var2}"


def pass_by(a):
    if type(a) == int:
        a += 1
    elif type(a) == str:
        a = a + " Test"
    elif type(a) == list:
        a.append(1)
    elif type(a) == dict:
        a["Test"] = 1
    elif type(a) == ExampleObject:
        a.var1 = a.var1 + " World"
        a.var2 = 12
    print(a)


print("Passing string...")
string = "Hello"
print(string)
pass_by(string)  # passed by value
print(string)

print("Passing integer...")
integer = 5
print(integer)
pass_by(integer)  # passed by value
print(integer)

print("Passing list...")
listt = []
print(listt)
pass_by(listt)  # passed by reference
print(listt)

print("Passing dict...")
dictt = {}
print(dictt)
pass_by(dictt)  # passed by reference
print(dictt)

print("Passing object of type ExampleObject...")
obj = ExampleObject()
print(obj)
pass_by(obj)  # passed by reference
print(obj)
