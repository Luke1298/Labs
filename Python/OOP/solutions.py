# solutions.py
"""Object Oriented Programming solutions file.
Written by Shane McQuarrie, Fall 2015.
"""

from math import sqrt

# Problem 1: Modify this class. Add 'name' and max_size' attributes, modify
#   the put() method, and add a dump() method. Remember to update docstrings.
class Backpack(object):
    """Backpack object. Has a name, color, maximum size,
    and a list of contents.
    
    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the color of the backpack.
        max_size (int): the maximum number of items that can fit in the
            backpack.
        contents (list): the contents of the backpack.
    """

    def __init__(self, name, color, max_size=5):
        """Set the color, name, and maximum size of the backpack.
        Also initialize an empty contents list.
        
        Inputs:
            color (str): the color of the backpack.
            name (str): a label for the backpack.
            max_size (int, opt): the maximum number of items that can
                fit in the backpack. Defaults to 5.
        
        Returns:
            A backpack object wth no contents.
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
    
    def put(self,item):
        """Add 'item' to the backpack's list of contents if there is room."""
        if len(self.contents) >= self.max_size:         # Check for overflow
            print("No Room!")
        else:
            self.contents.append(item)
    
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
    
    def dump(self):
        """Remove all items from the backpack."""
        self.contents = []
    
    # Magic Methods -----------------------------------------------------------
    
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)
    
    def __lt__(self,other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)

    # Problem 3: Write the __str__ and __eq__ methods for the Backpack class.
    def __eq__(self,other):
        """Two backpack objects are equal if and only if they have the same
        name, color, and contents. Note that the contents do not need to be
        in the same order for the contents to be the same.
        """
        if self.name != other.name or self.color != other.color:
            return False                                # Check name and color
        if len(self.contents) != len(other.contents):
            return False                                # Check contents size
        l1 = sorted(self.contents)                      # Sort for comparison
        l2 = sorted(other.contents)
        return l1 == l2                                 # Check contents

    def __str__(self):
        """String Representation: a list of the backpack's attributes."""
        return "Owner:\t\t%s\nColor:\t\t%s\nSize:\t\t%d\nMax Size:\t%d\nContents:\t%s"%(self.name,
            self.color, len(self.contents), self.max_size, self.contents)
        # Or, a slightly longer way:
        out = "Owner:\t\t" + self.name
        out += "\nColor:\t\t" + self.color
        out += "\nSize:\t\t" + str(len(self.contents))
        out += "\nMax Size:\t" + str(self.max_size)
        out += "\nContents:\t" + str(self.contents)
        return out

