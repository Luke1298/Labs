# solutions.py
"""Volume II Lab 4: Data Structures 1 (Linked Lists)
Solutions file. Written by Shane McQuarrie.
"""

# Problem 1: Modify the constructor of the Node class.
class Node(object):
    """A basic node class for storing data."""
    def __init__(self, data):
        """Store 'data' in the 'value' attribute.

        Raises:
            TypeError: if 'data' is not of type int, long, float, or str.
        """
        if type(data) not in {int, long, float, str}:
            raise TypeError("Invalid data type")
        self.value = data


class LinkedListNode(Node):
    """A node class for doubly-linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the linked list.
    """
    def __init__(self, data):
        """Store 'data' in the 'value' attribute and initialize
        attributes for the next and previous nodes in the list.
        """
        Node.__init__(self, data)       # Use inheritance to set self.value.
        self.next = None
        self.prev = None


# Problems 2, 3, 4, 5: Complete the LinkedList class.
class LinkedList(object):
    """Doubly-linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
    """
    def __init__(self):
        """Initialize the 'head' and 'tail' attributes by setting
        them to 'None', since the list is empty initially.
        """
        self.head = None
        self.tail = None
        self._size = 0                              # for __len__()

    def append(self, data):
        """Append a new node containing 'data' to the end of the list."""
        # Create a new node to store the input data.
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, assign the head and tail attributes to
            # new_node, since it becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, place new_node after the tail.
            self.tail.next = new_node               # tail --> new_node
            new_node.prev = self.tail               # tail <-- new_node 
            # Now the last node in the list is new_node, so reassign the tail.
            self.tail = new_node
        self._size += 1                             # for __len__()

    # Problem 2: Write LinkedList.find().
    def find(self, data):
        """Return the first node in the list containing 'data'.
        If no such node exists, raise a ValueError.
        """
        current = self.head                 # Start at the head.
        while current is not None:          # Iterate through each node.
            if current.value == data:       # Check for the data.
                return current              # Return node if found; if not
            current = current.next          #  found, raise a ValueError.
        raise ValueError("{} is not in the list".format(data))

    # Problem 3: Write LinkedList.__len__() and LinkedList.__str__().
    def __len__(self):
        """Return the number of nodes in the list."""
        return self._size

    def __str__(self):
        """String representation: the same as a standard Python list."""
        # List construction method (recommended).
        current = self.head
        items = []
        while current is not None:
            items.append(current.value)
            current = current.next
        return str(items)
        # String construction method.
        current = self.head          
        out = "["
        while current is not None:
            if isinstance(current.value, str):
                item = "'{}'".format(current.value)
            else:
                item = str(current.value)
            out += item
            current = current.next
            if current is not None:
                out += ", "
        out += "]"
        return out

    # Problem 4: Write LinkedList.remove().
    def remove(self, data):
        """Remove the first node in the list containing 'data'. Return nothing.

        Raises:
            ValueError: if the list is empty, or does not contain 'data'.
        """
        target = self.find(data)            # Raise the ValueError if needed.
        if self.head is self.tail:          # Case 1: remove only node.
            self.head = None                    # reassign the head.
            self.tail = None                    # reassign the tail.
        elif target is self.head:           # Case 1: remove the head.
            self.head = self.head.next          # reassign the head.
            self.head.prev = None               # target <-/- head
        elif target is self.tail:           # Case 2: remove the tail.
            self.tail = self.tail.prev          # reassign the tail.
            self.tail.next = None               # tail -/-> target
        else:                               # Case 3: remove from middle.
            target.prev.next = target.next      # -/-> target
            target.next.prev = target.prev      # target <-/-
        self._size -= 1

    # Problem 5: Write LinkedList.insert().
    def insert(self, data, place):
        """Insert a node containing 'data' immediately before the first node
        in the list containing 'place'. Return nothing.

        Raises:
            ValueError: if the list is empty, or does not contain 'place'.
        """
        after = self.find(place)            # Raise the ValueError if needed.
        new_node = LinkedListNode(data)      # Make the new node.
        if after is self.head:              # Case 1: insert before the head.
            new_node.next = self.head           # new --> head
            self.head.prev = new_node           # new <-- head
            self.head = new_node                # reassign the head.
        else:                               # Case 2: insert to middle.
            after.prev.next = new_node          # --> new
            new_node.prev = after.prev          # <-- new
            new_node.next = after               # new -->
            after.prev = new_node               # new <--
        self._size += 1


