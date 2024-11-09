# Author: Michael Savino
# Date: 11/9/24
# Description: Main class

from Employee import Employee
from Worker import Worker
from Supervisor import Supervisor

def calcTotalPay(employeeList):
    '''
    Function to calculate the total pay of all employees
    :param employeeList: List to hold all employees
    :type employeeList: List
    '''
    totalPay = 0
    for employee in employeeList:
        totalPay += employee.calcPay(40)
    return totalPay

def listEmployees(employeeList):
    '''
    Function to print out employee information
    :param employeeList: List to hold all employees
    :type employeeList: List
    '''
    for employee in employeeList:
        print(f"Name: {employee.getName()}")
        print(f"ID: {employee.getID()}")
        print(f"Pay Rate: ${employee.getPayRate():.2f}")
        if isinstance(employee,Worker):
            if employee.getShift() == 1:
                print(f"Shift: Day Shift")
            else:
                print(f"Shift: Night Shift")
        elif isinstance(employee, Supervisor):
            print(f"Level: {employee.getLevel()}")

def main():
    '''
    main function
    '''
    employeeList = []
    numEmployees = int(input("How many employees would you like to add: "))

    for i in range(numEmployees):
        type = input("Would you like to add a worker or a supervisor: ").strip().lower()

        while (type != "supervisor") and (type != "worker"):
            print(f"{type} is not a worker or supervisor. Try again!")
            print()
            type = input("Would you like to add a worker or a supervisor: ").strip().lower()
        

        if type == "worker":
            name = input("Please enter the name of the worker: ")
            id = int(input("Please enter the id of the worker: "))
            payRate = float(input("Please enter the pay rate of the worker: "))
            shift = int(input("Please enter the shift of the worker (1 for day, 2 for night): "))
            employeeList.append(Worker(name,id,payRate,shift))

        elif type == "supervisor":
            name = input("Please enter the name of the supervisor: ")
            id = input("Please enter the id of the supervisor: ")
            payRate = float(input("Please enter the pay rate of the supervisor: "))
            level = int(input("Please enter the level of the supervisor: "))
            employeeList.append(Supervisor(name,id,payRate,level))
        print()


    listEmployees(employeeList)
    totalPay = calcTotalPay(employeeList)
    print(f"The total cost of all of the worker's pay is ${totalPay}")


main()
