# name this file solutions.py
"""Volume II Lab 6: Nearest Neighbor Search
<Name>
<Class>
<Date>
"""

from Trees import BST


# Problem 1: Implement this function.
def euclidean_metric(x, y):
    """Return the euclidean distance between the vectors 'x' and 'y'.

    Raises:
        ValueError: if the two vectors 'x' and 'y' are of different lengths.
    
    Example:
        >>> print(euclidean_metric([1,2],[2,2]))
        1.0
        >>> print(euclidean_metric([1,2,1],[2,2]))
        ValueError: Incompatible dimensions.
    """
    raise NotImplementedError("Problem 1 Incomplete")

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
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3: Finish implementing this class by modifying __init__()
#   and adding the __sub__, __eq__, __lt__, and __gt__ magic methods.
class KDTNode(BSTNode):
    """Node class for K-D Trees. Inherits from BSTNode.

    Attributes:
        left (KDTNode): a reference to this node's left child.
        right (KDTNode): a reference to this node's right child.
        parent (KDTNode): a reference to this node's parent node.
        data (ndarray): a coordinate in k-dimensional space.
        axis (int): the 'dimension' of the node to make comparisons on.
    """

    def __init__(self, data):
        """Construct a K-D Tree node containing 'data'. The left, right,
        and prev attributes are set in the constructor of BSTNode.

        Raises:
            TypeError: if 'data' is not a a numpy array (of type np.ndarray).
        """
        BSTNode.__init__(self, data)
        self.axis  = 0


# Problem 4: Finish implementing this class by overriding
#   the insert() and remove() methods.
class KDT(BST):
    """A k-dimensional binary search tree object.
    Used to solve the nearest neighbor problem efficiently.

    Attributes:
        root (KDTNode): the root node of the tree. Like all other
            nodes in the tree, the root houses data as a numpy array.
        k (int): the dimension of the tree (the 'k' of the k-d tree).
    """
    
    def find(self, data):
        """Return the node containing 'data'.

        Raises:
            ValueError: if there is node containing 'data' in the tree,
                or the tree is empty.
        """

        # First check that the tree is not empty.
        if self.root is None:
            raise ValueError(str(data) + " is not in the tree.")
        
        # Define a recursive function to traverse the tree.
        def _step(current, target):
            """Recursively approach the target node."""
            
            if current is None:             # Base case: target not found.
                return current
            if current == other:            # Base case: target found!
                return current
            if target < current:            # Recursively search to the left.
                return _step(current.left, target)
            else:                           # Recursively search to the right.
                return _step(current.right, target)
            
        # Create a new node to use the KDTNode comparison operators.
        n = KDTNode(data)

        # Call the recursive function, starting at the root.
        found = _step(self.root, n)
        if found is None:                  # Report the data was not found.
            raise ValueError(str(data) + " is not in the tree.")
        return found                       # Otherwise, return the target node.


# Problem 5: Implement this function.
def nearest_neighbor(data_set, target):
    """Use the KDT class to solve the nearest neighbor problem.

    Inputs:
        data_set (mxk ndarray): An array of m k-dimensional points.
        target (1xk ndarray): A k-dimensional point to compare to 'dataset'.

    Returns:
        The point in the tree that is nearest to 'target' (1xk ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6: Implement this function.
def postal_problem():
    """Use the neighbors module in sklearn to classify the Postal data set
    provided in 'PostalData.npz'. Classify the testpoints with 'n_neighbors'
    as 1, 4, or 10, and with 'weights' as 'uniform' or 'distance'. For each
    trial print a report indicating how the classifier performs in terms of
    percentage of misclassifications.

    Your function should print a report similar to the following:
    n_neighbors = 1, weights = 'distance':  0.903
    n_neighbors = 1, weights =  'uniform':  0.903       (...and so on.)
    """
    raise NotImplementedError("Problem 6 Incomplete")

# =============================== END OF FILE =============================== #
