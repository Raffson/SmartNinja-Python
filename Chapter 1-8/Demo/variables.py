some_string = "Hey there!"
print(some_string)

string_a = "a"
string_b = "I am a SmartNinja"
string_c = ""
print(string_a, string_b, string_c)

string_a = "Hello"
string_b = "World!"
print(string_a + string_b)
print(string_a + " " + string_b)
print(string_a, string_b)

bool_one = True
bool_two = False
print(bool_one, bool_two)
print(bool_one or bool_two)
print(bool_one and bool_two)
print(not bool_one)

some_var = None
print(some_var)

user_name = input("Please enter your name: ")
print("Hello " + user_name + "!")
print("Hello", user_name + "!")
print("Hello {}!".format(user_name))
print("Hello %s!" % user_name)
print(f"Hello {user_name}!")

first_num = input("Enter the first number: ")
print(type(first_num))
second_num = input("Enter the second number: ")
print(type(second_num))
print("%s + %s = %s" % (first_num, second_num, first_num+second_num))

var_a = 5
print(type(var_a))
var_b = 2
print(type(var_b))
print(var_a + var_b)  # result is 7

var_a = "5"
var_b = "2"
print(var_a + var_b)  # result is 52

mood = "happy"
if mood == "happy":
    print("It is great to see you happy!")
else:
    print("Cheer up, mate!")

mood = "nervous"
if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "scared":
    print("It's all good...")
else:
    print("Cheer up, mate!")
