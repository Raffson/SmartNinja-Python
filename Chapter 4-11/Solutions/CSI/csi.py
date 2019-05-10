'''
A possible solution to the CSI problem,
however csi-short.py contains a simpler and more efficient solution
We can confirm this by measuring the runtime of each version,
but note that the runtime is not always the same,
so run it 10 or 20 times to get an idea of the average runtime...
Avg runtime of 0.000190 seconds on my machine...
'''

import datetime as dt

start = dt.datetime.now()

#first we need to put our given data into a suitable data-structure
#in this case we use dictionaries to map human properties to their respective dna-sequence
hair = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
face = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eyes = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

#map each person to a list of properties describing the person at hand...
#mind that the order of properties in the list is important
people = {"eva" : ["female", "white", "blonde", "blue", "oval"],
          "larisa" : ["female", "white", "brown", "brown", "oval"],
          "matej" : ["male", "white", "black", "blue", "oval"],
          "miha" : ["male", "white", "brown", "green", "square"]}

dna = open("dna.txt", "r").read() #read the dna file
person = [] #will represent our suspect...

#now we check properties in the same order
for i in gender: #check all genders, i.e. male & female
    #now check the gender[i] is a substring of dna,
    #i.e. does dna contain gender[i]...
    if gender[i] in dna: #if the current gender is present in the dna
        print(i)
        person.append(i) #add this property to our suspect
for i in race: #check all races...
    if race[i] in dna: #same idea as gender, only 1 race will match
        print(i)
        person.append(i)
for i in hair:
    if hair[i] in dna:
        print(i)
        person.append(i)
for i in eyes:
    if eyes[i] in dna:
        print(i)
        person.append(i)
for i in face:
    if face[i] in dna:
        print(i)
        person.append(i)

#now we have a description of our suspect,
#so now check who corresponds to this description...
for p in people:
    if people[p] == person:
        print("The person we're looking for is %s" % p.upper())
        break

end = dt.datetime.now()
print(f"Runtime = {end-start}")