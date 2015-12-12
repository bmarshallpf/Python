#Brandon Marshall       
#Python Scripting
#November 20, 2015
#Homework 8 - Search Engine

from flask import Flask, jsonify, request, abort
from searcher import perform_database_search, parse_terms

app=Flask(__name__)

#data=[{'fname':'Steve', 'lname':'Jobbs'},{'fname':'Bill', 'lname':'Gates'}]

@app.route('/data', methods=['GET'])
def get_data():
	return jsonify({'data' : data})

@app.route('/data/<int:id>', methods=['GET'])
def get_data_byid(id):
	return jsonify({'data' : data[id]})

@app.route('/search/<search_term>', methods=['GET'])
def get_results(search_term):
	values = parse_terms(search_term)
	terms = values['terms']
	hasAnd = values['hasAnd']
	hasOr = values['hasOr']
	results = perform_database_search(terms, hasOr, hasAnd)
	data = []
	count = 1
	for result in results:
		res_str = str(result)
		if len(res_str) > 0:
			temp = { str('Result ' + str(count)): str(result) }
			data.append(temp)
			count += 1
	return jsonify({'Search_Results' : data})

app.run()