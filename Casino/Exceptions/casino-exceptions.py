'''
Using exceptions just to demonstrate,
since this example would be considered bad practice...
Note the syntax for a try-block:
try: => mandatory presence
except: => mandatory presence, should only occur after a try-block
else: => optional presence, can also occur after "if" but now has different context
finally: => optional presence, should only occur after an except block,
                with possibly an else block in between
Refer to the comments in the code for more details.
'''
secret = 11

try:
    #always executed...
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))
except ValueError:
    #executed if and only if an exception occured in the 'try' block
    print("This not a number...")
    #raise RuntimeError
else:
    #executed only if no exception occurred in the 'try' block
    #raise RuntimeError #remove the hashtag at the beginning of the line to try this out...
    if guess == secret:
        #three ways to print same thing...
        print("You guessed it - congratulations! It's number " + str(secret) + " :)")
        print("You guessed it - congratulations! It's number %d :)" % secret)
        print("You guessed it - congratulations! It's number {} :)".format(secret))
    elif guess < secret:
        print "Try a larger number..."
    else: #guess must be larger that secret...
        print "Try something smaller..."
    #raise RuntimeError #remove the hashtag at the beginning of the line to try this out...
finally:
    #this will ALWAYS executed, whether or not an exception is raised
    # in the 'try', 'except' or 'else' block...
    print("As ALWAYS, have a good one!")
