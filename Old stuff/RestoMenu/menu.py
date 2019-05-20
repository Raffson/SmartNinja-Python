#optionally, ask for a filename from the user
#importing the module 'os' will even allow you to check if a file already exists...
#though the use of 'os' can potentially be dangerous,
#i.e. if you don't know exactly what you're doing...
#for demonstration purposes, we'll just use a hard-coded filename called "menu.txt"
#obviously there's numerous ways to generate/ask a filename...
with open("menu.txt", "w+") as menufile:
#opens a file called menu.txt and can be referenced as 'menufile'
#note that the 'w+' mode will overwrite menu.txt if it already exists
    menufile.write("Restaurant's Menu:\n") #write to the file...
    menus = {} #initialize an empty dictionary

    while True:
        menu = raw_input("Enter the menu: ") #ask a name for this menu
        if menus.has_key(menu): #if menu already exists...
            print "This menu already exists, please choose a different name for the next menu..."
            continue #-> will jump back to line 14 which is what we want...
        price = raw_input("Enter the price: ") #ask a price for this menu
        while not price.replace('.', '', 1).isdigit(): #while invalid price...
            print("You've entered an invalid price...")
            price = raw_input("Enter the price: ")
        menus[menu] = float(price) #we know we have a valid price, safe cast...
        menufile.write("- " + menu + "\t\t" + str(menus[menu]) + "\n")

        choice = raw_input("Do you want to add another menu to the list? (yes/no) ").lower()
        if choice == "no":
            break
