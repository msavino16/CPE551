# Author: Michael Savino
# Date: 11/9/24
# Description: Worker class inheriting Employee class

from Employee import Employee

class Worker(Employee):
    #Constructor
    def __init__(self, name, id, payRate, shift): #For shift, 1 means day, 2 means night

        Employee.__init__(self,name, id, payRate)
        self._shift = shift
    #Accessor
    def getShift(self):
        return self._shift
    #Mutator
    def setShift(self,shift):
        self._shift = shift