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
    if guess < 1 or guess > 30:
        print("Your input is out of bounds...")
    elif guess == secret:  # the actual check...
        # three ways to print same thing...
        print("You guessed it - congratulations! It's number " + str(secret) + " :)")
        print("You guessed it - congratulations! It's number %d :)" % secret)
        print("You guessed it - congratulations! It's number {} :)".format(secret))
    else:
        print("Too bad, it's not %d..." % guess)
print("As ALWAYS, have a good one!")
