# Author: Michael Savino
# Date: 11/22/24
# Description: Main file that uses the stack class

from Stack import Stack, EmptyStackException

def main():
    stack = Stack()

    with open("inputStack.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("push"):
                command, value = line.split()
                stack.push(int(value))
                print(f"Pushed {value}")

            elif line == "pop":
                try:
                    value = stack.pop()
                    print(f"Popped {value}")
                except EmptyStackException as e:
                    print(e)

            elif line == "peek":
                try:
                    value = stack.peek()
                    print(f"Peeked at {value}")
                except EmptyStackException as e:
                    print(e)

            elif line == "clear":
                stack.clear()
                print("Cleared out the stack.")

            else:
                print(stack)

main()