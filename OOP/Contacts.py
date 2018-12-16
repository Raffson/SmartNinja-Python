#the purpose of this file is to expand the example using datetime
#down at the bottom in the "if __name__ == 'main'" block I'll also
# demonstrate the difference between shallow copy and deep copy
import copy #to demonstrate shallow vs deep copy
import datetime as dt

#a contact class to be used in a 'ContactBook'
# will have 5 data-members (other than what we inherit from 'object'):
#  -firstname: represents the first name of the Contact, type = str
#  -lastname: represents the last name of the Contact, type = str
#  -gender: represents the gender of the Contact, type = str
#  -number: represents  the phone number of the Contact, type = str
#       note that we will not check for the validity of this number
#       this would involve checking the country-code,
#       followed by a "format"-check which is depends on the country
#       some countries may have similar formats,
#       which would allow us to reuse some of the code...
#  -dob: represents the date of birth of the Contact, type = datetime
class Contact(object):
    #constructor for 'Contact'
    #takes 5 mandatory arguments:
    # -firstname: type is expected to be str, raise TypeError otherwise
    # -lastname: type is expected to be str, raise TypeError otherwise
    # -gender: type is expected to be str, raise TypeError otherwise
    #   above that, we'll restrict possible values to "M" & "F" for male and female
    #   otherwise we'll be raising a ValueError
    # -number: type is expected to be str, raise TypeError otherwise
    # -dob: type can either be str or a datetime.date object
    #   in case it's a string, we'll attempt to construct a datetime object
    #   expecting DD-MM-YYYY format, otherwise this may cause an exception
    #   in case it's datetime.date object, just use the given object
    #   for other types we'll raise a TypeError
    #   at last we'll also check that the date of birth
    #   doesn't lie in the future, cause that wouldn't make sense...
    def __init__(self, firstname, lastname, gender, number, dob):
        #first do some type checking...
        if type(firstname) != str: raise TypeError
        if type(lastname) != str: raise TypeError
        if type(gender) != str: raise TypeError
        if type(number) != str: raise TypeError
        if not( type(dob) == str or type(dob) == dt.date): raise TypeError
        #if all types are good, we can start assigning...
        self.firstname = firstname
        self.lastname = lastname
        #what follows is a small value-check...
        gender = gender.upper()
        if not( gender == "M" or gender == "F"): raise ValueError
        self.gender = gender
        self.number = number
        if type(dob) == str: #try to construct a datetime.date object
            dob = dob.replace('-','').replace('/','') #clear the dashes/slashes...
            dob = dt.datetime.strptime(dob, '%d%m%Y').date()
        #and again another value-check...
        if dob > dt.datetime.now().date(): raise ValueError
        self.dob = dob

    #implement what should happen if str() is called on "this" Contact
    def __str__(self):
        #just putting all data-members in temporary variables
        # with short names so that the return statement
        # doesn't become too long...
        a,b,c = (self.firstname, self.lastname, self.gender)
        d,e = (self.number, self.dob.strftime('%d/%m/%Y'))
        return "{} {} ({}) - Phone#: {} - Born: {}".format(a,b,c,d,e)

    #simple method that returns a string "firstname lastname"
    def GetFullName(self):
        return self.firstname + " " + self.lastname

    #simple methods that only returns the last name
    # note that these are only here for demonstration purposes
    # since we could just as well use 'some_contact.lastname'
    # assuming 'some_contact' is an object of type 'Contact'
    def GetLastName(self):
        return self.lastname

    #same as GetLastName
    def GetGender(self):
        return self.gender

    #same as GetLastName
    def GetNumbers(self):
        return self.number

    #return day/month/year as a string
    def GetDateOfBirth(self):
        return self.dob.strftime('%d/%m/%Y')

