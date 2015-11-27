# solutions.py
"""NumPy and SciPy Arrays solutions file."""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Problem 1: Perform matrix multiplication
A = np.array([[2,4,0],[-3,1,-1],[0,3,2]])
B = np.array([[3,-1,2],[-2,-3,0],[1,0,-2]])
product = A.dot(B)


# Problem 2: Return an array with all nonnegative numbers.
def nonnegative(my_array):
    """Changes all negative entries in the inputed array to 0.

    Example:
    >>> my_array = np.array([-3,-1,3])
    >>> nonnegative(my_array)
    array([0,0,3])
    """
    
    my_array[my_array<0] = 0
    return my_array


# Problem 3: nxn array of floats and operations on that array.
def normal_var(n):
    """Creates nxn array with values from the normal distribution, computes 
    the mean of each row and computes the variance of these means.
    """
    my_array = np.random.randn(n*n).reshape((n,n))
    return np.var(np.mean(my_array,axis=1))


# Problem 4: Solving Laplace's Equation using the Jacobi method and array slicing.
def laplace(A, tolerance):
    """Solve Laplace's Equation using the Jacobi method and array slicing."""
    B = np.copy(A)
    difference = tolerance
    while difference >= tolerance:
        B[1:-1,1:-1] = (A[:-2,1:-1] + A[2:,1:-1] + A[1:-1,:-2] + A[1:-1,2:])/4.
        difference = np.max(np.abs(A-B))
        A[1:-1,1:-1] = B[1:-1,1:-1]
    return A   

def laplace_plot():    
    """Visualize your solution to Laplace equation"""
    n = 100
    tol = .0001
    U = np.ones ((n, n))
    U[:,0] = 100                # Set north boundary condition.
    U[:,-1] = 100               # Set south boundary condition.
    U[0] = 0                    # Set west boundary condition.
    U[-1] = 0                   # Set east boundary condition.
    # U has been changed in place (note that laplace is the name of
    # the function in this case).
    laplace(U, tol)
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface (X, Y, U, rstride=5)
    plt.show()

# Problem 5: Blue shift an RGB image.
def blue_shift():
    """Create a 100x100x3 array and perform a blue shift"""
    my_array = np.random.random_integers(0,255,100*100*3).reshape((100,100,3))
    blue = np.copy(my_array)    # or my_array.copy()
    blue[:,:,:2] = 0.5*my_array[:,:,:2]   
    return my_array, blue 

def blue_shift_plot():
    """Visualize the original and the blue_shift image"""
    original, blue = blue_shift()
    original = 255 - original
    blue = 255 - blue
    plt.subplot(1,2,1)
    plt.imshow(original)
    plt.subplot(1,2,2)
    plt.imshow(blue)
    plt.show()
    
# END OF SOLUTIONS ============================================================

from numpy.random import randint

# Test script
def test(student_module):
    """Test script. Import the student's solutions file as a module.
    
     5 points for problem 1
     5 points for problem 2
    10 points for problem 3
    10 points for problem 4
    10 points for problem 5
    
    Inputs:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 40.
        feedback (str): a printout of test results for the student.
    """
    tester = _testDriver()
    tester.test_all(student_module)
    return tester.score, tester.feedback

class _testDriver(object):
    """Class for testing a student's work. See test.__doc__ for more info."""

    # Constructor -------------------------------------------------------------
    def __init__(self):
        """Initialize the feedback attribute."""
        self.feedback = ""

    # Main routine -----------------------------------------------------------
    def test_all(self, student_module, total=40):
        """Grade the provided module on each problem and compile feedback."""
        # Reset feedback and score.
        self.feedback = ""
        self.score = 0

        def test_one(problem, number, value):
            """Test a single problem, checking for errors."""
            try:
                self.feedback += "\n\nProblem %d (%d points):"%(number, value)
                points = problem(student_module)
                self.score += points
                self.feedback += "\nScore += %d"%points
            except BaseException as e:
                self.feedback += "\nError: %s"%e

        # Grade each problem.
        test_one(self.problem1, 1, 5)   # Problem 1:  5 points.
        test_one(self.problem2, 2, 5)   # Problem 2:  5 points.
        test_one(self.problem3, 3, 10)  # Problem 3: 10 points.
        test_one(self.problem4, 4, 10)  # Problem 4: 10 points.
        test_one(self.problem5, 5, 10)  # Problem 5: 10 points.


        # Report final score.
        percentage = (100. * self.score) / total
        self.feedback += "\n\nTotal score: %d/%d = %s%%"%(
                                    self.score, total, percentage)
        if   percentage >=  98: self.feedback += "\n\nExcellent!"
        elif percentage >=  90: self.feedback += "\n\nGreat job!"

        # Add comments (optionally).
        print(self.feedback)
        comments = str(raw_input("Comments: "))
        if len(comments) > 0:
            self.feedback += '\n\n\nComments:\n\t%s'%comments

    # Helper Functions --------------------------------------------------------
    def arrTest(self, correct, student, message):
        """Test to see if the arrays 'correct' and 'student' are equal.
        Report the given 'message' if they are not.
        """
        if np.allclose(correct, student):
            return 1
        else:
            self.feedback += message
            self.feedback += "\nCorrect response:\narray(%s)"%correct
            self.feedback += "\nStudent response:\narray(%s)"%student
            return 0

    def eqTest(self, correct, student, message, tol):
        """Test to see if 'correct' and 'student' are within a tolerance of
        each other. Report the given 'message' if they are not.
        """
        if abs(correct - student) < tol:
            return 1
        else:
            self.feedback += message
            self.feedback += "\nCorrect response: %s"%correct
            self.feedback += "\nStudent response: %s"%student
            return 0

    def grade(self, points, message=None):
        """Manually grade a problem worth 'points'. Return the score."""
        credit = -1
        while credit > points or credit < 0:
            try:
                credit = int(input("\nScore out of %d: "%points))
            except:
                credit = -1
        if credit != points:
            # Add comments (optionally),
            comments = raw_input("Comments: ")
            if len(comments) > 0:
                self.feedback += "\n\t%s"%comments
            # Or add a predetermined error message.
            elif message is not None:
                self.feedback += message
        return credit

    # Problems ----------------------------------------------------------------
    def problem1(self, s):
        """Test Problem 1. 5 points."""
        return 5*self.arrTest(product, s.product, "\n\tIncorrect product.")

    def problem2(self, s):
        """Test nonnegative(). 5 points."""

        first = np.array([-3,-1,3])
        points = 2*self.arrTest(nonnegative(first.copy()),
                                s.nonnegative(first.copy()),
                                "\n\tnonnegative(array(%s)) failed"%first)
        
        second = randint(-50,50,10)
        points += 3*self.arrTest(nonnegative(second.copy()),
                                s.nonnegative(second.copy()), 
                                "\n\tnonnegative(array(%s)) failed"%second)
        return points

    def problem3(self, s):
        """Test normal_var(). 10 points."""
        points  = 4*self.eqTest(normal_var(100), s.normal_var(100),
                             "\n\tnormal_var(100) failed", tol=.01)
        points += 6*self.eqTest(normal_var(1000), s.normal_var(1000),
                             "\n\tnormal_var(1000) failed", tol=.0005)
        return points

    def problem4(self, s):
        """Test laplace_plot(). 10 points."""
        print("Generating laplace plot...")
        s.laplace_plot()
        return self.grade(10, "Incorrect plot.")

    def problem5(self, s):
        """Test blue_shift_plot(). 10 points."""
        print("Generating blue shift plot...")
        s.blue_shift_plot()
        return self.grade(10, "Incorrect plot.")

# END OF FILE =================================================================
