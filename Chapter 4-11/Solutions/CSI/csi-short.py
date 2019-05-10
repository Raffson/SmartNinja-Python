'''
Another possible solution to the CSI problem,
this solution ought to be simpler and more efficient solution
We can confirm this by measuring the runtime of each version,
but note that the runtime is not always the same,
so run it 10 or 20 times to get an idea of the average runtime...
Avg runtime of 0.000150 seconds on my machine...
'''

import datetime as dt

start = dt.datetime.now()

# map each person to a list of DNA sequences,
# each describing the properties of the person at hand...
# since everybody is white, we can technically leave "race" out
# but for demonstration purposes we'll simply keep it...
people = {"eva" : ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "larisa" : ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "matej" : ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "miha" : ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

dna = open("dna.txt", "r").read() #read the dna file

#simply check if all properties of a person appear in the DNA string
#as soon as one of the person's properties doesn't appear in the DNA string,
#we know that this person is innocent...
#only the real perpetrator will have all his/her properties in the DNA string
for person in people:
    suspect = True
    for prop in people[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect == True:
        print("%s is our perpetrator!" % person.upper())

end = dt.datetime.now()
print(f"Runtime = {end-start}")