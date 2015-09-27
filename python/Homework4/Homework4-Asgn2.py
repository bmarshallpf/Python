#Brandon Marshall       
#Python Scripting
#September 26, 2015
#Homework 4 - Assignment 2 - Security Scanner

import os

file_name = input("Enter a file name: ")

found = False

if os.path.exists(file_name):
	file = open(file_name, "r")
	while True:
		s = file.readline()
		if not s:
			break;
		if "password=" in s:
			found = True
			print("Found a password!")
			break;

	if not found:
		print("No password found in the file.")
else:
	print("Sorry - that file doesn't exist")