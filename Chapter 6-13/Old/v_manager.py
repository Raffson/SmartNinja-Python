# this file will contain the "Manager" class
# the goal of this class is to manage the vehicles of some company...
# a VManager object will have 2 data-members:
# -cname: represents the name of the company, type = str
# -cars: represents the company's vehicle-inventory (or something alike...)
#   internally stored in a dictionary
from vehicle import *
import cli
import datetime as dt
import os

#piece of code that's being used more than once
#funtion takes 2 parameters which are strings
def _common_code1(kmmsg, lsdmsg):
    km = cli.read_positive_float(kmmsg)
    ls = cli.read_date(lsdmsg)
    return (km, ls)

#another piece of code that's being reused,
#takes 2 parameters, the first being a string,
#the second being a function that takes the string as argument,
#but if and only if the sting is not empty...
def _common_code2(inp, func):
    if inp == "": func()
    else: func(inp)

class VManager(object):
    #constructor for VManager,
    #takes 1 mandatory argument:
    # -cname: type is expected to be string, raise TypeError otherwise
    #       cname may not be an empty string, otherwise raise ValueError
    #initialize the object with cname and an empty dictionary
    def __init__(self, cname):
        if type(cname) != str: raise TypeError
        if cname == "": raise ValueError
        self.cname = cname
        self.cars = {}

    #implement what happens if str() is called on "this" object
    def __str__(self):
        lines = "List of cars for " + self.cname + ":\n"
        if len(self.cars) == 0: return lines+"No cars available...\n"
        for c in self.cars:
            lines += str(c) + " : " + str(self.cars[c]) + "\n"
        return lines

    def __iter__(self):
        return self.cars.__iter__()

    def __getitem__(self, key):
        return self.cars[key]

    #adds a car to "this" VManager object,
    #expects 1 mandatory argument:
    # -car: represents the car to be added, type must be Vehicle,
    #       otherwise raise TypeError
    #   in case the ID is already taken, we'll do nothing...
    #    this should mean the user is trying to add the same car twice,
    #   alternatively it could also mean 2 different cars exist with the same ID,
    #    which would be even worse because that's not supposed to happen
    #   given the way 'Vehicle' was implemented,
    #    it's hard to find such a situation,
    #    but that doesn't mean it doesn't exist...
    #returns True upon successful addition, False otherwise...
    def AddCar(self, car):
        if type(car) != Vehicle:
            raise TypeError
        if self.cars.has_key(car.GetID()):
            if id(car) != id(self.cars[car.GetID()]): #should never be the case though...
                print("Two different cars with the same ID exist!")
                exit() #Quit the program cause things are so FUBAR, I don't even want to know...
            return False
        self.cars[car.GetID()] = car
        return True

    #edits a car given the car's ID, the new number of km and the last service date
    #thus expecting 3 mandatory parameters:
    # -id: expecting this key to be present in self.cars, otherwise return (False, False)
    # -km: expected to be of type int, float or str
    #       in case of str, the string must represent a valid positive number,
    #       otherwise (False, ?) will be returned
    # -ls: expected to be of type str or datetime.date, otherwise return (?, False)
    #       in case the date is in the future, (?, False) is also returned
    #as for the return value, this is a tuple of 2 booleans
    # these indicate (<result-of-EditKM>, <result-of-EditLastServiceDate>)
    def EditCar(self, id, km, ls):
        if self.cars.has_key(id):
            return (self.cars[id].EditKM(km), self.cars[id].EditLastServiceDate(ls))
        return (False, False)

    #writes the output of "option 1" to a file
    #if no filename is provided, <self.cname>.txt will be used
    def Write2File(self, fname=None):
        fname = self.cname+".txt" if fname == None else fname
        with open(fname, 'w+') as f:
            f.write(str(self))

    #load cars from a CSV file
    #takes 2 optional argumants:
    # -fname: the name of the file to be used,
    #           if fname isn't specified, <self.cname>.csv is used instead
    #           if the given filename doesn't exist, the method simply returns
    # -clear: a boolean value indicating whether or not
    #           self.cars should be emptied before adding the cars from the file
    def LoadFromCSV(self, fname=None, clear=True):
        fname = self.cname+".csv" if fname == None else fname
        if not os.path.isfile(fname): return #if the file doesn't exist, return
        if clear: self.cars = {}
        with open(fname, 'r') as f:
            rows = f.read().split('\n')#split on newlines
            #check the first row, it should equal "brand,model,km,lastservice"
            if rows[0] != "brand,model,km,lastservice":
                print("Can't interpret %s" % fname)
                return
            for row in rows[1:]: #rows[1:]->take all rows starting from 1, i.e. drop the first row
                cols = row.split(',') #returns a list with the columns
                if len(cols) != 4: continue #skip incomplete rows...
                if cols[2] == "": cols[2] = 0 #overwrite missing values
                try:
                    cols[2] = float(cols[2]) #the km-value must be converted
                    car = Vehicle(cols[0], cols[1], cols[2], cols[3])
                except ValueError:
                    #exception can either occur in the conversion to float,
                    #or in the construction of Vehicle...
                    #eiter way, we want to ignore this row in both cases...
                    print("Skipping invalid row: %s" % row)
                    continue
                self.AddCar(car)

    #writes all cars currently present in self.cars to a file in CSV format
    #takes 1 optional argument, i.e. the filename
    #which again is <self.cname>.csv if the filename is not provided...
    def WriteToCSV(self, fname=None):
        fname = self.cname+".csv" if fname == None else fname
        with open(fname, 'w+') as f:
            f.write("brand,model,km,lastservice\n")
            for id in self.cars:
                f.write(self.cars[id].toCSVrow()+"\n")

    #this function, as the name suggests, is the main loop of the program
    #this is basically what you could call "user" code,
    #i.e. code that uses the defined class(es) to achieve certain things...
    def Mainloop(self):
        #define some messages
        mainmsg = "\nPlease choose one of following options: \n" \
            "1: See a list of all cars\n2: Add a new car\n" \
            "3: Edit kilometers and last service date\n" \
            "4: Save list to file\n5: Save as CSV-file for future use\n" \
            "6: Load from CSV-file\n7: Quit"
        kmmsg = "Enter a number of km: "
        lsdmsg = "Please enter the last service date D-M-Y: "
        idmsg = "Select an ID number to edit a vehicle: "
        fmsg = "Enter a name for the file: "
        while True:
            print(mainmsg)
            select = raw_input("Enter your selection 1, 2, 3, 4, 5, 6 or 7: ")

            if select == "1": #list of all cars
                print(vman)
            elif select == "2": #add a car
                brand = raw_input("Enter the brand of the car: ")
                model = raw_input("Enter the model of the car: ")
                km, ls = _common_code1(kmmsg, lsdmsg) #refactored code into function for reuse
                if self.AddCar(Vehicle(brand, model, float(km), ls)):
                    print("Successfully added a car!")
                else: print("Failed to add a car!")
            elif select == "3": #edit a car
                print(self)
                id = cli.read_integer(idmsg)
                while not self.cars.has_key(id):
                    print("The given ID doesn't exist, please try again...")
                    id = cli.read_integer(idmsg)
                km, ls = _common_code1(kmmsg, lsdmsg)
                success = self.EditCar(id, km, ls)
                if success[0]: print("Successfully changed the number of kilometers!")
                else: print("Failed to change the number of kilometers!")
                if success[1]: print("Successfully changed the last service date!")
                else: print("Failed to change the last service date!")
            elif select == "4": #write list of cars to file
                inp = cli.read_filename(fmsg)
                _common_code2(inp, self.Write2File)
            elif select == "5": #write cars to file in CSV format
                inp = cli.read_filename(fmsg)
                print(inp)
                _common_code2(inp, self.WriteToCSV)
            elif select == "6": #load cars from CSV file
                print("Current working directory:\n%s" % os.getcwd())
                f = cli.select_csv_file()
                if f == "":
                    print("No files present in the current working directory...")
                    continue
                clear = raw_input("Do you wish to clear the current inventory? (y/n, default=y) ")
                clear = False if clear.lower() == 'n' else True
                self.LoadFromCSV(f, clear)
            elif select == "7": #quit program
                break
            else: #invalid...
                print("Invalid selection, please try again...")


if __name__ == "__main__":
    vman = VManager("TestCompany")
    vman.AddCar(Vehicle("BMW", "M3", 150, "18092018"))
    vman.AddCar(Vehicle("BMW", "M4", 150, dt.datetime(2018, 8, 11).date()))
    vman.AddCar(Vehicle("Pagani", "Zonda F", 30, "12/09/2018"))
    vman.AddCar(Vehicle("Porsche", "GT3RS", 3, "25/10/2018"))
    vman.AddCar(Vehicle("Lamborghini", "Aventador LP700-4", 70, "24-7-2018"))
    vman.AddCar(Vehicle("Toyota", "86GT", 109867, "9-2-2018"))

    vman.Mainloop()


    print("END OF PROGRAM...")
