from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


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
