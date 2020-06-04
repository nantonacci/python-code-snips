# queue with doubly linked list and with an array

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# using linked list
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        
        removed_value = self.storage.remove_from_head()
        self.size -= 1

        return removed_value
        
###############################################################################################

# using array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def dequeue(self):
        if self.size>0:
            self.size -= 1
            return self.storage.pop()
        else:
            return None
