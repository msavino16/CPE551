from painterFuncs import sleepingCat, sailingShip, frog, cerealAndCoffee, blank, intro

def main():
    choice,border = intro()
    
    if choice == 1:
        sleepingCat(border)
    elif choice == 2:
        sailingShip(border)
    elif choice == 3:
        frog(border)
    elif choice == 4:
        cerealAndCoffee(border)
    else:
        print("That option was not on the list. Here is a blank canvas instead")
        blank(border)
        exit(-1)
    print("Hope you enjoy the art!")

main()