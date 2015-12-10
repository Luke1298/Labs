import numpy as np
import scipy.sparse as spar
import scipy.linalg as la
from scipy.sparse import linalg as sla

def to_matrix(datafile,n):
    '''
    Return the nxn adjacency matrix described by datafile.
    INPUTS:
    datafile (.txt file): A .txt file describing a directed graph. Lines
        describing edges should have the form '<from node>\t<to node>\n'.
        The file may also include comments.
    n (int): The number of nodes in the graph described by datafile
    RETURN:
        Return a SciPy sparse `dok_matrix'.
    '''
    adj = spar.dok_matrix((n,n))
    with open(datafile, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            try:
                x,y = int(line[0]),int(line[1])
                adj[x,y] = 1
            except:
                continue
    return adj

def calculateK(A,N):
    '''
    Compute the matrix K as described in the lab.
    Input:
        A (array): adjacency matrix of an array
        N (int): the datasize of the array
    Return:
        K (array)
    '''
    n = A.shape[0]
    D = np.zeros(n)
    for row in range(n):
        D[row] = A[row].sum()
    for i in range(n):
        if D[i] == 0:
            D[i] = n
            A[i] = np.ones(n)
    K = (A.T/D)
    return K[:N,:N]

def iter_solve(data, datasize, N=None, d=.85, tol=1E-5):
    '''
    Return the page ranks of the network described by `data`. 
    Iterate through the PageRank algorithm until the error is less than `tol'.
    Inputs:
    data - A NumPy array representing the adjacency matrix of a directed graph
    datasize - An integer representing the size of the 'data' array.
    N (int) - Restrict the computation to the first `N` nodes of the graph.
            Defaults to N=None; in this case, the entire matrix is used.
    d     - The damping factor, a float between 0 and 1.
            Defaults to .85.
    tol  - Stop iterating when the change in approximations to the solution is
        less than `tol'. Defaults to 1E-5.
    Returns:
    The approximation to the steady state.
    '''
    if N is None:
        N = datasize
    pt = np.ones((N,1))/N    
    K = calculateK(data,N)
    pt1 = d*np.dot(K,pt) + ((1.-d)/N)*np.ones((N,1))
    while la.norm(pt1-pt) > tol:
        pt = pt1
        pt1 = d*np.dot(K,pt) + ((1.-d)/N)*np.ones((N,1))
    return pt1

def eig_solve( data, datasize, N=None, d=.85):
    '''
    Return the page ranks of the network described by `data`. Use the
    eigenvalue solver in \li{scipy.linalg} to calculate the steady state
    of the PageRank algorithm
    Inputs:
    data - A NumPy array representing the adjacency matrix of a directed graph
    datasize - An integer representing the size of the 'data' array.
    N - Restrict the computation to the first `N` nodes of the graph.
            Defaults to N=None; in this case, the entire matrix is used.
    d     - The damping factor, a float between 0 and 1.
            Defaults to .85.
    Returns:
    Use the eigenvalue solver in \li{scipy.linalg} to calculate the steady
    state of the PageRank algorithm.
    '''
    if N is None:
        N = datasize
    K = calculateK(data,N)
    B = d*K + ((1.-d)/N)*np.ones((N,N))
    evalues,evectors = la.eig(B)
    pt = (evectors[:,0].real)
    pt = pt*1/pt.sum()
    return pt
    
    
def problemOne():
    print to_matrix('datafile.txt',8).todense()

def problemTwo():
    A = to_matrix('datafile.txt',8).todense()
    print calculateK(A,8)

def problemThree():
    A = to_matrix('datafile.txt',8).todense()
    print iter_solve(A,8,N = 8)

def problemFour():
    A = to_matrix('datafile.txt',8).todense()
    a =iter_solve(A,8,N = 8)
    b = eig_solve(A,8,N = 8)
    print a
    print eig_solve(A,8,N=8)

if __name__ == '__main__':
    print "Testing 1"
    problemOne()
    print "Testing 2"
    problemTwo()
    print "Testing 3"
    problemThree()
    print "Testing 4"
    problemFour()
            