# Study this example of inheritance. You are not required to modify it.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.
    
    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit
            in the knapsack.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    
    def __init__(self, name, color, max_size=3):
        """Use the Backpack constructor to initialize the name and
        max_size attributes. A knapsack only holds 3 item by default
        instead of 5. 
        
        Inputs:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int, opt): the maximum number of items that can be
                stored in the knapsack. Defaults to 3.
        
        Returns:
            A knapsack object with no contents.
        """
        
        Backpack.__init__(self, name, color, max_size)
        self.closed = True
    
    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print "I'm closed!"
        else:
            Backpack.put(self, item)
    
    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print "I'm closed!"
        else:
            Backpack.take(self, item)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    In addition to storing items like a backpack, a jetpack has
    fuel that is used to fly.
    
    Attributes:
        color (str): the color of the jetpack.
        name (str): the name of the jetpack.
        max_size (int): the maximum number of items that can fit
            in the jetpack.
        contents (list): the contents of the jetpack.
        fuel (int): the amount of fuel in the jetpack's tank.
    """

    def __init__(self, color, name, max_size=2, fuel=10):
        """Constructor for a jetpack object. A jetpack only holds 2 items
        by default instead of 5, and has an additional attribute for fuel.
        
        Inputs:
            color (str): the color of the jetpack..
            name (str): the name of the jetpack.
            max_size (int, opt): the maximum number of items that can
                be stored in the jetpack. Defaults to 2.
            fuel (int, opt): the starting amount of fuel. Defaults to 10.
        
        Returns:
            A jetpck object with no contents and 10 units of fuel.
        """
        Backpack.__init__(self, color, name, max_size)
        self.fuel = fuel
    
    def fly(self, amount):
        """Fly by using 'amount' units of fuel."""
        if amount > self.fuel:                      # Check current fuel
            print "Not enough fuel!"
        else:
            self.fuel -= amount
    
    def dump(self):
        """Empty the contents of the jetpack and dump out all the fuel."""
        Backpack.dump(self)                         # Or self.contents = []
        self.fuel = 0                               # Reset fuel to 0


# Problem 4: Write a ComplexNumber class.
class ComplexNumber(object):
    """Complex number object. Has a real and imaginary part.
    
    Attributes:
        real (float): the real part of the complex number.
        imag (float): the imaginary part of the complex number.
    """
    def __init__(self, a, b):
        """Initialize (separately) the real and imaginary components.
        Inputs:
            a (float): the real part.
            b (float): the imaginary part.
        """
        self.real = a
        self.imag = b
    
    def conjugate(self):
        """Return a ComplexNumber object of the complex conjugate."""
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        """Return the magnitude of the complex number.
        |a+bi| = sqrt{a^2 + b^2}.
        """
        return sqrt(self.real**2 + self.imag**2)
    
    def __lt__(self, other):
        """(a+bi) < (c+di) iff |a+bi| < |c+di|."""
        return abs(self) < abs(other)

    def __gt__(self, other):
        """(a+bi) > (c+di) iff |a+bi| > |c+di|."""
        return abs(self) > abs(other)

    def __eq__(self, other):
        """(a+bi) = (c+di) iff a=c AND b=d."""
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        """(a+bi) != (c+di) iff a!=c OR b!=d."""
        return not self == other            # or, more explicitly,
        return self.real != other.real or self.imag != other.imag

    def __add__(self, other):
        """(a+bi) + (c+di) = (a+c) + (b+d)i"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """(a+bi) - (c+di) = (a-c) + (b-d)i"""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """(a+bi)*(c+di) = (ac-bd) + (ad+bc)i"""
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real, imag)
    
    def __div__(self,other):
        """Do a little algebra before implementing:
        (a+bi) / (c+di)
        = (a+bi)*(c-di) / (c+di)*(c-di)             # Multiply by the conjugate
        = ((ac+bd) + (bc-ad)i) / (c**2 + d**2)      # Distribute
        """
        denom = float(other.real**2 + other.imag**2)
        real = ((self.real * other.real) + (self.imag * other.imag))/denom
        imag = ((self.imag * other.real) - (self.real * other.imag))/denom
        return ComplexNumber(real, imag)

# END OF SOLUTIONS ============================================================

from numpy.random import randint

# Test script
def test(student_module):
    """Test script. Import the student's solutions file as a module.
    
    10 points for problem 1.
    10 points for problem 2.
    15 points for problem 3.
    25 points for problem 4.
    
    Inputs:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 60.
        feedback (str): a printout of test results for the student.
    """
    tester = _testDriver()
    tester.test_all(student_module)
    return tester.score, tester.feedback

# Test Driver
class _testDriver(object):
    """Class for testing a student's work. See test.__doc__ for more info.

    This particular test driver is designed to allow flexibility in the
    student's Backpack and Jetpack classes by never explicitly calling
    a particular attribute name. That is, instead of examining a Backpack's
    'max_size' attribute (which the student may or may not have called
    'max_size'), the Backpack's put() method is called to ensure that the
    contents list has not grown past the limit. The only exception is that
    'contents' is specifically referred to, because it is explicitly named
    that way in the example code.
    """

    # Constructor -------------------------------------------------------------
    def __init__(self):
        """Initialize the feedback attribute."""
        self.feedback = ""

    # Main routine ------------------------------------------------------------
    def test_all(self, student_module, total=60):
        """Grade the provided module on each problem and compile feedback."""
        self.feedback = ""
        self.score = 0

        def test_one(problem, number, total):
            try:
                self.feedback += "\n\nProblem %d (%d points):"%(number, total)
                points = problem(student_module)
                self.score += points
                self.feedback += "\nScore += %d"%points
            except BaseException as e:
                self.feedback += "\n%s: %s"%(self._errType(e),e)

        test_one(self.problem1, 1, 10)  # Problem 1: 10 points.
        test_one(self.problem2, 2, 10)  # Problem 2: 10 points.
        test_one(self.problem3, 3, 15)  # Problem 3: 15 points.
        test_one(self.problem4, 4, 25)  # Problem 4: 25 points.

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
            self.feedback += "\n\n\nComments:\n\t%s"%comments

    # Helper Functions --------------------------------------------------------
    @staticmethod
    def _errType(error):
        """Get just the name of the exception 'error' in string format."""
        if isinstance(error, BaseException):
            return str(type(error)).lstrip("<type 'exceptions.").rstrip("'>")
        else:
            return str(error)

    def _eqTest(self, correct, student, message):
        """Test to see if 'correct' == 'student'."""
        if correct == student:
            return 1
        else:
            self.feedback += "\n%s"%message
            self.feedback += "\n\tCorrect response: %s"%correct
            self.feedback += "\n\tStudent response: %s"%student
            return 0

    def _evalTest(self, expression, correct, message):
        """Test a boolean to see if it is correct (for Backpack.__eq__())."""
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
        """Test the Backpack class. 10 points."""

        # Test the constructor.
        b1 = Backpack("Teacher", "silver")
        try:
            b2 = s.Backpack("Student", "green")
        except TypeError as e:
            raise NotImplementedError("Problem 1 Incomplete: %s"%e)
        points = 2

        # Test put() (no going over the limit).
        for item in ['this', 'is', 'a', 'test', '...']:
            b1.put(item); b2.put(item)
        points += self._eqTest(b1.contents, b2.contents,
            "Backpack.put() failed to update Backpack.contents correctly")
        print("\nTest that Backpack.put() doesn't go over the max_size.")
        print("Correct output:\t"),; b1.put('this should not fit')
        print("Student output:\t"),; b2.put('this should not fit')
        points += self._grade(1,
                        "'No Room!' failed to print (check Backpack.put())")
        points += self._eqTest(b1.contents, b2.contents,
            "Backpack.put() failed to update Backpack.contents correctly")
        b1.max_size = 1; b1.dump(); b2 = s.Backpack("Student", "green", 1)
        b1.put("Testing..."); b2.put("Testing...")
        print("\nTest that Backpack.put() doesn't go over the max_size.")
        print("Correct output:\t"),; b1.put('this should not fit')
        print("Student output:\t"),; b2.put('this should not fit')
        points += self._grade(1,
                        "'No Room!' failed to print (check Backpack.dump())")
        points += 2*self._eqTest(b1.contents, b2.contents,
            "Backpack.put() failed to update Backpack.contents correctly")

        # Test dump().
        b1.dump(); b2.dump()
        points += 2*self._eqTest(b1.contents, b2.contents,
                            "Backpack.dump() failed to empty contents")
        return points

    def problem2(self, s):
        """Test the Jetpack class. 10 Points."""
        if not hasattr(s, "Jetpack"):
            raise NotImplementedError("Problem 2 Incomplete")

        # Test the constructor.
        j1, j2 = Jetpack("Teacher", "silver"), s.Jetpack("Student", "green")
        points = 2

        # Test put() (no going over the limit).
        for item in ['Testing', 'testing']:
            j1.put(item); j2.put(item)
        points += self._eqTest(j1.contents, j2.contents,
                                            "Jetpack.put() failed.")
        print("\nTest that Jetpack.put() doesn't go over the max_size.")
        print("Correct output:\t"),; j1.put('this should not fit')
        print("Student output:\t"),; j2.put('this should not fit')
        points += self._grade(1,
                        "'No Room!' failed to print (check Jetpack.put()")
        points += self._eqTest(j1.contents, j2.contents,
            "Jetpack.put() failed to update Jetpack.contents correctly")
        j1.max_size = 1; j1.dump(); j2 = s.Jetpack("Student", "green", 1)
        j1.put("Testing..."); j2.put("Testing...")
        print("\nTest that Jetpack.put() doesn't go over the max_size.")
        print("Correct output:\t"),; j1.put('this should not fit')
        print("Student output:\t"),; j2.put('this should not fit')
        points += self._grade(1,
                        "'No Room!' failed to print (check Jetpack.put())")
        points += self._eqTest(j1.contents, j2.contents,
            "Jetpack.put() failed to update Jetpack.contents correctly")

        # Test fly().
        print("\nTest that fly(amount) doesn't work if amount > fuel.")
        print("Correct output:\t"),; j1.fly(11)
        print("Student output:\t"),; j2.fly(11)
        points += self._grade(1,
                "'Not Enough Fuel!' failed to print (check Jetpack.fly())")
        
        # Test dump().
        j1.dump(); j2.dump()
        print("\nTest that Jetpack.dump() sets the fuel to zero.")
        print("Correct output:\t"),; j1.fly(1)
        print("Student output:\t"),; j2.fly(1)
        points += 2*self._grade(1,
                "'Not Enough Fuel!' failed to print (check Jetpack.dump())")

        if not issubclass(s.Jetpack, s.Backpack):
            self.feedback += "The Jetpack class must inherit from the "
            self.feedback += "Backpack class!"
            points = 0

        return points

    def problem3(self, s):
        """Test the Backpack class's magic methods. 15 points."""
        
        # Test Backpack.__eq__() in False case (4 points).
        try:
            b1 = s.Backpack("Name1", "Color", 10)
        except TypeError as e:
            raise NotImplementedError("Problem 3 Incomplete: %s"%e)
        b2 = s.Backpack("Name2", "Color", 10)
        points = self._evalTest(b1==b2, False,
                    "Backpack.__eq__() failed on different names")
        
        b1 = s.Backpack("Name", "Color1", 10)
        b2 = s.Backpack("Name", "Color2", 10)
        points += self._evalTest(b1==b2, False,
                    "Backpack.__eq__() failed on different colors")

        b1 = s.Backpack("Name", "Color", 10)
        b2 = s.Backpack("Name", "Color", 10)
        for item in [1, 2, 3]:
            b1.put(item); b2.put(item)
        b2.put(4)
        points += self._evalTest(b1==b2, False,
                    "Backpack.__eq__() failed on different contents")
        b1.put(5)
        points += self._evalTest(b1==b2, False,
                    "Backpack.__eq__() failed on different contents")

        # Test Backpack.__eq__() in True case (3 points).
        b1 = s.Backpack("Name", "Color", 100)
        b2 = s.Backpack("Name", "Color", 10)
        points += self._evalTest(b1==b2, True,
                    "Backpack.__eq__() failed on equal objects.")
        
        for item in ["apple", "banana", "carrot"]:
            b1.put(item); b2.put(item)
        points += self._evalTest(b1==b2, True,
                    "Backpack.__eq__() failed on equal objects.")

        b1.put("mango"); b1.put("salsa"); b2.put("salsa"); b2.put("mango")
        points += self._evalTest(b1==b2, True,
                    "Backpack.__eq__() failed on equal objects.")
        if not b1==b2:
            self.feedback += "(Hint: Backpack1.contents: %s"%b1.contents
            self.feedback += "Backpack2.contents: %s)"%b2.contents
        
        # Test Backpack.__str__() on an empty Backpack (4 points).
        b1 =   Backpack("Student", "green", 4)
        b2 = s.Backpack("Student", "green", 4)
        print("\nTest Backpack.__str__() on a Backpack with no contents.")
        print("\nCorrect output:"); print(b1)
        print("\nStudent output:"); print(b2)
        points += self._grade(4, "Incorrect Backpack.__str__():\n\n%s\n\n"%b2)
        
        # Test Backpack.__str__() on a Backpack with contents (4 points).
        b1 =   Backpack("Master Yoda", "tan", 7)
        b2 = s.Backpack("Master Yoda", "tan", 7)
        for item in ["Crystal", "Lightsaber", "Commlink", "Banana"]:
            b1.put(item); b2.put(item)
        print("\nTest Backpack.__str__() on a Backpack with some contents.")
        print("\nCorrect output:"); print(b1)
        print("\nStudent output:"); print(b2)
        points += self._grade(4, "Incorrect Backpack.__str__():\n\n%s\n\n"%b2)

        return points

    def problem4(self, s):
        """Test the ComplexNumber class. 25 points."""
        if not hasattr(s, "ComplexNumber"):
            raise NotImplementedError("Problem 4 Incomplete")

        # Test the constructor (2 points).
        a, b = randint(-50, 50, 2)
        cn = s.ComplexNumber(a, b)
        if not hasattr(cn, "real") or not hasattr(cn, "imag"):
            self.feedback += "ComplexNumber class must have attributes "
            self.feedback += "'real' and 'imag'!"
            return 0
        points  = self._eqTest(a, cn.real, "ComplexNumber.real failed")
        points += self._eqTest(b, cn.imag, "ComplexNumber.imag failed")

        # Check for cheating.
        if s.ComplexNumber is complex:
            print("Check solutions file; ComplexNumber is complex.")
            return 0

        # Test ComplexNumber.conjugate() (2 points).
        cn2 = cn.conjugate()
        if not isinstance(cn2, s.ComplexNumber):
            self.feedback += "ComplexNumber.conjugate() should return a "
            self.feedback += "new ComplexNumber object."
        else:
            points += self._eqTest(a, cn2.real,
                        "ComplexNumber.conjugate() failed on real part")
            points += self._eqTest(-1*b, cn2.imag,
                        "ComplexNumber.conjugate() failed on imag part")

        # Test ComplexNumber.__abs__() (1 point).
        a, b = randint(-50, 50, 2)
        cn = s.ComplexNumber(a, b)
        points += self._evalTest(abs(sqrt(a**2 + b**2) - abs(cn)) < 1e-8,
                                True, "ComplexNumber.__abs__() failed")

        # Test ComplexNumber.__lt__() (2 points).
        cn1, cn2 = s.ComplexNumber(5, 7), s.ComplexNumber(1, 2)
        points += self._evalTest(cn1 < cn2, False,
                                "ComplexNumber.__lt__() failed")
        points += self._evalTest(cn2 < cn1, True,
                                "ComplexNumber.__lt__() failed")

        # Test ComplexNumber.__gt__() (2 points).
        cn1, cn2 = s.ComplexNumber(1, 2), s.ComplexNumber(3, 4)
        points += self._evalTest(cn1 > cn2, False,
                                "ComplexNumber.__gt__() failed")
        points += self._evalTest(cn2 > cn1, True,
                                "ComplexNumber.__gt__() failed")

        # Test ComplexNumber.__eq__() (2 points).
        cn1, cn2 = s.ComplexNumber(2, 3), s.ComplexNumber(2, 4)
        points += self._evalTest(cn1 == cn2, False,
                        "ComplexNumber.__eq__() failed on nonequal")
        cn1, cn2 = s.ComplexNumber(2, 3), s.ComplexNumber(2, 3)
        points += self._evalTest(cn2 == cn1, True,
                        "ComplexNumber.__eq__() failed on equal")

        # Test ComplexNumber.__ne__() (2 points).
        cn1, cn2 = s.ComplexNumber(2, 3), s.ComplexNumber(2, 4)
        points += self._evalTest(cn1 != cn2, True,
                        "ComplexNumber.__ne__() failed on nonequal")
        cn1, cn2 = s.ComplexNumber(2, 3), s.ComplexNumber(2, 3)
        points += self._evalTest(cn2 != cn1, False,
                        "ComplexNumber.__ne__() failed on equal")

        # Test ComplexNumber.__add__() (2 points).
        a, b, c, d = randint(-50, 50, 4)
        cn = s.ComplexNumber(a, b) + s.ComplexNumber(c, d)
        points += self._eqTest(a+c, cn.real,
                    "ComplexNumber.__add__() failed on real part")
        points += self._eqTest(b+d, cn.imag,
                    "ComplexNumber.__add__() failed on imag part")

        # Test ComplexNumber.__sub__() (2 points).
        a, b, c, d = randint(-50, 50, 4)
        cn = s.ComplexNumber(a, b) - s.ComplexNumber(c, d)
        points += self._eqTest(a-c, cn.real,
                    "ComplexNumber.__sub__() failed on real part")
        points += self._eqTest(b-d, cn.imag,
                    "ComplexNumber.__sub__() failed on real part")

        # Test ComplexNumber.__mul__() (4 points).
        a, b, c, d = randint(-50, 50, 4)
        cn1 =   ComplexNumber(a, b) *   ComplexNumber(c, d)
        cn2 = s.ComplexNumber(a, b) * s.ComplexNumber(c, d)
        points += 2*self._eqTest(cn1.real, cn2.real,
                    "ComplexNumber.__mul__() failed on real part")
        points += 2*self._eqTest(cn1.imag, cn2.imag,
                    "ComplexNumber.__mul__() failed on imag part")
        
        # Test ComplexNumber.__div__() (4 points).
        a, b, c, d = randint(-50, 50, 4)
        cn1 =   ComplexNumber(a, b) /   ComplexNumber(c, d)
        cn2 = s.ComplexNumber(a, b) / s.ComplexNumber(c, d)
        points += 2*self._eqTest(cn1.real, cn2.real,
                    "ComplexNumber.__div__() failed on real part")
        points += 2*self._eqTest(cn1.imag, cn2.imag,
                    "ComplexNumber.__div__() failed on imag part")

        return points

# =============================== END OF FILE =============================== #
