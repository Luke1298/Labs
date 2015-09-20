# new_neighbor.py
"""Volume II Lab 7: K-D Trees and the Nearest Neighbor Search Problem
    Written by Shane McQuarrie, Summer 2015
    We should make this lab 6 as a follow-up to the BST lab.
    KBacon can go later.
"""

# =================== BSTNode / BST Classes from Trees.py =================== #
class BSTNode(object):
    """A Node class for Binary Search Trees. Contains some data, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        """Construct a new node and set the data attribute. The other
        attributes will be set when the node is added to a tree.
        """
        self.data = data
        self.prev = None        # A reference to this node's parent node
        self.left = None        # self.left.data < self.data
        self.right = None       # self.data < self.right.data
        
    def __str__(self):
        """String representation: the data contained in the node."""
        return str(self.data)

# Modify this class for problems 2 and 3
class BST(object):
    """Binary Search Tree data structure class.
    The first node is referenced to by 'root'.
    """
    def __init__(self):
        """Initialize the root attribute."""
        self.root = None
    
    def find(self, data):
        """Return the node containing 'data'. If there is no such node in the
        tree, raise a ValueError with error message "<data> is not in the tree."
        """
        # First, check to see if the tree is empty
        if self.root is None:
            raise ValueError(str(data) + " is not in the tree.")
        
        # Define a recursive function to traverse the tree
        def _step(current, item):
            """Recursively step through the tree until the node containing
            'item' is found. If there is no such node, raise a Value Error.
            """
            if current is None:                     # Base case 1: dead end
                raise ValueError(str(data) + " is not in the tree.")
            if item == current.data:                # Base case 2: data matches
                return current
            if item < current.data:                 # Step to the left
                return _step(current.left,item)
            else:                                   # Step to the right
                return _step(current.right,item)
        
        # Start the recursion on the root of the tree.
        return _step(self.root, data)
    
    # Problem 2: Implement BST.insert()
    def insert(self, data):
        """Insert a new node containing 'data' at the appropriate location.
        Do not allow for duplicates in the tree: if there is already a node
        containing 'data' in the tree, raise a ValueError.
        
        Example:
            >>> b = BST()       |   >>> b.insert(1)     |       (4)
            >>> b.insert(4)     |   >>> print(b)        |       / \
            >>> b.insert(3)     |   [4]                 |     (3) (6)
            >>> b.insert(6)     |   [3, 6]              |     /   / \
            >>> b.insert(5)     |   [1, 5, 7]           |   (1) (5) (7)
            >>> b.insert(7)     |   [8]                 |             \
            >>> b.insert(8)     |                       |             (8)
        """
        
        def _find_parent(current, item):
            """Recursively descend through the tree to find the node that
            should be the parent of the new node. Do not allow for duplicates.
            """
            if item == current.data:                # Base case 1: duplicate
                raise ValueError(str(item) + " is already in the tree.")
            if current is None:                     # Base case 2: failure
                raise ValueError("_find_parent() failed for " + str(item))
            if item < current.data:                 # Step to the left
                if current.left:
                    return _find_parent(current.left,item)
                else:                               # Base case: parent found
                    return current
            else:                                   # Step to the right
                if current.right:
                    return _find_parent(current.right,item)
                else:                               # Base case: parent found
                    return current
        
        n = BSTNode(data)                           # Make a new node
        if self.root is None:                       # Case 1: empty tree
            self.root = n                               # reset the root
        else:                                       # Case 2: use _find_parent
            parent = _find_parent(self.root,data)       # Get the parent
            if data < parent.data:                      # Insert as left child
                parent.left = n
            else:                                       # Insert as right child
                parent.right = n
            n.prev = parent                             # Double link
    
    # Problem 3: Implement BST.remove()
    def remove(self, data):
        """Remove the node containing 'data'. Consider several cases:
            - The tree is empty
            - The target is the root:
                - The root is a leaf node, hence the only node in the tree
                - The root has one child
                - The root has two children
            - The target is not the root:
                - The target is a leaf node
                - The target has one child
                - The target has two children
            If the tree is empty, or if there is no node containing 'data',
            raise a ValueError.
        
        Examples:
        
            >>> print(b)        |   >>> b.remove(1)     |   [3]
            [4]                 |   >>> b.remove(7)     |   [5]
            [3, 6]              |   >>> b.remove(6)     |   [8]
            [1, 5, 7]           |   >>> b.remove(4)     |
            [8]                 |   >>> print(b)        |
        """
        
        def _predecessor(node):
            """Find the next-smallest node in the tree by travelling
            right once, then left as far as possible.
            """
            if node.right is None:          # Function called inappropriately
                raise ValueError("IOP problem")
            node = node.right               # Step right once
            while node.left:
                node = node.left            # Step right until done
            return node
        
        # Case 1: the tree is empty
        if self.root is None:
            raise ValueError("The tree is empty.")
        # Case 2: the target is the root
        target = self.find(data)
        if target == self.root:
            # Case 2a: no children
            if not self.root.left and not self.root.right:
                self.__init__()
            # Case 2b: one child
            if not target.right:
                self.root = target.left
            elif not target.left:
                self.root = target.right
            # Case 2c: two children
            else:
                pred = _predecessor(target)
                self.remove(pred.data)
                target.data = pred.data
            # reset the new root's prev to None
            if self.root:
                self.root.prev = None
        # Case 3: the target is not the root
        else:
            # Case 3a: no children
            if not target.left and not target.right:
                parent = target.prev
                if target.data < parent.data:
                    parent.left = None
                elif target.data > parent.data:
                    parent.right = None
            # Case 3b: one child
            elif not target.right:
                parent = target.prev
                if parent.right == target:
                    parent.right = target.left
                elif parent.left == target:
                    parent.left = target.left
                target.left.prev = parent
            elif not target.left:
                parent = target.prev
                if parent.right == target:
                    parent.right = target.right
                elif parent.left == target:
                    parent.left = target.right
                target.right.prev = parent
            # Case 3c: two children
            else:
                pred = _predecessor(target)
                self.remove(pred.data)
                target.data = pred.data
    
    def __str__(self):
        """String representation: a hierarchical view of the BST.
        Do not modify this function, but use it often to test this class.
        (this function uses a depth-first search; can you explain how?)
        
        Example:  (3)
                  / \     '[3]          The nodes of the BST are printed out
                (2) (5)    [2, 5]       by depth levels. The edges and empty
                /   / \    [1, 4, 6]'   nodes are not printed.
              (1) (4) (6)
        """
        
        if self.root is None:                   # Print an empty tree
            return "[]"
        # If the tree is nonempty, create a list of lists.
        # Each inner list represents a depth level in the tree.
        str_tree = [list() for i in xrange(_height(self.root) + 1)]
        visited = set()                         # Track visited nodes
        
        def _visit(current, depth):
            """Add the data contained in 'current' to its proper depth level
            list and mark as visited. Continue recusively until all nodes have
            been visited.
            """
            str_tree[depth].append(current.data)
            visited.add(current)
            if current.left and current.left not in visited:
                _visit(current.left, depth+1)  # travel left recursively (DFS)
            if current.right and current.right not in visited:
                _visit(current.right, depth+1) # travel right recursively (DFS)
        
        _visit(self.root, 0)                    # Load the list of lists.
        out = ""                                # Build the final string.
        for level in str_tree:
            if level != list():                 # Ignore empty levels.
                out += str(level) + "\n"
            else:
                break
        return out

def _height(current):
    """Calculate the height of a given node by descending recursively until
    there are no further child nodes. Return the number of children in the
    longest chain down. Helper function for BST.__str__. Do not modify.
    """
    if current is None:     # Base case: the end of a branch.
        return -1           # Otherwise, descend down both branches.
    return 1 + max(_height(current.right), _height(current.left))

# ============================== solutions.py =============================== #

# from Trees import BST
import numpy as np
from sklearn import neighbors
from scipy.spatial import KDTree


# Problem 1: Implement this function.
def euclidean_metric(x, y):
    """Return the euclidean distance between the vectors 'x' and 'y'.
    Raise a ValueError if the two vectors are of different lengths.
    
    What type should 'x' and 'y' be?
    
    Example:
    
    >>> print(euclidean_metric([1,2],[2,2]))
    1.0
    >>> print(euclidean_metric([1,2,1],[2,2]))
    ValueError: Incompatible sizes
    """
    if len(x) != len(y):
        raise ValueError("Incompatible sizes")
    return np.linalg.norm(x - y)
    # Or a slightly longer way:
    return np.sqrt(np.sum(np.subtract(x, y)**2))
    # Or the longest/worst way:
    total = 0
    for i in xrange(len(x)):
        term = x[i] - y[i]
        term = term**2
        total += term
    total = np.sqrt(total)
    return total


# Problem 2: Implement this function.
def exhaustive_search(data_set, target):
    """Solve the nearest neighbor search problem exhaustively.
    Check the distances between 'target' and each point in 'data_set'.
    Use the Euclidean metric to calculate distances.
    
    Inputs:
        data_set (mxk ndarray): An array of m k-dimensional points.
        target (1xk ndarray): A k-dimensional point to compare to 'dataset'.
        
    Returns:
        the member of 'data_set' that is nearest to 'target' (1xk ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """

    # Validate the inputs (not required but always a good idea)
    if not isinstance(data_set, np.ndarray):
        raise TypeError("Both arguments must by numpy arrays.")
    if not isinstance(target, np.ndarray):
        raise TypeError("Both arguments must by numpy arrays.")
    if data_set.shape[1] != target.shape[1] or target.shape[0] != 1:
        raise ValueError("Mismatched dimensions: data_set must be mxk "
                                            + "and target must be 1xk")

    # Initialize the outputs
    minimum_distance = float("inf")
    nearest_neighbor = None

    # Search through the data set for the nearest neighbor
    for point in data_set:
        distance = euclidean_metric(target, point)
        if distance < minimum_distance:
            nearest_neighbor = point
            minimum_distance = distance
    return nearest_neighbor, minimum_distance


# Problem 3: Add magic methods to this class.
class KDTNode(BSTNode):
    """Node class for K-D Trees. Has a left child, a right child, a parent,
    a dimension, and contains data. The data must be of type 'tuple' or 'list'.
    Has a dimension."""
    def __init__(self, data):
        """Construct a K-D Tree node containing 'data'. The left, right,
        and prev attributes are set in the constructor of BSTNode.

        If 'data' is not a numpy array (of type np.ndarray) or a list,
        raise a TypeError.
        """
        if type(data) not in [list, np.ndarray]:
            raise ValueError("A numpy array or a list is required.")
        BSTNode.__init__(self,data)
        self.axis  = 0          # K-D dimension
    
    def __lt__(self, other):
        return self.data[other.axis] < other.data[other.axis]

    def __gt__(self, other):
        return self.data[other.axis] > other.data[other.axis]
    
    def __sub__(self, other):
        return euclidean_metric(self.data, other.data)

    def __eq__(self, other):
        return np.allclose(self.data, other.data)


# Problem 4: Finish implementing this class by overriding
#            the __init__(), insert(), and remove() methods.
class KDT(BST):
    """A k-dimensional binary search tree object.
    Used to solve the nearest neighbor problem efficiently.

    Attributes:
        root (KDTNode): the root node of the tree. Like all other
            nodes in the tree, the root houses data as a numpy array.
    """

    def __init__(self, data_set):
        """Set the k attribute and fill the tree with the points
        in 'data_set'.
        """
        BST.__init__(self)
        if not isinstance(data_set, np.ndarray):
            raise TypeError("data_set must be a numpy array.")
        self.k = data_set.shape[1]
        for point in data_set:
            self.insert(point)
    
    def find(self, data):
        """Return the node containing 'data'. Raise a ValueError if
        there is no such node in the tree or if the tree is empty.
        """
        
        def _step(current, target):
            """Recursively approach the target node."""
            
            if current is None:             # Base case: target not found.
                return current
            if current == other:            # Base case: target found!
                return current
            if target < current:            # Recursively search to the left
                return _step(current.left, target)
            else:                           # Recursively search to the right
                return _step(current.right, target)
        
        if self.root is None:               # Check for empty tree
            raise ValueError(str(data) + " is not in the tree.")
            
        # Create a new node to use the KDTNode comparison operators
        n = KDTNode(data)
        found = _step(self.root, n)
        if found is None:                   # Report the data was not found
            raise ValueError(str(data) + " is not in the tree.")
        return found                        # Return the node containing 'data'
    
    def insert(self, data):
        """Insert a new node at the appropriate location. Return the new
        node. This method will need to be totally rewritten.
        """
        
        def _find_parent(current, node):
            """Recursively descend through the tree to find the node that
            should be the parent of the new node. Do not allow for duplicates.
            """
            
            if node == current:
                raise ValueError(str(node.data) + " is already in the tree.")
            if node < current:                  # Travel left
                if current.left:
                    return _find_parent(current.left,node)
                else:
                    return current
            else:                               # Travel right
                if current.right:
                    return _find_parent(current.right,node)
                else:
                    return current
        
        n = KDTNode(data)                        # Make a new node
        if len(data) != self.k:
            raise ValueError("data must be of length " + str(self.k))
        if not self.root:
            self.root = n                       # Case 1: empty tree
            n.axis = 0
        else:                                   # Case 2: use _find_parent
            parent = _find_parent(self.root, n)         # Get the parent
            if n < parent: parent.left = n      # Insert the node
            else: parent.right = n
            n.prev = parent                             # Double link
            n.axis = (n.prev.axis + 1) % self.k
        return n
    
    def remove(self, *args):
        raise AttributeError(
            "'remove()' has been disabled for this class.")


# Problem 5: Implement this function
def nearest_neighbor(tree, point):
    """Use your KDTree class to solve the nearest neighbor problem."""
    
    k = tree.k
    p = KDTNode(point)
    
    # Helper function to KDstart. searches the kd-tree using recursion,
    # Algortihm can problaly simplified.
    def KDsearch(current, target, neighbor, distance):
        """
        Inputs:
            current (KDTNode)
            target (KDTNode)
            distance (float): the current minimum distance.
            neighbor (KDTNode): the current nearest neighbor.
        """
        
        # Base case. Return the distance and the nearest neighbor.
        if current is None:
            return neighbor, distance
        index = current.axis
        d = target - current
        if d < distance:
            distance = d
            neighbor = current
        if target < current:        # Recursively search 'left'
            neighbor, distance = KDsearch(
                current.left, target, neighbor, distance)
                                    # Back up if needed
            if target.data[index] + distance >= current.data[index]: # (?)
                neighbor, distance = KDsearch(
                    current.right, target, neighbor, distance)
        else:                       # Recursively search 'right'
            neighbor, distance = KDsearch(
                current.right, target, neighbor, distance)
                                    # Back up if needed
            if target.data[index] - distance <= current.data[index]: # (?)
                neighbor, distance = KDsearch(
                    current.left, target, neighbor, distance)
    
        return neighbor, distance
    
    # Search the KD-tree.
    return KDsearch(tree.root, p, tree.root, tree.root - p)

def handwriting_recognition():
    labels, points, testlabels, testpoints = np.load('PostalData.npz').items()
    nbrs = neighbors.KNeighborsClassifier(n_neighbors=8, weights='distance',
                                                                        p=2)
    nbrs.fit(points[1], labels[1])
    prediction = nbrs.predict(testpoints[1])
    return np.average(prediction/testlabels[1])

from matplotlib import pyplot as plt

def makeplots():
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,10), ylim=(0,10))

    point_list = [(5,5), (8,4), (3,2), (7,7), (2,6), (9,2), (4,7)]
    x = [5, 8, 3, 7, 2, 9, 4]
    y = [5, 4, 2, 7, 6, 2, 7]
    ax.axvline(5, 0, 1)
    ax.axhline(4, .5, 1, color='r')
    ax.axhline(2, 0, .5, color='r')
    ax.axvline(7, .4, 1)
    ax.axvline(2, .2, 1)
    ax.axvline(9, 0, .4)
    ax.axhline(7, .2, .5, color="r")
    #plt.annotate("root", xy=(5,5), xytext=(5.2,5))
    #plt.annotate("root.right", xy=(8,4), xytext=(7.65,4.35))
    #plt.annotate("root.right.left", xy=(9,2), xytext=(7,2))
    #plt.annotate("root.left", xy=(3,2), xytext=(2.65,1.6))
    #plt.annotate("root.left.right", xy=(1,6), xytext=(.2,6.1))
    #plt.annotate("root.left.right.right\n     (new node)", xy=(4,7),
    #                                        xytext=(2.35,7.3))

    ax.plot(x, y, 'ok')
    ax.plot([8], [4.45], '*k')
    mid = plt.Circle(xy=(8,4), radius=.5, color="green", alpha=.3)
    upp = plt.Circle(xy=(7,7), radius=.5, color="purple", alpha=.3)
    ax.add_artist(mid)
    ax.add_artist(upp)
    plt.annotate("target", xy=(8,4.5), xytext=(8.2,4.5))
    plt.show()

if __name__ == '__main__':
    makeplots()


