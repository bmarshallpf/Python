#Brandon Marshall       
#Python Scripting
#September 28, 2015
#Homework 4 - Assignment 4 - Pickle or Shelve User Data

# ask user to enter Name, Age and Country of Origin, then use Pickle and/or Shelve to store it, 
# write a separate function to open pickle and/or shelve and read it back. 

import pickle

name = input("Enter your name: ")
age = input("Enger your age: ")
country = input("Enter your country of origin: ")

info = [name, age, country]

f = open("pickles.txt", "bw")
pickle.dump(info, f)
f.close()

new_f = open("pickles.txt", "br")
new_info = pickle.load(new_f)
new_f.close()

print("Name: " + new_info[0])
print("Age: " + new_info[1])
print("Country: " + new_info[2])