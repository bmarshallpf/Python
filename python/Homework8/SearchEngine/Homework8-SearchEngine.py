#Brandon Marshall       
#Python Scripting
#November 19, 2015
#Homework 8 - Search Engine

import urllib.request
from urllib.error import  URLError
import re

def sanitize(str1):
	cleanStr = str.replace(str1, u"\u2018", "'")
	cleanStr = str.replace(str1, u"\u2019", "'")
	return cleanStr

def visit_url(url, domain, returnList):
	global crawler_backlog
	if(len(crawler_backlog) > 10):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_headers = re.compile('<h\d>(?P<header>(.*))</h\d>')
			regexp_span = re.compile('<span*>(?P<span>(.*))</span>')
			regexp_para = re.compile('<p*>(?P<para>(.*))</p>')
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)

			if result:
				title = result.group("title")
				returnList.append([url, title])

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				returnList.append([url, keywords])

			for headers in re.findall(regexp_headers, content_string):
				headerSet = set(headers)
				for header in headerSet:
					header = sanitize(header)
					returnList.append([url, header])

			for spans in re.findall(regexp_span, content_string):
				for span in spans:
					span = sanitize(span)
					returnList.append([url, span])

			for paras in re.findall(regexp_para, content_string):
				paraSet = set(paras)
				for para in paraSet:
					para = sanitize(para)
					returnList.append([url, para])

			for (urls) in re.findall(regexp_url, content_string):
				if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
					crawler_backlog[urls] = 0
					visit_url(urls, domain, returnList)

	except URLError as e:
		print("error")

	return returnList

from data_load import get_traversal_data
import indexer
import searcher
import pickle

crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
returnList = []
file_data = get_traversal_data()
web_data = visit_url(seed, "www.newhaven.edu", returnList)

webPickle = "raw_web.pickle"
dataPickle = "raw_data.pickle"

# catch exceptions dealing with pickling the objects, as well as catching 
# any exceptions dealing with opening the file to begin with
try:
	with open(webPickle, "bw") as out:
		try:
			pickle.dump(web_data, out)
		except pickle.PicklingError:
			print("Unpicklable object passed into dump().")
except IOError as ioe:
	print("Unable to write to file: " + ioe.filename)

# catch exceptions dealing with pickling the objects, as well as catching 
# any exceptions dealing with opening the file to begin with
try:
	with open(dataPickle, "bw") as out:
		try:
			pickle.dump(file_data, out)
		except pickle.PicklingError:
			print("Unpicklable object passed into dump().")
except IOError as ioe:
	print("Unable to write to file: " + ioe.filename)

indexer.process_data("unh_shelve", "indexed_files", dataPickle, webPickle)
searcher.search("unh_shelve", "indexed_files")