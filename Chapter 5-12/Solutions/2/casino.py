"""
A robust solution for homework 5.2 (12.2),
but instead of just printing the scores, we write them to files,
score_list.txt contains all scores while best.txt only contains the top 3
"""

import random
import datetime as dt
import os  # to check if files exist
import json


def get_score_list(filename):
    score_list = []
    if os.path.isfile(filename):  # check if file exists
        with open(filename, "r") as scorefile:
            score_list = json.loads(scorefile.read())  # load the data...
    return score_list


def play_game(game_level="easy"):
    score_list = get_score_list("score_list.txt")
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
                print(f"You guessed it - congratulations! It's number {secret} :)")
                break
            elif guess < secret and game_level == "easy":
                print("Try a bigger number...")
            elif guess > secret and game_level == "easy":
                print("Try a smaller number...")
            else:
                print("Your guess is wrong...")
            wrong_guesses.append(guess)

    # once we get here, we know the player guessed to correct number...
    score_list.append({"attempts": count,
                       "date": str(now),
                       "name": name,
                       "secret": secret,
                       "wrong guesses": wrong_guesses})
    write_score("score_list.txt", score_list)
    score_list = sorted(score_list, key=lambda e: e["attempts"])
    write_score("best.txt", score_list[:3])


def write_score(filename, score_list):
    with open(filename, "w") as scorefile:
        json.dump(score_list, scorefile, indent=4)
