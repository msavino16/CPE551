# Author: Michael Savino
# Date: 11/2/24
# Description: File to hold product class

class Product():
    '''
    Product Class with 4 variables - name, units, unitprice, and total price
    '''
    def __init__(self):
        self.__name = ''
        self.__units = ''
        self.__unitPrice = 0
        self.__totalPrice = 0
        
    def getName(self):
        return self.__name
    def getUnits(self):
        return self.__units
    def getUnitPrice(self):
        return self.__unitPrice
    def getTotalPrice(self):
        return self.__totalPrice
    
    def setName(self,name):
        self.__name = name
    def setUnits(self,units):
        self.__units = units
    def setUnitPrice(self,unitPrice):
        self.__unitPrice = unitPrice
    def setTotalPrice(self,totalPrice):
        self.__totalPrice = totalPrice