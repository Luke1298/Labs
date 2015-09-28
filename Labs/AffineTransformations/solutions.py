# solutions.py
"""Volume I Lab 5: Invertible Affine Transformations and Linear Systems.
Name: Tanner Christensen
Date: Fall 2015
"""

import numpy as np
import time
from matplotlib import pyplot as plt
from scipy import linalg as la

# Helper Functions
def plot_transform(original, new):
    """Display a plot of points before and after a transform.
    
    Inputs:
        original (array) - Array of size (2,n) containing points in R2 as columns.
        new (array) - Array of size (2,n) containing points in R2 as columns.
    """
    window = [-5,5,-5,5]
    plt.subplot(1, 2, 1)
    plt.title('Before')
    plt.gca().set_aspect('equal')
    plt.scatter(original[0], original[1])
    plt.axis(window)
    plt.subplot(1, 2, 2)
    plt.title('After')
    plt.gca().set_aspect('equal')
    plt.scatter(new[0], new[1])
    plt.axis(window)
    plt.show()

def type_I(A, i, j):  
    """Swap the i-th and j-th rows."""
    A[i], A[j] = np.copy(A[j]), np.copy(A[i])
    
def type_II(A, i, const):  
    """Multiply the i-th row of A by const."""
    A[i] *= const
    
def type_III(A, i, j, const):  
    """Add a constant of the j-th to the i-th row."""
    A[i] += const*A[j]


# Problem 1
def dilation2D(A, x_factor, y_factor):
    """Scale the points in A by x_factor in the x direction and y_factor in
    the y direction.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        x_factor (float) - scaling factor in the x direction.
        y_factor (float) - scaling factor in the y direction.
    """
    T = np.array([[x_factor,0],[0,y_factor]])
    return T.dot(A)
    
# Problem 2
def rotate2D(A, theta):
    """Rotate the points in A about the origin by theta radians.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        theta (float) - number of radians to rotate points in A.
    """
    T = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return T.dot(A)
    
# Problem 3
def translate2D(A, b):
    """Translate the points in A by the vector b.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        b (2-tuple (b1,b2)) - Translate points by b1 in the x direction and by b2 
            in the y direction.
    """
    b = np.vstack([b[0],b[1]])
    return A + b
   
# Problem 4
def rotatingParticle(time, omega, direction, speed):
    """Display a plot of the path of a particle P1 that is rotating 
    around another particle P2.
    
    Inputs:
     - time (2-tuple (a,b)): Time span from a to b seconds.
     - omega (float): Angular velocity of P1 rotating around P2.
     - direction (2-tuple (x,y)): Vector indicating direction.
     - speed (float): Distance per second.
    """
    direction = np.array(direction)
    T = np.linspace(time[0],time[1],100)
    start_P1 = [1,0]
    posP1_x = []
    posP1_y = []
    
    for t in T:
        posP2 = speed*t*direction/la.norm(direction)
        posP1 = translate2D(rotate2D(start_P1, t*omega), posP2)[0]
        posP1_x.append(posP1[0])
        posP1_y.append(posP1[1])
        
    plt.plot(posP1_x, posP1_y)
    plt.gca().set_aspect('equal')
    plt.show()
    
# Problem 5
def REF(A):
    """Reduce a square matrix A to REF. During a row operation, do not
    modify any entries that you know will be zero before and after the
    operation."""
    
    A1 = np.copy(A)
    
    step = 1
    for j in xrange(1,len(A1[0])):
        step = j
        for i in xrange(len(A1)-step):
            A1[i+step,step-1:] -= (A1[i+step,step-1]/A1[step-1,step-1]) * A1[step-1,step-1:]
    return A1
    
# Problem 6
def LU(A):
    """Returns the LU decomposition of a square matrix."""
    U = np.copy(A)
    L = np.identity(np.sqrt(A.size))
    
    for i in xrange(1,A.shape[0]):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] -= L[i,j]*U[j,j:]
    return L,U

# Problem 7
def time_LU():
    """Print the times it takes to solve a system of equations using
    LU decomposition and (A^-1)B where A is 1000x1000 and B is 1000x500."""
    
    A = np.random.random((1000,1000))
    B = np.random.random((1000,500))
    
    before = time.time()
    LU = la.lu_factor(A)
    time_lu_factor = time.time() - before
    
    before = time.time()
    A_inv = la.inv(A)
    time_inv = time.time() - before
    
    before = time.time()
    a = la.lu_solve(LU,B)
    time_lu_solve = time.time() - before
    
    before = time.time()
    b = A_inv.dot(B)
    time_inv_solve = time.time() - before

    print "LU solve: " + str(time_lu_factor + time_lu_solve)
    print "Inv solve: " + str(time_inv + time_inv_solve)
    
    # What can you conclude about the more efficient way to solve linear systems?
    print "For matrices of this size, LU decomposition is measureably faster."
