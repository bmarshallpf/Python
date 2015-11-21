#Brandon Marshall       
#Python Scripting
#November 19, 2015
#Homework 8 - Search Engine

import time
import shelve
import sqlite3

def search(shelve_to_process, shelve_key):
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
		query = input("Options: \n. > exit\na > REST API\nw > web search\ns > search\nf > forecast\nSelection:")
		
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
		elif query == 'w':
			import web_search
		elif query == 'a':
			import web_api_get
		elif query == 's':
			query = input("Search for: ")

			values = parse_terms(query)
			terms = values['terms']
			hasAnd = values['hasAnd']
			hasOr = values['hasOr']

			word = "OR" if hasOr else "AND"
			print("\nPerforming " + word + " search for: {\'" + '\', \''.join(terms) + "\'}")
			print("\nNormal Search:")
			perform_search(terms, indexedFiles, hasOr, hasAnd)
			print("\nDatabase Search:")
			dbResults = perform_database_search(terms, hasOr, hasAnd)
			# print the output
			for result in dbResults:
				print("Found at", result)
			print('\n')

def perform_database_search(terms, hasOr, hasAnd):
	# start timing of search functionality
	start_time = time.perf_counter() * 1000

	conn = sqlite3.connect("searchengine.sqlite")
	cursor = conn.cursor()

	if hasOr:
		term = "'" + terms[0] + "'"
		for i, t in enumerate(terms):
			if i > 0:
				term += " OR word = '" + t + "'"
		# select * from results where word = 'enrollment' or word = 'risen'
		allResults = cursor.execute("select * from results where word = " + term)
	
	oneTerm = True
	if hasAnd:
		term = "'" + terms[0] + "'"
		for i, t in enumerate(terms):
			if i > 0:
				term += " OR word = '" + t + "'"
				# we have at least 2 terms
				oneTerm = False
				
		# select * from results where word like '%enrollment%' or word like '%risen%'
		allResults = cursor.execute("select * from results where word = " + term)

	# finish timing of search functionality
	end_time = time.perf_counter() * 1000
	print("Execution time:", int(end_time - start_time))

	theResults = set()
	if hasOr:
		for result in allResults:
			theResults.add(result[1])

	oneResult = True
	if hasAnd:
		temp = dict()
		for result in allResults:
			temp[result[0]] = str(result[1]).split(', ')
		valList = list(temp.values())
		for i, tempStrs in enumerate(valList):
			if i == 0:
				# initially populate the results collection from first word results
				for ts in tempStrs:
					theResults.add(ts)
			else:
				# we have more than one result
				oneResult = False
				for res in theResults.copy():
					if res not in tempStrs:
						# not a part of the next word results, so remove
						theResults.remove(res)

		# handle the use case where they searched for more than one term but only one set of results 
		# was found because only one word existed in the database
		if not oneTerm and oneResult:
			theResults.clear()

	conn.close()

	return theResults

def perform_search(terms, indexedFiles, hasOr, hasAnd):
	# start timing of search functionality
	start_time = time.perf_counter() * 1000

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
	if '+' in query:
		# web sends + instead of space
		terms = query.split("+")
	else:
		# search from terminal sends spaces
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

