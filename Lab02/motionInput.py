# Author: Michael Savino
# Date: 09/10/24
# Description: Given a duration of time, this program computes 
# the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Initialize the radius:
time = float(input("Enter the time: "))

# Calculate the properties of the object:

velocity = initialVelocity + acceleration * time

avgVelocity = initialVelocity + (1/2)*acceleration*time

displacement = initialVelocity*time + (1/2)*acceleration*time*time

# Print the results:

print("time = ",time)
print()
print("velocity = ",velocity)
print("average velocity = ",avgVelocity)
print("displacement = ",displacement)

