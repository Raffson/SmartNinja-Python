"""
A robust solution for homework 4.2 (11.2)
For extra comments, check CasinoExpansion in Chapter 2-9
"""

import random
import datetime as dt
import os  # to check if files exist
import json

score_list = []
if os.path.isfile("score_list.txt"):  # check if file exists
    with open("score_list.txt", "r") as scorefile:
        score_list = json.loads(scorefile.read())  # load the data...

wrong_guesses = []

name = input("Please enter your name: ")
name = name if name != "" else "Anonymous"  # if no name was entered => Anonymous

now = dt.datetime.now()
print(f"Starting game @ {now}")

secret = random.randint(1, 30)

count = 0
while True:
    guess = input("Guess the secret number (between 1 and 30): ")
    if not guess.isdigit():
        print("This not a positive integer...")
    else:
        guess = int(guess)
        if guess < 1 or guess > 30:
            print("This wasn't a number between 1 and 30...")
            continue
        count += 1
        if guess == secret:
            print("You guessed it - congratulations! It's number %d :)" % secret)
            break
        elif guess < secret:
            print("Try a bigger number...")
        else:
            print("Try a smaller number...")
        wrong_guesses.append(guess)

# once we get here, we know the player guessed to correct number...
score_list.append({"attempts": count,
                   "date": str(now),
                   "name": name,
                   "secret": secret,
                   "wrong guesses": wrong_guesses})

with open("score_list.txt", "w") as scorefile:
    json.dump(score_list, scorefile, indent=4)

print("As ALWAYS, have a good one!")
