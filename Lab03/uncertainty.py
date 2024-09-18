# Author: Michael Savino
# Date: 09/17/24
# Description: Program that plays a game with a user to try to guess a position

import random
guess = 3

xCord = random.randint(1,10)
yCord = random.randint(1,10)

while guess != 0:
    print("You have ",guess,"guess(s) left. The particle is somewhere in this space")
    xGuess = int(input("Guess an X position (1-10): "))
    yGuess = int(input("Guess an Y position (1-10): "))

    if(xGuess == xCord and yGuess == yCord):
        print("You win!")
        break

    if (xGuess < 1 or xGuess > 10):
        print("Your X guess was outside of the 1-10 range!")
    elif xGuess > xCord :
        print("Your X guess was too high!")
    elif xGuess < xCord:
        print("Your X guess was too low!")
    else:
        print("Your X value is correct!")


    if (yGuess < 1 or yGuess > 10):
        print("Your Y guess was outside of the 1-10 range!")
    elif yGuess > yCord :
        print("Your Y guess was too high!")
    elif yGuess <yCord:
        print("Your Y guess was too low!")
    else:
        print("Your Y value is correct!")

    guess -=1
    print()

if (guess == 0):
    print(f"You lose! The position was ({xCord},{yCord})")


