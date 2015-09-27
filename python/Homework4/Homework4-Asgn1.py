#Brandon Marshall       
#Python Scripting
#September 26, 2015
#Homework 4 - Assignment 1

import os

start_dir = input("Enter a start path: ")
file = input("Enter a file name: ")

found = False

if (os.path.exists(start_dir)):
	for dirpath, dirs, files in os.walk(start_dir):
		for single_file in files:
			if single_file == file:
				print("Found the file here: " + os.path.join(dirpath, single_file))
				found = True
				break

	if not found:
		print("Sorry - the file was not found.")
else:
	print("Sorry - the path does not exist.")