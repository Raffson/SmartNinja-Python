'''
Basic solution for 'guess the secret number'
'''

secret = 13 #hard-code the secret number
guess = input("Guess the secret number (between 1 and 30): ")
guess = int(guess) #this line can throw an exception, i.e. conversion to int

if guess != secret:
    #print using "% format"
    print("Your guess was wrong, it's not %d, better luck next time!" % guess)
else:
    #print by concatenating strings,
    # since guess is of type integer, it must be casted to string
    #note that guess itself stays an integer, unless we do something like:
    # guess = str(guess)
    print("Congratulations! " + str(guess) + " the secret number!")
