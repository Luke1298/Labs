# solutions.py
"""Volume I Lab 1: Getting Started
Written Summer 2015 (Tanner Christensen, Shane McQuarrie)
"""

# Problem 1: Modify this file so that it prints out "Hello, world!"
#  when it is run from the terminal or from a Python interpreter.


# Problem 2: Implement this function.
def sphere_volume(r):
    """Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return (4 * 3.14159 / 3)*r**3


# Problem 3: Implement the first_half() and reverse() functions.
def first_half(my_string):
    """Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[:len(my_string)//2]
    
def reverse(my_string):
    """Return the reverse of the string 'my_string'.
    
    Examples:
        >>> reverse("python")
        'nohtyp'
        >>> reverse("ipython")
        'nohtypi'
    """
    return my_string[::-1]


# Problem 4: Implement this function.
def list_ops(my_list):
    """Perform the following operations on the list 'my_list':
        - Append "elephant".
        - Remove "ant"
        - Remove the entry at index 1.
        - Replace the entry at index 2 with "eagle".
        - Append "fox".

    Examples:
        >>> list_ops(["ant", "bear", "cat", "dog"])
        ['bear', 'dog', 'eagle', 'fox']
    """
    my_list.append("elephant")
    my_list.remove("ant")
    my_list.remove(my_list[1])
    my_list[2] = "eagle"
    my_list.append("fox")
    return my_list


# Problem 5: Implement this function.
def pig_latin(word):
    """Translate the string 'word' into Pig Latin
    
    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
        

# Problem 6: Implement this function.
def int_to_string(my_list):
    """Translate 'my_list', a list of numbers 1-26, to corresponding
    lowercase letters of the alphabet. 1 -> a, 2 -> b, 3 -> c, and so on.
    
    Example:
        >>> int_to_string([13, 1, 20, 8])
        ['m', 'a', 't', 'h'] 
    """
    my_dictionary = {1:'a',  2:'b',  3:'c',  4:'d',  5:'e',  6:'f',  7:'g',
                     8:'h',  9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n',
                    15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u',
                    22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    output = []
    for number in my_list:
        output.append(my_dictionary[number])
    return output


# Problem 7: Implement this generator.
def squares(n):
    """Yield all squares less than 'n'.

    Example:
        >>> for i in squares(10):
        ...     print(i),
        ... 
        0 1 4 9
    """
    i = 0
    while i*i < n:
        yield i*i
        i += 1


# Problem 8: Implement this function.
def stringify(my_list):
    """Using a list comprehension, convert the list of integers 'my_list'
    to a list of strings. Return the new list.

    Example:
        >>> stringify([1, 2, 3])
        ['1', '2', '3']
    """
    return [str(n) for n in my_list]


# Problem 9: Implement this function and use it to approximate ln(2).
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximae ln(2).
    """
    return sum([(-1)**(i+1)/float(i) for i in xrange(1,n)])


# Problem 1
if __name__ == '__main__':
    print("Hello, world!")

# ============================= END OF SOLUTIONS ============================ #

from os import system
from numpy.random import randint

# Test script        
def test(student_module):
    """Test script. Import the students file as a module.
    
     5 points for problem 1
     5 points for problem 2
    10 points for problem 3
     5 points for problem 4
     5 points for problem 5
     5 points for problem 6
     5 points for problem 7
     5 points for problem 8
    10 points for problem 9
    
    Parameters:
        student_module: the imported module for the student's file.
    
    Returns:
        score (int): the student's score, out of 55.
        feedback (str): a printout of results for the student.
    """
    tester = _testDriver()
    tester.test_all(student_module)
    return tester.score, tester.feedback

class _testDriver(object):
    """Class for testing a student's work. See test.__doc__ for more info."""

    # Constructor
    def __init__(self):
        self.feedback = ""

    # Main routine
    def test_all(self, student_module):
        self.feedback = ""
        score = 0

        try:    # Problem 1: 5 points
            self.feedback += "\n\nProblem 1 (5 points):"
            points = self.problem1(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message
        
        try:    # Problem 2: 5 points
            self.feedback += "\n\nProblem 2 (5 points):"
            points = self.problem2(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 3: 10 points
            self.feedback += "\n\nProblem 3 (10 points):"
            points = self.problem3(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 4: 5 points
            self.feedback += "\n\nProblem 4 (5 points):"
            points = self.problem4(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 5: 5 points
            self.feedback += "\n\nProblem 5 (5 points):"
            points = self.problem5(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 6: 5 points
            self.feedback += "\n\nProblem 6 (5 points):"
            points = self.problem6(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 7: 5 points
            self.feedback += "\n\nProblem 7 (5 points):"
            points = self.problem7(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 8: 5 points
            self.feedback += "\n\nProblem 8 (5 points):"
            points = self.problem8(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        try:    # Problem 9: 5 points
            self.feedback += "\n\nProblem 9 (10 points):"
            points = self.problem9(student_module)
            score += points
            self.feedback += "\nScore += " + str(points)
        except BaseException as e:
            self.feedback += "\nError: " + e.message

        # Report final score.
        total = 55
        percentage = (100.0 * score) / total
        self.feedback += "\n\nTotal score: " + str(score) + "/"
        self.feedback += str(total) + " = " + str(percentage) + "%"
        if   percentage >=  98.0: self.feedback += "\n\nExcellent!"
        elif percentage >=  90.0: self.feedback += "\n\nGreat job!"

        # Add comments (optionally).
        print self.feedback
        comments = str(raw_input("Comments: "))
        if len(comments) > 0:
            self.feedback += '\n\n\nComments:\n\t' + comments
        self.score = score

    # Helper functions
    def strTest(self, correct, student, message):
        """Test to see if correct and student have the same
        string representation.
        """
        if str(correct) == str(student):
            return 1
        else:
            self.feedback += message
            self.feedback += "\nCorrect response:\n" + str(correct)
            self.feedback += "\nStudent response:\n" + str(student)
            return 0

    def grade(self, points, message):
        """Manually grade a problem out of 'points' with error message 'm'.
        The points earned are returned.
        """
        credit = -1
        while credit > points or credit < 0:
            try:
                credit = int(input("\nScore out of " + str(points) + ": "))
            except:
                credit = -1
        if credit != points:
            self.feedback += message
        return credit

    # Problems
    def problem1(self, s):
        """Test Hello, world! printout. 5 points."""

        system("python " + s.__file__)
        return self.grade(5, "\n\t'Hello, world!' failed to print.")

    def problem2(self, s):
        """Test sphere_volume(). 5 Points."""
        if s.sphere_volume(1) is None:
            raise NotImplementedError("Problem 2 incomplete.")
        points  = 2*self.strTest(sphere_volume(5), s.sphere_volume(5),
                                            "\n\tsphere_volume(5) failed")
        points += 3*self.strTest(sphere_volume(3.14), s.sphere_volume(3.14),
                                            "\n\tsphere_volume(3.14) failed")
        return points

    def problem3(self, s):
        """Test first_half() and reverse(). 10 points."""
        if s.first_half("abcde") is None:
            raise NotImplementedError("Problem 3 incomplete.")
        points  = 2*self.strTest(first_half("abcde"), s.first_half("abcde"),
                                            "\n\tfirst_half('abcde') failed")
        points += 3*self.strTest(first_half("TK421"), s.first_half("TK421"),
                                            "\n\tfirst_half('TK421') failed")
        points += 2*self.strTest(reverse("abcde"), s.reverse("abcde"),
                                            "\n\tfirst_half('abcde') failed")
        points += 3*self.strTest(reverse("TK421"), s.reverse("TK421"),
                                            "\n\tfirst_half('TK421') failed")
        return points

    def problem4(self, s):
        """Test list_ops(). 5 points."""
        if s.list_ops(["ant", "bear", "cat", "dog"]) is None:
            raise NotImplementedError("Problem 4 incomplete.")
        points = 2*self.strTest(  list_ops(["ant", "bear", "cat", "dog"]),
                                s.list_ops(["ant", "bear", "cat", "dog"]),
                        '\n\tlist_ops(["ant", "bear", "cat", "dog"]) failed')
        points +=3*self.strTest(list_ops(["ant", "beaver", "cobra", "dragon"]),
                            s.list_ops(["ant", "beaver", "cobra", "dragon"]),
                '\n\tlist_ops(["ant", "beaver", "cobra", "dragon"]) failed')
        return points

    def problem5(self, s):
        """Test pig_latin(). 5 points."""
        if s.pig_latin("piglatin") is None:
            raise NotImplementedError("Problem 5 incomplete.")
        points = 2*self.strTest(  pig_latin("college"),
                                s.pig_latin("college"),
                                            "\n\tpig_latin('college') failed")
        points += 3*self.strTest(  pig_latin("university"),
                                 s.pig_latin("university"),
                                        "\n\tpig_latin('university') failed")
        return points

    def problem6(self, s):
        """Test int_to_string(). 5 points.""" 
        if s.int_to_string([1]) is None:
            raise NotImplementedError("Problem 6 incomplete.")
        points = 2*self.strTest(int_to_string([1, 2, 3]),
                                s.int_to_string([1, 2, 3]),
                                    "\n\tint_to_string([1, 2, 3]) failed")
        points += 3*self.strTest(
                        int_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]),
                        s.int_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]),
            "\n\tint_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]) failed")
        return points
        
    def problem7(self, s):
        """Test squares() generator. 5 points."""
        correct = []
        for i in squares(50):
            correct.append(i)
        student = []
        for i in s.squares(50):
            if i is None:
                raise NotImplementedError("Problem 7 incomplete.")
            student.append(i)
        return 5*self.strTest(correct, student, "\n\tsquares(50) failed")

    def problem8(self, s):
        """Test stringify(). 5 points."""
        if s.stringify([1]) is None:
            raise NotImplementedError("Problem 8 incomplete.")
        points = 2*self.strTest(stringify([1, 2, 3]), s.stringify([1, 2, 3]),
                                            "\n\tstringify([1, 2, 3]) failed")

        rand_list = ['start'] + list(randint(1,10,10)) + ['end']
        points += 3*self.strTest(stringify(rand_list), s.stringify(rand_list),
                            "\n\tstringify(" + str(rand_list) + ") failed")
        return points

    def problem9(self, s):
        """Test alt_harmonic(). 10 points."""
        points = 4*self.strTest(alt_harmonic(100), s.alt_harmonic(100),
                                            "\n\talt_harmonic(100) failed")
        points += 6*self.strTest(alt_harmonic(5000), s.alt_harmonic(5000),
                                            "\n\talt_harmonic(5000) failed")
        return points
