"""LAB2
CPE202
Richard Hua
"""

class ArrayList:
    """Array List
    Attributes:
        capacity (int): the capacity of the list
        num_items (int): the number of items in the list
        arr (list): a python list construct which stores items
    """
    # constructor
    def __init__(self, capacity=2, num_items=0):
        self.capacity = capacity
        self.num_items = num_items
        self.arr = [None]*self.capacity

    # check if an ArrayList instance is same as another inst
    def __eq__(self, other):
        return (self.arr == other.arr)\
        and (self.capacity == other.capacity)\
        and (self.num_items == other.num_items)

    # gives class and it's parameters
    def __repr__(self):
        return 'ArrayList(capacity=%d, num_items=%d)'\
        % (self.capacity, self.num_items)

def enlarge(lst):
    """double the original capacity of an array list
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with double the original capacity
    """
    lst.arr = lst.arr + [None]*lst.capacity
    lst.capacity = 2*lst.capacity
    return lst

def shrink(lst):
    """shrink an array list by halving the original capacity.
    Args:
        lst (ArrayList): an array list object
    Returns:
        ArrayList: an array list with half the original capacity
    """
    temp = [None]*(lst.capacity//2)
    # if lst.num_items <= (lst.capacity//4):
    for i in range(len(temp)):
        temp[i] = lst.arr[i]
    lst.arr = temp

    # lst.arr = lst.arr[:lst.capacity//2]
    # lst.arr = lst.arr[:lst.capacity//2]
    # lst.arr = lst.arr - lst.arr[lst.capacity//2:]
    lst.capacity = lst.capacity//2
    return lst

def insert(lst, val, idx):
    """takes an object of ArrayList lst, a integer val, and an integer idx,
    and insert the integer val to the arr of the ArrayList object at the index
    indicated by the integer idx, and returns the ArrayList object.
    The function shall enlarge the ArrayList by calling the enlarge
    function when the ArrayList is full (num_items == capacity).
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val inserted at the idx
    """
    if idx > lst.capacity:
        raise IndexError
    if lst.num_items == lst.capacity:
        lst = enlarge(lst)
    if idx < lst.num_items:
        temp = lst.num_items
        # only possible to shift to the right based on insert functionality
        # no need to worry about shifting left
        while temp > idx:
            lst.arr[temp] = lst.arr[temp-1]
            temp = temp - 1
        lst.arr[idx] = val
        # nxt line bad idea since splicing makes copies of list
        # lst.arr = lst.arr[:idx+1] + val + lst.arr[idx+1:lst.num_items+1]
    # if idx > # num_items
    else:
        lst.arr[lst.num_items] = val
    lst.num_items = lst.num_items+1
    return lst

def get(lst, idx):
    """get an item stored at the index indicated by the integer idx
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be retrieved
    Returns:
        int: an integer value stored at the idx in the lst
    Raises:
        IndexError if the index is out of bound ( >= num_items).
    """
    if idx >= lst.num_items:
        raise IndexError
    return lst.arr[idx]

def contains(lst, val):
    """searches for the value in the list, and returns True if the value is found or False if not.
    Args:
        lst (ArrayList): an array list object
        val (int): a integer value
    Returns:
        bool: True if the value exists in the list, False otherwise.
    """
    i = 0
    while i < lst.num_items:
        if lst.arr[i] == val:
            return True
        i = i + 1
    return False

def search(lst, val):
    """Searches for val in an array list.
    Args:
        lst (ArrayList): an array list object
        val (int): a value to search for
    Returns:
        int: the index where the integer is stored in the lst
             It returns None if the integer is not found.
    """
    idx = 0
    while idx < lst.num_items:
        if lst.arr[idx] == val:
            return idx
        idx = idx + 1
    return None

def remove(lst, val):
    """removes the first occurence of the val from the lst by shifting items on right by 1 to left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1).
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity),
    and the capacity is greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        val (int): the value to be removed
    Returns:
        ArrayList: an array list with the val removed
    """
    # gives index of # or None
    idx = search(lst, val)
    if idx is None:
        return None
    # number exists or idx = items-1
    lst, val = shrink_remove_lshift(lst, idx)
    return lst

#helper function, so can be reused in pop without going through search in remove
def shrink_remove_lshift(lst, idx):
    """helper function to check to see if list needs shrinking - Assumes idx is valid
    Removes the val at index and then shifts remaining items on right 1 index left
    Finally decrements num_items after removal and returns modified list
    Args:
        lst (ArrayList): an array list object
        idx (int): index to remove value at
    Returns:
        ArrayList: an array list with the value removed
    """
    val = lst.arr[idx]
    while idx < lst.num_items-1:
        lst.arr[idx] = lst.arr[idx+1]
        idx = idx + 1
    lst.arr[lst.num_items-1] = None
    lst.num_items = lst.num_items - 1
    if (4*lst.num_items <= lst.capacity) and lst.capacity > 2:
        lst = shrink(lst)
    return lst, val

def pop(lst, idx):
    """removes the val from the lst by shifting items on the right by one to the left.
    If the item to be removed is the last item in the ArrayList (index == num_items - 1),
    simply decrement the value of num_items by 1 (num_items -= 1).
    The function shall shrink the ArrayList by calling the shrink function
    when the ArrayList is a quarter full (4 * num_items <= capacity),
    and the capacity is greater than 2 (capacity > 2).
    Args:
        lst (ArrayList): an array list object
        idx (int): the index at which the val will be inserted
    Returns:
        ArrayList: an array list with the val removed
        int: the removed value at the index
    Raises:
        IndexError: if idx is out of range.
    """
    if idx >= lst.num_items:
        raise IndexError
    # returns val removed and modified list
    # print("index", lst.arr)
    lst, val = shrink_remove_lshift(lst, idx)
    # print(lst.arr)
    return lst, val

def size(lst):
    """returns the number of items stored in the ArrayList object (returns num_items).
    Args:
        lst (ArrayList): an array list object
    Returns:
        int: the number of items stored in the array list
    """
    return lst.num_items
