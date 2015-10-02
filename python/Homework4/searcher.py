#Brandon Marshall       
#Python Scripting
#October 1, 2015
#Homework 4 - File Traverser

import time
import shelve

def search(shelve_to_process, shelve_key):

	# start timing of search functionality
	start_time = time.perf_counter() * 1000

	s = shelve.open(shelve_to_process)
	indexedFiles = s[shelve_key]

	query = input("query:")
	terms = query.split(" ")

	hasOr = False
	hasAnd = "and" in terms
	if not hasAnd:
		hasOr = "or" in terms
		if not hasOr:
			hasAnd = True

	#remove the delimiter terms now
	while "and" in terms:
		terms.remove("and")
	while "or" in terms:
		terms.remove("or")

	goodFiles = set()

	if hasOr:
		for term in terms:
			goodFiles = goodFiles.union(indexedFiles[term])

	if hasAnd:
		for term in terms:
			if term in indexedFiles:
				if len(goodFiles) == 0:
					goodFiles.update(indexedFiles[term])
				else:
					goodFiles = goodFiles.intersection(indexedFiles[term])

	# finish timing of search functionality
	end_time = time.perf_counter() * 1000

	# print the output
	word = "OR" if hasOr else "AND"

	print("Performing " + word + 
	   " search for: {\'" + '\', \''.join(terms) + "\'}")

	if len(goodFiles) == 0:
		print("Sorry, no files found with that query!")
	else:
		for gf in goodFiles:
			print("Found at", gf)

	print("Execution time:", int(end_time - start_time))