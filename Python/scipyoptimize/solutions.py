# solutions.py
"""Volume 2 Lab 13: Optimization Packages I (scipy.optimize) solutions file."""

import scipy.optimize as opt
import numpy as np
from matplotlib import pyplot as plt


# Problem 1: use scipy.optimize.minimize() with different methods and compare.
def prob1():
    """Use the minimize() function in the scipy.optimize package to find the
    minimum of the Rosenbrock function (scipy.optimize.rosen) using the
    following methods:
        Nelder-Mead
        Powell
        CG
        BFGS
        Newton-CG (test with and without the hessian)
        L-BFGS-B
        TNC
        COBYLA
        SLSQP
    Use x0 = np.array([4., -2.5]) for the initial guess for each test.
    
    Print a statement answering the following questions:
        Which algorithm(s) take(s) the least number of iterations?
        Which algorithm(s) fail to find the (correct) minimum?
    """
    # Set up the initial guess, jacobian, and hessian.
    x0 = np.array([4.0,-2.5])
    jacobian = opt.rosen_der
    hessian = opt.rosen_hess

    # Test each method.
    info = {}
    info["Nelder-Mead"] = opt.minimize(opt.rosen, x0, method='Nelder-Mead',
                                                        options={'xtol':1e-8})
    info["Powell"] = opt.minimize(opt.rosen, x0, method='Powell',
                                                        options={'xtol':1e-8})
    info["CG"] = opt.minimize(opt.rosen, x0, method='CG')
    info["BFGS"] = opt.minimize(opt.rosen, x0, method='BFGS')
    info["Newton-CG w/out Hessian"] = opt.minimize(opt.rosen, x0, jac=jacobian,
                                method='Newton-CG', options={'xtol':1e-8})
    info["Newton-CG, w/ Hessian"] = opt.minimize(opt.rosen, x0, jac=jacobian,
                    hess=hessian, method='Newton-CG',options={'xtol':1e-8})
    info["L-BFGS-B"] = opt.minimize(opt.rosen, x0, method='L-BFGS-B',
                                                        options={'xtol':1e-8})
    info["TNC"] = opt.minimize(opt.rosen, x0, method='TNC', 
                                                        options={'xtol':1e-8})
    info["COBYLA"] = opt.minimize(opt.rosen, x0, method='COBYLA')
    info["SLSQP"] = opt.minimize(opt.rosen, x0, method='SLSQP')

    # Report the info.
    print("\n\t\tOptimization Tests")
    for method in info:
        print("Method: {}\n{}\n\n".format(method, info[method]))
    
    # Answer the problem questions.
    print("The Powell algorithm takes the least number of iterations (19).")
    print("COBYLA fails to find the correct minimum.")


# Problem 2: learn and use scipy.optimize.basinhopping()
def prob2():
    """Explore the documentation on the function scipy.optimize.basinhopping()
    online or via IPython. Use it to find the global minimum of the multmin()
    function given in the lab, with initial point x0 = np.array([-2, -2]) and
    the Nelder-Mead algorithm. Try it first with stepsize=0.5, then with
    stepsize=0.2.

    Return the minimum value of the function with stepsize=0.2.
    Print a statement answering the following question:
        Why doesn't scipy.optimize.basinhopping() find the minimum the second
        time (with stepsize=0.2)?
    """
    # Define the function to be optimized and the initial condition.
    def multimin(x):
        r = np.sqrt((x[0]+1)**2 + x[1]**2)
        return r**2 *(1+ np.sin(4*r)**2)
    x0 = np.array([-2, -2])
    
    info = {}
    info[.5] = opt.basinhopping(multimin, x0, stepsize=0.5,
                                minimizer_kwargs={'method':'nelder-mead'})
    info[.2] = opt.basinhopping(multimin, x0, stepsize=0.2,
                                minimizer_kwargs={'method':'nelder-mead'})

    # Print the results.
    for step in info:
        print("Stepsize:\t{}\nMinimum:\t{}\n".format(step, info[step].fun))

    # Answer the problem question and return the minimum value.
    print("0.2 is too small a stepsize to escape the basin of a local min.")
    return info[.2].fun


# Problem 3: learn and use scipy.optimize.root()
def prob3():
    """Find the roots of the system
    [       -x + y + z     ]   [0]
    [  1 + x^3 - y^2 + z^3 ] = [0]
    [ -2 - x^2 + y^2 + z^2 ]   [0]

    Returns the values of x,y,z as an array.
    """
    # Define the nonlinear system, its Jacobian, and the initial guess.
    def f(X):
        x,y,z = X
        return np.array([   -x + y + z,
                            1 + x**3 -y**2 + z**3,
                            -2 -x**2 + y**2 + z**2  ])
    def jacobian(X):
        x,y,z = X
        return np.array([   [    -1,    1, 1     ],
                            [3*x**2, -2*y, 3*z**2],
                            [  -2*x,  2*y, 2*z   ]  ])
    x0 = np.array([0,0,0])

    # Calculate the solution, check that it is a root, and return it.
    sol = opt.root(f, x0, jac=jacobian, method='hybr')
    assert np.allclose(np.zeros_like(sol.x), f(sol.x)), "FAILURE"
    return sol.x


# Problem 4: learn and use scipy.optimize.curve_fit().
def prob4():
    """Use the scipy.optimize.curve_fit() function to fit a heating curve to
    the data found in `heating.txt`. The first column of this file is time, and
    the second column is temperature in Kelvin.

    The fitting parameters should be gamma, C, and K, as given in Newton's law
    of cooling.

    Plot the data from `heating.txt` and the curve generated by curve_fit.
    Return the values gamma, C, K as an array.
    """
    # Load the data.
    data = np.loadtxt("../heating.txt")

    # Define the function to optimize.
    def f(x, gamma, c, K):
        return 290.0 + 59.43/gamma + K*np.exp(-gamma*x/c)

    # Use curve_fit and the data to get the parameters.
    popt, pcov = opt.curve_fit(f, data[:,0], data[:,1])
    curve = f(data[:,0], popt[0], popt[1], popt[2])

    # Plot the data and the curve.
    plt.plot(data[:,0], data[:,1], '.k', label='Data')
    plt.plot(data[:,0], curve,      'b', label='Curve', linewidth=2)
    plt.xlim(-50, 400)
    plt.ylim(260, 380)
    plt.legend(loc="lower right")
    plt.show()
    
    # Return the parameter values.
    return popt

# END OF SOLUTIONS ========================================================== #


