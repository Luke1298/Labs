# Packs.py
"""Volume II Lab 2: Object Oriented Programming.
<Name>
<Class>
<Date>
"""

# Problem 1: Modify this class. Add 'name' and max_size' attributes, modify
#   the put() method, and add a dump() method. Remember to update docstrings.
class Backpack(object):
    """Backpack object. Has a color, and a list of contents
    
    Attributes:
        color (str): the color of the backpack.
        contents (list): the contents of the backpack.
    """

    def __init__(self, color, name, max_size=5):
        """Set the color and initialize an empty contents list.
        
        Inputs:
            color (str): the color of the backpack.
        
        Returns:
            A backpack object wth no contents.
        """
        self.color = color
        self.contents = []
    
    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        self.contents.append(item)
    
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
    
    # Magic Methods -----------------------------------------------------------
    
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)
    
    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)

    # Problem 3: Write the __str__ and __eq__ methods for the Backpack class.


# Study this example of inheritance. You are not required to modify it.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.
    
    Attributes:
        color (str): the color of the knapsack.
        name (str): the name of the knapsack.
        max_size (int): the maximum number of items that can fit
            in the knapsack.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    
    def __init__(self, color, name, max_size=3):
        """Use the Backpack constructor to initialize the name and
        max_size attributes. A knapsack only holds 3 item by default
        instead of 5. 
        
        Inputs:
            color (str): the color of the knapsack.
            name (str): the name of the knapsack.
            max_size (int, opt): the maximum number of items that can be
                stored in the knapsack. Defaults to 3.
        
        Returns:
            A knapsack object with no contents.
        """
        
        Backpack.__init__(self, color, name, max_size)
        self.closed = True
    
    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print "I'm closed!"
        else:
            Backpack.put(self, item)
    
    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print "I'm closed!"
        else:
            Backpack.take(self, item)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.

# Problem 4: Write your own 'ComplexNumber' class.
