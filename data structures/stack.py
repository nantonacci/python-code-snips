# stacks with doubly linked list and with an array

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            popped_val = self.storage.remove_from_tail()
            return popped_val
        else:
            return None

###############################################################################################

# array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        else:
            return None