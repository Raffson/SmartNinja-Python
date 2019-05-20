from urllib.request import urlopen #python3 version of "import urllib2"
from bs4 import BeautifulSoup #BeautifulSoup4
import ssl #needed for 'context'

context = ssl._create_unverified_context() #needed for python3
url = "https://scrapebook22.appspot.com/" #variable for our url
response = urlopen(url, context=context).read().decode() #returns html-code
#print(response)
soup = BeautifulSoup(response, 'html.parser') #parses the html-code & creates a BeautifulSoup object
#this BeautifulSoup object will allow us to easily find elements/tags in the html-code,
#as well as allow you to extract data from it...
#print(soup.html.head.title.string)

people = {} #key=name, value = [gender, age, city, email]
for link in soup.findAll("a"): #loop over all links
    if link.string == "See full profile": #only those links to full profiles
        person_url = url[:-1] + link["href"] #create a new url
        person_html = urlopen(person_url, context=context).read().decode() #returns the html-code of the full profile
        person_soup = BeautifulSoup(person_html, 'html.parser') #parse the html-code & create BeautifulSoup object
        ul = person_soup.find("ul") #find the unordered list
        name = ul.findPreviousSibling("h1").string #ul's previous h1 sibling contains the name
        #notice that there is more than 1 <h1> title in the html-code...
        people[name] = [] #initialize empty list for person with 'name'
        for child in ul: #for each child in <ul>
            if len(child) == 1 and str(child) == "\n": continue #skip empty elements
            elif len(child) == 1: #special case 'Age'
                #no type-checking because we're writing a scraper for 1 particular website
                #if we want a more generic scraper, we'll need to pull out more tricks out of our hat...
                people[name].append(int(child.string.split(':')))
                continue
            people[name].append(child.find("span").string) #extract the value from the span element

#print in CSV format...
print("name,gender,age,city,email")
for person in people:
    line = person
    for prop in people[person]:
        line += ",{}".format(prop)
    print(line)