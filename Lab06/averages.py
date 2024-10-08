# Author: Michael Savino
# Date: 10/8/24
# Description: Inputs a file of numbers and prints the average


myFile = open("numbers.txt", "r")
nums = myFile.read()
print(nums)
myFile.close()

numList = nums.split("\n")

sum = 0

for i in numList:
    sum += int(i)
avg = sum / len(numList)

print(f"The average of the numbers is {avg}")