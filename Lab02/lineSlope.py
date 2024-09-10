# Author: Michael Savino
# Date: 09/10/24
# Description: This program computes the slope of a line given 
# the end points of the line. The result is then printed to the screen.

# Initialize the end points.
startX = -2
startY = 1
endX = 5
endY = 36

# Compute the slope.
slope = (endY - startY)/(endX - startX)

# Print the results.
print("Starting point: (", startX, ",", startY, ")")
print("Ending point: (", endX, ",", endY, ")")
print("Slope of the line =", slope)

