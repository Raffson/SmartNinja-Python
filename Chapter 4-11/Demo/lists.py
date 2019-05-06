'''
Some examples on how to use lists, just to show the different possibilities
'''

empty_list = [] # create an empty list, same as: empty_list = list()
l1 = [1, 2, 3] # create list with elements 1, 2 & 3
l2 = list(range(1, 4)) # another way to create a list with elements 1, 2 & 3
l3 = [3, 2, 1] # create a list with elements 3, 2 & 1

# print the lists...
print(f"empty_list = {empty_list}")
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")

# check is lists are equal (order matters for list, but not for set)
# a set is basically a special list for which order doesn't matter
# and no duplicate elements,
# i.e. if we add an element that's already in the set, nothing will happen
print(f"l1 == l2 = {l1 == l2}")
print(f"l1 == l3 = {l1 == l3}")
print(f"set(l1) == set(l3) = {set(l1) == set(l3)}")

# some examples of membership operator in/not in
print(f"0 in l1 = {0 in l1}")
print(f"1 not in l1 = {1 not in l1}")
print(f"2 in l1 = {2 in l1}")

# get the length of a list, using built-in function 'len()'
print(f"len(empty_list) = {len(empty_list)}")
print(f"len(l1) = {len(l1)}, len(l2) = {len(l2)}, len(l3) = {len(l3)}")

# difference between sorted(l3) and l3.sort()
print(f"sorted(l3) = {sorted(l3)}")
print(f"l3 = {l3}")
l3.sort()  # i.e. same as: l3 = sorted(l3)
print(f"l3 after doing l3.sort() = {l3}")
print(f"l1 == l3 is {l1 == l3}")


print("Enough of numbers, let's play with letters...")

wlist = list("Word") # convert "Word" in a list -> ['W', 'o', 'r', 'd']
print(f"list(\"Word\") = {wlist}")
print(f"First letter of 'Word' = wlist[0] = {wlist[0]}") # access 0th element
# REMEMBER! We start counting from 0...

print("Looping over 'Word' and 'wlist'...")

for letter in "Word": # when looping over a string,
    # it automatically splits the letters into a list
    print(letter)

for letter in reversed(wlist): # now looping over an actual list,
    # but to make things more fun, we reverse it using a built-in function
    print(letter)

print(f"wlist = {wlist}") # mind that wlist hasn't changed,
# 'reversed(wlist)' does not adjust wlist unless we assign its result back to wlist
# i.e. writing: wlist = reversed(wlist)
# OR similar to sorted() & list.sort(), there's also a list.reverse()
wlist.reverse()
print(f"wlist after reverse() = {wlist}")

# we can also have a list with more than 1 type in it...
mix = [1, "Two", 3.0, '4', None, [True, False, wlist]]
print(f"mix = {mix}")

print("Membership operator:")
# demonstrating membership operator, more thoroughly
print(f"\"Two\" in mix = {'Two' in mix}") # True
print(f"\"Three\" in mix = {'Three' in mix}") # False
print(f"1 not in mix = {1 not in mix}") # False
print(f"False not in mix = {False not in mix}") # True
print(f"False in mix[-1] = {False in mix[-1]}") # True

print("Looping over lists:")
# next up are two ways to loop over 'mix',
# or any list in general for that matter...
for element in mix:
    print(element)

for i in range(len(mix)):
    print(f"mix[{i}] = {mix[i]}")

print("List indexing and sub-lists:")
print(f"mix[-1] = {mix[-1]}") # last element
print(f"mix[-2] = {mix[-2]}") # second last element
print(f"mix[2:] = {mix[2:]}")
# sub-list starting from index 2 (3rd element) and further
print(f"mix[:2] = {mix[:2]}")
# sub-list with all elements below index 2, thus first 2 elements
print(f"mix[2:4] = {mix[2:4]}")
# sub-list from index 2 till 4, thus elements with indices 2 and 3

print("Deep copy VS Shallow copy:")

some_list = [3, 4, 5]
another_list = some_list # make a copy
another_list[0] += 1 # add one to first element to see what happens
print(f"some_list    = {some_list}")
print(f"another_list = {another_list}")
# both are the same, because a shallow copy was used,
# we can do an identity check...
if some_list is another_list:
    print("some_list IS another_list")
else:
    print("some_list IS NOT another_list")
print(f"id(some_list) = {id(some_list)} = {hex(id(some_list))}")
print(f"id(another_list) = {id(another_list)} = {hex(id(another_list))}")
# mind that the id's are equal

another_list = some_list.copy() # now make a deep copy
another_list[0] -= 1 # subtract one from first element, giving [3, 4, 5] again
print(f"some_list    = {some_list}")
print(f"another_list = {another_list}")
# no longer the same because a deep copy was used,
# let's do another identity check...
if some_list is another_list:
    print("some_list IS another_list")
else:
    print("some_list IS NOT another_list")
print(f"id(some_list) = {id(some_list)} = {hex(id(some_list))}")
print(f"id(another_list) = {id(another_list)} = {hex(id(another_list))}")
# mind that the id's are different now

print("Deleting elements from a list:")
del some_list[0] # delete first (=0th) element of some_list
print(f"some_list after deleting first element = {some_list}")

print("Appending an element to a list:")
some_list.append(4)
print(f"some_list after appending 4 = {some_list}")

print("Adding lists to each other:")
combined = some_list + another_list
print(f"combined = {combined}")

print("Clearing a list:")
some_list.clear()
print(f"some_list after clear() = {some_list}")

print("What happens when we try to access an element which is out of bounds:")
print(f"len(another_list) = {len(another_list)}")
try: # len(another_list) should be 3, so valid indices are 0, 1 & 2
    print(f"another_list[3] = {another_list[3]}")
except Exception as e:
    print("Exception occurred:", e)

