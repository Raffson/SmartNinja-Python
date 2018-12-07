number =  raw_input("Enter a number between 1 and 100: ")
while not number.isdigit():
    print("You've entered an invalid number...")
    number = raw_input("Please enter a number between 1 and 100: ")
#supposing the above lines don't need much comments...
#at this point we know that number can be cast to an 'int' safely
number = max(min(int(number), 100), 1) #cast to 'int' and make sure 1 <= number <= 100
#try to reason this yourself, should be trivial...
for i in range(1, number+1): #from 1 to number+1 which gives us [1, number]
    line = "" #initialize empty string
    if i % 3 == 0: line += "Fizz" #if divisible by 3 -> add 'Fizz'
    if i % 5 == 0: line += "Buzz" #if divisible by 5 -> add 'Buzz'
    if line == "": print i #if 'line' is still empty, implies not divisible by 3 nor by 5
    else: print(line) #otherwise we just print 'line'
    #note that if 'i' is divisible by 3 and also by 5,
    # then 'i' also divisible by 15 which produces 'FizzBuzz'
