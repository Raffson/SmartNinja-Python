"""
Slightly expanded example using the OpenWeatherMap API
"""
import json
from urllib.request import urlopen  # to send & receive over HTTP
import api_key as ak  # File containing my API key, file is in gitignore to avoid pushing it

api_key = ak.apikey  # insert your own API key!!! (as a string)

response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&units=metric&appid=' + api_key)

print(response)  # checking what comes out => <http.client.HTTPResponse object at 0xADRESS>

response = response.read()  # reads the actual response

data = json.loads(response)  # since response is in json format

print(type(data))  # double check the type of the data => dictionary

print(data)  # printing the whole dictionary

# extract some specific stuff regarding the current weather
print(f"{data['name']} has ID={data['id']} and the weather is:")
print(f"{data['weather']}")
print(f"Temperature = {data['main']['temp']}°C")
print(f"Pressure = {data['main']['pressure']} millibar")
print(f"Humidity = {data['main']['humidity']}%")

# now let's try getting imperial data instead of metric...
response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&units=imperial&appid=' + api_key)
response = response.read()
data = json.loads(response)
print(f"Temperature = {data['main']['temp']}°F")
print(f"Pressure = {data['main']['pressure']} millibar")
print(f"Humidity = {data['main']['humidity']}%")
