# name this file 'solutions.py'
"""Volume II Lab 5: Data Structures II (Trees)
<Name>
<Class>
<Date>
"""

from Trees import BST
from Trees import AVL

def iterative_search(linkedlist, data):
    """Find the node containing 'data' using an iterative approach.
    If there is no such node in the list, raise a ValueError with error
    message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    current = linkedlist.head
    while current.data != data:
        if current.next is None:
            raise ValueError(str(data) + " is not in the list.")
        else:
            current = current.next
    return current

# Problem 1: rewrite iterative_search() using recursion.
def recursive_search():
    """Find the node containing 'data' using a recursive approach.
    If there is no such node in the list, raise a ValueError with error
    message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    pass

# Problem 2: Implement BST.insert() in Trees.py.

# Problem 3: Implement BST.remove() in Trees.py

# Problem 4: Test build and retrieval times for LinkedList, BST, and AVL objects.
def test_build_times():
    pass

def test_search_times():
    pass