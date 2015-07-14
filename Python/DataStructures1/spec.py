# name this file 'solutions.py'
"""Volume II Lab 4: Data Structures 1
<Name>
<Class>
<Date>
"""

from Node import LinkedListNode
from WordList import create_word_list


# Problem 1: in Node.py, add magic methods to the Node class.


# Problems 2, 3, 4: Complete the implementation of this class for creating linked lists.
class LinkedList(object):
    """Singly-linked list data structure class.
    The first node in the list is referenced to by 'head'.
    """
    def __init__(self):
        """Create a new empty linked list. Create the head
        attribute and set it to None since the list is empty.
        """
        self.head = None

    def add(self, data):
        """Create a new Node containing 'data' and add it to
        the end of the list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.head.data
            1
            >>> my_list.add(2)
            >>> my_list.head.next.data
            2
        """
        
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, point the head attribute to the new node.
            self.head = new_node
        else:
            # If the list is not empty, traverse the list
            # and place the new_node at the end.
            current_node = self.head
            while current_node.next is not None:
                # This moves the current node to the next node if it is not
                # empty. Then when we break out of the loop, current_node
                # points to the last node in the list.
                current_node = current_node.next
            
            current_node.next = new_node
    
    # Problem 2: Implement the __str__ method so that a LinkedList instance can
    #   be printed out the same way that Python lists are printed.
    def __str__(self):
        """String representation: the same as a standard Python list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.add(2)
            >>> my_list.add(3)
            >>> print(my_list)
            [1, 2, 3]
            >>> str(my_list) == str([1,2,3])
            True
        """
        return ""

    # Problem 3: Finish implementing LinkedList.remove() so that if the node
    #   is not found, an exception is raised.
    def remove(self, data):
        """Remove the node containing 'data'. If the list is empty, or if the
        target node is not in the list, raise a ValueError with error message
        "<data> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.remove(2)
            >>> print(my_list)
            [1, 3]
            >>> my_list.remove(2)
            2 is not in the list.
            >>> print(my_list)
            [1, 3]
        """
        
        # First, check if the head is the node to be removed. If so, set the
        # new head to be the first node after the old head. This removes
        # the only reference to the old head, so it is then deleted.
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            # Move current_node through the list until it points to the node
            # that precedes the target node.
            while current_node.next.data != data:
                current_node = current_node.next
            
            # Point current_node to the node after the target node.
            new_next_node = current_node.next.next
            current_node.next = new_next_node

    # Problem 4: Implement LinkedList.insert().
    def insert(self, data, place):
        """Create a new Node containing 'data'. Insert it into the list before
        the first Node in the list containing 'place'. If the list is empty, or
        if there is no node containing 'place' in the list, raise a ValueError
        with error message "<place> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 3]
            >>> my_list.insert(2,3)
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.insert(2,4)
            4 is not in the list.
        """
        raise NotImplementedError("Problem 4 incomplete.")


# Problem 5: Implement this class for creating doubly-linked lists.
class DoublyLinkedList(LinkedList):
    """Doubly-linked list data structure class. Inherits from the 'LinkedList'
    class. Has a 'head' for the front of the list and a 'tail' for the end.
    """
    def __init__(self):
        raise NotImplementedError("Problem 5 incomplete")


# Problem 6: Implement this class for creating sorted linked lists.
#   Use an instance of your object to sort a large data set in sort_words().
class SortedLinkedList(DoublyLinkedList):
    """Sorted doubly-linked list data structure class."""

    # Overload add() and insert().
    def add(self, data):
        """Create a new Node containing 'data' and insert it at the
        appropriate location to preserve list sorting.
        
        Example:
            >>> print(my_list)
            [3, 5]
            >>> my_list.add(2)
            >>> my_list.add(4)
            >>> my_list.add(6)
            >>> print(my_list)
            [2, 3, 4, 5, 6]
        """
        raise NotImplementedError("Problem 6 incomplete")

# Conclude problem 6 by implementing this function.
def sort_words(filename = "English.txt"):
    """Use the 'create_word_list' method from the 'WordList' module to generate
    a scrambled list of words from the specified file. Use an instance of
    the SortedLinkedList class to sort the list. Then return the list.
    
    Inputs:
        filename (str, opt): the file to be parsed and sorted. Defaults to
            'English.txt.
    
    Returns:
        The SortedLinkedList object containing the sorted list.
    """
    raise NotImplementedError("Problem 6 incomplete.")

# =========================== END OF File =========================== #