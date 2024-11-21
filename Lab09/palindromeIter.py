# Author: Michael Savino
# Date: 11/14/24
# Description: Iterative version of palindrome test

def palinTest(test):

    '''
    Function to test if a word is a palindrome
    :param test: the word to be tested
    :type test: String
    '''

    length = len(test)
    for i in range(int(length/2)):
        if test[i] != test[length-i-1]:
            return False
    return True
    
def main():

    '''
    Main Function
    '''
    
    word = input("Please enter a word to test if it is a palindrome: ")
    
    if palinTest(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    

main()