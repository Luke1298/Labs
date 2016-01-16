
#Problem 4 Write tests for the Linked List Class (be sure to do sub classes seperatly, and for linkedlist node consider different data types)
class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def __lt__(self, other):
        if type(self.data) != type(other.data):
            raise ValueError("To compare nodes with __lt__ they must be of the same type")
        if self.data < other.data:
            return True
        else:
            return False
    def __eq__(self, other):
        if type(self.data) != type(other.data):
            raise ValueError("To compare nodes with __eq__ they must be of the same type")
        if self.data == other.data:
            return True
        else:
            return False
    def __gt__(self, other):
        if type(self.data) != type(other.data):
            raise ValueError("To compare nodes with __gt__ they must be of the same type")
        if self.data > other.data:
            return True
        else:
            return False

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        """
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
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def __str__(self):
        """
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
        return_list = []
        if self.head is None:
            return str(return_list)
        else:
            current_node = self.head
            while current_node.next is not None:
                return_list.append(current_node.data)
                current_node = current_node.next
            return_list.append(current_node.data) # Catches the last one, since it's next certainly will be falsely.
            return str(return_list)

    def remove(self, data):
        """
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
        if self.head is None:
            raise ValueError(str(data) +" is not in the list.")
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            try:
                while current_node.next.data != data:
                    current_node = current_node.next
                new_next_node = current_node.next.next
                current_node.next = new_next_node
            except:
                raise ValueError(str(data) +" is not in the list.")

    def insert(self, data, place):
        """
        Example:
            >>> print(my_list)
            [1, 3]
            >>> my_list.insert(2,3)
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.insert(2,4)
            4 is not in the list.
        """
        try:
            current = self.head
            temp = LinkedListNode(data)
            previous = None
            if current.data == place:
                temp.next = self.head
                self.head = temp
            else:
                while current.data != place:
                    previous = current
                    current = current.next
                    if current.data == place:
                        break
                previous.next = temp
                temp.next = current
                temp.back = previous
                current.back = temp
                current = self.head
        except:
            raise ValueError(str(place) + " is not in the list.")

