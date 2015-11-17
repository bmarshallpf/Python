#Brandon Marshall       
#Python Scripting
#November 12, 2015
#Homework 7 - Search Engine

import time
import shelve
import sqlite3

def search(shelve_to_process, shelve_key):

	# start timing of search functionality
	start_time = time.perf_counter() * 1000

	# catch any exception occurring when attempting to open the shelve
	try:
		s = shelve.open(shelve_to_process)
	except:
		print("Error opening shelve " + shelve_to_process)
		return
	
	# catch a key error if the shelve doesn't contain the specified key
	try:
		indexedFiles = s[shelve_key]
	except KeyError as ke:
		print("Could not find the specified key in the shelve: " + shelve_to_process + "\n" + str(ke.args[0]))
		return

	keepGoing = True
	while keepGoing:
		query = input("Options: \n. > exit\nf > forecast\ns > search\nSelection:")
		
		# raise exception to prevent user to search for numbers
		try:
			if query.isdigit():
				raise SyntaxError("Search term can't be a number!\n")
		except SyntaxError as e:
			print(e.msg)
			continue
		
		if query == '.':
			keepGoing = False
		elif query == 'f':
			import weather_forecast
		elif query == 's':
			query = input("Search for: ")

			values = parse_terms(query)
			terms = values['terms']
			hasAnd = values['hasAnd']
			hasOr = values['hasOr']

			word = "OR" if hasOr else "AND"
			print("\nPerforming " + word + " search for: {\'" + '\', \''.join(terms) + "\'}")
			print("\nNormal Search:")
			perform_search(terms, indexedFiles, start_time, hasOr, hasAnd)
			print("\nDatabase Search:")
			perform_database_search(terms, start_time, hasOr, hasAnd)
			print('\n')

def perform_database_search(terms, start_time, hasOr, hasAnd):
	conn = sqlite3.connect("searchengine.sqlite")
	cursor = conn.cursor()

	if hasOr:
		term = "'" + terms[0] + "'"
		for i, t in enumerate(terms):
			if i > 0:
				term += " OR word = '" + t + "'"
		allResults = cursor.execute("select * from results where word = " + term)
	
	if hasAnd:
		term = '%' + terms[0] + '%'
		for i, t in enumerate(terms):
			if i > 0:
				term += " AND results like %" + t + "%"
		allResults = cursor.execute("select * from results where results like ?", (term,))

	# finish timing of search functionality
	end_time = time.perf_counter() * 1000

	# print the output
	
	for result in allResults:
		print("Found at", result[1])	

	conn.close()

	print("Execution time:", int(end_time - start_time))

def perform_search(terms, indexedFiles, start_time, hasOr, hasAnd):
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

	if len(goodFiles) == 0:
		print("Sorry, no files found with that query!")
	else:
		for gf in goodFiles:
			print("Found at", gf)

	print("Execution time:", int(end_time - start_time))

def parse_terms(query):
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

	return { 'terms':terms, 'hasAnd':hasAnd, 'hasOr':hasOr }

