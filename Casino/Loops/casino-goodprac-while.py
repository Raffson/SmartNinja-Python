secret = 11
guess = 0

count = 0
while guess != secret and count < 5:
    guess = raw_input("Guess the secret number (between 1 and 30): ")
    if not guess.isdigit(): #isdigit will only accept natural numbers
        print("This not an integer...")
    else:
        #if we get here, it means guess is an integer,
        # so we can safely cast to int...
        guess = int(guess)
        if guess < 1 or guess > 30:
            print("This wasn't a number between 1 and 30...")
            continue #restart the loop to
        count += 1 #make sure we only get 5 valid attempts
        #mind that we shouldn't increase  count before the above "if"
        #otherwise we would possibly be counting invalid guesses...
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
