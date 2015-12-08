# spec.py
"""Volume I Lab 6: QR Decomposition.
Name: Ben Ehlert
Date: 10/13/2015
"""

import numpy as np
from scipy import linalg as la

def QR(A):
    '''
    Compute the QR decomposition of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
    m,n = A.shape
    Q = np.copy(A)
    R = np.zeros((n,n))
    for i in range(0,n):
        R[i,i] = la.norm(Q[:,i])
        Q[:,i] = Q[:,i]/R[i,i]
        for j in range(i+1,n):
            R[i,j] = np.dot(Q[:,j].T,Q[:,i])
            Q[:,j] = Q[:,j] - R[i,j]*Q[:,i]
    return Q,R
    
def prob2(A):
    '''
    Use your QR decomposition from the previous problem to compute 
    the determinant of A.
    Accept a square matrix A of full rank.
    Return |det(A)|.
    '''
    Q,R = QR(A)
    output = 1
    for r in np.diagonal(R):
        output = output * r
    return output

def householder(A):
    '''
    Use the Householder algorithm to compute the QR decomposition
    of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
    m,n = A.shape
    R = np.copy(A)
    Q = np.identity(m)
    for k in range(0,n):
        uk = np.copy(R[k:,k]).reshape(m-k,1)
        uk[0] += np.sign(uk[0])*la.norm(uk)
        uk = uk/la.norm(uk)
        R[k:,k:] = R[k:,k:] - 2*np.dot(uk,np.dot(uk.T,R[k:,k:]))
        Q[k:] = Q[k:] - 2*np.dot(uk,np.dot(uk.T,Q[k:]))
    return Q.T,R

def hessenberg(A):
    '''
    Compute the Hessenberg form of a matrix. Find orthogonal Q and upper
    Hessenberg H such that A = QtHQ.
    Accept a non-singular square matrix A.
    Return Q, H
    '''
    m,n = A.shape
    H = np.copy(A)
    Q = np.identity(m)
    for k in range(0,n-2):
        uk = np.copy(H[k+1:,k]).reshape(m-1-k,1)
        uk[0] += np.sign(uk[0])*la.norm(uk)
        uk = uk/la.norm(uk)
        H[k+1:,k:] = H[k+1:,k:] - 2*np.dot(uk,np.dot(uk.T,H[k+1:,k:]))
        H[:,k+1:] = H[:,k+1:] - 2*np.dot(np.dot(H[:,k+1:],uk),uk.T)
        Q[k+1:] = Q[k+1:] - 2*np.dot(uk,np.dot(uk.T,Q[k+1:]))
    return Q,H

def givens(A):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of matrix A.
    Assume that at the ijth stage of the algorithm, a_ij will be nonzero.
    Accept A
    Return Q, R
    '''
    m,n = A.shape
    R = np.copy(A)
    Q = np.identity(m)
    G = np.empty((2,2))
    for j in range(n):
        for i in reversed(range(j+1,m)):
            a,b = R[i-1,j],R[i,j]
            G = np.array([[a,b],[-b,a]])/np.sqrt(a**2+b**2)
            R[i-1:i+1,j:] = np.dot(G,R[i-1:i+1,j:])
            Q[i-1:i+1,:] = np.dot(G,Q[i-1:i+1,:])
    return Q.T,R

def prob6(H):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of an upper Hessenberg matrix.
    Accept upper Hessenberg H.
    
    '''
    m,n = A.shape
    R = np.copy(A)
    Q = np.identity(m)
    G = np.empty((2,2))
    for j in range(n):
        i = j+1
        if i>=m:
            break
        a,b = R[i-1,j],R[i,j]
        G = np.array([[a,b],[-b,a]])/np.sqrt(a**2+b**2)
        R[i-1:i+1,j:] = np.dot(G,R[i-1:i+1,j:])
        Q[i-1:i+1,:(i+1)] = np.dot(G,Q[i-1:i+1,:(i+1)])
    return Q.T,R

def test_one():
    # These matrices don't have to be square
    print "Testing problem 1"
    A = np.random.rand(10,10)
    Q,R = QR(A)
    print np.allclose(Q.T.dot(Q), np.eye(10)) and np.allclose(Q.dot(R), A)
    A = np.random.rand(100,10)
    Q,R = QR(A)
    print np.allclose(Q.T.dot(Q), np.eye(10)) and np.allclose(Q.dot(R), A)
    A = np.random.rand(1000,100)
    Q,R = QR(A)
    print np.allclose(Q.T.dot(Q), np.eye(100)) and np.allclose(Q.dot(R), A)

def test_two():
    # These matrices don't have to be square
    print "Testing problem 2"
    A = np.random.rand(10,10)
    print np.allclose(np.abs(findDet(A)), np.abs(la.det(A)))
    A = np.random.rand(100,100)
    print np.allclose(np.abs(findDet(A)), np.abs(la.det(A)))
    
def test_three():
    # These matrices don't have to be square
    print "Testing problem 3"
    A = np.random.rand(10,10)
    Q,R = houseHolder(A)
    print np.allclose(Q.T.dot(Q), np.eye(10)) and np.allclose(Q.dot(R), A)
    
    A = np.random.rand(1000,100)
    Q,R = houseHolder(A)
    
    print np.allclose(Q.T.dot(Q), np.eye(1000)) and np.allclose(Q.dot(R), A)
    
    A = np.random.rand(100,100)
    Q,R = houseHolder(A)
    print np.allclose(Q.T.dot(Q), np.eye(100)) and np.allclose(Q.dot(R), A)
    
def test_four():
    # These matrices must be square
    print "Testing problem 4"
    A = np.random.rand(10,10)
    Q,H = hessenberg(A)
    print np.allclose(A,(np.dot(np.dot(Q.T,H),Q)))
    A = np.random.rand(100,100)
    Q,H = hessenberg(A)
    print np.allclose(A,(np.dot(np.dot(Q.T,H),Q)))
    # If you give it a symmetric matrix then it will be a tridiagonal matrix

def test_five():
    # These matrices don't have to be square
    print "Testing problem 5"
    A = np.random.rand(10,10)
    Q,R = Givens(A)
    print np.allclose(A,np.dot(Q,R)) and np.allclose(np.eye(10),Q.T.dot(Q))
    A = np.random.rand(100,100)
    Q,R = Givens(A)
    print np.allclose(A,np.dot(Q,R)) and np.allclose(np.eye(100),Q.T.dot(Q))
    A = np.random.rand(100,10)
    Q,R = Givens(A)
    print np.allclose(A,np.dot(Q,R)) and np.allclose(np.eye(100),Q.T.dot(Q))

def test_six():
    # These matrices are upper hessenberg
    print "Testing problem 6"
    A = np.random.rand(5,5)
    A[1:] = la.triu(A[1:])
    Q,R = GivensForHessenberg(A)
    print np.allclose(A,np.dot(Q,R)) and np.allclose(np.eye(5),Q.T.dot(Q))
    
    A = np.random.rand(500,500)
    A[1:] = la.triu(A[1:])
    Q,R = GivensForHessenberg(A)
    print np.allclose(A,np.dot(Q,R)) and np.allclose(np.eye(500),Q.T.dot(Q))

if __name__ == '__main__':
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()
    test_six()