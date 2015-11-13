#Brandon Marshall       
#Python Scripting
#November 12, 2015
#Homework 7 - Search Engine

from wsgiref.simple_server import make_server
import sqlite3
# initialize database
#conn = sqlite3.connect("searchengine.sqlite")
#cursor = conn.cursor()
#cursor.execute("create table results (word text, results text)") 
#cursor.execute("insert into results(word, results) values('test', 'http://www.newhaven.edu/test_page')")
#conn.commit()
#conn.close()

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def search_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded:"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		
		if len(form_vals) > 0:
			word = ""
			res = ""
			for item in form_vals.keys():
				message += "<br/>" + item + " = " + form_vals[item]
				if item == "word":
					word = form_vals[item]
				elif item == "results":
					res = form_vals[item]
			
			# now print the whole database to verify
			conn = sqlite3.connect("searchengine.sqlite")
			cursor = conn.cursor()
			message += "<br><h3>Search Results for '" + word + "':</h3><br>"
			results = cursor.execute("select * from results")
			for result in results:
				message += "<p>" + str(result[1]) + "</p>"
			conn.commit()
			conn.close()

	message += "<h1>Search!</h1>"
	message += "<form method='POST'><br>Search Word:<input type=text name='word'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, search_app)
print("Serving on port 8000...")

httpd.serve_forever()