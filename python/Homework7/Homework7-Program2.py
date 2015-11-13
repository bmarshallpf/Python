#Brandon Marshall       
#Python Scripting
#November 12, 2015
#Homework 7 - Program 2

from wsgiref.simple_server import make_server
import sqlite3

# initialize database
#conn = sqlite3.connect("zoo.sqlite") #create connection to zoo.sqlite database, creates the database if it doesn't already exist
#cursor = conn.cursor() #provides are cursor to the above connection (the means of executing the SQL queries)
#cursor.execute("create table animal_count (name text, count integer)") #execute the create table query
#cursor.execute("insert into animal_count(name, count) values('Elephant', 3)") #inset a row into the animal_count table
#cursor.execute("insert into animal_count(name, count) values('Crocodile', 5)")
#conn.commit() #commit changes to the database
#conn.close() #close the connection

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def zoo_app(environ, start_response):
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
			conn = sqlite3.connect("zoo.sqlite")
			cursor = conn.cursor()
			
			animal = ""
			count = 0
			for item in form_vals.keys():
				message += "<br/>"+item + " = " + form_vals[item]
				if item == "animal":
					animal = form_vals[item]
				elif item == "count":
					count = int(form_vals[item])
			
			if animal and count > 0:
				cursor.execute("insert into animal_count(name, count) values('" + animal + "', " + str(count) + ")")
				conn.commit()

				# now print the whole database to verify
				message += "<br><h3>Zoo Animals:</h3><br>"
				results = cursor.execute("select * from animal_count")
				for res in results:
					message += "<li>" + str(res) + "</li>"
				conn.commit()
				conn.close()
	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, zoo_app)
print("Serving on port 8000...")

httpd.serve_forever()