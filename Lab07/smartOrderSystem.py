# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold calc total function and main function for smartproduct

from SmartProduct import SmartProduct

def calcTotal(products):
    '''
    Function to calculate total price of all items in the product list
    :param products: list of product objects
    :type producst: list
    '''
    totalCost = 0
    for product in products:
        totalCost += product.getUnits()*product.getUnitPrice()
    
    return totalCost
        
    
def main():
    '''
    Main function for program that uses the SmartProduct class
    '''
    
    productList = []
    
    numProduct = int(input("How many products would you like to order: "))
    
    for i in range(numProduct):
        name = input("Please enter the name of the product you wish to order: ")
        units = int(input("Please enter the number of units of product you wish to order: "))
        print()
        
        product = SmartProduct(i+1,name,units,9.99)
        
        productList.append(product)
    
    
    for product in productList:
        print(f"ID: {product.getID()}")
        print(f"Name: {product.getName()}")
        print(f"Units: {product.getUnits()}")
        print(f"Price: ${product.getUnitPrice()}")
        print(f"Total Cost: ${product.getTotalPrice()}")
        
    print(f"The total cost of your order is: {calcTotal(productList)}")
    
main()
    
    
    