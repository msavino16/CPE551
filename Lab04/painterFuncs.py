def intro():
    '''
    Function to welcome user to program, and recieve their input on art and border
    '''
    print("Welcome to the ASCII Art Painter!")
    print("Choose an artwork to display:")
    print("1. Sleeping Cat")
    print("2. Sailing Ship")
    print("3. Frog")
    print("4. Cereal and Coffee")

    art_choice = int(input("Enter the number of your choice (1-4): "))

    border = input("Enter a single symbol for the border: ")

    return art_choice, border

def printHeaderFooter(border, size):
    '''
    Function to print out a line of the border symbol for top and bottom of art
    '''
    print(border * size)

def sleepingCat(border):
    '''
    Function to print out the sleeping cat art with the users selected border
    '''

    art = [
        "      |\\      _,,,---,,_",
        "ZZZzz /,`.-'`'    -.  ;-;;,_",
        "     |,4-  ) )-,_. ,\\ (  `'-'",
        "    '---''(_/--'  `-'\\_)"
    ]

    max_length = max(len(line) for line in art)
    
    printHeaderFooter(border, max_length+4)
    
    for line in art:
        print(f"{border} {line.ljust(max_length)} {border}")
    
    printHeaderFooter(border, max_length + 4)


def sailingShip(border):
    '''
    Function to print out the sailing ship art with the users selected border
    '''
    art = [
        r"      |    |    |",
        r"     )_)  )_)  )_)",
        r"    )___))___))___)\\",
        r"   )____)____)_____)\\\\",
        r" _____|____|____|____\\\\\\__",
        r" \\    Satisfaction   /",
        r"^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    ]

    max_length = max(len(line) for line in art)
    
    printHeaderFooter(border, max_length+4)
    
    for line in art:
        print(f"{border} {line.ljust(max_length)} {border}")
    
    printHeaderFooter(border, max_length + 4)

def frog(border):
    '''
    Function to print out the frog art with the users selected border
    '''

    art = [
        r"        _  _",
        r"       (.)(.)",
        r"   ,-.(.____.),-.  ",
        r"  ( \ \ '--' / / )",
        r"   \ \ / ,. \ / /",
        r"    ) '| || |' ( mrf",
        r"OoO'- OoO''OoO -'OoO"
    ]

    max_length = max(len(line) for line in art)
    
    printHeaderFooter(border, max_length+4)
    
    for line in art:
        print(f"{border} {line.ljust(max_length)} {border}")
    
    printHeaderFooter(border, max_length + 4)

def cerealAndCoffee(border):
    '''
    Function to print out the coffee and cereal art with the users selected border
    '''

    art = [
        r"  ;)( ;",
        r" :----:     o8Oo./",
        r"C|====| ._o8o8o8Oo_.",
        r" |    |  \========/",
        r" `----'   `------'"
    ]

    max_length = max(len(line) for line in art)
    
    printHeaderFooter(border, max_length+4)
    
    for line in art:
        print(f"{border} {line.ljust(max_length)} {border}")
    
    printHeaderFooter(border, max_length + 4)


def blank(border):
    '''
    Function to print out an empty border with the users selected border
    '''

    printHeaderFooter(border, 9)

    for i in range(5):
        print(f"{border}       {border}")

    printHeaderFooter(border, 9)
