'''
Basic solution for the km2miles converter, using a lambda function
'''

km2miles = lambda x : x*0.621371192

print("Welcome to our kilometer-miles conversion program...")
while True: #loop indefinitely, we'll break if needed
    dist = float(input("Please enter a distance in kilometers: "))
    converted = km2miles(dist)
    print("%f kilometers = %f miles" % (dist, converted))
    #now let's print the same line, but with the distances rounded to 2 decimals
    print("%.2f kilometers = %.2f miles" % (dist, converted))
    choice = input("Do you want to do more conversions? (y/n)  ").lower()
    if choice != "y" and choice != "yes" and choice != "ja": #break if needed
        break
