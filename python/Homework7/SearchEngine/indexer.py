#Brandon Marshall       
#Python Scripting
#November 12, 2015
#Homework 7 - Search Engine

import pickle
import shelve

def process_data(shelve_file, shelve_key, data_pickle, web_pickle = ""):
	indexed = {}

	# catch exceptions with loading from the pickle as well as opening the 
	# file to begin with
	try:
		with open(data_pickle, "br") as f:
			try:
				foundData = pickle.load(f)
			except pickle.UnpicklingError:
				print("Problem unpickling object.")
	except IOError as ioe:
		print("Unable to access file: " + ioe.filename)

	for file in foundData:
		path = file[0][0]
		contents = file[0][1]
		words = tuple(contents.split())
		for word in words:
			if word not in indexed.keys():
				indexed[word] = set()

			indexed[word].add(path)

	if web_pickle != "":

		# catch exceptions with loading from the pickle as well as opening the 
		# file to begin with
		try:
			with open(web_pickle, "br") as f:
				try:
					foundData = pickle.load(f)
				except pickle.UnpicklingError:
					print("Problem unpickling object.")
		except IOError as ioe:
			print("Unable to access file: " + ioe.filename)

		for data in foundData:
			url = data[0]
			words = tuple(data[1].split())
			for word in words:
				if word not in indexed.keys():
					indexed[word] = set()

				indexed[word].add(url)

	# catch any exception occurring when attempting to open the shelve
	try:
		s = shelve.open(shelve_file)
	except:
		print("Error opening shelve " + shelve_file)
		return

	s[shelve_key] = indexed
	