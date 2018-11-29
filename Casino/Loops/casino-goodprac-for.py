secret = 11
first = True

for i in range(5):
    guess = 0 #0 so the while loop isn't skipped...
    while guess < 1 or guess > 30 or type(guess) == str:
        #initially first = True, so "not True" => False
        if not first and type(guess) == int:
            print("This wasn't a number between 1 and 30...")
        first = False #from now on, the above "if" will execute if guess' type is int...
        guess = raw_input("Guess the secret number (between 1 and 30): ")
        if guess.isdigit(): guess = int(guess)
        else: print("This is not an integer...")
        #mind that single statements are allowed to be put
        # on the same line after the ':'
    #once we get here, guess is a 'valid' number
    #'valid' in the sense that it is between 1 and 30
    if guess == secret: #the actual check...
        #three ways to print same thing...
        print("You guessed it - congratulations! It's number " + str(secret) + " :)")
        print("You guessed it - congratulations! It's number %d :)" % secret)
        print("You guessed it - congratulations! It's number {} :)".format(secret))
        break
    elif guess < secret: print("Try a bigger number...")
    else: #guess must be larger that secret...
        #no other choice left cause we ruled out == and <
        print("Try a smaller number...")
print("As ALWAYS, have a good one!") #mind indentation, i.e. no longer part of the loop
