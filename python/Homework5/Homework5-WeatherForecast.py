#Brandon Marshall       
#Python Scripting
#October 5, 2015
#Homework 5 - Task 4

import urllib.request
import json
from pprint import pprint

#query = input("What location do you want the weather for? ")
#query = query.replace(" ", "%20")
query = "Mystic,%20CT"

page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=" + query)
#page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + query)
content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)

count = 0
print("Weather Forecast for " + query + '\n');

try:
	while (True):
		time = json_data["list"][count]["dt_txt"]
		main = json_data["list"][count]["weather"][0]["main"]
		desc = json_data["list"][count]["weather"][0]["description"]
		print(time + " " + main + " - " + desc)
		count = count + 1
except ValueError:
	print("The end.")
except IndexError:
	print("The end.")

#pprint(json_data)