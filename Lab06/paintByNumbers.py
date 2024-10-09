# Author: Michael Savino
# Date: 10/8/24
# Description: Main function for Paint By Number program


from pbnFunctions import getFileName, processFile
def main():
    """
    General function description
    """

    filename = getFileName()
    processFile(filename)
    print("Your image can be found in painting.txt . Enjoy!")

if __name__ == "__main__":
    main()