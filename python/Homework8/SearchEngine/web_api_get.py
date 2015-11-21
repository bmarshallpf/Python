#Brandon Marshall       
#Python Scripting
#November 20, 2015
#Homework 8 - Search Engine

from flask import Flask, jsonify, request, abort
from searcher import perform_database_search, parse_terms

app=Flask(__name__)

data=[{'fname':'Steve', 'lname':'Jobbs'},{'fname':'Bill', 'lname':'Gates'}]

@app.route('/data', methods=['GET'])
def get_data():
	return jsonify({'data' : data})

@app.route('/data/', methods=['GET'])
def get_data_byid(id):
	return jsonify({'data' : data[id]})

@app.route('/search/', methods=['GET'])
def get_results(search_term):
	values = parse_terms(search_term)
	terms = values['terms']
	hasAnd = values['hasAnd']
	hasOr = values['hasOr']
	results = perform_database_search(terms, hasOr, hasAnd)
	data = list()
	for i, result in enumerate(results):
		data.append({'result' + str(i), str(result)})
	return jsonify({'data' : data[search_term]})

app.run()