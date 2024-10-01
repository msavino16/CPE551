def intro():
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
    print(border * size)

def sleepingCat(border):

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

    printHeaderFooter(border, 9)

    for i in range(5):
        print(f"{border}       {border}")

    printHeaderFooter(border, 9)

def main():
    choice,border = intro()
    
    if choice == 1:
        sleepingCat(border)
    elif choice == 2:
        sailingShip(border)
    elif choice == 3:
        frog(border)
    elif choice == 4:
        cerealAndCoffee(border)
    else:
        print("That option was not on the list. Here is a blank canvas instead")
        blank(border)
        exit(-1)
    print("Hope you enjoy the art!")

main()