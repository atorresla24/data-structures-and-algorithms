# Code Challenge 8

## Challenge Summary

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Whiteboard

![Stacks and Queue](CodeChallenge10.jpg)

## Approach & Efficiency


## Solution

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if self.front == None:
            raise InvalidOperationError

        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return not self.front

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.top = None
        self.size = 0

    def push(self, value):
        # method body here
        self.top = Node(value, self.top)

    def pop(self):
        if self.top == None:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_top = self.top
        self.top = old_top.next
        old_top.next = None
        return old_top.value

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return self.size == 0

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

## Collaborators
Ryan McMillan, Ricky Plaza, Jamal Malik