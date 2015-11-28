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
from os import system

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
                self.feedback += "\n%s: %s"%(self._errType(e),e)

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
            self.feedback += message
            self.feedback += "\nCorrect response:\n%s"%correct
            self.feedback += "\nStudent response:\n%s"%student
            return 0

    def _strTest(self, correct, student, message):
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
        """Test Problem 1. X points."""
        if not hasattr(s, "my_func"):
            raise NotImplementedError("Problem 1 Incomplete")

        def test_my_func(arg, a, b, c, d, e):
            print("\nTesting my_func() with bad %s argument..."%arg)
            try:
                s.my_func(a, b, c, d, e)
            except TypeError as e:
                print("Student Error message: %s"%e)
                return self._grade(1,
                            "\n\tInclude a more informative error message")
            except BaseException as e:
                self.feedback += "\n\tFailed to raise a TypeError "
                self.feedback += "(got a %s instead)"%self._errType(e)
            else:
                self.feedback += "\n\tFailed to raise a TypeError"
            return 0

        # Test my_func() with different bad inputs (5 points).
        points  =   test_my_func("1st", 1, 2, 3, 4, 5)
        points += 2*test_my_func("3rd", 'a', 2, 'c', 4, 5)
        points += 2*test_my_func("4th/5th", 'a', 2, 3, 'd', 5)
        return points

    def problem2(self, s):
        """Test Problem 2. 5 points."""
        if not hasattr(s, "forever"):
            raise NotImplementedError("Problem 2 Incomplete")

        def _handle(signum, frame):
            raise KeyboardInterrupt("Arificial KeyboardInterrupt")

        # Test forever(), letting it run to completion (2 points).
        print("\nCorrect Output:\tProcess Completed\nStudent Output:\t"),
        points = self._eqTest(s.forever(10),10,
                                "\n\tforever(10) didn't return 10.")
        points += self._grade(1, "\n\t'Process Completed' not printed")

        # Test forever(), interrupting it with a KeyboardInterrupt (3 points).
        print("\nCorrect Output:\tProcess Interrupted\nStudent Output:\t"),
        signal.signal(signal.SIGALRM, _handle); signal.alarm(1)
        try:
            x = s.forever(1000000000)
        except KeyboardInterrupt:
            self.feedback += "\n\tKeyboardInterrupt not caught"
        else:
            points += 2
        points += self._grade(1, "\n\t'Process Interrupted' not printed")

        return points

    def problem3(self, s):
        """Test InvalidOptionError. 5 points."""
        if not hasattr(s, "InvalidOptionError"):
            raise NotImplementedError("Problem 3 Incomplete")

        # Check that InvalidOptionError inherits from Exception (1 point).
        points = 0
        if issubclass(s.InvalidOptionError, Exception):
            points += 1

        # Check that InvalidOptionError behaves like Exception (4 points).
        try:
            raise s.InvalidOptionError("This", "is", "a", "test")
        except s.InvalidOptionError as e:
            points += 4
        except BaseException as e:
            self.feedback += "\n\tFailed to raise an InvalidOptionError "
            self.feedback += "(got a %s instead)"%self._errType(e)

        return points

    def problem4(self, s):
        """Test ContentFilter.__init__(). 5 points."""

        if not hasattr(s, "ContentFilter"):
            raise NotImplementedError("Problem 4 Incomplete")
        points = 0

        # Test faulty initialization (2 points).
        try:
            x = s.ContentFilter(123456789)
        except TypeError as e:
            points += 2
        except BaseException as e:
            self.feedback += "\n\tFailed to raise a TypeError "
            self.feedback += "(got a %s instead)"%self._errType(e)
        else:
            self.feedback += "\n\tFailed to raise a TypeError"

        # Test proper initialization (3 points).
        x = s.ContentFilter("contentfilter_test.txt")
        return points + 3

    def problem5(self, s, sourcefile="contentfilter_test.txt"):
        """Test the ContentFilter class's methods. 20 points."""
        if not hasattr(s, "ContentFilter"):
            raise NotImplementedError("Problem 5 Incomplete")
        sFilter = s.ContentFilter(sourcefile)

        def test_bad(x, statement, method):
            """Test that eval(statement) raises an InvalidOptionError."""
            try:
                eval(statement)
            except s.InvalidOptionError:
                return 1
            except BaseException as e:
                print(e)
                self.feedback += "\n\tContentFilter.%s() "%method
                self.feedback += "failed to raise an InvalidOptionError "
                self.feedback += "(got a %s instead)"%self._errType(e)
            else:
                self.feedback += "\n\tFailed to raise an InvalidOptionError"
            return 0

        # Test that each method raises an InvalidOptionError for bad 'mode'.
        points  = test_bad(sFilter, 'x.hyphenate("out.txt", mode="z")',
                                                                "hyphenate")
        points += test_bad(sFilter, 'x.uniform("out.txt", mode="z")',
                                                                "uniform")
        points += test_bad(sFilter, 'x.reverse("out.txt", mode="z")',
                                                                "reverse")
        points += test_bad(sFilter, 'x.transpose("out.txt", mode="z")',
                                                                "transpose")

        # Test that uniform() and reverse() raise InvalidOptionErrors correctly
        points += test_bad(sFilter, 'x.uniform("out.txt", case="middle")',
                                                                    'uniform')
        points += test_bad(sFilter, 'x.reverse("out.txt", unit="chunk")',
                                                                    'reverse')

        def test_good(x, statement, method, value):
            """Test a ContentFilter method with correct usage."""
            print("\nOutput of ContentFilter.%s:\n"%method)
            filename = "temporary_outfile.txt"
            eval(statement)
            with open(filename, 'r') as f:
                for line in f:
                    print(line.rstrip())
            return self._grade(value, "\n\tContentFilter.%s failed"%method)

        # Test each method with correct usage (11 points).
        print("\nSource file for testing ContentFilter class:\n")
        with open(sourcefile) as f:
            for line in f:
                print(line.rstrip())

        points += test_good(sFilter, 'x.hyphenate(filename, mode="w")',
                                                        'hyphenate()', 2)
        points += test_good(sFilter,
                            'x.uniform(filename, mode="w", case="upper")',
                                                'uniform(case="upper")', 1)
        points += test_good(sFilter,
                            'x.uniform(filename, mode="w", case="lower")',
                                                'uniform(case="lower")', 1)
        points += test_good(sFilter,
                            'x.reverse(filename, mode="w", unit="word")',
                                                'reverse(unit="word")', 2)
        points += test_good(sFilter,
                            'x.reverse(filename, mode="w", unit="line")',
                                                'reverse(unit="line")', 2)
        points += test_good(sFilter, 'x.transpose(filename, mode="w")',
                                                        'transpose()', 3)
        system("rm temporary_outfile.txt")

        # Test ContentFilter.__str__() (3 points).
        template = ContentFilter(sourcefile)
        print("\nCorrect ContentFilter.__str__() output:\n")
        print(template)
        print("\nStudent ContentFilter.__str__() output:\n")
        print(sFilter)
        points += self._grade(3, "\n\tContentFilter.__str__() failed")

        return points

# END OF FILE =================================================================
