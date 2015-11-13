#Brandon Marshall       
#Python Scripting
#November 11, 2015
#Homework 7 - Program 1

import psutil, datetime

# retrieve data
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
cpu_util = psutil.cpu_percent(interval=1, percpu=True)
mem = psutil.virtual_memory()
THRESHOLD = 100 * 1024 * 1024  # 100MB
users = psutil.users()
cpu_percent = psutil.cpu_percent()
pids = psutil.pids()
partitions = psutil.disk_partitions()

first = "<tr><td bgcolor=\"green\">"
middle = "</td><td bgcolor=\"#89C35C\">"
end = "</td></tr>"

text = "<table border=1>"
text = text + first + "BOOT TIME" + middle + str(boot_time) + end
text = text + first + "CPU UTILIZATION" + middle
i = 1
for cpu in cpu_util:
	text = text + "<li>CPU {} : {}%".format(i, cpu) + "</li>"
	i+=1
i = 1
text = text + end
text = text + first + "AVAILABLE MEMORY" + middle + str(mem.available) + end
text = text + first + "USED MEMORY" + middle + str(mem.used) + end
text = text + first + "USED PERCENTAGE" + middle + str(mem.percent) + "%" + end
text = text + first + "CPU PERCENT" + middle + str(cpu_percent) + "%" + end
text = text + first + "USERS" + middle + str(users[0].name) + end
text = text + first + "PIDS (First 10)" + middle
i = 1
for pid in pids:
	text = text + "<li>" + str(pid) + "</li>"
	i += 1
	if i > 10:
		break
i = 1
text = text + end
text = text + first + "DISKS" + middle
i = 1
for part in partitions:
	text = text + "<li>" + str(part.device) + "</li>"
	i += 1
text = text + end
text = text + "</table>"

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self): 
		self.send_response(200)
		self.end_headers()
		self.wfile.write(str.encode(text))
		return

server = HTTPServer(("", 8000), MyHTTPRequestHandler)
server.serve_forever()