#now we define a ContactBook
#internally we'll use a dictionary to store our contacts
#other than that, nothing must be provided...
#the idea is that each phone number is unique
#and thus can only belong to one person at a time...
class ContactBook(object):
    #constructor for ContactBook
    #expects no parameters...
    def __init__(self):
        self.book = {} #initilize empty

    #implement what needs to happen in case str() is called on "this" object
    def __str__(self):
        return self.PrintBook()

    #adds a contact to "this" ContactBook
    #expects a parameter of type 'Contact'
    #id the person's phone number already exists in self.book
    # then we simply overwrite the information in self.book
    def AddContact(self, person):
        if type(person) != Contact: raise TypeError
        self.book[person.number] = person

    #returns a string, printing a summary of "this" ContactBook
    def PrintBook(self):
        lines = ""
        for c in self.book:
            line = c + " - " + self.book[c].GetFullName() + "\n"
            lines += line
        if lines == "":
            lines = "ContactBook is empty..."
        return lines

    #given a number, delete the contact associated with that number
    #if the number if not present, nothing will be done
    #returns True if the number & contact were deleted,
    #returns False otherwise
    def DeleteContact(self, number):
        if self.book.has_key(number):
            del self.book[number]
            return True
        return False

    #edits a contact given a number
    #this method takes 1 mandatory parameter and 5 optional parameters:
    # -number: mandatory parameter, represents the contact's current phone number
    #   this is needed to identify the contact that needs to be edited...
    #   if the number is not present in the ContactBook, nothing is done...
    # -first: optional argument, if type is different from str,
    #   we simply adopt the old value and thus not editing the contact
    # -last: same as first...
    # -gender: same as first, except we also check for "M" & "F"
    # -fnumber: same as first...
    # -dob: same as first, except type can also be datetime.date
    #   also checking for invalid dates, i.e. dates in the future
    #returns True on a successful edit, False otherwise
    def EditContact(self, number, first=None, last=None, gender=None, fnumber=None, dob=None):
        if self.book.has_key(number):
            self.book[number].firstname = first if type(first) == str else self.book[number].firstname
            self.book[number].lastname = last if type(last) == str else self.book[number].lastname
            self.book[number].gender = gender if type(gender) == str and (gender == "M" or gender == "F") else self.book[number].gender
            self.book[number].number = fnumber if type(number) == str else self.book[number].number
            if type(dob) == str:
                dob = dob.replace('-','').replace('/','')
                self.book[number].dob = dt.datetime.strptime(dob, '%d%m%Y').date()
            elif type(dob) == dt.date:
                self.book[number].dob = dob
            if number != fnumber: #if the number changed, remove the old one...
                self.book[fnumber] = self.book[number]
                del self.book[number]
            return  True
        return False


#now some examples of how Contact and ContactBook work...
if __name__ == "__main__":
    #first, let's create 3 contacts...
    #the first two are the same, yet they are different objects...
    p1 = Contact("john", "doe", number="0123456789", gender="M", dob="16/12/1985")
    p2 = Contact("john", "doe", number="0123456789", gender="M", dob="16/12/1985")
    p3 = Contact("jane", "doe", number="9876543210", gender="F", dob="25/12/1985")

    #now let's demonstrate the difference between shallow copy and deep copy
    #first, 2 ways of checking if 2 objects are actually the same,
    #i.e. they share the same address & thus only 1 actual object is "alive"
    print("Same object" if id(p1) == id(p2) else "Different object")
    print("Same object" if p1 is p2 else "Different object")
    print("id(p1) = {}    id(p2) = {}".format(id(p1),id(p2)))
    print("executing 'p2 = p1', i.e. shallow copy...")
    p2 = p1
    print("id(p1) = {}    id(p2) = {}".format(id(p1),id(p2)))
    #now let's do a deep copy,
    #note that originally p2 was in fact a copy,
    #yet "lived" in a different address
    #the same phenomenon will present itself...
    print("executing 'p2 = copy.deepcopy(p1)', i.e. deep copy...")
    p2 = copy.deepcopy(p1)
    print("id(p1) = {}    id(p2) = {}".format(id(p1),id(p2)))

    #now some examples of how to use and manipulate a Contact object
    print(p2.GetFullName())
    p2.firstname = "Test" #note that changing members like this won't trigger type checking...
    print(p2.GetFullName())
    print(p2.GetDateOfBirth())
    print(p2.dob)
    print(p2)

    #some examples for ContactBook
    cbook = ContactBook()
    #first, let's show that cbook.PrintBook() returns the same as str(cbook)
    print(cbook) #implicitly calls str() on cbook
    print(cbook.PrintBook()) #cbook.PrintBook() returns a string...
    #now let's add some contacts, jane & john...
    cbook.AddContact(p1)
    cbook.AddContact(p3)
    print(cbook)
    #now notice how p2 will overwrite p1 since the same number is used...
    cbook.AddContact(p2)
    print(cbook)

    #now let's delete a contact...
    cbook.DeleteContact("0123456789")
    print(cbook)
    #and add p1 again...
    cbook.AddContact(p1)

    #now lets edit p1, notice how gender is left unchanged in the output
    cbook.EditContact("0123456789", last="doeee", first="joooohn", gender="invalid", fnumber="1122334455")
    print(cbook)
