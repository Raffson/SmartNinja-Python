"""
Making the user guess 5 times using a while-loop, with hints & random secrets
Also reads the best score so far from score.txt (if it exists)
and writes the best score back to score.txt at the end of the game.
Thus if the player manages to beat the best score so far,
score.txt will be updated.
If score.txt did not exist yet,
the player's score is simply written into score.txt,
thus creating the file.
"""

import random as r  # remember, you can shorten the name for easier reference
import os

secret = r.randint(1, 30)

best = None  # initialize best to None, in case score.txt doesn't exist
if os.path.isfile("score.txt"):  # checks if score.txt is present in folder of execution
    # mind this "folder of execution" --> check notes at bottom
    with open("score.txt", "r") as scorefile:
        best = int(scorefile.read())  # this is dangerous without checks!
        # if the user decides to change the content of score.txt,
        # it may contain invalid data and cause an exception

count = 0  # keep a count for the number of attempts,
# initializing on 0 means we need to increment count at the beginning of the loop,
# if we initialize with 1, we'd have to increment count at the end of the loop...
while True:
    count += 1  # count every attempt, including invalid ones...
    guess = input("Guess the secret number (between 1 and 30): ")
    if not guess.isdigit():  # isdigit will only accept natural numbers
        print("This not a positive integer...")
    else:
        # if we get here, it means guess is an integer,
        # so we can safely cast to int...
        guess = int(guess)
        if guess == secret:  # the actual check...
            print("You guessed it - congratulations! It's number %d :)" % secret)
            break
        elif guess < secret:
            print("Try a bigger number...")
        else:  # guess must be larger that secret...
            # no other choice left cause we ruled out == and <
            print("Try a smaller number...")
print("As ALWAYS, have a good one!")  # mind indentation, i.e. no longer part of the loop

# write the best attempt to score.txt
with open("score.txt", "w") as file:
    if best is None or best > count:
        file.write(str(count))
    else:
        file.write(str(best))

'''
The "folder of execution" is basically the folder from which you ran your
python command, in IDE's (like PyCharm for example) this folder
is equivalent to your working directory.
'''