# Problem 6: Write a SortedList class and a function called sort_file().
class SortedList(LinkedList):
    """Sorted doubly-linked list data structure class.
    Inherits from the 'LinkedList' class.
    
    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
    """

    def add(self, data):
        """Create a new Node containing 'data' and insert it at the
        appropriate location to preserve list sorting.
        """
        if self.head is None:               # Case 1: Empty list.
            LinkedList.append(self, data)
        elif self.tail.value <= data:       # Case 2: Append after the tail.
            LinkedList.append(self, data)
        else:                               # Case 3: Insert to middle.
            current = self.head
            while current.value < data:         # Find insertion location.
                current = current.next
            LinkedList.insert(self, data, current.value)
    
    def append(*args, **kwargs):
        raise NotImplementedError("append() is disabled (use add())")

    def insert(*args, **kwargs):
        raise NotImplementedError("insert() is disabled (use add())")

def sort_file(infile, outfile):
    """Sort the file 'infile' by line and write the results to 'outfile'."""
    with open(infile, 'r') as f:            # Read the lines in as a list.
        lines = f.readlines()
    sorted_list = SortedList()              # Instantiate a SortedList object.
    for line in lines:                      # Add each line to the SortedList.
        sorted_list.add(line)
    current = sorted_list.head              # Write the sorted lines to the
    with open(outfile, 'w') as f:           #  outfile.
        while current is not None:
            f.write(str(current.value))
            current = current.next


# Problem 7: Write a Deque class and a function called reverse_file().
class Deque(LinkedList):
    """Deque doubly-linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
    """
    def appendleft(self, data):
        """Place a new node containing 'data' at the beginning of the list."""
        if self.head is None:               # Case 1: Empty list.
            LinkedList.append(self, data)
        else:                               # Case 2: Nonempty list.
            LinkedList.insert(self, data, self.head.value)

    def pop(self):
        """Remove the last node in the list and return its value."""
        if self.tail is None:               # Case 1: Empty list.
            raise ValueError("The list is empty")
        else:                               # Case 2: Nonempty list.
            data = self.tail.value
            LinkedList.remove(self, data)
            return data

    def popleft():
        """Remove the first node in the list and return its value."""
        if self.head is None:               # Case 1: Empty list.
            raise ValueError("The list is empty")
        else:                               # Case 2: Nonempty list.
            data = self.head.value
            LinkedList.remove(self, data)
            return data

    def remove(*args, **kwargs):
        raise NotImplementedError("remove() is disabled")

    def insert(*args, **kwargs):
        raise NotImplementedError("insert() is disabled")

def reverse_file(infile, outfile):
    """Reverse the file 'infile' by line and write the results to 'outfile'."""
    with open(infile, 'r') as f:            # Read the lines in as a list.
        lines = f.readlines()
    deque = Deque()                         # Instantiate a SortedList object.
    for line in lines:                      # Add each line to the SortedList.
        print(repr(line))
        deque.append(line)
    with open(outfile, 'w') as f:           # Write to the outfile in reverse.
        while deque.head is not None:
            f.write(str(deque.pop()))


# END OF SOLUTIONS ========================================================== #


from numpy.random import permutation # numpy is not required for this lab

