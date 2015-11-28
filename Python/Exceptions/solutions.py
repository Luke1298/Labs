# solution.py
"""Exceptions and File I/O Protocol solutions file."""

# Problem 1: Modify this function to account for bad inputs.
def my_func(a, b, c, d, e):
    # Validate arg 1.
    if not isinstance(a, str):
        raise TypeError("arg 1 must be a string.")
    print("The first argument is " + a)
    
    # Validate args 2 and 3.
    numerical = {int, float, long, complex}
    if type(b) not in numerical or type(c) not in numerical:
        raise TypeError("args 2 and 3 must be a numerical type.")
    x = sum([b, c])
    
    # Validate args 4 and 5.
    if type(d) is not type(e):
        raise TypeError("args 5 and 6 must be the same type")
    y = d + e
    
    return a, x, y

# Problem 2: Modify this function to account for KeyboardInterrupts.
def forever(max_iters=1000000000000):
    iters = 0
    try:
        while True:
            iters += 1
            if iters >= max_iters:
                break
    except KeyboardInterrupt:
        print("Process Interrupted")
    else:
        print("Process Completed")
    return iters

# Problem 3: Write a custom Exception class.
class InvalidOptionError(Exception):
    pass

# Problems 4 and 5: Write the ContentFilter class.
class ContentFilter(object):
    """docstring for ContentFilter"""
    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("'filename' must be a string")
        self.filename = filename
        with open(filename, 'r') as f:
            self.contents = f.read()

    def _validate_mode(self, mode):
        """Validate the 'mode' keyword argument for each method."""
        if mode not in {'a', 'w'}:
            raise InvalidOptionError("'mode' must be 'a' or 'w'")
    
    def hyphenate(self, outfile, mode='w'):
        """Write the data to the outfile in a single line,
        with hyphens between each word.
        """
        self._validate_mode(mode)

        # Replace whitespace with hyphens.
        out = self.contents.replace('\n', '-')
        out = out.replace('\t', '-')
        out = out.replace(' ', '-')

        # Write the results.
        with open(outfile, mode) as f:
            f.write(out)
            if self.contents[-1].isspace():     # replace final character
                f.write(self.contents[-1])

    def uniform(self, outfile, mode='w', case='upper'):
        """Write the data ot the outfile in uniform case."""
        self._validate_mode(mode)

        # Translate into the indicated case.
        if case == "upper":
            data = self.contents.upper()
        elif case == "lower":
            data = self.contents.lower()
        else:
            raise InvalidOptionError("'case' must be 'upper' or 'lower'")

        # Write the data.
        with open(outfile, mode) as f:
            f.write(data)

    def reverse(self, outfile, mode='w', unit='word'):
        """Write the data to the outfile in reverse order."""
        self._validate_mode(mode)

        # Get the data into a list of lists: each inner list is a line
        # of the data, containing the words of the line.
        lines = self.contents.split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        lines = [line.split() for line in lines]

        # Perform the reversal.
        if unit == 'word':
            data = [line[::-1] for line in lines]
        elif unit == 'line':
            data = list(reversed(lines))
        else:
            raise InvalidOptionError("'unit' must be 'word' or 'line'")

        # Paste each line back together.
        data = [" ".join(line) for line in data]

        # Write the data out. Don't forget newlines!
        with open(outfile, mode) as f:
            for line in data:
                f.write(line)
                f.write('\n')

    def transpose(self, outfile, mode='w'):
        """Write the transposed version of the data to the outfile."""
        self._validate_mode(mode)

        # Get the data into a list of lists as in reverse().
        lines = self.contents.split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        lines = [line.split(' ') for line in lines]

        # Calculate the max length so we can iterate.
        max_len = max([len(line) for line in lines])

        # Write the data.
        f = open(outfile, mode)
        for i in xrange(max_len):
            for line in lines:
                try:
                    f.write(line[i])
                    f.write(" ")
                except IndexError:
                    # Catch errors
                    pass
            f.write("\n")
        f.close()

    def __str__(self):
        """String representation: info about the contents of the file."""
        chars = len(self.contents)
        alpha = sum([s.isalpha() for s in self.contents])
        numer = sum([s.isdigit() for s in self.contents])
        space = sum([s.isspace() for s in self.contents])
        lines = len(self.contents.split('\n'))
        return "Source file:\t\t%s\nTotal characters:\t%d\nAlphabetic characters:\t%d\nNumerical characters:\t%d\nWhitespace characters:\t%d\nNumber of lines:\t%d"%(self.filename, chars, alpha, numer, space, lines)
        # Or, the slightly longer way.
        out = "Source file:\t\t" + self.filename
        out += "\nTotal characters:\t" + str(chars)
        out += "\nAlphabetic characters:\t" + str(alpha)
        out += "\nNumerical characters:\t" + str(numer)
        out += "\nWhitespace characters:\t" + str(space)
        out += "\nNumber of lines:\t" + str(lines)
        return out

