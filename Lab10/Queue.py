# Author: Michael Savino
# Date: 11/22/24
# Description: Queue Class using Linked List

class Node: #Node Class
    def __init__(self, data):
        self.__data = data
        self.__next = None

    #Accessors
    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next
    
    #Mutators
    def setData(self,data):
        self.__data = data

    def setNext(self, next):
        self.__next = next


class EmptyQueueException(Exception): #EmptyStackException Class
    def __init__(self, action):
        message = f"Sorry, the queue is empty and we cannot {action}!"
        super().__init__(message)


class Queue: #Stack Class
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.setNext(new_node)
        self._tail = new_node

    def dequeue(self):
        if self._head is None:
            raise EmptyQueueException("dequeue")
        data = self._head.getData()
        self._head = self._head.getNext()
        if self._head is None:
            self._tail = None
        return data

    def peek(self):
        if self._head is None:
            raise EmptyQueueException("peek")
        return self._head.getData()

    def clear(self):
        self._head = None
        self._tail = None

    def __str__(self):
        elements = []
        current = self._head
        while current:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ", ".join(elements)
