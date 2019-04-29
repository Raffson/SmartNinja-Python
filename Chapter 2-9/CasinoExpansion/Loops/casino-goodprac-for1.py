'''
Making the user guess 5 times using a for-loop, with hints & random secrets
'''

import random

secret = random.randint(1, 30)


for i in range(5):
    guess = input("Guess the secret number (between 1 and 30): ")
    if guess.isdigit(): #guess can still be 0 or >30, making this guess a waste
        guess = int(guess)
    else:
        print("This is not a positive integer...")
        continue #mind that in this case the user wasted an attempt (invalid input)
    if guess == secret: #the actual check...
        print("You guessed it - congratulations! It's number %d :)" % secret)
        break
    elif guess < secret:
        print("Try a bigger number...")
    else: #guess must be larger that secret...
        #no other choice left cause we ruled out == and <
        print("Try a smaller number...")
print("As ALWAYS, have a good one!") #mind indentation, i.e. no longer part of the loop
