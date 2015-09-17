from matplotlib import pyplot as plt
from mayavi import mlab
import numpy as np

# Problem 1
def curve():
    """Plot the curve 1/(x-1) on [-2,6]. Plot the two sides of the curve separately
    (still with a single call to plt.plot()) so that the graph looks discontinuous 
    at x = 1.
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
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on [-2*pi, 2*pi]x[-2*pi, 2*pi].
    Include the scale bar in your plot. 
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
    """Plot a histogram and a scatter plot of 50 random numbers chosen in the
    interval [0,1)
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
    
# ============= END OF SOLUTIONS =================== #
import inspect
import os

# Test script
def test(student_module, late=False):


    """Test script. You must import the students file as a module.
    
    10 points for problem 1
    10 points for problem 2
    10 points for problem 3
    10 points for problem 4
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 20
        feedback (str): a printout of test results for the student.
    """

    s = student_module
    sFile = s.__file__    
    if os.system('ls ' + sFile):
        return

    score = 0
    total = 40
    feedback = ""

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
    
    try:    # Problem 1: 10 points
        feedback += "\n\nProblem 1 (10 points):"
        points = 0

        # check that they only used 1 plot command.
        lines = inspect.getsourcelines(s.curve)[0]
        print "\nOnly use plt.plot() once. \nStudent Code:"
        for i in lines:
            print i[:-1]
        p,f = grade(5, "Only call plt.plot() once.")
        points += p; feedback += f
        
        # check the plot output.
        print """
        Specifications:
        - Discontinuous
        - think, magenta, dotted line
        - window should be [-2,6]x[-6,6]
        """
        plt.ion()   # turn on interactive plotting
        s.curve()
        p,f = grade(5, "Plot does not match specifications")
        points += p; feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 2: 10 points
        feedback += "\n\nProblem 2 (10 points):"
        points = 0
        
        plt.close('all')
        s.colormesh()
        print "\nOverall appearance."
        p,f = grade(8, "Plot does not match specifications")
        points += p; feedback += f
        print "\nNot pixelated."
        p,f = grade(2, "adjust plot so it is not pixelated.")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        
        plt.close('all')
        s.histogram()
        # histogram
        print "\nHistogram with 5 bins"
        p,f = grade(4, "Histogram does not match specifications")
        points += p; feedback += f
        
        # scatterplot
        print "\nScatter plot"
        p,f = grade(4, "Scatter plot does not match specifications.")
        points += p; feedback += f
        
        # average
        print "\nAverage"
        p,f = grade(2, "Average not displayed on scatter plot correctly.")
        points += p; feedback += f
        plt.close('all')
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 10 points
        feedback += "\n\nProblem 4 (10 points):"
        points = 0
        
        s.ripple()
        p,f = grade(10, "Ripple plot does not match specifications.")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    # Late submission penalty
    if late:
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >= 100.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    feedback += "\n\n-------------------------------------------------------\n"
    return score, feedback

# ============================== END OF FILE ================================ #

