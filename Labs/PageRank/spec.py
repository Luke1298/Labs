# spec.py

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
    raise NotImplementedError("Problem 1 incomplete")
    
def calculateK(A,N):
    '''
    Compute the matrix K as described in the lab.
    Input:
        A (array): adjacency matrix of an array
        N (int): the datasize of the array
    Return:
        K (array)
    '''
    raise NotImplementedError("Problem 2 incomplete")

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
    raise NotImplementedError("Problem 3 incomplete")

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
    raise NotImplementedError("Problem 4 incomplete")