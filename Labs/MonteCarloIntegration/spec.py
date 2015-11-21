# solutions.py
"""Volume I: Monte Carlo Integration
<Name>
<Class>
<Date>
"""

def mc_int(f, mins, maxs, numPoints=500, numIters=100):
    """Use Monte-Carlo integration to approximate the integral of f
    on the box defined by mins and maxs.
    
    Inputs:
        f (function) - The function to integrate. This function should 
            accept a 1-D NumPy array as input.
        mins (1-D np.ndarray) - Minimum bounds on integration.
        maxs (1-D np.ndarray) - Maximum bounds on integration.
        numPoints (int, optional) - The number of points to sample in 
            the Monte-Carlo method. Defaults to 500.
        numIters (int, optional) - An integer specifying the number of 
            times to run the Monte Carlo algorithm. Defaults to 100.
        
    Returns:
        estimate (int) - The average of 'numIters' runs of the 
            Monte-Carlo algorithm.
                
    Example:
        >>> f = lambda x: np.hypot(x[0], x[1]) <= 1
        >>> # Integral over the square [-1,1] x [-1,1]. Should be pi.
        >>> mc_int(f, np.array([-1,-1]), np.array([1,1]))
        3.1290400000000007
    """
    pass
    
def joint_normal(mins, maxs):
    """Caluclate the integral of the joint normal distribution using SciPy and 
    Monte Carlo integration.
    
    Inputs:
        mins (1-D np.ndarray) - Minimum bounds of integration.
        maxs (1-D np.ndarray) - Maximum bounds of integration.
    
    Returns:
        value (int) - result from intregration using SciPy
        estimate (1-D np.ndarray) - result of Monte Carlo integration
            using 'numPoints' = {10,100,1000,10000}
    """
    pass
