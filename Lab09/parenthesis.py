# Author: Michael Savino
# Date: 11/16/24
# Description: Correct parenthesis test


count = 0

def parenTest(line,position):
    '''
    Recursive function to test if parenthesis are balanced
    :param line: String made up of parenthesis
    :type line: String
    :param position:  current position on the parenthesis string
    :type position: int
    '''
    global count
    #Base Case
    if position == len(line):
        if count == 0:
            return True
        else:
            return False
    
    #Recursive Step
    if line[position] == '(':
        count += 1
    elif line[position] == ')':
        count -= 1
    
    if count < 0:
        return False
    
    return parenTest(line, position + 1)


def main():
    
    '''
    Main Function
    '''
    
    line = input("Please enter a series of parenthesis to see if they are balanced: ")
    
    if parenTest(line, 0):
        print(f"{line} is balanced.")
    else:
        print(f"{line} is not balanced.")

main()