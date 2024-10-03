# Author: Michael Savino
# Date: 10/3/24
# Description: A program to generate random capture rates in a 2 dimensional list and record the highest and lowest in the 2d list

MAP_DIMENSIONS = 8

captureRates = [[0 for i in range(MAP_DIMENSIONS)]for i in range(MAP_DIMENSIONS)]

import random

for i in range(MAP_DIMENSIONS):
    for j in range(MAP_DIMENSIONS):
        captureRates[i][j] = random.randint(0,500)

xHigh = 0
xLow = 0

yHigh = 0
yLow = 0

highestRate = -1
lowestRate = 1000

for i in range(MAP_DIMENSIONS):
    for j in range(MAP_DIMENSIONS):
        currentValue = captureRates[i][j]

        if currentValue > highestRate:
            highestRate = currentValue
            xhigh, yHigh = i, j

        if currentValue < lowestRate:
            lowestRate = currentValue
            xLow, yLow = i, j

xHigh +=1
xLow += 1

yHigh += 1
yLow += 1

print(f"The highest capture rate was {highestRate} at location ({xHigh},{yHigh})")
print(f"The lowest capture rate was {lowestRate} at location ({xLow},{yLow})")

for row in captureRates:
    for val in row:
        print(f"{val:4}", end=" ")
    print()

