#Brandon Marshall       
#Python Scripting
#November 12, 2015
#Homework 7 - Search Engine

import os
import fnmatch
import pickle

def get_traversal_data():
	found = False
	foundFiles = []

	start_dir = "C:\\Users\\Marshall\\Documents\\School\\PythonProgramming\\fortune1"

	if (os.path.exists(start_dir)):
		for dirpath, dirs, files in os.walk(start_dir):
			for single_file in files:
				if fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log"):
					f = open(os.path.join(dirpath, single_file), "r")
					foundFiles.append([(os.path.abspath(single_file), f.read())])
					found = True
		if not found:
			print("Sorry - the file was not found.")
	else:
		print("Sorry - the path does not exist.")

	return foundFiles