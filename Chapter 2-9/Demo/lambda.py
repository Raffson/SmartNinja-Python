"""
A small demo wrt lambda-functions
"""

x2 = lambda x: x**2
crazyfunction = lambda x, y, z: x+y*z


print(x2(4))
print(crazyfunction(1, 2, 3))
print((lambda x, y, z: x+y*z)(3, 2, 1))  # preferred way according to PEP8
