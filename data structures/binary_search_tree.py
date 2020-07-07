# binary search tree with node

import sys
sys.path.append('../queue')
from queue import Queue

sys.path.append('../stack')
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        if value < self.value:
            # go left
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # all the way to the right
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        ordered = []

        ordered.append(self)

        while len(ordered) > 0:
            current = ordered.pop()
            if current.right:
                ordered.append(current.right)
            if current.left:
                ordered.append(current.left)

            (current.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)

        while bft_queue.__len__() != 0:
            current_node = bft_queue.dequeue()
            if current_node.left is not None:
                bft_queue.enqueue(current_node.left)
            if current_node.right is not None:
                bft_queue.enqueue(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(node)

        while dft_stack.__len__() != 0:
            current_node = dft_stack.pop()
            if current_node.left is not None:
                dft_stack.push(current_node.left)
            if current_node.right is not None:
                dft_stack.push(current_node.right)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
