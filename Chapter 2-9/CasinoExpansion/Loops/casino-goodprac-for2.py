'''
Making the user guess 5 times using a for-loop, with hints & random secrets
Also, this version will make sure only valid attempts are counted
'''

import random

secret = random.randint(1, 30)

first = True

for i in range(5):
    guess = 0 #0 so the while loop isn't skipped...
    while type(guess) == str or guess < 1 or guess > 30:
        #initially first = True, so "not True" => False
        if not first and type(guess) == int:
            print("This wasn't a number between 1 and 30...")
        first = False #from now on, the above "if" will execute if guess' type is int...
        guess = input("Guess the secret number (between 1 and 30): ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("This is not a positive integer...")
    #once we get to line 26, guess is a 'valid' number
    #'valid' in the sense that it is between 1 and 30
    if guess == secret: #the actual check...
        print("You guessed it - congratulations! It's number %d :)" % secret)
        break
    elif guess < secret:
        print("Try a bigger number...")
    else: #guess must be larger that secret...
        #no other choice left cause we ruled out == and <
        print("Try a smaller number...")
print("As ALWAYS, have a good one!") #mind indentation, i.e. no longer part of the loop