def test(student_module, late=False):
    """Test script. You must import the student's 'solutions.py' and 'Node.py'
    files as modules.
    
     5 points for problem 1
    10 points for problem 2
    10 points for problem 3
    15 points for problem 4
    20 points for problem 5
    20 points for problem 6
    
    Inputs:
        student_module: the imported module for the student's file.
        late (bool): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 80.
        feedback (str): a printout of test results for the student.
    """
    s = student_module
    SNode = s.LinkedListNode
    score = 0
    total = 80
    feedback = ""

    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\t\tCorrect response: " + str(x)
            m += "\n\t\tStudent response: " + str(y)
            return 0, m
    
    def testTail(x,y,m):
        """Test to see if x and y have the same tail attribute. If correct,
        award a point and return no message. If incorrect, return 0 and
        return 'm' as feedback. Problematic if list has 0 or 1 entries.
        """
        if x.tail.prev.next == y.tail.prev.next: return 1, ""
        else:
            m += "\n\t\tCorrect tail: " + str(x)
            m += "\n\t\tStudent tail: " + str(y)
            return 0, m
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p,""
        else: return part,m
    
    def shrink_file(infile, outfile):
        """Shrink the dataset in problem 6 so it can be tested quickly."""
        try:
            f = open(infile, 'r')
            f = f.read()
            f = f.split('\n')
            f = f[:-1]
            x = list(permutation(f))[::20]
            f = open(outfile, 'w')
            for i in x:
                f.write(i + '\n')
            f.close()
        except IOError:
            raise IOError(str(infile) + " not found!")
    
    try:    # Problem 1: 5 points
        feedback += "\n\nProblem 1 (5 points):"
        points = 0
        # Comparison magic methods
        n1 = SNode(5)
        n2 = SNode(5)
        if not (n1 < n2): points += 1
        if n1 == n2: points += 1
        n1 = SNode(4)
        n2 = SNode(6)
        if n1 < n2: points += 1
        if points < 3:
            feedback += "\n\t" + str(3-points)
            feedback += " Node class comparison magic method(s) failed"
        # __str__
        n1 = Node(6)
        p,f = strTest(n1,n2,"\n\tNode.__str__ failed")
        points += (p * 2); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 10 points
        feedback += "\n\nProblem 2 (10 points):"
        points = 0
        # Empty list
        l1 = list()
        l2 = s.LinkedList()
        p,f = strTest(l1,l2,"\n\tLinkedList.__str__ failed on empty list")
        points += p; feedback += f
        # Single item
        l1.append('this')
        l2.add('this')
        p,f = strTest(l1,l2,"\n\tLinkedList.__str__ failed with single item")
        points += (p * 3); feedback += f
        # Two items
        l1.append('little')
        l2.add('little')
        p,f = strTest(l1,l2,"\n\tLinkedList.__str__ failed with two items")
        points += (p * 3); feedback += f
        # Many items
        entries = ['Linked List',3,10.0,-1+3j,set(),[1,2,3]]
        for i in entries:
            l1.append(i)
            l2.add(i)
        p,f = strTest(l1,l2,"\n\tLinkedList.__str__ failed with many items")
        points += (p * 3); feedback += f
        if points == 0:
            feedback += "\n\tCheck LinkedList.add() and LinkedList.__str__"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        l1 =   LinkedList()
        l2 = s.LinkedList()
        # remove() from empty list
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.remove(100)
            feedback += "\n\tNo exception raised by LinkedList.remove()"
            feedback += " on empty list"
        except ValueError as e:
            points += 1; print(e.message)
            p,f = grade(1,
                "\n\tLinkedList.remove() failed to report on empty list")
            points += p; feedback += f;
        # Test add() (no credit, but vital for other points)
        for i in [1,3,2,5,4,7,6,9,8]:
            l1.add(i); l2.add(i)
        p,f=strTest(l1,l2,
            "\n\tIf LinkedList.__str__ fails, these tests will all fail!")
        feedback += f
        # remove() head
        l1.remove(1); l1.remove(3)
        l2.remove(1); l2.remove(3)
        p,f = strTest(l1,l2, "\n\tLinkedList.remove() failed on head removal")
        points += (p * 2); feedback += f
        # remove() end
        l1.remove(8); l1.remove(9)
        l2.remove(8); l2.remove(9)
        p,f = strTest(l1,l2, "\n\tLinkedList.remove() failed on tail removal")
        points += (p * 2); feedback += f
        # remove() from middle
        l1.remove(5); l1.remove(4)
        l2.remove(5); l2.remove(4)
        p,f=strTest(l1,l2, "\n\tLinkedList.remove() failed on middle removal")
        points += (p * 2); feedback += f
        # remove() nonexistent
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.remove(100)
            feedback += "\n\tNo exception raised by LinkedList.remove(x)"
            feedback += " for 'x' not in list"
        except ValueError as e:
            points += 1; print(e.message)
            p,f = grade(1,
                "\n\tLinkedList.remove(x) failed to report for 'x' not in list")
            points += p; feedback += f;
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 15 Points
        feedback += "\n\nProblem 4 (15 points):"
        points = 0
        l1 =   LinkedList()
        l2 = s.LinkedList()
        # insert() empty list
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.insert(1,100)
            feedback += "\n\tNo exception raised by LinkedList.insert()"
            feedback += " on empty list"
        except ValueError as e:
            points += 1; print(e.message)
            p,f = grade(1,
                "\n\tLinkedList.insert() failed to report on empty list")
            points += p; feedback += f;
        # insert() before head
        l1.add(5); l1.insert(3,5); l1.insert(1,3)
        l2.add(5); l2.insert(3,5); l2.insert(1,3)
        p,f=strTest(l1,l2,"\n\tLinkedList.insert() failed on head insertion")
        points += (p * 5); feedback += f
        # insert() in the middle
        l1.insert(2,3); l1.insert(4,5)
        l2.insert(2,3); l2.insert(4,5)
        p,f=strTest(l1,l2,
            "\n\tLinkedList.insert() failed on middle insertion")
        points += (p * 5); feedback += f
        # insert(place, x) on nonexistant place
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.insert(1,100)
            feedback += "\n\tNo exception raised by LinkedList.insert(x, place)"
            feedback += " for 'place' not in list"
        except ValueError as e:
            points += 2; print(e.message)
            p,f = grade(1, "\n\tLinkedList.remove(x, place)" + 
                                " failed to report for 'place' not in list")
            points += p; feedback += f;
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 5: 20 points
        feedback += "\n\nProblem 5 (20 points):"
        points = 0
        l1 =   DoublyLinkedList()
        l2 = s.DoublyLinkedList()
        # remove() from empty list
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.remove(100)
            feedback += "\n\tNo exception raised by DoublyLinkedList.remove()"
            feedback += " on empty list"
        except ValueError as e:
            print(e.message)
            p,f = grade(1,
                "\n\tDoublyLinkedList.remove() failed to report on empty list")
            points += p; feedback += f;
        # Test add() (no credit, but vital for other points)
        for i in [1,3,2,5,4,7,6,9,8]:
            l1.add(i); l2.add(i)
        p,f = strTest(l1,l2,"\n\tDoublyLinkedList.add() failed")
        feedback += f
        p,f = testTail(l1,l2,"\n\tDoublyLinkedList.tail failed on add()")
        points += p; feedback += f
        # remove() head
        l1.remove(1); l1.remove(3)
        l2.remove(1); l2.remove(3)
        p,f = strTest(l1,l2,
            "\n\tDoublyLinkedList.remove() failed on head removal")
        points += (p * 2); feedback += f
        p,f = testTail(l1,l2,
            "\n\tDoublyLinkedList.tail failed on head removal")
        points += p; feedback += f
        # remove() end
        l1.remove(8); l1.remove(9)
        l2.remove(8); l2.remove(9)
        p,f = strTest(l1,l2,
            "\n\tDoublyLinkedList.remove() failed on tail removal")
        points += (p * 2); feedback += f
        p,f = testTail(l1,l2,
            "\n\tDoublyLinkedList.tail failed on tail removal")
        points += p; feedback += f
        # remove() from middle
        l1.remove(5); l1.remove(4)
        l2.remove(5); l2.remove(4)
        p,f=strTest(l1,l2,
            "\n\tDoublyLinkedList.remove() failed on middle removal")
        points += (p * 2); feedback += f
        p,f = testTail(l1,l2,
            "\n\tDoublyLinkedList.tail failed on middle removal")
        points += p; feedback += f
        # remove() nonexistent
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.remove(100)
            feedback += "\n\tNo exception raised by DoublyLinkedList.remove(x)"
            feedback += " for 'x' not in list"
        except ValueError as e:
            print(e.message)
            p,f = grade(1, "\n\tDoublyLinkedList.remove(x)" + 
                                " failed to report for 'x' not in list")
            points += p; feedback += f;
        # insert() empty list
        l1.__init__(); l2.__init__()
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.insert(1,100)
            feedback += "\n\tNo exception raised by DoublyLinkedList.insert()"
            feedback += " on empty list"
        except ValueError as e:
            print(e.message)
            p,f = grade(1, "\n\tDoublyLinkedList.insert()" + 
                                " failed to report on empty list")
            points += p; feedback += f;
        # insert() before head
        l1.add(5); l1.insert(3,5); l1.insert(1,3)
        l2.add(5); l2.insert(3,5); l2.insert(1,3)
        p,f=strTest(l1,l2,
            "\n\tDoublyLinkedList.insert() failed on head insertion")
        points += (p * 2); feedback += f
        p,f = testTail(l1,l2,
            "\n\tDoublyLinkedList.tail failed on head insertion")
        points += p; feedback += f
        # insert() in the middle
        l1.insert(2,3); l1.insert(4,5)
        l2.insert(2,3); l2.insert(4,5)
        p,f=strTest(l1,l2,
            "\n\tDoublyLinkedList.insert() failed on middle insertion")
        points += (p * 2); feedback += f
        p,f = testTail(l1,l2,
            "\n\tDoublyLinkedList.tail failed on middle insertion")
        points += p; feedback += f
        # insert(place, x) on nonexistant place
        print("\nCorrect output:\t100 is not in the list.")
        print("Student output:\t"),
        try:
            l2.insert(1,100)
            feedback += "\n\tNo exception raised by"
            feedback += " DoublyLinkedList.insert(x,place)"
            feedback += " for 'place' not in list"
        except ValueError as e:
            print(e.message)
            p,f = grade(1, "\n\tDoublyLinkedList.remove(x,place)" + 
                                " failed to report for 'place' not in list")
            points += p; feedback += f;
        if not issubclass(s.DoublyLinkedList, s.LinkedList):
            points = 0
            feedback += "\n\tDoublyLinkedList must inherit from LinkedList!"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 6: 20 points
        feedback += "\n\nProblem 6 (20 points):"
        points = 0
        l1 =   SortedLinkedList()
        l2 = s.SortedLinkedList()
        # Test sorting (9 points)
        # test 1
        entries = [1,2,3,4,5,6,7,8,9]
        for i in entries:
            l1.add(i); l2.add(i)
        p,f = strTest(l1,l2,"\n\tSortedLinkedList.add() failed")
        points += (p * 3); feedback += f
        # test 2
        l1.__init__(); l2.__init__()
        entries = [9,8,7,6,5,4,2,3,1]
        for i in entries:
            l1.add(i); l2.add(i)
        p,f = strTest(l1,l2,"\n\tSortedLinkedList.add() failed")
        points += (p * 3); feedback += f
        # test 3
        l1.__init__(); l2.__init__()
        entries = [1,3,5,7,9,2,4,6,8]
        for i in entries:
            l1.add(i); l2.add(i)
        p,f = strTest(l1,l2,"\n\tSortedLinkedList.add() failed")
        points += (p * 3); feedback += f
        # Test that insert() was disabled (1 point)
        print("\nCorrect output:\tinsert() has been disabled for this class.")
        print("Student output:\t"),
        try:
            l2.insert(1,2,3,4,5)
            feedback += "\n\tNo ValueError exception raised by"
            feedback += " SortedLinkedList.insert()"
        except NotImplementedError as e:
            print(e.message)
            p,f = grade(1, "\n\tSortedLinkedList.insert()" + 
                                " failed to report as disabled")
            points += p; feedback += f;
        except TypeError:
            feedback += "\n\tSortedLinkedList.insert() not disabled correctly"
            feedback += "\n\t\t(insert() should accept any number of arguments)"
        # 10 points for correct sort_words() output.
        shrink_file("English.txt", "Short.txt")
        word_list = create_word_list("Short.txt")
        word_list.sort()
        out = s.sort_words("Short.txt")
        p,f = strTest(word_list, out, "\n\tsort_words() function failed.")
        points += (p * 10); feedback += f
        # detect cheating
        if out.__doc__ != l2.__doc__:
            points = 0
            feedback += "\n\tA SortedLinkedList object must be "
            feedback += "returned in sort_words()!"
        if not issubclass(s.SortedLinkedList, s.DoublyLinkedList):
            points = 0
            feedback += "\n\tSortedLinkedList must inherit "
            feedback += "from DoublyLinkedList!"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if percentage < 72.0 and not late:
        feedback += "\n\nOn any given problem, if one test fails then"
        feedback += " subsequent tests are likely to fail.\nFix the tests in"
        feedback += " the order that they are mentioned in this feedback file."
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    feedback += "\n\n-------------------------------------------------------\n"
    return score, feedback
