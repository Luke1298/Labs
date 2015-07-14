# Node.py
"""Volume II Lab 4: Data Structures 1 (Linked Lists). Auxiliary file.
Define various Node classes. Modify this file for problem 1.
<Name>
<Class>
<Date>
"""


# Problem 1: Add the magic methods __str__, __lt__, __eq__, and __gt__.
class Node(object):
    """A Node class for storing data."""
    def __init__(self, data):
        """Construct a new node that stores some data."""
        self.data = data


class LinkedListNode(Node):
    """A Node class for linked lists. Inherits from the 'Node' class.
    Contains a reference to the next node in the list.
    """
    def __init__(self, data):
        """Construct a Node and initialize an attribute for the next
        node in the list.
        """
        Node.__init__(self, data)
        self.next = None


class DoublyLinkedListNode(LinkedListNode):
    """A Node class for doubly-linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the list.
    """
    def __init__(self,data):
        """Initialize the next and prev attributes."""
        Node.__init__(self,data)
        self.next = None
        self.prev = None

# =============================== END OF FILE =============================== #
