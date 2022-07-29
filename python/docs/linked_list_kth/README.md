# Code Challenge 7

# Challenge Summary

k-th value from the end of a linked list.

## Whiteboard Process

![linked list kth](CodeChallenge7.jpg)

## Approach & Efficiency



## Solution

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError
        length = self.get_length()
        if k >= length:
            raise TargetError
        target_idx = (length - 1) - k
        current_idx = 0
        current = self.head
        while current:
            if current_idx == target_idx:
                return current.value
            current_idx += 1
            current = current.next

## Collaborators
Ryan McMillan, Ricky Plaza, Jamal Malik