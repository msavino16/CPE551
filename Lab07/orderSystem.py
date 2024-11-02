# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold calc total function and main function

from Product import Product

def calcTotal(product):
    '''
    Function to calculate total price, then assign the products total price variable to that value
    :param product: Project object
    :type product: product
    '''
    totalCost = product.getUnits()*product.getUnitPrice()
    product.setTotalPrice(totalCost)
    
def main():
    '''
    Main function that uses Product class
    '''
    product = Product()
    
    product.setName(input("Please enter the name of the product you wish to order: "))
    product.setUnits(int(input("Please enter the number of units of product you wish to order: ")))
    
    product.setUnitPrice(9.99)
    
    calcTotal(product)
    
    print(f"Name: {product.getName()}")
    print(f"Units: {product.getUnits()}")
    print(f"Price: ${product.getUnitPrice()}")
    print(f"Total Cost: ${product.getTotalPrice()}")
    
main()
    
    
    