#solutions.py
"""Volume 1 Lab 2: NumPy and SciPy
Written Summer 2015 (Tanner Christensen)
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# student's file should be called solutions.py

# Problem 1: Perform matrix multiplication

A = np.array([[2,4,0],[-3,1,-1],[0,3,2]])
B = np.array([[3,-1,2],[-2,-3,0],[1,0,-2]])
product = A.dot(B)


# Problem 2: Return an array with all nonnegative numbers

def nonnegative(my_array):
    """Changes all negative entries in the inputed array to 0.

    Example:
    >>> my_array = np.array([-3,-1,3])
    >>> nonnegative(my_array)
    array([0,0,3])
    """
    
    my_array[my_array<0] = 0
    return my_array

# Problem 3: nxn array of floats and operations on that array

def normal_var(n):
    """Creates nxn array with values from the normal distribution, computes 
    the mean of each row and computes the variance of these means.
    """
    my_array = np.random.randn(n*n).reshape((n,n))
    return np.var(np.mean(my_array,axis=1))
   
# Problem 4: Solving Laplace's Equation using the Jacobi method and array slicing

def laplace(A, tolerance):
    """Solve Laplace's Equation using the Jacobi method and array slicing."""
    B = np.copy(A)
    difference = tolerance
    while difference >= tolerance:
        B[1:-1,1:-1] = (A[:-2,1:-1] + A[2:,1:-1] + A[1:-1,:-2] + A[1:-1,2:])/4.
        difference = np.max(np.abs(A-B))
        A[1:-1,1:-1] = B[1:-1,1:-1]
    return A   

def laplace_plot():    
    """Visualize your solution to Laplace equation"""
    n = 100
    tol = .0001
    U = np.ones ((n, n))
    U[:,0] = 100 # sets north boundary condition
    U[:,-1] = 100 # sets south boundary condition
    U[0] = 0 # sets west boundary condition
    U[-1] = 0 # sets east boundary condition
    # U has been changed in place (note that laplace is the name of
    # the function in this case).
    laplace(U, tol)
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface (X, Y, U, rstride=5)
    plt.show()

# Problem 5: Blue shift an RGB image

def blue_shift():
    """Create a 100x100x3 array and perform a blue shift"""
    my_array = np.random.random_integers(0,255,100*100*3).reshape((100,100,3))
    blue = np.copy(my_array)
    blue[:,:,:2] = 0.5*my_array[:,:,:2]   
    return my_array, blue 

def blue_shift_plot():
    """Visualize the original and the blue_shift image"""
    original, blue = blue_shift()
    original = 255 - original
    blue = 255 - blue
    plt.subplot(1,2,1)
    plt.imshow(original)
    plt.subplot(1,2,2)
    plt.imshow(blue)
    plt.show()
    
# ============== END OF SOLUTIONS ========================== #

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
     5 points for problem 1
     5 points for problem 2
    10 points for problem 3
    10 points for problem 4
    10 points for problem 5
    
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

    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p,""
        else: return part,m

    s = student_module
    score = 0
    total = 40
    feedback = s.__doc__
    
    try:    # Problem 1: 5 points
        feedback += "\n\nProblem 1 (5 points):"
        points = 0
        
        p,f = strTest(product, s.product, "Problem 1 failed")
        
        points += (p * 5); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 5 points
        feedback += "\n\nProblem 2 (5 points):"
        points = 0
        
        first = np.array([-3,-1,3])
        p,f  = strTest(nonnegative(first), s.nonnegative(first), 
                                       "np.array[-3,-1,3] failed")
        points += (p * 2); feedback += f
        
        second = np.array([-5,2,0,-144,12])
        p,f  = strTest(nonnegative(first), s.nonnegative(first), 
                                       "np.array[-5,2,0,-144,12] failed")
        points += (p * 3); feedback += f
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
        
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        
        print "Answers will not match, but should be relatively close"
        print "Correct: " + str(normal_var(100))
        print "Student: " + str(s.normal_var(100))
        print "-------"
        print "Correct: " + str(normal_var(1000))
        print "Student: " + str(s.normal_var(1000))
        
        p,f = grade(10, "Incorrect answer")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    
    try:    # Problem 4: 10 points
        feedback += "\n\nProblem 5 (10 points):"
        points = 0
        
        s.laplace_plot()
        
        p,f = grade(10, "Incorrect answer")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message    
    
    
    try:    # Problem 5: 10 points
        feedback += "\n\nProblem 5 (10 points):"
        points = 0
        
        s.blue_shift_plot()
        
        p,f = grade(10, "Incorrect answer")
        points += p; feedback += f
        
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

