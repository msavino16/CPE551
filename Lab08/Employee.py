# Author: Michael Savino
# Date: 11/9/24
# Description: Employee class

class Employee():
    
    #Constructor
    def __init__(self,name,id,payRate):
        self._name = name
        self._ID = id
        self._payRate = payRate

    def calcPay(self,hours):
        '''
        Function to return the total pay of an employee
        '''
        return hours * self._payRate
    
    #Accessors
    def getName(self): 
        return self._name
    def getID(self):
        return self._ID
    def getPayRate(self):
        return self._payRate
    
    #Mutators
    def setName(self,name):
        self._name = name
    def setID(self,id):
        self._ID = id
    def setPayRate(self,payRate):
        self._payRate = payRate
    