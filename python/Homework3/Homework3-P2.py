#Brandon Marshall       
#Python Scripting
#September 24, 2015
#Homework 3 - Problem 2

# Write a function count_frequency that takes a list of words as an argument, counts how many 
# times each word appears in the list, and then returns this frequency listing as a Python dictionary
# Sample function call and output:

def count_frequency(mylist):
	output = {}
	for word in mylist:
		if word in output.keys():
			output[word] = output[word] + 1
		else:
			output[word] = 1

	return output

mylist=["one", "two", "eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))