print("Welcome to our kilometer-miles conversion program...")
while True: #loop indefinitely, we'll break if needed
    unit = "kilometers"
    ismi2km = raw_input("Do you wish to convert miles to km? (y/n)  ").lower()
    if ismi2km == "y" or ismi2km == "yes":
        unit = "miles" #unit to be converted, used for screen-output
    dist = raw_input("Please enter a distance in %s: " % unit)
    if dist.replace('.', '', 1).isdigit(): #checks if dist valid
        #if dist represents a positive real number, we cast to float...
        dist = float(dist)
    else:
        print("Bad distance input, please try again...")
        continue
    converted = dist*0.621371192 if unit == "kilometers" else dist/0.621371192
    #infer the converted unit, used for screen-output
    cunit = "miles" if unit == "kilomets" else "kilometers"
    print("%f %s = %f %s" % (dist, unit, converted, cunit))
    #now let's print the same line, but with the distances rounded to 2 decimals
    print("%.2f %s = %.2f %s" % (dist, unit, converted, cunit))
    choice = raw_input("Do you want to do more conversions? (y/n)  ").lower()
    if choice != "y" and choice != "yes" and choice != "ja": #break if needed
        break
