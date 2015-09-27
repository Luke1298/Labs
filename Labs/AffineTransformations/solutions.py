import numpy as np
from scipy import linalg as la
from matplotlib import pyplot as plt
import time

def plot_transform(original, new):
    '''Inputs:
    original -- a (2,n) numpy array containing x-coordinates on the first 
                row and y-coordinates on the second row.
    new -- a (2,n) numpy array containing x-coordinates on the first row 
           and y-coordinates on the second row.
    '''
    v = [-5,5,-5,5]
    plt.subplot(1, 2, 1)
    plt.title('Before')
    plt.gca().set_aspect('equal')
    plt.scatter(original[0], original[1])
    plt.axis(v)
    plt.subplot(1, 2, 2)
    plt.title('After')
    plt.gca().set_aspect('equal')
    plt.scatter(new[0], new[1])
    plt.axis(v)
    plt.show()

def dilation2D(array, x_factor, y_factor):
    T = np.array([[x_factor,0],[0,y_factor]])
    return T.dot(array)
    
def rotate2D(array, theta):
    T = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return T.dot(array)
    
def translate2D(array, b):
    b = np.vstack([b[0],b[1]])
    return array + b
        
def rotatingParticle(time,omega,direction,speed):
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
        
def type_I(A, i, j):  
    '''Swap two rows.'''
    A[i], A[j] = np.copy(A[j]), np.copy(A[i])
    
def type_II(A, i, const):  
    '''Multiply row i of A by const.'''
    A[i] *= const
    
def type_III(A, i, j, const):  
    '''Add a constant time row j to row i.'''
    A[i] += const*A[j]
    
def REF(A):
    A1 = np.copy(A)
    
    step = 1
    for j in xrange(1,len(A1[0])):
        step = j
        for i in xrange(len(A1)-step):
            A1[i+step,step-1:] -= (A1[i+step,step-1]/A1[step-1,step-1]) * A1[step-1,step-1:]
    return A1
    
def LU(A):
    U = np.copy(A)
    L = np.identity(np.sqrt(A.size))
    
    for i in xrange(1,A.shape[0]):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] -= L[i,j]*U[j,j:]
    return U, L

def time_LU():
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
    
    print "LU factor: " + str(time_lu_factor)
    print "Inv: " + str(time_inv)
    print "LU solve: " + str(time_lu_solve)
    print "Inv solve: " + str(time_inv_solve)
