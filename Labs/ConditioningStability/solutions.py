import numpy as np
from scipy import linalg as la
from scipy.linalg.flapack import dtrtrs
from matplotlib import pyplot as plt


def root_error(roots):
    """ Make a scatter plot of the real and imaginary parts of
    the real and imaginary parts of roots and of the real and
    imaginary parts of the computed roots of the polynomial with
    coefficients calculated so that it should have roots at
    the same points as the original set of roots. """
    computed_roots = np.poly1d(np.poly(roots)).roots
    plt.scatter(roots.real, roots.imag, color='b')
    plt.scatter(computed_roots.real, computed_roots.imag, color='r')
    plt.show()

def estimate_condition(eig, A, peturbation = 1E-4, tries=10000):
    """ A brute force way of estimating the condition number
    of the eigenvalue problem. 'eig' is expected to be a callable
    function that returns *only* the eigenvalues of matrices of
    the same shape as 'A' (not the eigenvectors).
    Some examples of what 'eig' would be are:
    
    lambda A: scipy.linalg.eig(A, right=False)
    lambda A: scipy.linalg.eigh(A, eigvals_only=False)
    
    The first will work for nonsymmetric matrices.
    The second will work only symmetric ones.
    'peturbation' is the element-wise standard deviation of
    the normally distributed peturbations that are to be
    added to 'A' to test for the condition number.
    'tries' is the number of tries to use to try to
    approximate the maximum. """
    A_eigs = eig(A)
    A_eigs_norm = la.norm(A_eigs)
    A_norm = la.norm(A)
    changes = np.empty(tries)
    for i in xrange(tries):
        dx = np.random.normal(scale=peturbation, size=A.size).reshape(A.shape)
        changes[i] = la.norm(A_eigs - eig(A + dx)) / A_eigs_norm
        changes[i] /= la.norm(dx) / A_norm
    return changes.max()

# Helper functions given in the lab.
def qr_solve(A, b):
    """ Solve the system A x = b using QR decomposition. """
    Q, R = la.qr(A)
    return dtrtrs(R.T, Q.T.dot(b), lower=1, trans=1)[0]

def bad_arr_1(n):
    """ Construct a specific pathological example
    that breaks LU decomposition. These examples
    are very rare, but they do exist.
    Strictly speaking, the condition number
    for this matrix isn't terribly bad. """
    A = - np.ones((n, n))
    A[:,:-1] = np.tril(A[:,:-1])
    np.fill_diagonal(A, 1)
    A[:,-1] = 1
    return A

def bad_arr_2(n, peturbation = 1E-8):
    """ Construct another matrix that is nearly singular
    by computing A.dot(A.T) for a matrix A that is
    not square and then adding some small changes
    so it is not exactly singular. """
    A = np.random.rand(n, n // 2)
    return A.dot(A.T) + peturbation * np.random.rand(n, n)

# Some helper functions for the last problem
def check_solve(A):
    b = np.random.rand(A.shape[0])
    b2 = A.dot(b)
    return la.norm(b - la.solve(A, b2))

def check_qr(A):
    b = np.random.rand(A.shape[0])
    b2 = A.dot(b)
    return la.norm(b - qr_solve(A, b2))

def check_lstsq(A):
    b = np.random.rand(A.shape[0])
    b2 = A.dot(b)
    return la.norm(b - la.lstsq(A, b2)[0])

# Errors of different algorithms for solving systems.
def plot_errs(low, high, step, make_A):
    """ Plot the errors when solving the system A x = b using
    LU decomposition (scipy.linalg.solve),
    QR decomposition (the function given in the lab),
    and the SVD (scipy.linalg.lstsq).
    The x axis for the plot is the number of rows of 'A'.
    'make_A' is a function that takes an integer 'n' as input
    and returns an nxn array 'A' to be used for testing
    stability. 'low', 'high', and 'step' are used to
    determine which sizes to use to test the errors.
    Test the errors at sizes in 'range(low, high, step)'. """
    nvals = range(low, high, step)
    solve_err = []
    qr_solve_err = []
    lstsq_err = []
    for i in nvals:
        A = make_A(i)
        solve_err.append(check_solve(A))
        qr_solve_err.append(check_qr(A))
        lstsq_err.append(check_lstsq(A))
    plt.semilogy(nvals, solve_err,
                 nvals, qr_solve_err,
                 nvals, lstsq_err)
    plt.show()

# Test Script and Class =======================================================

def test(student_module):
    """Test script. Import the student's solutions file as a module.
        
        X points for problem 1
        X points for problem 2
        ...
        
        Inputs:
        student_module: the imported module for the student's file.
        
        Returns:
        score (int): the student's score, out of TOTAL.
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
    def test_all(self, student_module, total=100):
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
        test_one(self.problem1, 1, 0)   # Problem 1: X points.
        test_one(self.problem2, 2, 0)   # Problem 2: X points.
        
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

# Possible Helper Functions -----------------------------------------------
@staticmethod
    def _errType(error):
        """Get just the name of the exception 'error' in string format."""
        if isinstance(error, BaseException):
            return str(type(error)).lstrip("<type 'exceptions.").rstrip("'>")
        else:
            return str(error)

def _eqTest(self, correct, student, message):
    """Test to see if 'correct' and 'student' are equal.
        Report the given 'message' if they are not.
        """
            if correct == student:
            return 1
                else:
                    self.feedback += "\n%s"%message
                        self.feedback += "\n\tCorrect response: %s"%correct
                            self.feedback += "\n\tStudent response: %s"%student
                                return 0

def _strTest(self, correct, student, message):
    """Test to see if 'correct' and 'student' have the same string
        representation. Report the given 'message' if they are not.
        """
            if str(correct) == str(student):
            return 1
                else:
                    self.feedback += "\n%s"%message
                        self.feedback += "\n\tCorrect response: %s"%correct
                            self.feedback += "\n\tStudent response: %s"%student
                                return 0

def _evalTest(self, expression, correct, message):
    """Test a boolean 'expression' to see if it is 'correct'.
        Report the given 'message' if it is not.
        """
            if expression is correct:
            return 1
                else:
                    self.feedback += "\n%s"%message
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
                self.feedback += "\n%s"%comments
        # Or add a predetermined error message.
        elif message is not None:
            self.feedback += "\n%s"%message
return credit
    
    # Problems ----------------------------------------------------------------
    def problem1(self, s):
        """Test Problem 1. X points."""
        
        points = 0
        # Test problem 1 here.
        return points
    
    def problem2(self, s):
        """Test Problem 2. X points."""
        
        points = 0
        # Test problem 2 here.
        return points

