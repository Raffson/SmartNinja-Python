#a procedural GUI version of v_manager
#first import the necessary modules
import Tkinter as tk #Tkinter, tkinter for python3
import tkMessageBox #tkMessageBox ( messagebox becomes part of tkinter in python3 )
import v_manager as vm #vehicle manager
from vehicle import * #vehicle

#small helper-fcuntion which takes a Tkinter.Frame object
#and simply calls the tkraise() function which switches the active frame
def _raise_frame(frame):
    frame.tkraise()

#function which will list all the cars on the main frame
#mind that every time a change is made,
#the list must be re-composed & re-rendered
def _list_cars():
    global vman #declare global variables
    global carlist_frame
    for widget in carlist_frame.winfo_children(): #remove everything in the carlist frame
        widget.destroy()

    #first render a row with the column names
    headers = ["ID", "Brand", "Model", "KM", "Last Service Date"]
    i = 0
    for h in headers:
        tk.Label(carlist_frame, text=h, font=("Courier", 20)).grid(row=0, column=i)
        i += 1

    #now start printing rows containing the actual cars
    i = 1
    for car in vman:
        tk.Label(carlist_frame, text=car, font=("Courier", 16)).grid(row=i, column=0) #render the ID
        j = 1
        row = vman[car].toCSVrow().split(',')
        for col in row: #render the rest...
            label = tk.Label(carlist_frame, text = col, font=("Courier", 16))
            label.grid(row=i, column=j, padx=5, pady=5)
            j +=1
        #at last, add a button to edit the current 'car'
        tk.Button(carlist_frame, text="Edit", font=("Courier", 20), command=lambda i=vman[car]:_edit_car_frame(i)).grid(row=i, column=5)
        i += 1

#function to be triggered whenever the 'edit' button is pressed on one of the cars in the list
def _edit_car_frame(car):
    #declare global variables
    global current_car
    global carname_ecf
    global carkm_ecf
    global carlsd_ecf
    global editcar_frame
    current_car = car #have to keep a reference to the current car
    #now set some StringVars to context specific values,
    #i.e. name of the car, current KM & current LSD
    carname_ecf.set("Editing car : " + str(current_car.GetName()))
    carkm_ecf.set(current_car.GetKM())
    carlsd_ecf.set(current_car.GetLSDstring())
    _raise_frame(editcar_frame) #finally, change to the editcar frame

#function to be trigger when the 'Edit car' button is pressed on the editcar frame
def _edit_car():
    #declaring globals variables
    global vman
    global current_car
    global carkm_ecf
    global carlsd_ecf
    #check if KM and/or LSD have changed
    diffkm, difflsd = (True, True)
    if carkm_ecf.get() == str(current_car.GetKM()): diffkm = False
    if carlsd_ecf.get() == str(current_car.GetLSDstring()): difflsd = False
    if diffkm or difflsd: #if KM or LSD changed...
        #try editing the car, res = True => success, res = False => failure
        res = vman.EditCar(current_car.GetID(), carkm_ecf.get(), carlsd_ecf.get())
        response = "" #fix some output for a messagebox...
        if res[0] == True and diffkm: response += "Kilometers successfully changed!\n"
        elif diffkm: "Failed to change the number of kilometers!\n"
        if res[1] == True and difflsd: response += "Last service date successfully changed!\n"
        elif difflsd: "Failed to change the last service date!\n"
        tkMessageBox.showinfo("Information", response)
        _refresh() #will list the cars & change back to main frame
    else: tkMessageBox.showwarning("Warning", "You must change one of the values in order to edit the car...")

#since this code is used in multiple functions, refactored it...
def _refresh():
    _list_cars()
    global main_frame
    _raise_frame(main_frame)

#function to be triggered when the delete button is pressed on the editcar frame
def _delete_car():
    #declaring global variables
    global vman
    global current_car
    #messagebox with yes/no question, acting as failsafe...
    res = tkMessageBox.askquestion("Delete", "Are you sure you want to delete this car?", icon='warning')
    if res == "yes": del vman.cars[current_car.GetID()]
    else: return
    current_car = None
    _refresh()

#funtion to be tiggered when we press the button to add a car on the addcar frame
def _add_car():
    #declaring global variables
    global vman
    global inputs_acf
    inputs = [] #list to store the values of the inputs
    for input in inputs_acf:
        inputs.append(input.get())
    brand, model, km, lsd = inputs #unpack, just like a tuple
    if brand == "" or model == "": #check model/brand
        tkMessageBox.showerror("Error", "Invalid input was provided!")
        return
    if km == "": km = 0 #overwrite KM if not specified
    try: #catch any exception raised by the next 3 lines
        if lsd != "": car = Vehicle(brand, model, float(km), lsd)
        else: car = Vehicle(brand, model, float(km))
        vman.AddCar(car)
    except ValueError: #only catching ValueErrors, other exceptions will still be raised
        tkMessageBox.showerror("Error", "Invalid input was provided!")
        return
    for input in inputs_acf: #clear the input fields
        input.set("")
    _refresh()


