#Brandon Marshall
#Python Scripting
#August 29, 2015
#Homework 1

tries = 1
larger = False
nextGuess = 50
modifier = 50
name = input("Hello, what is your name?\n")
print("Hello " + name + ". It's nice to meet you!")
print("Think of a random number from 1 to 100, and I'll try to guess it!")
guessed = "yes" == input("Is it " + str(nextGuess) + "? (yes/no)")

while guessed != True:
    tries = tries + 1

    if modifier > 1:
        modifier = modifier // 2

    larger = "yes" == input("Is it larger than " + str(nextGuess) + "? (yes/no) ")

    if larger:
        nextGuess = nextGuess + int(modifier)
    else:
        nextGuess = nextGuess - int(modifier)

    guessed = "yes" == input("Is it " + str(nextGuess) + "? (yes/no) ")
else:
    print("Yeah, I got it in " + str(tries) + " try!")