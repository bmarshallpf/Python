#Brandon Marshall       
#Python Scripting
#October 5, 2015
#Homework 5 - Task 4

def formatTemp(kelvin):
	return "{:.0f}".format(kelvin * (9/5) - 459.67) + "F"

import urllib.request
import json
import datetime
from pprint import pprint

query = input("What location do you want the weather for? ")
query = query.replace(" ", "%20")
#query = "Mystic,%20CT"

page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=" + query)
#page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + query)
content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)

count = 0
query = query.replace("%20", " ")
print("Weather Forecast for " + query);

try:
	curDay = 0
	while (True):
		time = json_data["list"][count]["dt_txt"]
		dt = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
		if curDay != dt.day:
			print("\n" + dt.strftime("%A") + " " + dt.strftime('\n%b %d:'))
			curDay = dt.day
		formattedDT = dt.strftime('%I:%M %p')
		main = json_data["list"][count]["weather"][0]["main"]
		desc = json_data["list"][count]["weather"][0]["description"]
		temp = json_data["list"][count]["main"]["temp"]
		#min = json_data["list"][count]["main"]["temp_min"]
		#max = json_data["list"][count]["main"]["temp_max"]
		humid = json_data["list"][count]["main"]["humidity"]
		press = json_data["list"][count]["main"]["pressure"]

		print(formattedDT + " " + main + " - " + desc)
		print("\tTemp: " + formatTemp(temp))
		print("\tHumidity: " + str(humid) + "%")
		print("\tPressure: " + "{:.2f}".format(press))
	   # + " [" + formatTemp(min) + " to " + formatTemp(max) + "]")
		count = count + 1
except ValueError:
	print("The end.")
except IndexError:
	print("The end.")

#pprint(json_data)