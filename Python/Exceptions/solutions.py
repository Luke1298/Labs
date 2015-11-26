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

# Problem 3: Write a custom Exception class.
class InvalidOptionError(Exception):
    pass

# Problems 4 and 5: Write the ContentFilter class.
class ContentFilter(object):
    """docstring for ContentFilter"""
    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("'filename' must be a string")
        self.filename = filename
        with open(filename, 'r') as f:
            self.contents = f.read()

    def _validate_mode(self, mode):
        """Validate the 'mode' keyword argument for each method."""
        if mode not in {'a', 'w'}:
            raise InvalidOptionError("'mode' must be 'a' or 'w'")
    
    def hyphenate(self, outfile, mode='w'):
        """Write the data to the outfile in a single line,
        with hyphens between each word.
        """
        self._validate_mode(mode)

        # Replace whitespace with hyphens.
        out = self.contents.replace('\n', '-')
        out = out.replace('\t', '-')
        out = out.replace(' ', '-')

        # Write the results.
        with open(outfile, mode) as f:
            f.write(out)
            if self.contents[-1].isspace():     # replace final character
                f.write(self.contents[-1])

    def uniform(self, outfile, mode='w', case='upper'):
        """Write the data ot the outfile in uniform case."""
        self._validate_mode(mode)

        # Translate into the indicated case.
        if case == "upper":
            data = self.contents.upper()
        elif case == "lower":
            data = self.contents.lower()
        else:
            raise InvalidOptionError("'case' must be 'upper' or 'lower'")

        # Write the data.
        with open(outfile, mode) as f:
            f.write(data)

    def reverse(self, outfile, mode='w', unit='word'):
        """Write the data to the outfile in reverse order."""
        self._validate_mode(mode)

        # Get the data into a list of lists: each inner list is a line
        # of the data, containing the words of the line.
        lines = self.contents.split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        lines = [line.split() for line in lines]

        # Perform the reversal.
        if unit == 'word':
            data = [line[::-1] for line in lines]
        elif unit == 'line':
            data = list(reversed(lines))
        else:
            raise InvalidOptionError("'unit' must be 'word' or 'line'")

        # Paste each line back together.
        data = [" ".join(line) for line in data]

        # Write the data out. Don't forget newlines!
        with open(outfile, mode) as f:
            for line in data:
                f.write(line)
                f.write('\n')

    def transpose(self, outfile, mode='w'):
        """Write the transposed version of the data to the outfile."""
        self._validate_mode(mode)

        # Get the data into a list of lists as in reverse().
        lines = self.contents.split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        lines = [line.split(' ') for line in lines]

        # Calculate the max length so we can iterate.
        max_len = max([len(line) for line in lines])

        # Write the data.
        f = open(outfile, mode)
        for i in xrange(max_len):
            for line in lines:
                try:
                    f.write(line[i])
                    f.write(" ")
                except IndexError:
                    # Catch errors
                    pass
            f.write("\n")
        f.close()

    def __str__(self):
        """String representation: info about the contents of the file."""
        chars = len(self.contents)
        alpha = sum([s.isalpha() for s in self.contents])
        numer = sum([s.isdigit() for s in self.contents])
        space = sum([s.isspace() for s in self.contents])
        lines = len(self.contents.split('\n'))
        return "Source file:\t\t%s\nTotal characters:\t%d\nAlphabetic characters:\t%d\nNumerical characters:\t%d\nWhitespace characters:\t%d\nNumber of lines:\t%d"%(self.filename, chars, alpha, numer, space, lines)
        # Or, the slightly longer way.
        out = "Source file:\t\t" + self.filename
        out += "\nTotal characters:\t" + str(chars)
        out += "\nAlphabetic characters:\t" + str(alpha)
        out += "\nNumerical characters:\t" + str(numer)
        out += "\nWhitespace characters:\t" + str(space)
        out += "\nNumber of lines:\t" + str(lines)
        return out

