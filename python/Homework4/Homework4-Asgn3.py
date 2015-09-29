#Brandon Marshall       
#Python Scripting
#September 28, 2015
#Homework 4 - Assignment 3 - How mcuh operation on a dictionary is 
# faster than operation on a shelve?

# Use following to time your code. Do similar operations on a dictionary and 
# shelve with same data in them and document which one is faster.

import time
import shelve

counter = 0
testDict = {}

# start timing
start_time = time.perf_counter()*1000


while counter < 100:
	testDict.update({str(counter): "value"})
	counter = counter + 1

# finish timing
end_time = time.perf_counter()*1000
print("Dictionary time:", end_time - start_time)

counter = 0
testShelve = shelve.open("testShelf")

# start timing
start_time = time.perf_counter()*1000

while counter < 100:
	testShelve.update({str(counter): "value"})
	counter = counter + 1

# finish timing
end_time = time.perf_counter()*1000

testShelve.close()

print("Shelve time:", end_time - start_time)

# Restuls: Dictionary (2.2 milliseconds), Shelve (9924.0 milliseconds)
# Dictionary is a lot faster, by a factor of 4,511!