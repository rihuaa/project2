"""LAB2
CPE202
Richard Hua
"""

class Node:
    """Linked List is one of None or Node
    Attributes:
        val (int): an item in the list
        next (Node): a link to the next item in the list (Linked List)
    """
    def __init__(self, val, nxt=None):
        # self.head = head
        self.val = val
        self.next = nxt

    def __repr__(self):
        return "Node(data=%s, next=%s)"\
        % (self.val, self.next)

    def __eq__(self, other):
        return (self.val == other.val)\
        and (self.next == other.next)


def insert(lst, val, pos):
    """inserts the integer at the position pos in the linked list recursively.
    Args:
        lst (Node)": the list
        val (int): the value to be inserted in the list
        pos (int): the position
    Returns:
        Node: the head of a LinkedList
    Raises:
        IndexError: when the position is out of bound ( > num_items).
    """
    if pos > size(lst):
        raise IndexError
    # keep decr pos until u get to ur pos from left to right
    new = Node(val)
    if (lst is None) and pos == 0:
        return new
    if (lst is not None) and pos == 0:
        new.next = lst
        lst = new
    lst.next = insert(lst.next, val, pos-1)
    return lst

def get(lst, pos):
    """gets an item stored at the specified position recursively.
    Args:
        lst (Node): a head of linked list
        pos (int): the specified position
    Returns:
        int: the value of the item at the position pos.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if lst is None:
        return None
    if pos == 0:
        return lst.val
    if pos < 0 or pos >= size(lst):
        raise IndexError
    return get(lst.next, pos-1)

def search(lst, val):
    """searches for a specified value in a given list.
    Args:
        lst (Node): an object of Node (LinkedList)
        val (int): a value to search for
    Returns:
        int: the position where the value is stored in the list.
            It returns None if the value is not found.
    """
    pos = 0
    return search_helper(lst, val, pos)

def search_helper(lst, val, pos):
    """searches for a specified value in a given list.
    Args:
        lst (Node): an object of Node (LinkedList)
        val (int): a value to search for
        pos (int): loc of curr pos
    Returns:
        int: the position where the value is stored in the list.
            It returns None if the value is not found.
    """
    if lst is None:
        return None
    if lst.val == val:
        return pos
    return search_helper(lst.next, val, pos+1)

def contains(lst, val):
    """checks if a specified value exists in a given list.
    This function calls search function.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        bool: True if the value is found or False if not.
    """
    if search(lst, val) is None:
        return False
    return True

def remove(lst, val):
    """removes the first occurrence of a specified value in a given list recursively.
    Args:
        lst (Node): the head of a LinkedList
        val (int): a value to be removed
    Returns:
        Node: the head of the linked list with the first occurrence of the value removed.
    """
    if lst is None:
        return None
    if lst.val == val:
        # lst.next = remove()
        return lst.next
    lst.next = remove(lst.next, val)
    return lst

def pop(lst, pos):
    """removes the item at a specified position in a given list recursively
    Args:
        lst (Node): the head of a LinkedList
        pos (int): the position in the list where an item is removed
    Returns:
        Node: the head of the LinkedList with the item removed
        int: the removed item’s value.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if pos < 0 or pos >= size(lst):
        raise IndexError
    if lst is None:
        return None
    if pos == 0:
        return lst.next, lst.val
    lst.next, val = pop(lst.next, pos-1)
    return lst, val

def size(lst):
    """returns the number of items stored in the LinkedList recursively.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        int: the number of items stored in the list
    """
    if lst is None:
        return 0
    return 1 + size(lst.next)
