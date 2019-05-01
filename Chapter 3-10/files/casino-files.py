'''
Making the user guess 5 times using a while-loop, with hints & random secrets
'''

import random
import os

secret = random.randint(1, 30)

best = None
if os.path.isfile("score.txt"):
    with open("score.txt", "r") as scorefile:
        best = int(scorefile.read())

guess = 0
count = 0
while True:
    count += 1  # count every attempt, including invalid ones...
    guess = input("Guess the secret number (between 1 and 30): ")
    if not guess.isdigit(): #isdigit will only accept natural numbers
        print("This not a positive integer...")
    else:
        #if we get here, it means guess is an integer,
        # so we can safely cast to int...
        guess = int(guess)
        if guess == secret: #the actual check...
            print("You guessed it - congratulations! It's number %d :)" % secret)
            break
        elif guess < secret:
            print("Try a bigger number...")
        else: #guess must be larger that secret...
            #no other choice left cause we ruled out == and <
            print("Try a smaller number...")
print("As ALWAYS, have a good one!") #mind indentation, i.e. no longer part of the loop

with open("score.txt", "w") as file:
    if best == None or best > count:
        file.write(str(count))
    else:
        file.write(str(best))