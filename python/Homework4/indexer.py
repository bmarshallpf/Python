#Brandon Marshall       
#Python Scripting
#October 1, 2015
#Homework 4 - File Traverser

import pickle
import shelve

def process_data(pickle_file, shelve_file, shelve_key):
	f = open(pickle_file, "br")
	foundFiles = []
	foundFiles = pickle.load(f)
	f.close()

	indexed = {}

	for file in foundFiles:
		path = file[0][0]
		contents = file[0][1]
		words = tuple(contents.split())
		for word in words:
			if word not in indexed.keys():
				indexed[word] = set()

			indexed[word].add(path)

	s = shelve.open(shelve_file)
	s[shelve_key] = indexed