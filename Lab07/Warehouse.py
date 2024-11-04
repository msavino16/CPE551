# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold warehouse class

class Warehouse():
    '''
    Warehouse Class with 1 variable called goods
    '''
    def __init__(self,initalGoods): # Constructor
        self.__goods = initalGoods

    def addGoods(self): # Function to add goods to the object
        newGoods = int(input("How many goods would you like to add: "))
        self.__goods += newGoods
    
    def removeGoods(self): # Function to remove goods to the object
        removed = int(input("How many goods would you like to remove: "))
        
        if removed > self.__goods:
            print("You do not have that many goods!")
        else:
            self.__goods -= removed
    
    def getGoods(self): # Accessor
        return self.__goods
    
    def setGoods(self,goods): # Mutator
        self.__goods = goods