"""
Simple example on how to read a json file, just like in the curriculum...
"""
import json

with open("people.json") as file:
    data = json.load(file)

print(data)

for user in data:
    print(user["first_name"] + " " + user["last_name"] + " " + user["email"])
