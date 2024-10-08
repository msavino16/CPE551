# Author: Michael Savino
# Date: 10/8/24
# Description: Inputs a poem and outputs the poem summary to another file
import os

filename = input("Please enter the name of the file: ")

while not os.path.exists(filename):
    filename = input(f"{filename} does not exist! Please enter the name of the file: ")

myFile = open(filename, "r")  
poem = myFile.readlines()
myFile.close()

title = poem[0]
author = poem[1]
newPoem = poem[2:]

output = open("Output.txt","w")

output.write(f"The name of the poem is {title}")
output.write(f"The author of the poem is {author}")
output.write(f"The number of lines in the poem is {len(newPoem)}\n")
output.write("A preview of the poem is:\n")
output.write(newPoem[0])
output.write(newPoem[1])
output.write(newPoem[2])

output.close()

