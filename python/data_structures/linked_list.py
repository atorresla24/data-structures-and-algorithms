class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        text = ""
        current = self.head

        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            current = current.next
        return text + "NULL"

    def includes(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_before(self, target, new):
        if self.head is None:
            raise TargetError
        current = self.head
        if current.value == target:
            new_node = Node(new)
            new_node.next = self.head
            self.head = new_node
            return "Success"
        while current is not None:
            if current.next.value == target:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Success"
            current = current.next

    def insert_before_first(self, target, new):
        if self.head is None:
            raise TargetError
        current = self.head
        if current.value == target:

            while current is not None:
                if current.value == target:
                    new_node = Node(new)
                    new_node.next = current.next
                    current.next = new_node
                    return f"Success"
                current = current.next

    def insert_after(self, target, new):
        if self.head is None:
            raise TargetError
        current = self.head
        while current is not None:
            if current.value == target:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Success"
            current = current.next

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError(Exception):
    pass