if __name__ == "__main__":
    #some prior initialization of global variables
    current_car = None
    vman = vm.VManager("Some Garage")
    vman.AddCar(Vehicle("BMW", "M3", 150, "18092018"))
    vman.AddCar(Vehicle("BMW", "M4", 150, dt.datetime(2018, 8, 11).date()))
    vman.AddCar(Vehicle("Pagani", "Zonda F", 30, "12/09/2018"))
    vman.AddCar(Vehicle("Porsche", "GT3RS", 3, "25/10/2018"))
    vman.AddCar(Vehicle("Lamborghini", "Aventador LP700-4", 70, "24-7-2018"))
    vman.AddCar(Vehicle("Toyota", "86GT", 109867, "9-2-2018"))

    window = tk.Tk() #create a window
    main_frame = tk.Frame(window) #create a frame linked to 'window'
    editcar_frame = tk.Frame(window)
    addcar_frame = tk.Frame(window)

    #initializations of frames
    for frame in (main_frame, editcar_frame, addcar_frame):
        frame.grid(row=0, column=0, sticky='news')


    window.geometry("1024x512") #define starting size
    #mind that you can also prevent the user from resizing the window if necessary

    #fixing main_frame
    label_mf = tk.Label(main_frame, text="Vehicle Manager : " + vman.cname) #label
    label_mf.config(font=("Courier", 30)) #change configuration after object was created
    label_mf.grid() #when no arguments are provided, it implies the next available row
    carlist_frame = tk.Frame(main_frame) #create a frame within the main frame to list the cars
    carlist_frame.grid() #must use grid or pack, but can't combine them,
    #so since we already started off with grid, we continue with grid
    _list_cars()
    add_mf = tk.Button(main_frame, text="Add Vehicle", font=("Courier", 20), command=lambda:_raise_frame(addcar_frame)).grid()
    #the above button allows us to change to the addcar frame, mind the command...

    #now fix editcar_frame
    carname_ecf = tk.StringVar() #needed for the editcar frame to show the name of the car to be edited...
    carkm_ecf = tk.StringVar() #needed for the KM input
    carlsd_ecf = tk.StringVar() #needed for the car's LSD
    #all of the following should be trivial, if not, let me know ;)
    label_ecf = tk.Label(editcar_frame, textvariable=carname_ecf, font=("Courier", 20)).grid(row=0, columnspan=2)
    back_ecf = tk.Button(editcar_frame, text="Go back", font=("Courier", 20), command=lambda:_raise_frame(main_frame)).grid(row=0, column=3)
    newkm_ecf = tk.Label(editcar_frame, text="New KM", font=("Courier", 20)).grid(row=1, column=0)
    inpkm_ecf = tk.Entry(editcar_frame, textvariable=carkm_ecf).grid(row=1, column=1, padx=5, pady=5)
    newlsd_ecf = tk.Label(editcar_frame, text="New L.S.D.", font=("Courier", 20)).grid(row=2, column=0)
    inplsd_ecf = tk.Entry(editcar_frame, textvariable=carlsd_ecf).grid(row=2, column=1, padx=5, pady=5)
    del_ecf = tk.Button(editcar_frame, text="Delete car", font=("Courier", 20), command=lambda:_delete_car()).grid(row=3, column=0)
    edit_ecf = tk.Button(editcar_frame, text="Edit car", font=("Courier", 20), command=lambda:_edit_car()).grid(row=3, column=1)

    #at last, fix addcar_frame, again rather trivial...
    label_acf = tk.Label(addcar_frame, text="Enter the information for the new car or", font=("Courier", 20)).grid(row=0, columnspan=2)
    back_acf = tk.Button(addcar_frame, text="Go back", font=("Courier", 20), command=lambda:_raise_frame(main_frame)).grid(row=0, column=2)
    labels = ["Brand", "Model", "KM", "L.S.D."]
    inputs_acf = []  #creating a list with inputs instead of a seperate variable for each entry...
    row=1
    for l in labels:
        tk.Label(addcar_frame, text=l, font=("Courier", 20)).grid(row=row, column=0)
        inputs_acf.append(tk.StringVar())
        tk.Entry(addcar_frame, textvariable=inputs_acf[-1]).grid(row=row, column=1, padx=5, pady=5)
        row += 1
    addcar_acf = tk.Button(addcar_frame, text="Add vehicle", font=("Courier", 20), command=lambda:_add_car()).grid(columnspan=2)


    _raise_frame(main_frame) #the frame we want to start with...
    window.mainloop() #let the window do it's thing...
