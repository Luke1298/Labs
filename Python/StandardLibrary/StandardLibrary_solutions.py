# StandardLibrary_solutions.py
"""Volume II Lab 1: The Standard Library
Solutions file. Written by Shane McQuarrie, Summer 2015.
"""

# import calculator # as c
import sys
import time
# import matrix_multiply # as m

# In many labs, students will submit multiple files.
# Every solutions file contains all of the code that students will write,
# separated by file.


# ============================== calculator.py ============================== #
# Students write this module as part of problem 3. Do not provide to students.

import math

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def sqrt(x):
    return math.sqrt(x)

# Or "sqrt = math.sqrt"

# =========================== matrix_multiply.py ============================ #
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


# ============================== Solutions.py =============================== #
# The students are provided a specifications file called 'spec.py' with the
# following functions. They are to rename the file 'solutions.py'.

# Problem 1: Implement this function.
def prob1(l):
    """Accept a list 'l' of numbers as input and return a list with the minimum,
    maximum, and average of the original list.
    """
    ans = []
    ans.append(min(l))
    ans.append(max(l))
    ans.append(float(sum(l))/len(l))
    return ans


# Problem 2: Implement this function.
def prob2():
    """Determine which Python objects are mutable and which are immutable. Test
    numbers, strings, lists, tuples, and dictionaries.
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


# Problem 3: Create a 'calculator' module and use it to implement this function.
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
        print("No input")
    elif sys.argv[1] != "matrices.npz":
        print("Incorrect Input")
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


# Everything under this 'if' statement is executed when this file is run from
#   the terminal. In this case, if we enter 'python solutions.py word' into
#   the terminal, then sys.argv is ['solutions.py', 'word'], and prob4() is
#   executed. Note that the arguments are parsed as strings. Do not modify.
if __name__ == "__main__":
    prob4()

# ============================ END OF SOLUTIONS ============================= #

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
    3 points for problem 1
    5 points for problem 2
    5 points for problem 3
    7 points for problem 4
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 20
        feedback (str): a printout of test results for the student.
    """

    s = student_module
    sFile = s.__file__    
    import os
    if os.system('ls ' + sFile):
        return

    score = 0
    total = 20
    feedback = s.__doc__
    
    try:    # Problem 1: 3 points
        feedback += "\n\nTesting problem 1 (3 points):"
        points = 0
        l = [192102312,-234892,9423,1220002,82,3432,23892,100000,-123812]
        [min1,max1,ave1] =   prob1(l)
        [min2,max2,ave2] = s.prob1(l)
        if max1 == max2: points += 1
        else: feedback += "\n\tincorrect maximum"
        if min1 == min2: points += 1
        else: feedback += "\n\tincorrect minimum"
        if ave1 == ave2: points += 1
        else: feedback += "\n\tincorrect average"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 2: 5 points
        feedback += "\n\nTesting problem 2 (5 points):"
        print"\nCorrect output:";   prob2()
        print"\nStudent output:"; s.prob2()
        points = -1
        while points > 5 or points < 0:
            points = int(input("\nScore out of 5: "))
        if points < 5:
            feedback += "\n\t" + str(5 - points) + " incorrect response(s)"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 5 points
        feedback += "\n\nTesting problem 3 (5 points):"
        points = 0
        if s.prob3(5,12) == prob3(5,12): points += 1
        else: feedback += "\n\tincorrect hypotenuse length"
        if s.prob3(6,7) == prob3(6,7): points += 2
        else: feedback += "\n\tincorrect hypotenuse length"
        c = s.calculator
        if prob3(2,7) == c.sqrt(c.add(c.mult(2,2),c.mult(7,7))): points += 2
        else: feedback += "\n\t'calculator' module operations failed"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 7 points
        feedback += "\n\nTesting problem 4 (7 points):"
        print("\nCorrect output:")
        os.system("python " + __file__)
        os.system("python " + __file__ + " Wrong Name")
        os.system("python " + __file__ + " matrices.npz")
        print("\nStudent output:")
        os.system('python ' + sFile)
        os.system('python ' + sFile + ' "Wrong Name"')
        os.system('python ' + sFile + ' "matrices.npz"')
        points = -1
        while points > 7 or points < 0:
            points = int(input("\nScore out of 7: "))
        if points < 7: feedback += "\n\tincorrect outputs"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >= 100.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback

# ============================== END OF FILE ================================ #
