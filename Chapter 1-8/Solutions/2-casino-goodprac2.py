"""
A more robust solution against faulty input, without causing exceptions
"""

secret = 13
guess = input("Guess the secret number (between 1 and 30): ")
if guess == str(secret):  # the actual check...
    # 5 ways to print same thing...
    print("You guessed it - congratulations! It's number " + secret + " :)")
    print("You guessed it - congratulations! It's number %s :)" % secret)
    print("You guessed it - congratulations! It's number {} :)".format(secret))
    print("You guessed it - congratulations! It's number", secret, ":)")
    print(f"You guessed it - congratulations! It's number {secret} :)")  # python3 only
else:
    print("Too bad, it's not %s..." % guess)
print("As ALWAYS, have a good one!")
