# testDriver.py
"""Outline for Foundations of Applied Mathematics lab test drivers.

The _testDriver class is designed to be flexible. The test_all() routine will
grade an entire module, while each problem can be graded individually via the
different problemX() methods. This allows the instructor to grade from
IPython, or to automate grading using Git, Google Drive, or another file
system manager.

Each time this test script is put into a lab, customize the docstrings of the
test() function and the _testDriver class to give specific instructions about
how the lab is to be graded, if it is different than normal. All functions and
classes from this file should be placed below all other code in the lab
solutions file.

The @_autoclose tag makes it easy to grade a problem that produces a plot.
It should only be on a problem-grading function that uses _testDriver._grade()
or some other pausing command (like raw_input()) so that the plot is not closed
immediately after it is created.

The @_timeout tag prevents a function from running for longer than a
specificied number of seconds. Be careful not to use this wrapper in
conjunction with _testDriver._grade() or another pausing command that waits
for the grader's response. NOTE that this decorator will only work on Unix.

To test a particular test driver, navigate to the solutions file and start
IPython. Import the solutions file, and use it as the input for test().

In [1]: import solutions as s

In [2]: reload(s); feedback, score = s.test(s)

This file can also be run from the terminal. To grade a file called
student.py, run the following command:

$ python testDriver.py student.py

and the resulting feedback will be printed out.
"""

# Wrappers ====================================================================

import signal
from functools import wraps
from matplotlib import pyplot as plt

def _autoclose(func):
    """function decorator for closing figures automatically."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            plt.ion()
            return func(*args, **kwargs)
        finally:
            plt.close('all')
            plt.ioff()
    return wrapper

def _timeout(seconds):
    """Decorator for preventing a function from running for too long.

    Inputs:
        seconds (int): The number of seconds allowed.

    Notes:
        This decorator uses signal.SIGALRM, which is only available on Unix.
    """
    assert isinstance(seconds, int), "@timeout(sec) requires an int"
    
    class TimeoutError(Exception):
        pass

    def _handler(signum, frame):
        """Handle the alarm by raising a custom exception."""
        raise TimeoutError("Timeout after {0} seconds".format(seconds))

    def decorator(func):
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handler)
            signal.alarm(seconds)               # Set the alarm.
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)                 # Turn the alarm off.
            return result
        return wraps(func)(wrapper)
    return decorator

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

# Grade from the terminal
if __name__ == '__main__':
    import sys, imp
    filename = sys.argv[1]
    student = imp.load_source("student", filename)
    score, feedback = test(student)
    # now use/store the score and feedback as desired.
