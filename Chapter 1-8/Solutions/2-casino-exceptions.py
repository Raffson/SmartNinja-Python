"""
Using exceptions just to demonstrate,
since this example would be considered bad practice...
Note the syntax for a try-block:
try: => mandatory presence
except: => mandatory presence, should only occur after a try-block
else: => optional presence, can also occur after "if" but now has different context
finally: => optional presence, should only occur after an except block,
                with possibly an else block in between
Refer to the comments in the code for more details.
"""

secret = 11


try:
    # always executed...
    guess = int(input("Guess the secret number (between 1 and 30): "))
except ValueError:
    # executed if and only if an exception occured in the 'try' block
    print("This not a number...")
    # raise RuntimeError #uncomment to see the effects on the output
else:
    # executed only if no exception occurred in the 'try' block
    # raise RuntimeError #uncomment to see the effects on the output
    if guess == secret:
        # 5 ways to print same thing...
        print("You guessed it - congratulations! It's number " + str(secret) + " :)")
        print("You guessed it - congratulations! It's number %d :)" % secret)
        print("You guessed it - congratulations! It's number {} :)".format(secret))
        print("You guessed it - congratulations! It's number", secret, ":)")
        print(f"You guessed it - congratulations! It's number {secret} :)")
    else:
        print("Too bad, you guessed wrong...")
    # raise RuntimeError #uncomment to see the effects on the output
finally:
    # this will ALWAYS be executed, whether or not an exception is raised
    # in the 'try', 'except' or 'else' block...
    print("As ALWAYS, have a good one!")
