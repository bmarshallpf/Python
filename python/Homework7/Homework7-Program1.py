#Brandon Marshall       
#Python Scripting
#November 11, 2015
#Homework 7 - Program 1

import psutil, datetime

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

print("\nBOOT TIME:", boot_time)

cpu_util = psutil.cpu_percent(interval=1, percpu=True)

i=1
print("\nCPU UTILIZATION:")
for cpu in cpu_util:
	print("CPU {} : {}%".format(i, cpu))
	i+=1


mem = psutil.virtual_memory()
THRESHOLD = 100 * 1024 * 1024  # 100MB
print("\nAVAILABLE MEMORY:", mem.available)
print("USED MEMORY:", mem.used)
print("USED PERCENTAGE:", mem.percent)

# Added by Brandon
print("\nUSERS: ")
for usr in psutil.users():
	print(usr)

print("\nPIDS: ", psutil.pids())

print("\nDISK PARTITIONS: ")
for part in psutil.disk_partitions():
	print(part)