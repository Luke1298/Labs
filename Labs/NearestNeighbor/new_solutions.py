# new_neighbor.py
"""Volume II Lab 7: Nearest Neighbor Search
Solutions file. Written by Shane A. McQuarrie, Fall 2015
"""

# =================== BSTNode / BST Classes from Trees.py =================== #
class BSTNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def __str__(self):
        if self.root is None:
            return "[]"
        str_tree = [list() for i in xrange(_height(self.root) + 1)]
        visited = set()
        
        def _visit(current, depth):
            str_tree[depth].append(current.data)
            visited.add(current)
            if current.left and current.left not in visited:
                _visit(current.left, depth+1)
            if current.right and current.right not in visited:
                _visit(current.right, depth+1)
        
        _visit(self.root, 0)
        out = ""
        for level in str_tree:
            if level != list():
                out += str(level) + "\n"
            else:
                break
        return out

def _height(current):
    if current is None:
        return -1
    return 1 + max(_height(current.right), _height(current.left))

# ============================== solutions.py =============================== #

# from Trees import BST
import numpy as np
from sklearn import neighbors
from scipy.spatial import KDTree


# Problem 1: Implement this function.
def euclidean_metric(x, y):
    """Return the euclidean distance between the vectors 'x' and 'y'.

    Raises:
        ValueError: the two vectors 'x' and 'y' are of different lengths.
    
    Example:
        >>> print(euclidean_metric([1,2],[2,2]))
        1.0
        >>> print(euclidean_metric([1,2,1],[2,2]))
        ValueError: Incompatible dimensions.
    """
    if len(x) != len(y):
        raise ValueError("Incompatible dimensions.")
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
            TypeError: 'data' is not a a numpy array (of type np.ndarray).
        """
        if type(data) != np.ndarray:
            raise TypeError("A numpy array or a list is required.")
        BSTNode.__init__(self, data)
        self.axis  = 0
    
    def __sub__(self, other):
        return euclidean_metric(self.data, other.data)

    def __eq__(self, other):
        return np.allclose(self.data, other.data)

    def __lt__(self, other):
        return self.data[other.axis] < other.data[other.axis]

    def __gt__(self, other):
        return self.data[other.axis] > other.data[other.axis]


# Problem 4: Finish implementing this class by overriding
#            the __init__(), insert(), and remove() methods.
class KDT(BST):
    """A k-dimensional binary search tree object.
    Used to solve the nearest neighbor problem efficiently.

    Attributes:
        root (KDTNode): the root node of the tree. Like all other
            nodes in the tree, the root houses data as a numpy array.
        k (int): the dimension of the tree (the 'k' of the k-d tree).
    """

    def __init__(self, data_set):
        """Set the k attribute and fill the tree with the points
        in 'data_set'. Raise a TypeError if the input is not a numpy
        array.
        """
        BST.__init__(self)
        if not isinstance(data_set, np.ndarray):
            raise TypeError("data_set must be a numpy array.")
        self.k = data_set.shape[1]
        for point in data_set:
            self.insert(point)
    
    def find(self, data):
        """Return the node containing 'data'.

        Raises:
            ValueError: there is node containing 'data' in the tree,
                or the tree is empty.
        """
        
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
        
        if self.root is None:               # Check for empty tree.
            raise ValueError(str(data) + " is not in the tree.")
            
        # Create a new node to use the KDTNode comparison operators.
        n = KDTNode(data)
        found = _step(self.root, n)
        if found is None:                   # Report the data was not found.
            raise ValueError(str(data) + " is not in the tree.")
        return found                        # Return the target node.
    
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
def nearest_neighbor(tree, target):
    """Use your KDTree class to solve the nearest neighbor problem.

    Inputs:
        tree (KDT): A KDT object loaded with a data set of m
            k-dimensional points (as numpy arrays).
        target (1xk ndarray): A k-dimensional point to compare to the
            data housed in 'tree'.

    Returns:
        The point in the tree that is nearest to 'target' (1xk ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """
    
    k = tree.k
    p = KDTNode(point)
    
    def KDsearch(current, target, neighbor, distance):
        """The actual nearest neighbor search algorithm.
        Inputs:
            current (KDTNode): the node to examine.
            target (KDTNode): the target (stored in a KDTNode).
            neighbor (KDTNode): the current nearest neighbor.
            distance (float): the current minimum distance.
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
    result = KDsearch(tree.root, p, tree.root, tree.root - p)
    return result[0].data, result[1]

def postal_problem():
    """Use the neighbors module in sklearn to classify the Postal data set
    provided in 'PostalData.npz'. Classify the testpoints with 'n_neighbors'
    as 1, 4, or 10, and with 'weights' as 'uniform' or 'distance'. For each
    trial print a report indicating how the classifier performs in terms of
    percentage of misclassifications. Which combination gives the most
    correct classifications?

    Your function should print a report similar to the following:
    n_neighbors = 1, weights = 'distance':  0.903
    n_neighbors = 1, weights =  'uniform':  0.903       (...and so on.)
    """

    labels, points, testlabels, testpoints = np.load('PostalData.npz').items()

    def trial(n, w):
        nbrs = neighbors.KNeighborsClassifier(n_neighbors=n, weights=w, p=2)
        nbrs.fit(points[1], labels[1])
        prediction = nbrs.predict(testpoints[1])
        return np.average(prediction/testlabels[1])

    print "n_neighbors =  1, weights = 'distance':\t", trial(1, 'distance')
    print "n_neighbors =  1, weights = 'uniform' :\t", trial(1, 'uniform')
    print "n_neighbors =  4, weights = 'distance':\t", trial(4, 'distance')
    print "n_neighbors =  4, weights = 'uniform' :\t", trial(4, 'uniform')
    print "n_neighbors = 10, weights = 'distance':\t", trial(10, 'distance')
    print "n_neighbors = 10, weights = 'uniform' :\t", trial(10, 'uniform')

# ============================= END OF SOLUTIONS ============================ #

'''
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
'''

import inspect

def test(student_module):
    """Test script. You must import the students file as a module.
    
     5 points for problem 1
     5 points for problem 2
    10 points for problem 3
    15 points for problem 4
    15 points for problem 5
    10 points for problem 6
    
    Parameters:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 60.
        feedback (str): a printout of results for the student.
    """
    
    # Helper functions
    def numTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if np.allclose(x, y, atol=1e-04): return 1, ""
        else:
            m += "\n\t\tCorrect response: " + str(x)
            m += "\n\t\tStudent response: " + str(y)
            return 0, m
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            try:
                part = int(input("\nScore out of " + str(p) + ": "))
            except:
                part = -1
        if part == p: return p,""
        else: return part,m

    def getCode(func):
        rawcode = inspect.getsource(func).splitlines()[len(func.__doc__.splitlines())+1:]
        for line in rawcode: print line

    s = student_module
    score = 0
    total = 60
    feedback = ""
    
    try:    # Problem 1: 5 points
        feedback += "\n\nProblem 1 (5 points):"
        points = 0
        x = np.array([1, 2])
        y = np.array([2, 2])
        p,f = numTest(euclidean_metric(x,y), s.euclidean_metric(x,y),
                "\n\teuclidean_metric() failed.")
        points += p; feedback += f
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = np.array([2, 6, 4, 8, 0, 2, 4, 7, 5, 11])
        p,f = numTest(euclidean_metric(x,y), s.euclidean_metric(x,y),
                "\n\teuclidean_metric() failed.")
        points += p; feedback += f
        x = (np.random.random(100)-.5)*200
        y = (np.random.random(100)-.5)*200
        p,f = numTest(euclidean_metric(x,y), s.euclidean_metric(x,y),
                "\n\teuclidean_metric() failed.")
        points += p; feedback += f
        x = np.array([1, 2])
        y = np.array([1, 2, 3])
        try:
            s.euclidean_metric(x, y)
            feedback += "\n\teuclidean_metric() failed to raise a ValueError"
            feedback += "for vectors of different lengths"
        except:
            points += 2
        
        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 5 points
        feedback += "\n\nProblem 2 (5 points):"
        points = 0

        def neighbor(m, k):
            """Do a single nearest neighbor search trial."""
            data = np.random.random((m, k))
            target = np.random.random(k)
            tree = KDTree(data)
            dist, index = tree.query(target)
            point = tree.data[index]
            spoint, sdist = s.exhaustive_search(data, target)
            p1, f1 = numTest(point, spoint, "\n\tIncorrect nearest neighbor")
            p2, f2 = numTest(dist, sdist, "\n\tIncorrect minimum distance")
            return p1 + p2, f1 + f2
        
        p,f = neighbor(100, 10)
        points += p; feedback += f
        p,f = neighbor(10, 100)
        points += p; feedback += f

        getCode(s.exhaustive_search)
        print "\n(Check for cheating)"
        p,f = grade(1, "\n\tNo cheating! You must use the naive method here.")
        points += 1; feedback += f
        points *= p

        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0

        # Test KDTNode.__init__ (can only hold np.ndarrays)
        try:
            s.KDTNode([10, "apple", 1.0])
            feedback += "\n\t__init__ failed to report TypeError"
        except:
            points += 2

        # Test KDTNode.__sub__ (euclidean distance)
        x = np.random.random(10); y = np.random.random(10)
        A =   KDTNode(x); B =   KDTNode(y)
        C = s.KDTNode(x); D = s.KDTNode(y)
        p,f = numTest(A-B, C-D, "\n\tKDTNode.__sub__ failed")
        points += (p * 2); feedback += f

        # Test KDTNode.__eq__
        D = s.KDTNode(1.5*x)
        if C != D: points += 1
        else: feedback += "\n\tKDTNode.__eq__ failed on nonequal"
        D = s.KDTNode(x)
        if C == D: points += 1
        else: feedback += "\n\tKDTNode.__eq__ failed on equal"

        # Test KDTNode.__lt__ and KDTNode.__gt__
        x = s.KDTNode(np.array([3,1,0,5], dtype=np.int)); x.axis = 0
        y = s.KDTNode(np.array([1,2,4,3], dtype=np.int)); y.axis = 1
        if x < y: points += 1
        else: feedback += "\n\tKDTNode.__lt__ failed"
        if y < x: points += 1
        else: feedback += "\n\tKDTNode.__lt__ failed"
        x.axis = 2; y.axis = 3
        if x > y: points += 1
        else: feedback += "\n\tKDTNode.__gt__ failed"
        if y > x: points += 1
        else: feedback += "\n\tKDTNode.__gt__ failed"

        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 15 points
        feedback += "\n\nProblem 4 (15 points):"
        points = 0
        # Test KDT.insert
        key = KDT()

        # Test KDT.remove
        try:
            K
        # Test problem 4 here
        
        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message

    try:    # Problem 5: 15 points
        feedback += "\n\nProblem 5 (15 points):"
        points = 0
        # Test problem 5 here
        
        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message

    try:    # Problem 6: 10 points
        feedback += "\n\nProblem 6 (10 points):"
        points = 0
        # Test problem 6 here
        
        score += points; feedback += "\nScore += " + str(points)
    except BaseException as e: feedback += "\nError: " + e.message
    
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"

    # Add comments (optionally).
    print feedback
    comments = str(raw_input("Comments: "))
    if len(comments) > 0: feedback += '\n\n\nComments:\n\t' + comments

    return score, feedback

# =============================== END OF FILE =============================== #
