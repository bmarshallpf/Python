#Brandon Marshall       
#Python Scripting
#October 29, 2015
#Homework 6 - Program 2

from random import randrange

print("INTEGER DIVISIONS")

while True:
	a = randrange(5)
	b = randrange(5)
	guess = ""
	try:
		answer = a // b
	except:
		continue

	try:
		guess = input(str(a) + " / " + str(b) + " = ")
		if guess == "exit":
			break
		else:
			intAns = int(guess)
	except:
		print("Please enter Integers only!")
		guess = "exception"
	finally:
		if guess != "exit" and guess != "exception":
			if intAns == answer:
				print("CORRECT!")
			else:
				print("INCORRECT!")
