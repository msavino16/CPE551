# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold main function

from Warehouse import Warehouse

def main():
    '''
    Main function that uses warehouse class
    '''
    warehouse = Warehouse(0)
    
    while True:
        print()
        print("Please select from the following options: ")
        print("1. Add Goods")
        print("2. Remove Goods")
        print("3. Output Total Goods")
        print("4. Quit")

        choice = input("Choose: ")

        if choice == '1':
            warehouse.addGoods()
        elif choice == '2':
            warehouse.removeGoods()
        elif choice == '3':
            print(f"There are {warehouse.getGoods()} goods in the warehouse.")
        elif choice == '4':
            print("Good bye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
main()
    
    
    