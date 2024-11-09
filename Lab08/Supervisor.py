# Author: Michael Savino
# Date: 11/9/24
# Description: Supervisor class that inherits Employee class

from Employee import Employee

class Supervisor(Employee):
    #Constructor
    def __init__(self, name, id, payRate, level): 
        Employee.__init__(self,name, id, payRate)
        self._level = level

    def calcPay(self,hours):
        '''
        Function to return the total pay of an supervisor
        '''
        return hours*self._payRate + 1000*self._level
    #Accessor
    def getLevel(self):
        return self._level
    #Mutator
    def setLevel(self,level):
        self._shift = level