# Author: Michael Savino
# Date: 11/14/24
# Description: File to hold powers function

def powers(base,exp):

    '''
    Recursive function to calculate an exponent expression
    :param base: base of the expression
    :type base: int
    :param exp: exponent of  the expression
    :type exp: int
    '''

    print(f"powers({base},{exp})")

    if exp == 1: #Base Case
        return base
    
    return base * powers(base,exp-1) #Recursive Step

def main():

    '''
    Main Function
    '''
    
    base = int(input("Please enter the base value: "))
    exp = int(input("Please enter the exponent value: "))

    result = powers(base,exp)

    print(f"{base}^{exp} is {result}")

main()