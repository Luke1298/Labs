"""
GMRES

"""

#Problem 1: Implement the following function
def gmres(A, b, x0, k=100, tol=1e-8):
    '''Calculate approximate solution of Ax=b using GMRES algorithm.
    
    INPUTS:
    A    - Callable function that calculates Ax for any input vector x.
    b    - A NumPy array of length m.
    x0   - An arbitrary initial guess.
    k    - Maximum number of iterations of the GMRES algorithm. Defaults to 100.
    tol  - Stop iterating if the residual is less than 'tol'. Defaults to 1e-8.
    
    RETURN:
    Return (y, res) where 'y' is an approximate solution to Ax=b and 'res' 
    is the residual.
    '''
    return ValueError("Problem 1 not implemented")