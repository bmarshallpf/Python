#Brandon Marshall       Python Scripting
#September 3, 2015      Homework 1

tries, nextGuess, modifier = 1, 50, 50
name = input("Hello, what is your name?\n")
print("Hello " + name + ". It's nice to meet you!")
print("Think of a random number from 1 to 100, and I'll try to guess it!")

while True:
    if ("yes" == input("Is it " + str(nextGuess) + "? (yes/no) ")):
        print("Yeah, I got it in " + str(tries) + " tries!")
        if ("no" == input("Do you want to play more? (yes/no) ")):
            break
        else:
            print("Okay " + name + ", think of another number!")
            tries, nextGuess, modifier = 1, 50, 50
    else:
        tries = tries + 1

        if modifier > 1:
            modifier = modifier // 2

        if ("yes" == input("Is it larger than " + str(nextGuess) + "? (yes/no) ")):
            nextGuess = nextGuess + int(modifier)
        else:
            nextGuess = nextGuess - int(modifier)