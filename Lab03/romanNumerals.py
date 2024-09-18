# Author: Michael Savino
# Date: 09/17/24
# Description: user inputs a number and it gets converted to a roman numeral

number = int(input("Enter a number from 1-9: "))

if 1<=number<=9:
    #code for number inside 1-9
    if(number==1):
        print("\u2160")
    elif(number==2):
        print("\u2161")
    elif(number==3):
        print("\u2162")
    elif(number==4):
        print("\u2163")
    elif(number==5):
        print("\u2164")
    elif(number==6):
        print("\u2165")
    elif(number==7):
        print("\u2166")
    elif(number==8):
        print("\u2167")
    elif(number==9):
        print("\u2168")
else:
    #code for number outside of 1-9
    print("Error: Number is not in the appropriate range")