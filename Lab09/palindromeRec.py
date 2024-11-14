# Author: Michael Savino
# Date: 11/14/24
# Description: Recursive version of palindrome test

def palinTest(test):

    '''
    Recursive function to test if a word is a palindrome
    :param test: the word to be tested
    :type test: String
    '''

    #Base Case

    if len(test) <= 1:
          return True
    
    #Recursive Step
    if test[0] == test[-1]:
         newtest = test[1:-1]
         return palinTest(newtest)
    else:
         return False
    
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