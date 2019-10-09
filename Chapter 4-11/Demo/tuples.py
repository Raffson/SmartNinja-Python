"""
Some examples on how to use tuples, just to show the different possibilities
Very similar to lists, except tuples are immutable,
i.e. they can't be changed after they've been created
"""

empty_tuple = ()  # empty tuple, same as: empty_tuple = tuple()
print(type((1,)))  # a 1-tuple, mind the ',' to indicate it's a tuple,
print(type((1)))  # if we forget the ',' it will be interpreted as an int...
t1 = (1, 2, 3)
t2 = tuple(range(1, 4))
t3 = (3, 2, 1)

# print the tuples...
print(f"empty_tuple = {empty_tuple}")
print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t3 = {t3}")

# check if tuples are equal...
print(f"t1 == t2 = {t1 == t2}")
print(f"t1 == t3 = {t1 == t3}")

# membership
print(f"0 in t1 = {0 in t1}")
print(f"1 not in t1 = {1 not in t1}")
print(f"2 in t1 = {2 in t1}")

# length of tuple using 'len()', i.e. number of elements...
print(f"len(empty_tuple) = {len(empty_tuple)}")
print(f"len(t1) = {len(t1)}, len(t2) = {len(t2)}, len(t3) = {len(t3)}")


print("Enough of numbers, let's play with letters...")

wtuple = tuple("Word")
print(f"tuple(\"Word\") = {wtuple}")
print(f"First letter of 'Word' = wtuple[0] = {wtuple[0]}")

print("Looping over 'Word' and 'wtuple'...")

for letter in "Word":  # when looping over a string,
    # it automatically splits the letters into a tuple
    print(letter)

for letter in reversed(wtuple):  # now looping over an actual tuple,
    # but to make things more fun, we reverse it using a built-in function
    print(letter)

print(wtuple)  # mind that wtuple hasn't changed,
# 'reversed(wtuple)' does not adjust wtuple unless we assign its result back to wtuple
# i.e. writing: wtuple = tuple(reversed(wtuple))

mix = (1, "Two", 3.0, '4', None, (True, False, wtuple))
print(mix)

print("Membership operator:")
# demonstrating membership operator
print(f"\"Two\" in mix = {'Two' in mix}")
print(f"\"Three\" in mix = {'Three' in mix}")
print(f"1 not in mix = {1 not in mix}")
print(f"False not in mix = {False not in mix}")

print("Looping over tuples:")
# next up are two ways to loop over 'mix',
# or any tuple in general for that matter...
for element in mix:
    print(element)

for i in range(len(mix)):
    print(f"mix[{i}] = {mix[i]}")

print("Tuple indexing and sub-tuples:")
print(f"mix[-1] = {mix[-1]}")  # last element
print(f"mix[-2] = {mix[-2]}")  # second last element
print(f"mix[2:] = {mix[2:]}")
# sub-tuple starting from index 2 (3rd element) and further
print(f"mix[:2] = {mix[:2]}")
# sub-tuple with all elements below index 2, thus first 2 elements
print(f"mix[2:4] = {mix[2:4]}")
# sub-tuple from index 2 till 4, thus elements with indices 2 and 3

print("Deep copy VS Shallow copy:")

some_tuple = (3, 4, 5)
another_tuple = some_tuple  # make a copy
try:
    another_tuple[0] += 1  # will cause an exception because tuple is immutable
except Exception as e:
    print("Exception occurred:", e)
print(f"some_tuple    = {some_tuple}")
print(f"another_tuple = {another_tuple}")
# both are the same, because a shallow copy was used,
# we can do an identity check...
if some_tuple is another_tuple:
    print("some_tuple IS another_tuple")
else:
    print("some_tuple IS NOT another_tuple")
print(f"id(some_tuple) = {id(some_tuple)} = {hex(id(some_tuple))}")
print(f"id(another_tuple) = {id(another_tuple)} = {hex(id(another_tuple))}")
# mind that the id's are equal


another_tuple = tuple(list(some_tuple))  # making a deep copy
try:
    another_tuple[0] -= 1  # will cause an exception because tuple is immutable
except Exception as e:
    print("Exception occurred:", e)
print(f"some_tuple    = {some_tuple}")
print(f"another_tuple = {another_tuple}")
# no longer the same because a deep copy was used,
# let's do another identity check...
if some_tuple is another_tuple:
    print("some_tuple IS another_tuple")
else:
    print("some_tuple IS NOT another_tuple")
print(f"id(some_tuple) = {id(some_tuple)} = {hex(id(some_tuple))}")
print(f"id(another_tuple) = {id(another_tuple)} = {hex(id(another_tuple))}")
# mind that the id's are different now

print("Deleting elements from a tuple:")
try:
    del some_tuple[0]  # will cause an exception because tuple is immutable
except Exception as e:
    print("Exception occurred:", e)
print(f"some_tuple after deleting first element = {some_tuple}")

print("Appending an element to a tuple:")
try:
    some_tuple.append(4)  # exception because tuple has no method 'append()'
    # also, immutable, so it wouldn't make sense to have an 'append()' method...
except Exception as e:
    print("Exception occurred:", e)
print(f"some_tuple after appending 4 = {some_tuple}")

print("Adding tuples to each other:")
combined = some_tuple + another_tuple  # safe because we create a new tuple...
print(f"combined = {combined}")

print("Clearing a tuple:")
try:
    some_tuple.clear()  # exception because tuple has no method 'clear()'
    # also, immutable, so it wouldn't make sense to have a 'clear()' method...
except Exception as e:
    print("Exception occurred:", e)
print(f"some_tuple after clear() = {some_tuple}")

print("What happens when we try to access an element which is out of bounds:")
print(f"len(another_tuple) = {len(another_tuple)}")
try:  # len(another_tuple) should be 3, so valid indices are 0, 1 & 2
    print(f"another_tuple[3] = {another_tuple[3]}")
except Exception as e:
    print("Exception occurred:", e)
