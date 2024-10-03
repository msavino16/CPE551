# Author: Michael Savino
# Date: 10/1/24
# Description: A lab management program that allows users to store up
# to 5 items, remove items, view items, or leave 

def dialogue():

    """
    Function to print dialogue to the user to prompt them options
    """

    print("You can choose from the following options:")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")
    return int(input("What would you like to do: "))

equipment = []

choice = 1
print ("Welcome to the inventory manager for your laboratory!")
while (choice != 4):
    choice = dialogue()

    if (choice == 1 and (len(equipment) != 5)):
        item = input("What would you like to add to the laboratory: ")
        equipment.append(item)
        print(f"{item} has been added")
        print()
    elif(choice == 1 and (len(equipment) == 5)):
        print("Your laboratory cannot support any more equipment!")
        print()
    elif(choice == 2):
        item = input("What would you like to remove from the laboratory: ")
        if(item in equipment):
            equipment.remove(item)
            print(f"{item} has been removed")
        else:
            print(f"{item} could not be found!")
        print()
        
    elif(choice == 3):
        print("Your laboratory currently contains: ", end = "")
        for i in range(len(equipment)):
            print(equipment[i],end=" ")
        print()
        print()
    elif(choice == 4):
        print("Good luck on your journey of discovery!")
    else:
        print(f"{choice} was not a valid option. Please try again")
        print()
        