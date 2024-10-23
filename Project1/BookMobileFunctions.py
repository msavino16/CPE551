# Author: Michael Savino
# Date: 10/21/24
# Description: Functions for the BookMobile program

import os

def loadFile(): # Selection 1
    
    """
    Function to take in a csv file and return a dictionary that has key's of book titles and their value's are a list of the details of the book. 
    Function also returns a list a categories.

    """
    
    books = {} #Dictonaries of books
    categories = set() #Set of catagories
    
    filename = input("Please enter the name of the book file: ")

    while not os.path.exists(filename):
        filename = input(f"{filename} does not exist. Please enter the name of the book file: ")

    with open(filename,"r") as inputFile:
        next(inputFile) #Skips header
        
        for line in inputFile:
            line = line.strip()
            data = line.split(',')
            
            title = data[0] 
            category = data[5]
            
            books[title] = data
            categories.add(category.lower())
    
    return books, categories

def loadReview(books): # Selection 2
    
    """
    Function to take in a reviews csv, which titles gets compared to the books dictionary to see if they exist
    :param books: Dictionary of books with key's being titles and values being details
    :type books: Dictionary
    """
    
    reviews = []
    
    filename = input("Please enter the name of the book reviews file: ")

    while not os.path.exists(filename):
        filename = input(f"{filename} does not exist. Please enter the name of the book reviews file: ")
        
    with open(filename,"r") as inputFile:
        next(inputFile) #Skips header
        
        for line in inputFile:
            line = line.strip()
            data = line.split(',')
            
            title = data[1]
            
            if title not in books:
                    raise LookupError(f"{title}' is not a known book!")
                
            reviews.append(data)
            
    return reviews

def chooseCategory(books,categorySet): # Selection 3
    
    """
    Function to provide users with all unique catagories from the book file, and allow them to choose one and output all the books in that category
    
    :param books: Dictionary of books with key's being titles and values being details
    :type books: Dictionary
    
    :param categorySet: A set of categories from the books dictionary
    :type categorySet: Set
    """
    
    print("Currently, we have books in the following categories:")
    count = 0
    for item in categorySet:
        count += 1
        print(f'{count}: {item}')
        
    choice = input("Which category of books would you like to see: ").lower()
    
    while choice not in categorySet:
        print(f"'{choice}' is not a valid category.",end=' ')
        choice = input("Which category of books would you like to see: ").lower()
    
    for title, data in books.items():
        category = data[5].strip().lower()
        
        if category == choice:
            title = data[0]
            authors = data[2]
            print(f'"{title}" by {authors}')       
            
def detailBook(books,bookReviews): # Selection 4
    
    """
    Function to provide users with review details of a book if available such title, description, authors, publisher, date, category, price, and average rating
    
    :param books: Dictionary of books with key's being titles and values being details
    :type books: Dictionary
    
    :param bookReviews: A 2D list that contains all reviews for books, and their details such as price, reviewer, review score, etc
    :type bookReviews: List
    """
    
    print("Currently, we have the following books:")
    
    count = 0
    for title in books.keys():
        count += 1
        print(f'{count}: {title}')
        
    choice = input("Which book would you like to see the details of: ")
    
    while choice not in books:
        print(f"{choice} is not a valid book. ", end='')
        choice = input("Which book would you like to see the details of: ")
        
    bookData = books[choice]
    
    
    totalPrice = 0
    totalRating = 0
    reviewCount = 0
    
    reviewsExist = False #Flag to detect if a review exists
    for review in bookReviews:
        if choice == review[1]:
            totalPrice += float(review[2])
            totalRating += float(review[6])
            reviewCount += 1
            reviewsExist = True
        
        
    print(f"{bookData[0]} by {bookData[2]}") #Title and Author(s)
    print(f"{bookData[1]}") #Description
    print(f"Published by {bookData[3]} in {bookData[4]}") #Publisher and Date
    print(f"Category: {bookData[5]}") # category 
        
    if reviewsExist:
        avgPrice = totalPrice/reviewCount
        avgRating = totalRating/reviewCount
        print(f"Price: ${avgPrice:.2f}")
        print(f"Average Rating: {avgRating:.1f}/5")
    else:    
        print("There are no reviews for this book.")
    
def calcAuthorAvg(books, bookReviews): # Selection 5
    
    """
    Function to provide users with average rating between authors books
    
    :param books: Dictionary of books with key's being titles and values being details
    :type books: Dictionary
    
    :param bookReviews: A 2D list that contains all reviews for books, and their details such as price, reviewer, review score, etc
    :type bookReviews: List
    """
    
    authorsBooks = {}
    authorsRatings = {}
    
    for title, data in books.items():
        authors = data[2].split(';')
        for author in authors:
            if author not in authorsBooks:
                authorsBooks[author] = []
            authorsBooks[author].append(title)
    
    for author in authorsBooks:
        authorsRatings[author] = {'totalRating': 0, 'count': 0}
    
    for review in bookReviews:
        title = review[1]
        rating = float(review[6])
        
        for author, books in authorsBooks.items():
            if title in books:
                authorsRatings[author]['totalRating'] += rating
                authorsRatings[author]['count'] += 1
    
    print("The average rating for each author is: ")
    for author, data in authorsRatings.items():
        if data['count'] > 0:
            averageRating = data['totalRating'] / data['count']
            print(f"{author}: {averageRating:.2f}/5")
        else:
            print(f"{author}: No Ratings")

def helpfulReviewer(BookReviews): # Selection 6
    
    """
    Function to provide users the most helpful reviewer from their reviews file
    
    :param bookReviews: A 2D list that contains all reviews for books, and their details such as price, reviewer, review score, etc
    :type bookReviews: List
    """
    
    reviewerHelp = {}
    
    for review in BookReviews:
        
        profileName = review[4]
        
        scoreToTotal = review[5].split('/') 

        helpfulCount = int(scoreToTotal[0])
        totalCount = int(scoreToTotal[1])

        if profileName not in reviewerHelp:
            reviewerHelp[profileName] = {'helpfulCount': [], 'totalCount': []}

        reviewerHelp[profileName]['helpfulCount'].append(helpfulCount)
        reviewerHelp[profileName]['totalCount'].append(totalCount)
    
    mostHelpful = ''
    highestAverage = 0

    for reviewer, data in reviewerHelp.items():
        totalHelpful = sum(data['helpfulCount'])
        totalReviewed = sum(data['totalCount'])

        if totalReviewed >= 10:
            averageHelpfulness = (totalHelpful / totalReviewed) * 100
            
            if averageHelpfulness > highestAverage:
                highestAverage = averageHelpfulness
                mostHelpful = reviewer
                
    if mostHelpful:
        print(f"The most helpful reviewer is {mostHelpful} with an average helpfulness rating of {int(highestAverage)}%")
    else:
        print("No reviewers meet the criteria for helpfulness.")

def welcomeMessage():
    """
    Function to simply print out a welcome message
    """
    print("Welcome to the Book Mobile! We have many books to offer. Please choose from the following menu of options")

def goodbyeMessage():
    """
    Function to simply print out a goodbye message
    """
    
    print("Thank you for visiting the Book Mobile!")
    
def displayMenu():
    
    """
    Function that returns users choice from the main menu
    """
    print()
    print("1. Load Book File")
    print("2: Load Review File")
    print("3. Books by Category")
    print("4. Book Details")
    print("5. Author Average Ratings")
    print("6. Most Helpful Reviewer")
    print("7: Quit")
    
    return input("Please enter a choice (1-7): ")