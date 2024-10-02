# Author: Michael Savino
# Date: 10/1/24
# Description: Allows a user to enter different distances at different 
# trials and the program outputs the max 3 distances and their respective trials

topDist = [0,0,0]

topTrials = [0,0,0]

additionalTrials = "Y"

currentTrial = 1

while (additionalTrials == "Y"):
    tempDist = int(input(f"Please enter your distance for trial {currentTrial}: "))
    if (tempDist > topDist[0]):
        topDist[2] = topDist[1]
        topDist[1] = topDist[0]
        topDist[0] = tempDist

        topTrials[2] = topTrials[1]
        topTrials[1] = topTrials[0]
        topTrials[0] = currentTrial


    elif (tempDist > topDist[1]):
        topDist[2] = topDist[1]
        topDist[1] = tempDist

        topTrials[2] = topTrials[1]
        topTrials[1] = currentTrial

    elif (tempDist > topDist[2]):
        topDist[2] = tempDist
        topTrials[2] = currentTrial

    additionalTrials = input("Would you like to input another trial? (Y/N): ")
    if (additionalTrials == "Y"):
        currentTrial += 1

print("\nTrial  Distance")
for i in range(3):
    print(f"{topTrials[i]:>5} {topDist[i]:>9}")