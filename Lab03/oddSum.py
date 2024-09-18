# Author: Michael Savino
# Date: 09/17/24
# Description: program picks a number between 1-10 and a number between 11-20 and adds up all the odd numbers

import random

firstInt = random.randint(1,10)
secondInt = random.randint(11,20)

sum = 0

for i in range(firstInt,secondInt+1):
    if i % 2 == 1:
        sum += i
    
print("The first number is",firstInt)
print("The second number is",secondInt)

print("The sum of the odd numbers between those two numbers is",sum)