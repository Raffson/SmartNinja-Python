#this file will contain the "Manager" class
#the goal of this class is to manage the vehicles of some company...
#a VManager object will have 2 date-members:
# -cname: represents the name of the company, type = str
# -cars: represents the company's vehicle-inventory (or something alike...)
#   internally stored in a dictionary
from vehicle import *
import cli
import datetime as dt
import os

def _common_code1(kmmsg, lsdmsg):
    km = cli.read_positive_float(kmmsg)
    ls = cli.read_date(lsdmsg)
    return (km, ls)

def _common_code2(inp, func):
    if inp == "": func()
    else: func(inp)

class VManager(object):
    #constructor for VManager,
    #takes 1 mandatory argument:
    # -cname: type is expected to be string, raise TypeError otherwise
    #initialize the object with cname and an empty dictionary
    def __init__(self, cname):
        if type(cname) != str:
            raise TypeError
        self.cname = cname
        self.cars = {}

    #implement what happens if str() is called on "this" object
    def __str__(self):
        lines = "List of cars for " + self.cname + ":\n"
        for c in self.cars:
            lines += str(c) + " : " + str(self.cars[c]) + "\n"
        return lines

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
            msg = "Two different cars with the same ID exist!"
            assert id(car) == id(self.cars[car.GetID()]), msg
            return False
        self.cars[car.GetID()] = car
        return True


    def EditCar(self, id, km, ls):
        if self.cars.has_key(id):
            self.cars[id].EditKM(km)
            self.cars[id].EditLastServiceDate(ls)
            return True
        return False

    def Write2File(self, fname="default.txt"):
        with open(fname, 'w+') as f:
            f.write(str(self))

    def LoadFromCSV(self, fname="default.csv", clear=True):
        if clear: self.cars = {}
        #should check for a valid CSV file...
        with open(fname, 'r') as f:
            rows = f.read().split('\n')#split on newlines
            #check the first row, it should equal "brand,model,km,lastservice"
            if rows[0] != "brand,model,km,lastservice":
                print("Can't interpret %s" % fname)
                return
            for row in rows[1:-1]:
                cols = row.split(',')
                if cols[2] == "": cols[2] = 0 #overwrite missing values
                try:
                    cols[2] = float(cols[2])
                    car = Vehicle(cols[0], cols[1], cols[2], cols[3])
                except ValueError:
                    print("Skipping invalid row: %s" % row)
                    continue
                self.AddCar(car)

    def WriteToCSV(self, fname="default.csv"):
        with open(fname, 'w+') as f:
            f.write("brand,model,km,lastservice\n")
            for id in self.cars:
                f.write(self.cars[id].toCSVrow()+"\n")

    def Mainloop(self):
        mainmsg = "\nPlease choose one of following options: \n" \
            "1: See a list of all cars\n2: Add a new car\n" \
            "3: Edit kilometers and last service date\n" \
            "4: Save list to file\n5: Save as CSV-file for future use\n" \
            "6: Load from CSV-file\n7: Quit"
        kmmsg = "Enter a number of km: "
        lsdmsg = "Please enter the last service date D-M-Y: "
        idmsg = "Select an ID number to edit a vehicle: "
        fmsg = "Enter a name for the file: "
        optmsg = "Choose an option: "
        while True:
            print(mainmsg)
            select = raw_input("Enter your selection 1, 2, 3, 4, 5, 6 or 7: ")

            if select == "1":
                print(vman)
            elif select == "2":
                brand = raw_input("Enter the brand of the car: ")
                model = raw_input("Enter the model of the car: ")
                km, ls = _common_code1(kmmsg, lsdmsg)
                self.AddCar(Vehicle(brand, model, float(km), ls))
            elif select == "3":
                print(self)
                id = cli.read_integer(idmsg)
                while not self.cars.has_key(id):
                    print("The given ID doesn't exist, please try again...")
                    id = cli.read_integer(idmsg)
                km, ls = _common_code1(kmmsg, lsdmsg)
                self.EditCar(id, km, ls)
            elif select == "4":
                inp = cli.read_filename(fmsg)
                _common_code2(inp, self.Write2File)
            elif select == "5":
                inp = cli.read_filename(fmsg)
                print(inp)
                _common_code2(inp, self.WriteToCSV)
            elif select == "6":
                print("Current working directory:\n%s" % os.getcwd())
                files = [f for f in os.listdir('.') if os.path.isfile(f) and ".csv" in f]
                option = 0
                for file in files:
                    print("{}: {}".format(option, file))
                    option += 1
                if len(files) == 0:
                    print("No files present in the current working directory...")
                    continue
                index = cli.read_integer(optmsg)
                while index >= len(files):
                    print("The given selection doesn't exist, please try again...")
                    index = cli.read_integer(optmsg)
                clear = raw_input("Do you wish to clear the current inventory? (y/n, default=y) ")
                clear = False if clear.lower() == 'n' else True
                self.LoadFromCSV(files[index], clear)
            elif select == "7":
                break
            else:
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
