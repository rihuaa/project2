"""Contains code for StackADTs
CPE202
Project 1

Author:
    Richard Hua
"""
from array_list import ArrayList
# from linked_list import Node
import array_list
# import linked_list

class StackArray:
    """Stack using array list
    Attributes:
        arr_list (ArrayList) : An array
        num_items (int) : number of items
    """
    def __init__(self, num_items=0):
        self.num_items = num_items
        self.arr_list = ArrayList()

    def __repr__(self):
        return 'StackArray(arr_list=%s, num_items=%s)'\
        % (self.arr_list, self.num_items)

    def __eq__(self, other):
        return (self.arr_list == other.arr_list)\
        and (self.num_items == other.num_items)

    def is_empty(self):
        """Write signature and purpose
        """
        if self.size():
            return False
        return True

    def push(self, item):
        """Write signature and purpose
        """
        # self.num_items & array_list.num_items are different
        self.arr_list = array_list.insert(self.arr_list, item, self.num_items)
        self.num_items = self.num_items + 1
        return self.arr_list

    def pop(self):
        """Write signature and purpose
        """
        # pop() from array_list only raises IndexError for idx > num_items
        # not protected against empty stack
        if self.is_empty():
            raise IndexError
        self.arr_list, val = array_list.pop(self.arr_list, self.num_items-1)
        self.num_items = self.num_items - 1
        return val

    def peek(self):
        """Write signature and purpose
        """
        if not self.size():
            raise IndexError
        return array_list.get(self.arr_list, self.num_items-1)

    def size(self):
        """Write signature and purpose
        """
        return self.num_items

class StackLinked:
    """Stack using linked list
    Attributes:
        top (Node) : a linked list
        num_items (int) : number of items
    """

    def __init__(self, num_items=0):
        self.num_items = num_items
        self.top = Node(None)

    def __repr__(self):
        return 'StackLinked(num_items=%s, %s)'\
        % (self.num_items, self.top)

    def __eq__(self, other):
        return (self.num_items == other.num_items)\
        and (self.top == other.top)

    def is_empty(self):
        """Write signature and purpose
        """
        if self.size():
            return False
        return True

    def push(self, item):
        """Write signature and purpose
        """
        self.top = linked_list.insert(self.top, item, self.num_items)
        self.num_items = self.num_items + 1
        return self.top

    def pop(self):
        """Write signature and purpose
        """
        self.top, val = linked_list.pop(self.top, self.num_items-1)
        self.num_items = self.num_items - 1
        return val

    def peek(self):
        """Write signature and purpose
        """
        if self.is_empty():
            raise IndexError
        return linked_list.get(self.top, self.num_items-1)

    def size(self):
        """Write signature and purpose
        """
        return self.num_items
