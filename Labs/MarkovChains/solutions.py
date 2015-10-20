# solutions.py
"""Volume II Lab 8: Markov Chains
Solutions file. Written by Shane McQuarrie, even though
it should have been written by Jared Webb. All well.
"""

import numpy as np
from scipy.sparse import lil_matrix
from os import system


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

        # Or, if you prefer,
        >>> forecast(5)
        ['cold', 'hot', 'hot', 'cold', 'cold']
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


# Problem 3: implement this function.
def four_state_forecast(days=1):
    transition = np.array(
        [[.5, .3, .1, 0],[.3, .3, .3, .3],[.2, .3, .4, .5],[0, .1, .2, .1]])
    current_state = 0
    record = []
    for day in xrange(days):
        current_state = np.argmax(
                    np.random.multinomial(1, transition[:,current_state]))
        record.append(current_state)
    return record
# Roughly 24.6% of the entries should be zeros.
# Roughly 30.1% of the entries should be ones.
# Roughly 33.2% of the entries should be twos.
# Roughly 12.1% of the entries should be threes.


# Problem 4: implement this function.
def analyze_simulation():
    """Analyze the results of the previous two problems."""
    hot1, cold1, hot2, mild, cold2, freezing  = [], [], [], [], [], []
    for i in xrange(10):
        f2 = forecast(10000)
        f4 = four_state_forecast(10000)
        hot1.append(f2.count(0))
        cold1.append(f2.count(1))
        hot2.append(f4.count(0))
        mild.append(f4.count(1))
        cold2.append(f4.count(2))
        freezing.append(f4.count(3))
    print("2-state forecast Hot days:\t%f%%"%(np.mean(hot1)/100.))
    print("2-state forecast Cold days:\t%f%%"%(np.mean(cold1)/100.))
    print("4-state forecast Hot days:\t%f%%"%(np.mean(hot2)/100.))
    print("4-state forecast Mild days:\t%f%%"%(np.mean(mild)/100.))
    print("4-state forecast Cold days:\t%f%%"%(np.mean(cold2)/100.))
    print("4-state forecast Freezing days:\t%f%%"%(np.mean(freezing)/100.))


def problem5(filename):
    """Read in from a file, convert to ints, read out to a file."""

    word_list = ['$tart']
    with open(filename, 'r') as f:
        contents = f.readlines()
    outfile = open("int_file.txt", 'w')
    for line in contents:
        sentence = line.split()
        for word in sentence:
            if word not in word_list:
                word_list.append(word)
            outfile.write(str(word_list.index(word)) + " ")
        outfile.write('\n')
    word_list.append('en&')
    return word_list


def problem6(int_file, num_states, sparse=False):

    # Initialize the transition matrix.
    if sparse:
        markov = lil_matrix((num_states, num_states))
    else:
        markov = np.zeros((num_states, num_states))

    # Read in the data and process it.
    with open(int_file, 'r') as f:
        contents = f.readlines()
    data = []
    for line in contents:
        data.append(line.split())

    # Build the matrix.
    for i in xrange(len(data)-1):
        line = data[i]
        markov[int(line[0]), 0] += 1
        for j in xrange(len(line)-1):
            markov[int(line[j+1]), int(line[j])] += 1
        markov[num_states-1, int(line[-1])] += 1

    # Divide by nonzero column sums.
    for j in xrange(num_states):
        s = markov[:,j].sum()
        if s != 0:
            markov[:,j] /= s
    return markov

def sentences(infile, outfile, num_sentences=1):
    """Generate random sentences using the word list generated in
    Problem 5 and the transition matrix generated in Problem 6.
    Write the results to the specified outfile.

    Parameters:
        infile (str): The path to a filen containing a training set.
        outfile (str): The file to write the random sentences to.
        num_sentences (int): The number of random sentences to write.

    Returns:
        None
    """

    # Get output from previous problems.
    word_list = problem5(infile)
    transition = problem6('int_file.txt', len(word_list), False)

    # Transition through the Markov chain.
    stop = transition.shape[1] - 1
    output = ""
    for i in xrange(num_sentences):
        current_state = 0
        while current_state != stop:
            current_state = np.argmax(
                np.random.multinomial(1, transition[:,current_state]))
            if current_state != stop:
                output += word_list[current_state] + " "
            else:
                output += "\n"

    # Write the results to the specified output file.
    with open(outfile, 'w') as f:
        f.write(output)
    system("rm int_file.txt")
