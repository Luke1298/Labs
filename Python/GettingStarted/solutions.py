# GettingStarted_solutions.py
"""Volume I Lab 1: Getting Started
Written Summer 2015 (Tanner Christensen)
"""

# The student's file should be called solutions.py

# Problem 1: Write and run a "Hello World" script.
# There is nothing to grade for this problem.


# Problem 2: Implement this function.
def sphere_volume(r):
    """Return the volume of the sphere of radius 'r'."""
    return (4 * 3.14159 / 3)*r**3


# Problem 3: Implement the first_half() and reverse() functions.
def first_half(my_string):
    """Return the first half of the string 'my_string'.

    Example:
        >>> first_half("python")
        'pyt'
    """
    return my_string[:len(my_string)/2]
    
def reverse(my_string):
    """Return the reverse of the string 'my_string'.
    
    Example:
        >>> reverse("python")
        'nohtyp'
    """
    return my_string[::-1]

    
# Problem 4: Perform list operations
my_list =  ["ant","baboon","cat","dog"] 
my_list.append("elephant")
my_list.remove("ant")
my_list.remove(my_list[1])
my_list[2] = "donkey"
my_list.append("fox")
# Resulting list should be ['baboon', 'donkey', 'elephant', 'fox']
    

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
    """Use a dictionary to translate a list of numbers 1-26 to corresponding
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
        ...     print(i)
        ... 
        0
        1
        4
        9
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

ln2 = None # put your approximation for ln(2) here


# ============================= END OF SOLUTIONS ============================ #


# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
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
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 55.
        feedback (str): a printout of results for the student.
    """

    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\t\tCorrect response: " + str(x)
            m += "\n\t\tStudent response: " + str(y)
            return 0, m

    s = student_module
    score = 0
    total = 55
    feedback = s.__doc__
    
    try:    # Problem 1: 5 points
        feedback += "\n\nProblem 1 (5 points):"
        points = 5
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 5 points
        feedback += "\n\nProblem 2 (5 points):"
        points = 0
        p,f = strTest(sphere_volume(5), s.sphere_volume(5),
                                            "\n\tsphere_volume(5) failed")
        points += (p * 2); feedback += f
        p,f = strTest(sphere_volume(3.14), s.sphere_volume(3.14),
                                            "\n\tsphere_volume(3.14) failed")
        points += (p * 3); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        p,f = strTest(first_half("abcde"), s.first_half("abcde"),
                                            "\n\tfirst_half('abcde') failed")
        points += (p * 2); feedback += f
        p,f = strTest(first_half("TK421"), s.first_half("TK421"),
                                            "\n\tfirst_half('TK421') failed")
        points += (p * 3); feedback += f
        p,f = strTest(reverse("abcde"), s.reverse("abcde"),
                                            "\n\tfirst_half('abcde') failed")
        points += (p * 2); feedback += f
        p,f = strTest(reverse("TK421"), s.reverse("TK421"),
                                            "\n\tfirst_half('TK421') failed")
        points += (p * 3); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 5 points
        feedback += "\n\nProblem 4 (5 points):"
        points = 0
        p,f = strTest(my_list, s.my_list, "\n\t'my_list' incorrect")
        points += (p * 5); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 5: 5 points
        feedback += "\n\nProblem 5 (5 points):"
        points = 0
        p,f = strTest(pig_latin("college"), s.pig_latin("college"),
                                    "\n\tpig_latin('college') failed")
        points += (p * 2); feedback += f
        p,f = strTest(pig_latin("university"), s.pig_latin("university"),
                                    "\n\tpig_latin('university') failed")
        points += (p * 3); feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 6: 5 points
        feedback += "\n\nProblem 6 (5 points):"
        points = 0
        p,f = strTest(int_to_string([1, 2, 3]), s.int_to_string([1, 2, 3]),
                                    "\n\tint_to_string([1, 2, 3]) failed")
        points += (p * 2); feedback += f
        p,f = strTest(int_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]),
                    s.int_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]),
            "\n\tint_to_string([24, 25, 12, 15, 16, 8, 15, 14, 5]) failed")
        points += (p * 3); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 7: 5 points
        feedback += "\n\nTesting problem 4 (5 points):"
        points = 0
        
        solution_list = []
        for i in squares(50):
            solution_list.append(i)

        student_list = []
        for i in s.squares(50):
            student_list.append(i)

        p,f = strTest(solution_list, student_list,
                                            "\n\tsquares(50) failed")
        points += (p * 5); feedback += f


        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 8: 5 points
        feedback += "\n\nProblem 8 (5 points):"
        points = 0
        
        p,f = strTest(stringify([1, 2, 3]), s.stringify([1, 2, 3]),
                                    "\n\tstringify([1, 2, 3]) failed")
        points += (p * 2); feedback += f
        p,f = strTest(stringify([1.632, 2, 3.7141]), 
            s.stringify([1.632, 2, 3.7141]), "\n\tstringify([1, 2, 3]) failed")
        points += (p * 3); feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 9: 10 points
        feedback += "\n\nTesting problem 9 (10 points):"
        points = 0
        
        p,f = strTest(alt_harmonic(100), s.alt_harmonic(100),
                                            "\n\talt_harmonic(100) failed")
        points += (p * 4); feedback += f
        p,f = strTest(alt_harmonic(5000), s.alt_harmonic(5000),
                                            "\n\talt_harmonic(5000) failed")
        points += (p * 6); feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    if late:    # Late submission penalty
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
        