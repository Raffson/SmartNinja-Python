#this file contains a representation for a Vehicle as specified by the assignment
#a Vehicle will have the following data-members:
# -id: a self-maintained data-member to uniquely distinguish
# -brand: indicates the brand of the car, type = str
# -model: indicates the model of the car, type = str
# -km: number of kilometers done so far, type = float
# -lastservice: datetime.date object representing the last service date
import datetime as dt
from copy import deepcopy

_IDgen = 0 #ID generator, increment by 1 for each Vehicle being constructed

class Vehicle(object):
    #constructor for Vehicle,
    #takes 2 mandatory parameters and 2 optional parameters:
    # -brand: mandatory and expected type = str, otherwise raise TypeError
    # -model: mandatory and expected type = str, otherwise raise TypeError
    # -km: optional and expected type = float or int, otherwise raise TypeError
    #   default value for km is 0
    #   absolute value will be taken so negative values will have no effect...
    # -lastservice: optional and expected type = datetime.date or str,
    #                                       otherwise raise TypeError
    #   default value for lastservice is "today's" date
    #   additional check to see if lastservice isn't in the future,
    #                                       otherwise raise ValueError
    def __init__(self, brand, model, km=0, lastservice=dt.datetime.now().date()):
        #type-checking...
        if type(brand) != str \
                or type(model) != str \
                or (type(km) != int and type(km) != float) \
                or not(type(lastservice) == dt.date or type(lastservice) == str):
            raise TypeError
        if type(lastservice) == str: #attempt to construct datetime.date object
            lastservice = lastservice.replace('/', '').replace('-', '')
            lastservice = dt.datetime.strptime(lastservice, "%d%m%Y").date()
        if lastservice > dt.datetime.now().date(): #value-check
            raise ValueError
        #start of actual initialization
        global _IDgen
        self._id = _IDgen #private variable, users should touch this...
        _IDgen += 1
        self._brand = brand.upper()
        self._model = model.upper()
        self._km = abs(float(km))
        self._lastservice = lastservice

    #implements what should happen when str() is called on "this" object
    def __str__(self):
        return "%s - %s with %.2fkm, last serviced at %s" % \
               (self._brand, self._model, self._km, self._lastservice.strftime("%d/%m/%Y"))

    #simple getter for the ID
    def GetID(self):
        return deepcopy(self._id) #return a copy to prevent accidental overwrite...

    #return "Brand - Model"
    def GetName(self):
        return self._brand + " - " + self._model

    def GetKM(self):
        return self._km

    def GetLSDstring(self):
        return self._lastservice.strftime("%d/%m/%Y")

    #methods to edit the number of kilometers,
    #expects 1 mandatory argument:
    # -km: represents the new number of kilometers,
    #       type is expected to be either str, int or float
    #return True if 'self._km' was successfully edited, False otherwise
    def EditKM(self, km):
        if type(km) == str:
            #do some checks to verify valid input...
            if km == "": return False
            km = km[1:] if km[0] == '-' else km #remove '-' sign if present...
            if km.replace('.','',1).isdigit():
                self._km = abs(float(km))
                return True
            else: return False
        elif type(km) == int or type(km) == float:
            self._km = abs(float(km)) #cast to float in case type(km) is int
            #otherwise float() will have no effect
            #but we still want abs() for the absolute value...
            return True
        else:
            return False

    #method to edit the last service date,
    #takes 1 optional argument:
    # -ls: represents the new last service date,
    #       type can either be str or datetime.date
    #   in case type = str, attempt to construct a datetime.date object
    #   in case type = datetime.date, only check if date is valid...
    #return True if 'self._lastservice' was successfully updated, False otherwise
    def EditLastServiceDate(self, ls=dt.datetime.now().date()):
        if type(ls) == str:
            ls = ls.replace("/", "").replace("-", "") #clean dashes&slashes
            try:
                ls = dt.datetime.strptime(ls, "%d%m%Y").date()
            except ValueError:
                return False #meaning a bad string was passed...
        #mind that if type(ls) was initially str and
        #if the value of 'ls' was valid, type(ls) now became dt.date
        if  type(ls) == dt.date:
            #if we get here, we're almost "safe"
            #just need to check if date is valid...
            if ls > dt.datetime.now().date(): return False
            #at this point, we're considered to be "safe"
            self._lastservice = ls
            return True
        else:
            return False

    #a method wich returns "this" Vehicle as a CSV row
    def toCSVrow(self):
        a,b,c = (self._brand, self._model, self._km)
        d = self._lastservice.strftime("%d/%m/%Y")
        return "{},{},{},{}".format(a,b,c,d)

if __name__ == "__main__":
    car1 = Vehicle("BMW", "M3", 150, dt.datetime(2017, 3, 17).date())
    print(car1)
    car1.EditLastServiceDate(dt.datetime(2018, 10, 26).date())
