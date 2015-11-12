#Brandon Marshall       
#Python Scripting
#November 11, 2015
#Homework 7 - Program 1

import psutil, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen

# retrieve data
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
cpu_util = psutil.cpu_percent(interval=1, percpu=True)
mem = psutil.virtual_memory()
THRESHOLD = 100 * 1024 * 1024  # 100MB
users = psutil.users()
cpu_percent = psutil.cpu_percent()
pids = psutil.pids()
partitions = psutil.disk_partitions()

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self): 
		self.send_response(200)
		self.end_headers()

		text = "\nBOOT TIME: " + str(boot_time)
		self.wfile.write(str.encode(text))

		text = "\n\nCPU UTILIZATION:"
		self.wfile.write(str.encode(text))
		i=1
		for cpu in cpu_util:
			text = "\nCPU {} : {}%".format(i, cpu)
			self.wfile.write(str.encode(text))
			i+=1

		text = "\n\nAVAILABLE MEMORY: " + str(mem.available)
		self.wfile.write(str.encode(text))
		text = "\n\nUSED MEMORY: " + str(mem.used)
		self.wfile.write(str.encode(text))
		text = "\n\nUSED PERCENTAGE: " + str(mem.percent) + "%"
		self.wfile.write(str.encode(text))

		# Added by Brandon
		text = "\n\nUSERS (name): "
		self.wfile.write(str.encode(text))
		for user in users:
			text = str(user.name)
			self.wfile.write(str.encode(text))

		text = "\n\nCPU PERCENT: " + str(cpu_percent) + "%"
		self.wfile.write(str.encode(text))

		text = "\n\nPIDS:\n" + str(pids)
		self.wfile.write(str.encode(text))

		text = "\n\nDISK PARTITIONS:\n"
		self.wfile.write(str.encode(text))
		for part in partitions:
			text = str(part) + "\n"
			self.wfile.write(str.encode(text))

		return

server = HTTPServer(("", 8000), MyHTTPRequestHandler)
server.serve_forever()