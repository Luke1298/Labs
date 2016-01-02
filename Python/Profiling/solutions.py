# Unlike other solutions files, this file will serve more as a reference 
#    since we wish to compile the Cython code separately. For the Cython
#    and Numba solutions, we will provide the code as it should be if it 
#    is being run from IPython.

# Problem 1
def foo_fast(n):
    my_list = np.random.random_integers(-9,9,n)
    return my_list, np.sum(my_list[::2])
    
# Problem 2
def pysum(X):
    total = 0
    for i in xrange(len(X)):
        total += X[i]
    return total

In [1]: load_ext Cython
In [2]: %%cython
        def cysum(double[:] X):
            cdef double total = 0
            cdef int i
            for i in xrange(len(X)):
                total += X[i]
            return total
       
# Problem 3
def LU_part1(A):
    """Returns the LU decomposition of a square matrix."""
    n = A.shape[0]
    U = np.array(np.copy(A), dtype=float)
    L = np.eye(n)
    
    for i in xrange(1,n):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            for k in xrange(j,n):
                U[i,k] -= L[i,j]*U[j,k]
    return L,U

In [1]: load_ext Cython     #if this hasn't been done already
In [2]: %%cython
        import numpy as np
        def cy_LU(double[:,:] A):
            cdef int n = A.shape[0]
            cdef double[:,:] U = np.array(np.copy(A))
            cdef double[:,:] L = np.eye(n).astype(float)
            cdef int i,j,k
            
            for i in xrange(1,n):
                for j in xrange(i):
                    L[i,j] = U[i,j]/U[j,j]
                    for k in xrange(j,n):
                        U[i,k] -= L[i,j]*U[j,k]
            return L,U
       
# Problem 4
def pymatpow(X, power):
    """ Return X^{power}.
    
    Inputs:
        X (array) - A square 2-D NumPy array
        power (int) - The power to which we are taking the matrix X.
    Returns:
        prod (array) - X^{power}
    """
    prod = X.copy()
    temparr = np.empty_like(X[0])
    size = X.shape[0]
    for n in xrange(1, power):
        for i in xrange(size):
            for j in xrange(size):
                tot = 0.
                for k in xrange(size):
                    tot += prod[i,k] * X[k,j]
                temparr[j] = tot
            prod[i] = temparr
    return prod

In [1]: load_ext Cython     # if this hasn't been done already
In [2]: %%cython
        def cymatpow(double[:,:] X, int power):
            """ Return X^{power}.
            
            Inputs:
                X (array) - A square 2-D NumPy array
                power (int) - The power to which we are taking the matrix X.
            Returns:
                prod (array) - X^{power}
            """
            cdef double[:,:] prod = X.copy().astype(float)
            cdef double[:,:] temparr = np.empty_like(X[0]).astype(float)
            cdef int size = X.shape[0]
            cdef int n,i,j,k
            cdef double tot
            
            for n in xrange(1, power):
                for i in xrange(size):
                    for j in xrange(size):
                        tot = 0.
                        for k in xrange(size):
                            tot += prod[i,k] * X[k,j]
                        temparr[j] = tot
                    prod[i] = temparr
            return prod

In [1]: from numba import jit
In [2]: @jit
        def numbamatpow(X, power):
            """ Return X^{power}.
            
            Inputs:
                X (array) - A square 2-D NumPy array
                power (int) - The power to which we are taking the matrix X.
            Returns:
                prod (array) - X^{power}
            """
            prod = X.copy()
            temparr = np.empty_like(X[0])
            size = X.shape[0]
            for n in xrange(1, power):
                for i in xrange(size):
                    for j in xrange(size):
                        tot = 0.
                        for k in xrange(size):
                            tot += prod[i,k] * X[k,j]
                        temparr[j] = tot
                    prod[i] = temparr
            return prod

# Problem 5
In [1]: %load_ext Cython    # if this hasn't been done already
In [2]: %%cython
        import numpy as np
        def cytridiag(double[:] a, double[:] b, double[:] c, double[:] d):
            """Solve the tridiagonal system Ax = d where A has diagonals a, b, and c.
            
            Inputs:
                a, b, c, d (array) - All 1-D NumPy arrays of equal length.
            Returns:
                x (array) - solution to the tridiagonal system.
            """
            cdef int n = a.size
            
            # Make copies so the original arrays remain unchanged
            cdef double[:] aa = np.copy(a)
            cdef double[:] bb = np.copy(b)
            cdef double[:] cc = np.copy(c)
            cdef double[:] dd = np.copy(d)
            
            cdef int i
            cdef double temp
            # Forward sweep
            for i in xrange(1, n):
                temp = aa[i]/bb[i-1]
                bb[i] = bb[i] - temp*cc[i-1] 
                dd[i] = dd[i] - temp*dd[i-1]

            cdef double[:] x
            # Back substitution
            x = np.zeros_like(a)
            x[-1] = dd[-1]/bb[-1]
            for i in xrange(n-2, -1, -1):
                x[i] = (dd[i]-cc[i]*x[i+1])/bb[i]

            return x
