# Author: Michael Savino
# Date: 10/21/24
# Description: Main function for the BookMobile program

from BookMobileFunctions import * #Imports all functions form BookMobileFunctions.py

def main():
    
    """
    Main function for the BookMobile program that operates the main menu selections
    """
    
    welcomeMessage()
    
    fileLoaded = False
    reviewLoaded = False
    
    
    while True:
        choice = int(displayMenu())

        match choice:
            case 1: 
                books, categories = loadFile()
                fileLoaded = True

            case 2:
                if not fileLoaded: 
                    print("You need to load a book file first.")
                else:
                    try:
                        bookReviews = loadReview(books)
                        reviewLoaded = True
                    except LookupError as e:
                        print(f"Error loading book reviews: \n{e}")
                        print("Please try another list of reviews.")

            case 3:
                if not reviewLoaded:
                    print("You need to load a book reviews first before trying this function.")
                else:
                    chooseCategory(books, categories)

            case 4:
                if not reviewLoaded:
                    print("You need to load a book reviews first before trying this function.")
                else:
                    detailBook(books,bookReviews)

            case 5:
                if not reviewLoaded:
                    print("You need to load a book reviews first before trying this function.")
                else:
                    calcAuthorAvg(books, bookReviews)
            case 6:
                if not reviewLoaded:
                    print("You need to load a book reviews first before trying this function.")
                else:
                    helpfulReviewer(bookReviews)
            case 7:
                goodbyeMessage()
                break

            case _:
                print(f"{choice} is not a valid option! Try again.")
    
if __name__ == "__main__":
    main()
    
    