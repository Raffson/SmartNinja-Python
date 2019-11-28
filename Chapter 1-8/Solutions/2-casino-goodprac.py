"""
A more robust solution against faulty input, without causing exceptions
"""

secret = 13
guess = input("Guess the secret number (between 1 and 30): ")
if not guess.isdigit():  # isdigit will only accept positive integers
    print("This not a (positive) number...")
else:
    # if we get here, it means guess is an integer,
    # so we can safely cast to int...
    guess = int(guess)
    if guess == secret:  # the actual check...
        # 5 ways to print same thing...
        print("You guessed it - congratulations! It's number " + str(secret) + " :)")
        print("You guessed it - congratulations! It's number %d :)" % secret)
        print("You guessed it - congratulations! It's number {} :)".format(secret))
        print("You guessed it - congratulations! It's number", secret, ":)")
        print(f"You guessed it - congratulations! It's number {secret} :)")  # python3 only
    else:
        print("Too bad, it's not %d..." % guess)
print("As ALWAYS, have a good one!")