# END OF SOLUTIONS ============================================================

import signal
from sys import stdout

# Test script
def test(student_module):
    """Test script. Import the student's solutions file as a module.
    
    5  points for problem 1
    5  points for problem 2
    5  points for problem 3
    5  points for problem 4
    20 points for problem 5
    
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
    def test_all(self, student_module, total=40):
        """Grade the provided module on each problem and compile feedback.

        For problems 4 and 5, you must have a "contentfilter_test.txt" file
        in current directory. This is the source file that will be used to
        test the ContentFilter class.
        """
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
        test_one(self.problem3, 3, 5)   # Problem 3:  5 points.
        test_one(self.problem4, 4, 5)   # Problem 4:  5 points.
        test_one(self.problem5, 5, 20)  # Problem 5: 25 points.

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
    def eqTest(self, correct, student, message):
        """Test to see if 'correct' and 'student' are equal.
        Report the given 'message' if they are not.
        """
        if correct == student:
            return 1
        else:
            self.feedback += message
            self.feedback += "\nCorrect response:\n%s"%correct
            self.feedback += "\nStudent response:\n%s"%student
            return 0

    def strTest(self, correct, student, message):
        """Test to see if 'correct' and 'student' have the same string
        representation. Report the given 'message' if they are not.
        """
        if str(correct) == str(student):
            return 1
        else:
            self.feedback += message
            self.feedback += "\nCorrect response:\n%s"%correct
            self.feedback += "\nStudent response:\n%s"%student
            return 0

    # used
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
        """Test Problem 1. X points."""

        def test_my_func(arg, a, b, c, d, e):
            print("\nTesting my_func() with bad %s argument..."%arg)
            try:
                s.my_func(a, b, c, d, e)
            except TypeError as e:
                print("Student Error message: %s"%e)
                return self.grade(1,
                            "\n\tInclude a more informative error message")
            except BaseException as e:
                self.feedback += "\n\tFailed to raise a TypeError "
                self.feedback += "(got a %s instead)"%type(e)
            else:
                self.feedback += "\n\tFailed to raise a TypeError"

        points  =   test_my_func("1st", 1, 2, 3, 4, 5)
        points += 2*test_my_func("3rd", 'a', 2, 'c', 4, 5)
        points += 2*test_my_func("4th/5th", 'a', 2, 3, 'd', 5)
        return points

    def problem2(self, s):
        """Test Problem 2. 5 points."""

        def _handle(signum, frame):
            raise KeyboardInterrupt("Arificial KeyboardInterrupt")

        print("Testing forever() to completion..."),; stdout.flush()
        points = self.eqTest(s.forever(10),10,
                                "\n\tforever(10) didn't return 10.")
        points += self.grade(1, "\n\t'Process Completed' not printed")

        print("Testing forever() with a KeyboardInterrupt..."),
        stdout.flush()
        signal.signal(signal.SIGALRM, _handle)
        signal.alarm(1)
        try:
            x = s.forever(1000000000)
        except KeyboardInterrupt:
            self.feedback += "\n\tKeyboardInterrupt not caught"
        else:
            points += 2
        points += self.grade(1, "\n\t'Process Interrupted' not printed")

        return points

    def problem3(self, s):
        """Test InvalidOptionError. 5 points."""
        points = 0

        try:
            if issubclass(s.InvalidOptionError, Exception):
                points += 1
        except AttributeError:
            raise NotImplementedError("Problem 3 Incomplete")

        try:
            raise s.InvalidOptionError("This", "is", "a", "test")
        except s.InvalidOptionError as e:
            points += 4
        except BaseException as e:
            self.feedback += "\n\tFailed to raise an InvalidOptionError "
            self.feedback += "(got a %s instead)"%type(e)

        return points

    def problem4(self, s):
        """Test ContentFilter.__init__(). 5 points."""

        points = 0

        # try to initialize a CF object without a string argument

        # try to initialize a CF object correctly.
        
        return points

    def problem5(self, s):
        """Test the ContentFilter class's methods. 20 points."""

        points = 0
        
        return points
