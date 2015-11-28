# solutions.py
"""The Standard Library solutions file."""

# In several labs, students will submit multiple files.
# Every solutions file contains all of the code that students will write,
# separated by file.

# calculator.py ============================================================= #
# Students write this module as part of problem 3. Do not provide to students.

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def sqrt(x):
    return x**.5
    # or, from math import sqrt at the top.

# matrix_multiply.py ======================================================== #
# This module is provided to students and used to complete problem 4.

import numpy as np

def load_matrices(filename):
    """Returns two matrices if the correct filename is given."""
    
    files = np.load(filename)
    return files['arr_0'], files['arr_1']


def method1(A,B):
    """Multiply the matrices 'A' and 'B' together using nested for loops."""
    
    product_matrix = np.zeros((A.shape[0], B.shape[1]))
    for i in range(product_matrix.shape[0]):
        for j in range(product_matrix.shape[1]):
            for k in range(product_matrix.shape[0]):
                product_matrix[i,j] += A[i,k]*B[k,j] 
    
    return product_matrix


def method2(A,B):
    """Multiply the matrices 'A' and 'B' together with some vectorization.
    Use xrange() instead of range() to make things a little faster.
    """
    
    product_matrix = np.zeros((A.shape[0], B.shape[1]))
    for i in xrange(product_matrix.shape[0]):
        for j in xrange(product_matrix.shape[1]):
            product_matrix[i,j] = np.dot(A[i,:], B[:,j])
    
    return product_matrix


def method3(A,B):
    """Use numpy's matrix multiplication method for maximum speed."""
    
    return np.dot(A,B)


# solutions.py ============================================================== #
# The students are provided a specifications file called 'spec.py' with the
# following functions. They are to rename the file as the instructor specifies.

import sys
import time

# Problem 1: Implement this function.
def prob1(l):
    """Accept a list 'l' of numbers as input and return a list with the
    minimum, maximum, and average of the original list (in that order).
    """
    return [min(l), max(l), float(sum(l))/len(l)]


# Problem 2: Implement this function.
def prob2():
    """Programmatically determine which Python objects are mutable and which
    are immutable. Test numbers, strings, lists, tuples, and dictionaries.
    Print your results to the terminal.
    """

    # numbers: num+= 1
    num1 = 0
    num2 = num1
    num1 += 1
    print("Numbers:\t"),
    if num1 == num2:
        print("Mutable")
    else:
        print("Immutable")

    # strings: str1 += 'a'
    str1 = "a"
    str2 = str1
    str1 += "a"
    print("Strings:\t"),
    if str1 == str2:
        print("Mutable")
    else:
        print("Immutable")

    # lists: list1.append(1)
    list1 = [4,3,2]
    list2 = list1
    list1.append(1)
    print("Lists:\t\t"),
    if list1 == list2:
        print("Mutable")
    else:
        print("Immutable")

    # tuples: tup1 += (1,)
    tup1 = (4,3,2)
    tup2 = tup1
    tup1 += (1,)
    print("Tuples:\t\t"),
    if tup1 == tup2:
        print("Mutable")
    else:
        print("Immutable")

    # dictionaries: dic1[1] = 'a'
    dic1 = dict()
    dic1[1] = 'b'
    dic2 = dic1
    dic1[1] = 'a'
    print("Dictionaries:\t"),
    if dic1 == dic2:
        print("Mutable")
    else:
        print("Immutable")


