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
import random

secret = random.randint(1, 30)

guess = None  # initialize guess,
# otherwise the program will crash the first time we pass line 19

while guess != secret:
    try:
        # always executed...
        guess = int(input("Guess the secret number (between 1 and 30): "))
    except ValueError:
        # executed if and only if an exception occured in the 'try' block
        print("This not an integer...")
        # raise RuntimeError #uncomment to see the effects on the output
    else:
        # executed only if no exception occurred in the 'try' block
        # raise RuntimeError #uncomment to see the effects on the output
        if guess == secret:
            print("You guessed it - congratulations! It's number", secret, ":)")
            break
        elif guess < secret:
            print("Try a larger number...")
        else:  # guess must be larger that secret...
            print("Try something smaller...")
        # raise RuntimeError #uncomment to see the effects on the output
    finally:
        # this will ALWAYS be executed, whether or not an exception is raised
        # in the 'try', 'except' or 'else' block...
        print("Maybe next time you'll get luckier ;)")
        # mind how this line is printed, even when we break out at line 36,
        # which goes against what we would expect...
