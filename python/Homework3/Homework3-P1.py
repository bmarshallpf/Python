#Brandon Marshall       
#Python Scripting
#September 24, 2015
#Homework 3 - Problem 1

# We have bunnies standing in a line, numbered 1, 2, ... 
# The odd bunnies (1, 3, ..) have the normal 2 ears. 
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. 
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication). 

# bunnyEars2(0) ? 0
# bunnyEars2(1) ? 2
# bunnyEars2(2) ? 5

def bunny_ears(bunnies):
	if (bunnies == 0):
		return 0
	elif (bunnies % 2 == 0):
		return 2 + bunny_ears(bunnies - 1)
	else:
		return 3 + bunny_ears(bunnies - 1)

print(bunny_ears(0))
print(bunny_ears(1))
print(bunny_ears(2))