# doubly linked list with node

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

##########################################################################################

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_from_head(self):
        val = self.head.value
        self.delete(self.head)
        return val

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length+=1

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_tail(self):
        val = self.tail.value
        self.delete(self.tail)
        return val

    def move_to_front(self, node):
        value = node.value
        if node == self.head:
            return
        if node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        if node == self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    def delete(self, node):
        self.length -= 1
        # if empty
        if not self.head:
            print('nothing doing')
            return

        # if just one node
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # at least two nodes and we want to delete the head
        elif node == self.head:
            self.head = node.next
            node.delete()

        #  we want to delete tail
        elif node == self.tail:
            self.tail = node.prev
            node.delete()     

        else:
            node.delete() # refers to method line 29

    def get_max(self):
        if not self.head:
            return None

        max_val = self.head.value
        current = self.head

        while current:
            if current.value > max_val:
                max_val = current.value
            else:
                current = current.next

        return max_val
