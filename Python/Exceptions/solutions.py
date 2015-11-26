# solution.py
"""Exceptions and File I/O Protocol solutions file.
Written by Shane McQuarrie and Tanner Thompson, Fall 2015
"""

# Problem 1: Modify this function to account for bad inputs.
def my_func(a, b, c, d, e):
    if not isinstance(a, str):
        raise TypeError("arg 1 must be a string.")
    print("The first argument is " + a)
    
    numerical = {int, float, long, complex}
    if type(b) not in numerical or type(c) not in numerical:
        raise TypeError("args 2 and 3 must be a numerical type.")
    x = sum([b, c])
    
    if type(d) is not type(e):
        raise TypeError("args 5 and 6 must be the same type")
    y = d + e
    
    return a, x, y

# Problem 2: Modify this function to account for KeyboardInterrupts.
def forever(max_iters=1000000000000):
    iters = 0
    try:
        while True:
            iters += 1
            if iters >= max_iters:
                break
    except KeyboardInterrupt:
        print("Process Interrupted")
    else:
        print("Process Terminated")
    return iters

# Write a custom Exception class.
class BadDataError(Exception):
    pass
