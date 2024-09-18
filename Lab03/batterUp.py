# Author: Michael Savino
# Date: 09/17/24
# Description: Program generates a random number and outputs a distance and a base location

import random

dist = random.randint(0,450)

if(dist>400):
    print("The ball was hit",dist,"feet and was a homerun! Score!")
elif(135<=dist<=400):
    print("The ball was hit",dist,"feet and is in the outfield! You made it to 3rd base!")
elif(10<=dist<=134):
    print("The ball was hit",dist,"feet and is in the infield! You made it to 2nd base!")
elif(1<=dist<=9):
    print("The ball was hit",dist,"feet as a bunt! You made it to 1st base!")
else:
    print("Strike!")
