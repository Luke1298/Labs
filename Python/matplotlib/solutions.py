# solutions.py
"""MatPlotLib solutions file."""

from matplotlib import pyplot as plt
from mayavi import mlab
import numpy as np

# Problem 1
def curve():
    """Plot the curve 1/(x-1) on [-2,6]. Plot the two sides of the
    curve separately (still with a single call to plt.plot()) so that
    the graph looks discontinuous at x = 1.
    """
    x1 = np.linspace(-2,.999,100)
    y1 = 1./(x1-1)
    x2 = np.linspace(1.001,6,100)
    y2 = 1./(x2-1)
    plt.plot(x1,y1,'m--',x2,y2,'m--',linewidth=5)
    plt.axis([-2,6,-6,6])
    plt.show()


# Problem 2
def colormesh():
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on the domain
    [-2*pi, 2*pi]x[-2*pi, 2*pi]. Include the scale bar in your plot. 
    """
    x = np.linspace(-2*np.pi,2*np.pi,300)
    y = np.linspace(-2*np.pi,2*np.pi,300)
    X, Y = np.meshgrid(x,y)
    f = (np.sin(X)*np.sin(Y))/(X*Y)
    plt.pcolormesh(X,Y,f,cmap='seismic')
    plt.colorbar()
    plt.axis([-2*np.pi,2*np.pi,-2*np.pi,2*np.pi])
    plt.gca().set_aspect('equal')
    plt.show()


# Problem 3
def histogram():
    """Plot a histogram and a scatter plot of 50 random numbers chosen
    in the interval [0,1)
    """
    y = np.random.rand(50)
    plt.subplot(1,2,1)
    plt.hist(y,bins=5)
    x = np.linspace(1,50,num=50)
    plt.subplot(1,2,2)
    plt.scatter(x,y)
    plt.axis([0,50,-.2,1.2])
    z = np.mean(y)
    z = np.ones(len(x))*z
    plt.plot(x,z,color='r')
    plt.show()

    
# Problem 4
def ripple():
    """Plot z = sin(10(x^2 + y^2))/10 on [-1,1]x[-1,1] using Mayavi."""
    X, Y = np.mgrid[-1:1:.025,-1:1:.025]
    Z = np.sin(10*(X**2+Y**2))/10.
    mlab.surf(X,Y,Z)
    mlab.show()
    
# END OF SOLUTIONS ============================================================

import inspect

# Test script
def test(student_module):
    """Test script. Import the student's solutions file as a module.
    
    10 points for problem 1
    10 points for problem 2
    10 points for problem 3
    10 points for problem 4
    
    Inputs:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 40.
        feedback (str): a printout of test results for the student.
    """
    tester = _testDriver()
    tester.test_all(student_module)
    return tester.score, tester.feedback

def _autoclose(func):
    """decorator for closing figures automatically during grading."""
    def wrapper(*args, **kwargs):
        plt.ion()
        plt.close('all')
        result = func(*args, **kwargs)
        plt.close('all')
        return result
    return wrapper

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
                self.feedback += "\n%s: %s"%(self._errType(e),e)

        # Grade each problem.
        test_one(self.problem1, 1, 10)   # Problem 1: 10 points.
        test_one(self.problem2, 2, 10)   # Problem 2: 10 points.
        test_one(self.problem3, 3, 10)   # Problem 2: 10 points.
        test_one(self.problem4, 4, 10)   # Problem 2: 10 points.

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

    # Helper Function ---------------------------------------------------------
    @staticmethod
    def _errType(error):
        """Get just the name of the exception 'error' in string format."""
        if isinstance(error, BaseException):
            return str(type(error)).lstrip("<type 'exceptions.").rstrip("'>")
        else:
            return str(error)

    def _grade(self, points, message=None):
        """Manually grade a problem worth 'points'. Return the score."""
        credit = -1
        while credit > points or credit < 0:
            try:
                credit = int(input("Score out of %d: "%points))
            except:
                credit = -1
        if credit != points:
            # Add comments (optionally),
            comments = raw_input("Comments: ")
            if len(comments) > 0:
                self.feedback += "\n\t%s"%comments
            # Or add a predetermined error message.
            elif message is not None:
                self.feedback += "\n\t%s"%message
        return credit

    # Problems ----------------------------------------------------------------
    @_autoclose
    def problem1(self, s):
        """Test curve(). 10 points."""
        if not hasattr(s, "curve"):
            raise NotImplementedError("Problem 1 Incomplete")
        points = 0

        # Check that they only used 1 plot command.
        doclength = len(s.curve.__doc__.split('\n'))
        lines = inspect.getsourcelines(s.curve)[0][doclength:]
        count = sum([line.count('plot') for line in lines])
        if count == 1:
            points += 3
        elif count > 1:
            print("\Ensure that plt.plot() is only used once. \nStudent Code:")
            for i in lines:
                print i[:-1]
            points += self._grade(3, "Only call plt.plot() once.")
        
        # Check the plot output.
        print("""\nSpecifications:
        - Discontinuous
        - think, magenta, dotted line
        - window should be [-2,6]x[-6,6]""")
        s.curve()
        points += self._grade(7, "curve() plot does not match specifications")
        return points

    @_autoclose
    def problem2(self, s):
        """Test colormesh(). 10 points."""
        if not hasattr(s, "colormesh"):
            raise NotImplementedError("Problem 2 Incomplete")

        s.colormesh()
        print("\nOverall appearance\t"),
        points  = self._grade(8, "Plot does not match specifications")
        
        print("Not pixelated\t\t"),
        points += self._grade(2, "Plot should not be so pixelated")
        return points

    @_autoclose
    def problem3(self, s):
        """Test histogram(). 10 points."""
        if not hasattr(s, "histogram"):
            raise NotImplementedError("Problem 1 Incomplete")

        s.histogram()
        print("\nHistogram with 5 bins\t"),
        points  = self._grade(4, "Histogram does not match specifications")
        
        print("Scatter plot\t\t"),
        points += self._grade(4, "Scatter plot does not match specifications.")
        
        print("Average line\t\t"),
        points += self._grade(2,
                            "Average not displayed on scatter plot correctly.")
        return points

    @_autoclose
    def problem4(self, s):
        """Test ripple(). 10 points."""
        if not hasattr(s, "ripple"):
            raise NotImplementedError("Problem 4 Incomplete")

        s.ripple()
        return self._grade(10,
                        "ripple() plot does not match specifications.")


# ============================== END OF FILE ================================ #
