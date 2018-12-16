#this file will contain some helper functions to deal with input
#via the command-line interface, making sure the input is valid...
import datetime as dt

#define a list of illegal characters w.r.t. filenames
_illegalchars = ['\\', '/', '?', '%', '*', ':', '|', '\"', '<', '>']

#will read & return a float, negative sign will simply be ignored...
# thus returning only positive floats
def read_positive_float(msg="Enter a real number: "):
    f = raw_input(msg)
    if f != "" and f[0] == '-': f = f[1:]
    while f == "" or not f.replace('.','',1).isdigit():
        print("Invalid number was given, please try again...")
        f = raw_input(msg)
    return float(f)

#will read & return a datetime.date object
def read_date(msg = "Enter a date (D-M-Y): ", no_future=True):
    ls = raw_input(msg)
    while type(ls) != dt.date:
        ls = ls.replace("/", "").replace("-", "") #remove dashes&slashes
        dataformat = "%d%m%Y"
        if len(ls) <= 6: #meaning we're using a 2-digit year
            dateformat = "%d%m%y"
        try: #wondering if we could do our own value-checks instead...
            ls = dt.datetime.strptime(ls, dateformat).date()
        except ValueError:
            print("The given date is invalid, please try again...")
            ls = raw_input(msg)
    if no_future and ls > dt.datetime.now().date():
        print("Given date is in the future, overwriting with today's date...")
        ls = dt.datetime.now().date()
    return ls

#will read & return an integer
def read_integer(msg="Enter an integer: "):
    id = raw_input(msg)
    while not id.isdigit():
        print("The given input is invalid, please try again...")
        id = raw_input(msg)
    return int(id)

def read_filename(msg="Enter a filename: "):
    inp = raw_input(msg)
    while any(letter in inp for letter in _illegalchars):
        print("Invalid filename was specified, please try again...")
        inp = raw_input(msg)
    return inp
