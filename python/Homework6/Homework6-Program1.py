#Brandon Marshall       
#Python Scripting
#October 29, 2015
#Homework 6 - Program 1

class Animal:
	def __init__(self, name):
		self.name = name

	def guess_who_am_i(self):
		count = 0
		guess = ""
		while guess != self.name:

			if count > 0 and count < 3:
				print("Nope, try again!\n")

			if self.name == "elephant":
				if count == 0:
					print("I have an exceptional memory. ")
					count = 1
				elif count == 1:
					print("I am the largest land-living mammal in the world. ")
					count = 2
				elif count == 2:
					print("I am gray. ")
					count = 3
			elif self.name == "tiger":
				if count == 0:
					print("I am the biggest cat. ")
					count = 1
				elif count == 1:
					print("I come in black and white or orange and black. ")
					count = 2
				elif count == 2:
					print("I am not a lion. ")
					count = 3
			elif self.name == "bat":
				if count == 0:
					print("I use echo-location. ")
					count = 1
				elif count == 1:
					print("I can fly. ")
					count = 2
				elif count == 2:
					print("I see well in dark. ")
					count = 3

			guess = input("Who am I? ")
			
			if count == 3:
				print("I'm out of hints! The answer is: " + self.name + "\n")
				count = 4
				break

		if count < 4:
			print("You got it! I am a " + self.name + "\n")

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

animals = [e, t, b]
for a in animals:
	print("I will give you 3 hints, guess what animal I am!\n")
	a.guess_who_am_i()