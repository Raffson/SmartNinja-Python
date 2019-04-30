'''
Basic but robust solution for fizzbuzz
'''

number = input("Enter a number between 1 and 100: ")
while not number.isdigit():
    print("Your input was invalid...")
    number = input("Enter a number between 1 and 100: ")
#at this point we know we can safely cast number to 'int'
number = max(min(int(number), 100), 1) #make sure 1 <= number <= 100
for i in range(1, number+1): #from 1 to number+1 which gives us [1, number]
    line = "" #initialize empty string
    if i % 3 == 0: line += "Fizz" #if divisible by 3 -> add 'Fizz'
    if i % 5 == 0: line += "Buzz" #if divisible by 5 -> add 'Buzz'
    if line == "": print(i) #if 'line' is still empty, implies not divisible by 3 nor by 5
    else: print(line) #otherwise we just print 'line'
    #note that if 'i' is divisible by 3 and also by 5,
    # then 'i' also divisible by 15 which produces 'FizzBuzz'
