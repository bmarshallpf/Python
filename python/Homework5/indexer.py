#Brandon Marshall       
#Python Scripting
#October 1, 2015
#Homework 4 - File Traverser

import pickle
import shelve

def process_data(shelve_file, shelve_key, data_pickle, web_pickle = ""):
	indexed = {}

	f = open(data_pickle, "br")
	foundData = pickle.load(f)
	f.close()

	for file in foundData:
		path = file[0][0]
		contents = file[0][1]
		words = tuple(contents.split())
		for word in words:
			if word not in indexed.keys():
				indexed[word] = set()

			indexed[word].add(path)

	if web_pickle != "":
		f = open(web_pickle, "br")
		foundData = pickle.load(f)
		f.close()

		for data in foundData:
			url = data[0]
			words = tuple(data[1].split())
			for word in words:
				if word not in indexed.keys():
					indexed[word] = set()

				indexed[word].add(url)

	s = shelve.open(shelve_file)
	s[shelve_key] = indexed