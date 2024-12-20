# Author: Michael Savino
# Date: 11/22/24
# Description: Stack Class using Linked List
 
class Node(): #Node Class
    def __init__(self, data):
        self.__data = data
        self.__next = None

    #Accessors
    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    #Mutators
    def setData(self, data):
        self.__data = data

    def setNext(self, next_node):
        self.__next = next_node


class EmptyStackException(Exception): #EmptyStackException Class
    def __init__(self, action):
        message = f"Sorry, the stack is empty and we cannot {action}!"
        super().__init__(message)


class Stack(): #Stack Class
    def __init__(self):
        self._head = None

    def push(self, data):
        node = Node(data)
        node.setNext(self._head)
        self._head = node

    def pop(self):
        if self._head is None:
            raise EmptyStackException("pop")
        data = self._head.getData()
        self._head = self._head.getNext()
        return data

    def peek(self):
        if self._head is None:
            raise EmptyStackException("peek")
        return self._head.getData()

    def clear(self):
        self._head = None

    def __str__(self):
        elements = []
        current = self._head
        while current:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ", ".join(elements)
