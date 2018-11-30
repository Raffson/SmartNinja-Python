print("Welcome to our kilometers-miles conversion program...")
km2mi = lambda x : x*0.621371192 #define the lambda-function
mi2km = lambda x : x/0.621371192 #equivalent to x/km2mi(1)
while True: #loop indefinitely, we'll break if needed
    converter = km2mi #default we take km2mi
    unit = "kilometers"
    ismi2km = raw_input("Do you wish to convert miles to km? (y/n)  ").lower()
    if ismi2km == "y" or ismi2km == "yes":
        converter = mi2km
        unit = "miles" #unit to be converted, used for screen-output
    dist = raw_input("Please enter a distance in %s: " % unit)
    if dist.replace('.', '', 1).isdigit(): #checks if dist valid
        #if dist represents a positive real number, we cast to float...
        dist = float(dist)
    else:
        print("Bad distance input, please try again...")
        continue
    #infer the converted unit, used for screen-output
    cunit = "miles" if unit == "kilometers" else "kilometers"
    #mind how we call the lambda-function "converter",
    print("%f %s = %f %s" % (dist, unit, converter(dist), cunit))
    #i.e. just like any other function...
    #now let's print the same line, but with the distances rounded to 2 decimals
    print("%.2f %s = %.2f %s" % (dist, unit, converter(dist), cunit))
    choice = raw_input("Do you want to do more conversions? (y/n)  ").lower()
    if choice != "y" and choice != "yes" and choice != "ja": #break if needed
        break
