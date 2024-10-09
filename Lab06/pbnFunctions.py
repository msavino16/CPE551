# Author: Michael Savino
# Date: 10/8/24
# Description: Functions for Paint By Number program

def getFileName():

    """
    Function to prompt user for a file name, and repeats until user enteres a valid file name
    """

    import os
    filename = input("Please enter the name of the file: ")

    while not os.path.exists(filename):
        filename = input(f"{filename} does not exist! Please enter the name of the file: ")

    return filename

def convertLine(line):
    
    """
    Function takes in a line, and converts the numbers within the line to a respective 
    symbol, and adds that symbol to a new string

    :param line: line from a read file
    :type line: String
    """

    line = line.strip()
    newLine = ""
    numbers = line.split(",")

    for num in numbers:
        num = int(num)
        match num:
            case 1:
                newLine += ' '
            case 2: 
                newLine += ','
            case 3:
                newLine += '_'
            case 4:
                newLine += '('
            case 5:
                newLine += 'O'
            case 6:
                newLine += ')'
            case 7:
                newLine += '-'
            case 8:
                newLine += '"'
            case _:
                newLine += ''

    return newLine

def processFile(filename):

    """
    Function to take in a file, convert the numbers in each line to a symbol, and store it in a new file
    :param filename: name of opened file
    :type filename: String
    """

    with open(filename,"r") as inputFile:
        with open("painting.txt","w") as outputFile:
            for line in inputFile:
                newLine = convertLine(line)
                outputFile.write(newLine+"\n")


