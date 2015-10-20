# spec.py
"""Volume II Lab 8: Markov Chains
<Name>
<Class>
<Date>
"""


# Problem 1: implement this function.
def random_markov(n):
    """Create and return a transition matrix for a random
    Markov chain with 'n' states as an nxn NumPy array.
    """
    raise NotImplementedError("Problem 1 incomplete.")


# Problem 2: modify this function.
def forecast(num_days):
    """Run a simulation for the weather over 'num_days' days, with
    "hot" as the starting state. Return a list containing the day-by-day
    results, not including the starting day.

    Example:
        >>> forecast(5)
        [1, 0, 0, 1, 0]
        # Or, if you prefer,
        ['cold', 'hot', 'hot', 'cold', 'hot']
    """
    raise NotImplementedError("Problem 2 incomplete.")


# Problem 3: implement this function.
def four_state_forecast(days=1):
    """Same as forecast(), but using the four-state transition matrix."""
    raise NotImplementedError("Problem 3 incomplete.")


# Problem 4: implement this function.
def analyze_simulation():
    """Analyze the results of the previous two problems. What percentage
    of days are in each state? Print your results to the terminal.
    """
    raise NotImplementedError("Problem 4 incomplete.")


# Problems 5-6: define and implement the described functions.


# Problem 7: implement this function.
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
    raise NotImplementedError("Problem 7 incomplete.")
