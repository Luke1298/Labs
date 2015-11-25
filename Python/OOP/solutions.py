# solutions.py
"""Volume II Lab 2: Object Oriented Programming
Solutions file. Written by Shane McQuarrie, Spring 2015.
"""

from math import sqrt

# Problem 1: Modify this class. Add 'name' and max_size' attributes, modify
#   the put() method, and add a dump() method. Remember to update docstrings.
class Backpack(object):
    """Backpack object. Has a color, name, maximum size, and a list of contents
    
    Attributes:
        color (str): the color of the backpack.
        name (str): the name of the backpack.
        max_size (int): the maximum number of items that can fit in the
            backpack.
        contents (list): the contents of the backpack.
    """

    def __init__(self, color, name, max_size=5):
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
        self.color = color
        self.name = name
        self.max_size = max_size
        self.contents = []
    
    def put(self,item):
        """Add 'item' to the backpack's list of contents if there is room."""
        if len(self.contents) >= self.max_size:         # Check for overflow
            print("I'm Full!")
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
        return "Name:\t\t%s\nColor:\t\t%s\nSize:\t\t%d\nMax Size:\t%d\nContents:\t%s"%(self.name,
            self.color, len(self.contents), self.max_size, self.contents)
        # Or, a slightly longer way:
        out = "Name:\t\t" + self.name
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
        color (str): the color of the knapsack.
        name (str): the name of the knapsack.
        max_size (int): the maximum number of items that can fit
            in the knapsack.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    
    def __init__(self, color, name, max_size=3):
        """Use the Backpack constructor to initialize the name and
        max_size attributes. A knapsack only holds 3 item by default
        instead of 5. 
        
        Inputs:
            color (str): the color of the knapsack.
            name (str): the name of the knapsack.
            max_size (int, opt): the maximum number of items that can be
                stored in the knapsack. Defaults to 3.
        
        Returns:
            A knapsack object with no contents.
        """
        
        Backpack.__init__(self, color, name, max_size)
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
        = (a+bi)*(c-di) / (c+di)*(c-di)             # Multiply by conjugate
        = ((ac+bd) + (bc-ad)i) / (c**2 + d**2)      # Distribute
        """
        denom = float(other.real**2 + other.imag**2)
        real = ((self.real * other.real) + (self.imag * other.imag))/denom
        imag = ((self.imag * other.real) - (self.real * other.imag))/denom
        return ComplexNumber(real, imag)

# ============================ END OF SOLUTIONS ============================= #

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
    10 points for problem 1
    15 points for problem 2
    15 points for problem 3
    15 points for problem 4
    
    Inputs:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 55.
        feedback (str): a printout of the test results for the student.
    """
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part < p: return part,m
        else: return part,""
    
    def attrTest(x,y,m):
        """Test that 'x' and 'y' are equal with error message 'm'."""
        if x == y: return 1, ""
        else:
            message  = m
            message += "\n\t\tCorrect response: " + str(x)
            message += "\n\t\tStudent response: " + str(y)
            return 0, message
    
    s = student_module
    score = 0
    total = 55
    feedback = ""
    
    try:    # Problem 1: 10 points
        feedback += "\n\nProblem 1 (10 points):"
        points = 0
        # Test default name and max_size attributes
        b1 =   Backpack()
        b2 = s.Backpack()
        p,f = attrTest(b1.name, b2.name,
            "\n\tBackpack.name failed on default value")
        points += p; feedback += f
        p,f = attrTest(b1.max_size, b2.max_size,
            "\n\tBackpack.max_size failed on default value")
        points += p; feedback += f
        # Test non-default color, name, and max_size attributes
        b1 =   Backpack(color='teal',name='Francis', max_size=3)
        b2 = s.Backpack(color='teal',name='Francis', max_size=3)
        p,f = attrTest(b1.name, b2.name,
            "\n\tBackpack.name failed on nondefault value")
        points += p; feedback += f
        p,f = attrTest(b1.max_size, b2.max_size,
            "\n\tBackpack.max_size failed on nondefault value")
        points += p; feedback += f
        p,f = attrTest(b1.color, b2.color,
            "\n\tBackpack.color failed on nondefault value")
        points += p; feedback += f
        # Test put() (no going over the limit)
        b1.put('f'); b1.put('u'); b1.put('n')
        b2.put('f'); b2.put('u'); b2.put('n')
        print("Correct output:\t"),; b1.put('this should not fit')
        print("Student output:\t"),; b2.put('this should not fit')
        p,f = grade(1,"\n\tBackpack.put() failed to print 'Backpack Full!'")
        points += p; feedback += f
        p,f = attrTest(b1.contents, b2.contents,
            "\n\tBackpack.put() failed (Backpack.contents over max_size)")
        points += p; feedback += f
        # Test dump()
        b1.dump(); b2.dump()
        p,f = attrTest(b1.contents, b2.contents,
            "\n\tBackpack.dump() failed to empty contents")
        points += p; feedback += f
        # Test docstrings
        print("\nStudent Backpack class docstrings:\n")
        print(b2.__doc__); print(b2.__init__.__doc__)
        p,f = grade(2,"\n\tbad Backpack docstring(s)")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 2: 15 points
        feedback += "\n\nProblem 2 (15 points):"
        points = 0
        # Test default name, and max_size attributes
        b1 =   Jetpack()
        b2 = s.Jetpack()
        p,f = attrTest(b1.name, b2.name,
            "\n\tJetpack.name failed on default value")
        points += p; feedback += f
        p,f = attrTest(b1.max_size, b2.max_size,
            "\n\tJetpack.max_size failed on default value")
        points += p; feedback += f
        # Test non-default color, name, and max_size attributes
        b1 =   Jetpack(color='Gold',name='Golden Boy', max_size=3)
        b2 = s.Jetpack(color='Gold',name='Golden Boy', max_size=3)
        p,f = attrTest(b1.name, b2.name,
            "\n\tJetpack.name failed on nondefault value")
        points += p; feedback += f
        p,f = attrTest(b1.max_size, b2.max_size,
            "\n\tJetpack.max_size failed on nondefault value")
        points += p; feedback += f
        p,f = attrTest(b1.color, b2.color,
            "\n\tJetpack.color failed on nondefault value")
        points += p; feedback += f
        # Test fuel attribute
        p,f = attrTest(b1.fuel, b2.fuel,
            "\n\tJetpack.fuel failed on default value")
        points += p; feedback += f
        # Test put() (no going over the limit)
        b1.put('f'); b1.put('u'); b1.put('n')
        b2.put('f'); b2.put('u'); b2.put('n')
        print("\nCorrect output:\t"),; b1.put('this should not fit')
        print("Student output:\t"),; b2.put('this should not fit')
        p,f = grade(1,"\n\tBackpack.put() failed to print 'Backpack Full!'")
        points += p; feedback += f
        p,f = attrTest(b1.contents, b2.contents,
            "\n\tJetpack.put() failed (Jetpack.contents over max_size)")
        points += p; feedback += f
        # Test dump()
        b1.dump(); b2.dump()
        p,f = attrTest(b1.contents, b2.contents,
            "\n\tJetpack.dump() failed to empty contents")
        points += p; feedback += f
        # Test fly()
        b1.fuel = 10; b2.fuel = 10
        print("\nCorrect output:\t"),; b1.fly(20)
        print(  "Student output:\t"),; b2.fly(20)
        p,f = grade(1,"\n\tJetpack.put() failed to print 'Not enough fuel!'")
        points += p; feedback += f
        p,f = attrTest(b1.fuel, b2.fuel,
            "\n\tJetpack.fly() failed to decrease fuel correctly")
        points += p; feedback += f
        b1.fly(5); b2.fly(5)
        p,f = attrTest(b1.fuel, b2.fuel,
            "\n\tJetpack.fly() failed to decrease fuel correctly")
        points += (p*2); feedback += f        
        # Test docstrings
        print("\nStudent Jetpack class docstrings:\n")
        print(b2.__doc__); print(b2.__init__.__doc__)
        p,f = grade(2,"\n\tbad Jetpack docstring(s)")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 15 points
        points = 0
        feedback += "\n\nProblem 3 (15 points):"
        # Test __str__ on an empty, default backpack
        b1 =   Backpack()
        b2 = s.Backpack()
        print("\nCorrect output:"); print(b1)
        print("\nStudent output:"); print(b2)
        p,f = grade(3,"\n\tBackpack.__str__ failed")
        points += p; feedback += f
        if p < 3: feedback += "\n\tStudent str(Backpack):\n\n" + str(b2) + '\n'
        # Test __str__ on a partially full backpack
        b1 =   Backpack(color='Blue and White',name='ACME',max_size=7)
        b2 = s.Backpack(color='Blue and White',name='ACME',max_size=7)
        b1.put('thing1'); b1.put('thing2'); b1.put('thing3')
        b2.put('thing1'); b2.put('thing2'); b2.put('thing3')
        print("\nCorrect output:"); print(b1)
        print("\nStudent output:"); print(b2)
        p,f = grade(5,"\n\tBackpack.__str__ failed")
        points += p; feedback += f
        if p < 5: feedback += "\n\tStudent str(Backpack):\n\n" + str(b2) + '\n'
        # Test __eq__ in False case
        b1 = s.Backpack(color='Color',name='Name',max_size=5)
        b2 = s.Backpack(color='Color',name='Name',max_size=5)
        b1.name = 'FalseName'
        if b1 == b2:
            feedback += "\n\tBackpack.__eq__ failed on different names"
        else: points += 1
        b1.name = 'Name'; b1.color = 'Red'
        if b1 == b2:
            feedback += "\n\tBackpack.__eq__ failed on different colors"
        else: points += 1
        b1.color = 'Color'
        b1.put('an item'); b2.put("a different item")
        if b1 == b2:
            feedback += "\n\tBackpack.__eq__ failed on different contents"
            feedback += "\n\t\tBackpack_1.contents: " + str(b1.contents)
            feedback += "\n\t\tBackpack_2.contents: " + str(b2.contents)
        else: points += 1
        b1.put("yet another item")
        if b1 == b2:
            feedback += "\n\tBackpack.__eq__ failed on different contents"
            feedback += "\n\t\tBackpack_1.contents: " + str(b1.contents)
            feedback += "\n\t\tBackpack_2.contents: " + str(b2.contents)
        else: points += 1
        # Test __eq__ in True case
        b1 = s.Backpack(color='green',name='Math',max_size=3)
        b2 = s.Backpack(color='green',name='Math',max_size=3)
        if not (b1 == b2): feedback += "\n\tBackpack.__eq__ failed on equal"
        else: points += 1
        b1.put('an item'); b2.put('an item')
        if not (b1 == b2): feedback += "\n\tBackpack.__eq__ failed on equal"
        else: points += 1
        b1.put('A'); b1.put('B')
        b2.put('B'); b2.put('A')
        if not (b1 == b2):
            feedback += "\n\tBackpack.__eq__ failed on equal"
            feedback += "\n\t\tBackpack_1.contents: " + str(b1.contents)
            feedback += "\n\t\tBackpack_2.contents: " + str(b2.contents)
            feedback += "\n\t\t(two backpacks with the same contents"
            feedback += "\n\t\t are equal even if the contents are in"
            feedback += "\n\t\t a different order"
        else: points += 1
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 20 points
        feedback += "\n\nProblem 4 (15 points):"
        points = 0
        x1 =   ComplexNumber(3392,-493)
        y1 = s.ComplexNumber(3392,-493)
        # Test real / imag attributes
        p,f = attrTest(x1.real, y1.real, "\n\tComplexNumber.real failed")
        points += p; feedback += f
        p,f = attrTest(x1.imag, y1.imag, "\n\tComplexNumber.imag failed")
        points += p; feedback += f
        # Test conjugate()
        x2 = x1.conjugate(); y2 = y1.conjugate()
        p,f = attrTest(x2.real, y2.real,
            "\n\tComplexNumber.conjugate() failed on real part")
        points += p; feedback += f
        p,f = attrTest(x2.imag, y2.imag,
            "\n\tComplexNumber.conjugate() failed on imag part")
        points += p; feedback += f
        # Test norm()
        p,f = attrTest(x1.norm(), y1.norm(),
            "\n\tComplexNumber.norm() failed")
        points += p; feedback += f
        # Test __add__
        x2 = ComplexNumber(-21,210); y2 = ComplexNumber(-21,210)
        x3 = x1 + x2; y3 = y1 + y2
        p,f = attrTest(x3.real, y3.real,
            "\n\tComplexNumber.__add__ failed on real part")
        points += p; feedback += f
        p,f = attrTest(x3.imag, y3.imag,
            "\n\tComplexNumber.__add__ failed on imag part")
        points += p; feedback += f
        # Test __sub__
        x3 = x1 - x2; y3 = y1 - y2
        p,f = attrTest(x3.real, y3.real,
            "\n\tComplexNumber.__sub__ failed on real part")
        points += p; feedback += f
        p,f = attrTest(x3.imag, y3.imag,
            "\n\tComplexNumber.__sub__ failed on imag part")
        points += p; feedback += f
        # Test __mul__
        x3 = x1 * x2; y3 = y1 * y2
        p,f = attrTest(x3.real, y3.real,
            "\n\tComplexNumber.__mul__ failed on real part")
        points += p; feedback += f
        p,f = attrTest(x3.imag, y3.imag,
            "\n\tComplexNumber.__mul__ failed on imag part")
        points += p; feedback += f
        # Test __div__
        x3 = x1 / x2; y3 = y1 / y2
        p,f = attrTest(x3.real, y3.real,
            "\n\tComplexNumber.__div__ failed on real part")
        points += p; feedback += f
        p,f = attrTest(x3.imag, y3.imag,
            "\n\tComplexNumber.__div__ failed on imag part")
        points += p; feedback += f
        # Test docstrings
        print("\nStudent docstrings:\n")
        print(y1.__doc__); print(y1.__init__.__doc__)
        p,f = grade(2,"\n\tbad ComplexNumber docstring(s)")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    # Late submission penalty
    if late:
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback

# =============================== END OF FILE =============================== #