# Problem 3: Write a 'calculator' module and use it to implement this function.
def prob3(a,b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any methods other than those that are imported from the
    'calculator' module.
    Parameters:
        a : the length one of the sides of the triangle.
        b : the length the other nonhypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    # Students should use calculator.method() instead of method()
    a2 = mult(a,a)
    b2 = mult(b,b)
    a2plusb2 = add(a2, b2)
    return sqrt(a2plusb2)
    # Or, simply
    c = calculator              # or "import calculator as c" at the top
    return c.sqrt(c.add(c.mult(a,a),c.mult(b,b)))


# Problem 4: Utilize the 'matrix_multiply' module and 'matrices.npz' file to
#   implement this function.
def prob4():
    """If no command line argument is given, print "No Input."
    If anything other than "matrices.npz is given, print "Incorrect Input."
    If "matrices.npz" is given as a command line argument, use functions
    from the provided 'matrix_multiply' module to load two matrices, then
    time how long each method takes to multiply the two matrices together.
    Print your results to the terminal.
    """
    # Students should use matrix_multiply.method() instead of method()
    # m = matrix_multiply     # or "import matrix_multiply as m" at the top
    if len(sys.argv) == 1:
        print("No Input.")
    elif sys.argv[1] != "matrices.npz":
        print("Incorrect Input.")
    else:   # If the correct filename is given,
        # load the matrices
        A,B = load_matrices(sys.argv[1])
        
        # time method1()
        start = time.time()
        method1(A,B)
        print(time.time() - start)
        
        # time method2()
        start = time.time()
        method2(A,B)
        print(time.time() - start)
        
        # time method3()
        start = time.time()
        method3(A,B)
        print(time.time() - start)

if __name__ == "__main__":
    prob4()

# ============================ END OF SOLUTIONS ============================= #

import os
from numpy.random import randint

# Test script
def test(student_module):
    """Test script. Import the student's solutions file as a module.
    
    3 points for problem 1
    5 points for problem 2
    5 points for problem 2
    7 points for problem 2
    
    Inputs:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 'total'.
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
    def test_all(self, student_module, total=20):
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
                self.feedback += "\n%s: %s"%(self._errType(e),e)

        # Grade each problem.
        test_one(self.problem1, 1, 3)   # Problem 1: 3 points.
        test_one(self.problem2, 2, 5)   # Problem 2: 5 points.
        test_one(self.problem3, 3, 5)   # Problem 2: 5 points.
        test_one(self.problem4, 4, 7)   # Problem 2: 7 points.

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
    @staticmethod
    def _errType(error):
        """Get just the name of the exception 'error' in string format."""
        if isinstance(error, BaseException):
            return str(type(error)).lstrip("<type 'exceptions.").rstrip("'>")
        else:
            return str(error)

    def _eqTest(self, correct, student, message):
        """Test to see if 'correct' and 'student' are close to each other.
        Report the given 'message' if they are not.
        """
        if abs(correct - student) < 1e-12:
            return 1
        else:
            self.feedback += message
            self.feedback += "\n\tCorrect response: %s"%correct
            self.feedback += "\n\tStudent response: %s"%student
            return 0

    def _grade(self, points, message=None):
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
        """Test prob1() (built-in functions). 3 points."""

        l = list(randint(-50,50,10))
        key, response = prob1(l), s.prob1(l)
        if response is None:
            raise NotImplementedError("Problem 1 Incomplete")

        points  = self._eqTest(key[0], response[0], "\nIncorrect maximum")
        points += self._eqTest(key[1], response[1], "\nIncorrect minimum")
        points += self._eqTest(key[2], response[2], "\nIncorrect average")

        return points

    def problem2(self, s):
        """Test prob2() (mutable vs. immutable objects). 5 points."""

        print"\nCorrect output:";   prob2()
        print"\nStudent output:"; s.prob2()
        return self._grade(5, "\n\tIncorrect response(s)"
                     "\n\t(Hint: 3 are immutable and 2 are mutable)")

    def problem3(self, s):
        """Test prob3() (make and use the calculator module). 5 points."""

        points  = 2*self._eqTest(prob3(5,12), s.prob3(5,12),
                                "\nIncorrect hypotenuse length")
        a, b = randint(1,50,2)
        points += 3*self._eqTest(prob3(a,b), s.prob3(a,b),
                                "\nIncorrect hypotenuse length")
        return points

    def problem4(self, s):
        """Test prob4() (using another module). 7 points."""

        print("Testing Problem 4")
        print("Correct outputs:")
        os.system("python " + __file__)
        os.system("python " + __file__ + " Wrong Name")
        os.system("python " + __file__ + " matrices.npz")
        print("\nStudent outputs:")
        os.system('python ' + s.__file__)
        os.system('python ' + s.__file__ + ' "Wrong Name"')
        os.system('python ' + s.__file__ + ' "matrices.npz"')
        return self._grade(7, "\n\tIncorrect outputs")

# ============================== END OF FILE ================================ #
