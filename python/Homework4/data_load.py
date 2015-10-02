#Brandon Marshall       
#Python Scripting
#October 1, 2015
#Homework 4 - File Traverser

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

	out = open("raw_data.pickle", "bw")
	pickle.dump(foundFiles, out)
	out.close()

	# for testing
	#for f in foundFiles:
	#	print(f[0][0])
	#	print('\n')
	#	print(f[0][1])
	#	print('\n')