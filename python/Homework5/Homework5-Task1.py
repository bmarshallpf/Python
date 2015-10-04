#Brandon Marshall       
#Python Scripting
#October 3, 2015
#Homework 5 - Task 1

import urllib.request
from urllib.error import  URLError
import re

def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>10):
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
				print("title: " + title)

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				print("keywords: " + keywords)

			for headers in re.findall(regexp_headers, content_string):
				headerSet = set(headers)
				for header in headerSet:
					header = str.replace(header, u"\u2018", "'")
					header = str.replace(header, u"\u2019", "'")
					print("header: " + header)

			for spans in re.findall(regexp_span, content_string):
				for span in spans:
					span = str.replace(span, u"\u2018", "'")
					span = str.replace(span, u"\u2019", "'")
					print("span: " + span)

			for paras in re.findall(regexp_para, content_string):
				paraSet = set(paras)
				for para in paraSet:
					para = str.replace(para, u"\u2018", "'")
					para = str.replace(para, u"\u2019", "'")
					print("para: " + para)

			for (urls) in re.findall(regexp_url, content_string):
				if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
					crawler_backlog[urls] = 0
					visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
visit_url(seed, "www.newhaven.edu")