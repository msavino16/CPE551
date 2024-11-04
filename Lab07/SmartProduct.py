# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold SmartProduct class

class SmartProduct():
    '''
    Product Class with 5 variables - name, units, unit price, total price, and id
    '''
    def __init__(self, id, name, units, unitprice): #Constructor
        self.__id = id
        self.__name = name
        self.__units = units
        self.__unitPrice = unitprice
        self.__totalPrice = self.__units* self.__unitPrice
      
      
 
    '''
    Accessor Methods
    '''    
    def getName(self):
        return self.__name
    def getUnits(self):
        return self.__units
    def getUnitPrice(self):
        return self.__unitPrice
    def getTotalPrice(self):
        return self.__totalPrice
    def getID(self):
        return self.__id
    
    '''
    Mutator Methods
    ''' 
    def setName(self,name):
        self.__name = name
    def setUnits(self,units):
        self.__units = units
    def setUnitPrice(self,unitPrice):
        self.__unitPrice = unitPrice
    def setTotalPrice(self,totalPrice):
        self.__totalPrice = totalPrice
    def setID(self,id):
        self.__id = id