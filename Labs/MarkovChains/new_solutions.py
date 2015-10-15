# solutions.py
"""Volume II Lab 8: Markov Chains
Solutions file. Written by Shane McQuarrie, even though
it should have been written by Jared Webb. All well.
"""

import numpy as np
from scipy import linalg as la
from sys import stdout
flush = stdout.flush
del stdout

# Problem 1: implement this function.
def random_markov(n):
    """Create a transition matrix for a random Markov chain with n states.
    This should be stored as an nxn numpy array. The columns sum to 1.
    """
    transition_matrix = np.empty((n,n))
    for j in range(n):
        column = np.random.random(n)
        column /= column.sum()
        transition_matrix[:,j] = column
    return transition_matrix

# Problem 2: modify this function.
def forecast(num_days):
    """Run a simulation for the weather over 'num_days' days, with
    'hot' as the starting state. Return a list containing the day-by-day
    results, not including the starting day.

    Example:
        >>> forecast(3)
        [1, 1, 0]
        >>> forecast(5)
        [1, 0, 0, 1, 1]
    """
    transition_matrix = np.array([[.7, .6], [.3, .4]])
    current_state = 0
    record = []
    for day in xrange(num_days):
        random_number = np.random.random()
        if random_number < transition_matrix[1, current_state]:
            current_state = 1
        else:
            current_state = 0
        record.append(current_state)
    return record
# Roughly 66.7% of the entries should be zeros.
# Roughly 33.3% of the entries should be ones.


def three_state_forecast(days=1):
    transition_matrix = np.array([[.6, .3, .2],[.3, .4, .4],[.1, .3, .4]])
    current_state = 0
    record = []
    for day in xrange(days):
        random_number = np.random.random()
        cold_check = transition_matrix[2, current_state]
        mild_check = transition_matrix[1, current_state] + cold_check
        if random_number < cold_check:
            current_state = 2
        elif random_number < mild_check:
            current_state = 1
        else:
            current_state = 0
        record.append(current_state)
    return record
# Roughly 39.4% of the entries should be zeros.
# Roughly 36.0% of the entries should be ones.
# Roughly 24.6% of the entries should be twos.

def analyze_simulation():
    hot1, cold1, hot2, mild, cold2  = [], [], [], [], []
    for i in xrange(10):
        f = forecast(10000)
        t = three_state_forecast(10000)
        hot1.append(f.count(0))
        cold1.append(f.count(1))
        hot2.append(t.count(0))
        mild.append(t.count(1))
        cold2.append(t.count(2))
    print " Hot days in 2-state forecast:\t%d%%"%(np.mean(hot1)/100)
    print "Cold days in 2-state forecast:\t%d%%"%(np.mean(cold1)/100)
    print " Hot days in 3-state forecast:\t%d%%"%(np.mean(hot2)/100)
    print "Mild days in 3-state forecast:\t%d%%"%(np.mean(mild)/100)
    print "Cold days in 3-state forecast:\t%d%%"%(np.mean(cold2)/100)

if __name__ == '__main__':
    analyze_simulation()

