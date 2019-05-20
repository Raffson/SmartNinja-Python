"""
This file will contain some helper functions to deal with input
via the command-line interface, making sure the input is valid...
"""
import datetime as dt
import os

# define a list of illegal characters w.r.t. filenames
_illegalchars = ['\\', '/', '?', '%', '*', ':', '|', '\"', '<', '>']


# will read & return a float, negative sign will simply be ignored...
# thus returning only positive floats
def read_positive_float(msg="Enter a real number: "):
    f = input(msg)
    f = f[1:] if f != "" and f[0] == '-' else f
    while f == "" or not f.replace('.', '', 1).isdigit():
        print("Invalid number was given, please try again...")
        f = input(msg)
    return float(f)


# will read & return a datetime.date object
def read_date(msg="Enter a date (D-M-Y): ", no_future=True):
    ls = input(msg)
    while type(ls) != dt.date:
        ls = ls.replace("/", "").replace("-", "")  # remove dashes&slashes
        dateformat = "%d%m%Y"
        if len(ls) <= 6:  # meaning we're using a 2-digit year
            dateformat = "%d%m%y"
        try:  # wondering if we could do our own value-checks instead...
            ls = dt.datetime.strptime(ls, dateformat).date()
        except ValueError:
            print("The given date is invalid, please try again...")
            ls = input(msg)
    if no_future and ls > dt.datetime.now().date():
        print("Given date is in the future, overwriting with today's date...")
        ls = dt.datetime.now().date()
    return ls


# will read & return a positive integer
def read_integer(msg="Enter an integer: "):
    integer = input(msg)
    while not integer.isdigit():
        print("The given input is invalid, please try again...")
        integer = input(msg)
    return int(integer)


# will read & return a filename, making sure no illegal characters are present
def read_filename(msg="Enter a filename: "):
    inp = input(msg)
    # mind that the expression "letter in inp for letter in _illegalchars"
    # returns a list of booleans,
    # any() basically checks in any of these booleans are true,
    # if so, any() will return true, otherwise false
    while any(letter in inp for letter in _illegalchars):
        print("Invalid filename was specified, please try again...")
        inp = input(msg)
    return inp


# lists all csv-files in the current working directory
# allows you to select one of these files and return the selected csv-file's name
def select_csv_file(msg="Choose a file (enter the corresponding number): "):
    # first get a list of all filenames in the current working directory that contain ".csv"
    # i.e. all csv-files in the current working directory...
    files = [f for f in os.listdir('.') if os.path.isfile(f) and ".csv" in f]
    option = 0
    for file in files:  # list all the csv-files
        print("{}: {}".format(option, file))
        option += 1
    if len(files) == 0:
        return ""  # if there are no files, return empty string
    index = read_integer(msg)  # read the selection...
    while index >= len(files):  # while selection is out of bounds...
        print("The given selection doesn't exist, please try again...")
        index = read_integer(msg)
    return files[index]  # return selected file...
