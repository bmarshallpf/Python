#Brandon Marshall       
#Python Scripting
#November 16, 2015
#Homework 8 - Program 1

import os
import random
from tkinter import *
from PIL import ImageTk

dog1 = "dog.png"
dog2 = "dog_bark.png"
cur = dog1
text1 = "Good Dog!"
text2 = "Bark! Bark!"
curText = text1

def buttonReleased(event):
	global cur, dog1, dog2
	if cur == dog1:
		img2 = ImageTk.PhotoImage(file = dog2)
		cur = dog2
		curText = text2
		rand = random.randrange(1, 6)
		os.system("start dog_bark" + str(rand) + ".wav")
	else:
		img2 = ImageTk.PhotoImage(file = dog1)
		cur = dog1
		curText = text1
	panel.configure(image = img2)
	panel.image = img2
	panel2.configure(text = curText)

base = Tk()
w, h = base.winfo_screenwidth(), base.winfo_screenheight()
base.geometry("%dx%d+0+0" % (w, h))

frame = Frame(base)
frame.pack()

img = ImageTk.PhotoImage(file = dog1)
panel = Label(frame, image = img)
panel.pack(side = "top", fill = "both")
panel.bind("<ButtonRelease-1>", buttonReleased)
panel2 = Label(base, text = text1, font=("Helvetica", 72))
panel2.pack(side = "bottom")

mainloop()