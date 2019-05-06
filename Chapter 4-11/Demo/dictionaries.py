'''
Some examples on how to use dictionaries, just to show the different possibilities
'''

d = {} # initialize empty dictionary, same as: d = dict()
print(f"d = {d}") # print the empty dictionary
l = dict([(0, 1), ("one", 2), (2, 3)]) # convert a list of 2-tuples to a dictionary
# this is possible because the first element of each tuple can represent the key,
# while the second element of each tuple is the value
# if python can't make such a convertion, an exception will be raised...
print(f"l = {l}") # print the converted list
l = dict(((0, 1), ("one", 2), (2, 3))) # convert a 3-tuple of 2-tuples to a dictionary
print(f"l = {l}") # print the converted list

# add some stuff to 'd'
d["key1"] = "value1"
d[1] = 0.1
d["abc"] = 123
print(f"d = {d}")

print("Let's do some checks!")
# d.keys() returns a list with all keys of 'd'
print(f"'key1' in d.keys()     = {'key1' in d.keys()}")
print(f"'key2' in d.keys()     = {'key2' in d.keys()}")

# but a shorter way is also possible:
print(f"'key1' in d            = {'key1' in d}")
print(f"'key2' in d            = {'key2' in d}")

# but notice how values are not checked...
print(f"'value1' in d            = {'value1' in d}")
print(f"'value2' in d            = {'value2' in d}")

# d.values() returns us a list with all values from 'd'
print(f"'value1' in d.values() = {'value1' in d.values()}")
print(f"'value2' in d.values() = {'value2' in d.values()}")
print(f"123 in d.values()      = {123 in d.values()}")


print("Now lets change values for keys: \"key1\" & 1")
d["key1"] = "changed1"
d[1] = 1.23
print(f"d = {d}")

# check current keys of 'd'
print(f"d.keys() = {d.keys()}")

print("Adding more stuff to 'd'...")
# now lets add more items to 'd'
# we'll loop from 0 to 9, only adding items that don't exist yet,
# so in this case all iterations will add something except for i==1,
# because d[1] already has a value...
for i in range(10):
    if i not in d.keys():
        d[i] = i*10 # the actual assignment
        print(f"Added key {i} with value {i*10}") # a message to the user...
    else:
        print(f"{i} is already a key for 'd'!")
print(f"d = {d}")

print("Looping over 'd' to print the contents...")
# now lets loop over 'd' and print everything in a neat way...
# d.items() returns a list of 2-tuples (key, value)
for k, v in d.items(): # unpack each item into: k for key, v for value
    print(f"d[{k}] = {v}")


print("Trying to access keys that don't exist VS 'get()' method")
# now let's see what happens when we try to
# access an item with a key that doesn't exist
try:
    print(d["doesntExist"])
except KeyError as e:
    print(f"KeyError exception: key {e} does not exist.")

print(f"d.get('doesntExist') = {d.get('doesntExist')}")
# using the 'get()' method, this doesn't raise an exception so it is "safer",
# even though the key doesn't exist, it returns None instead
# mind that this can introduce confusion as to whether or not the given key exists,
# there's 2 possibilities, either None is returned because the key didn't exist,
# OR, None is returned because that's the value of the given key,
# meaning the key actually exists...
print(f"d.get(1) = {d.get(1)}")

print("Deleting d[0]...")
# let's delete d[0]
del d[0]
print(f"d = {d}")

print("Shallow vs Deep copy")
# Shallow vs deep copy, same principle as with lists
e = d # shallow copy
if d is e:
    print("d IS e")
else:
    print("d IS NOT e")
print(f"id(d) = {id(d)} = {hex(id(d))}")
print(f"id(e) = {id(e)} = {hex(id(e))}")
e = d.copy() # deep copy
if d is e:
    print("d IS e")
else:
    print("d IS NOT e")
print(f"id(d) = {id(d)} = {hex(id(d))}")
print(f"id(e) = {id(e)} = {hex(id(e))}")

