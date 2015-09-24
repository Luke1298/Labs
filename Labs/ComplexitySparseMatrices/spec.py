import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
from scipy import sparse
from scipy.sparse import linalg as sl

# Run through a single for loop.
def func1(n):
    n = 500*n
    sum(xrange(n))

# Run through a double for loop.
def func2(n):
    n = 3*n
    t = 0
    for i in xrange(n):
        for j in xrange(i):
            t += j

# Square a matrix.
def func3(n):
    n = int(1.2*n)
    A = np.random.rand(n, n)
    np.power(A, 2)

# Invert a matrix.
from scipy import linalg as la
def func4(n):
    A = np.random.rand(n, n)
    la.inv(A)

# Find the determinant of a matrix.
from scipy import linalg as la
def func5(n):
    n = int(1.25*n)
    A = np.random.rand(n, n)
    la.det(A)


def Problem1():
    """Create a plot comparing the times of func1, func2, func3, func4, 
    and func5. Time each function 4 times and take the average of each.
    """
    pass

def Problem2(n):
    """takes an integer argument n and returns a sparse n × n 
    tri-diagonal array with 2's along the diagonal and −1's along
    the two sub-diagonals above and below the diagonal.
    """
    pass

def Problem3(n):
    """Generate an nx1 random array b and solve the linear system Ax=b
    where A is the tri-diagonal array in Problem 2 of size nxn
    """

def Problem4(n):
    """Write a function that accepts an integer argument n and returns
    (lamba)*n^2 where (lamba) is the smallest eigenvalue of the sparse 
    tri-diagonal array you built in Problem 2.
    """
    pass

