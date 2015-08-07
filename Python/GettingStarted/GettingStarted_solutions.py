#GettingStarted_solutions.py
'''
Volume 1, Lab 1: Getting Started
Solutions file written by Tanner Christensen, Summer 2015
'''

# PROBLEM 1: Run "Hello World" script
'''
Everything is provided to the students. There is nothing to grade for this problem.
'''

# PROBLEM 2: Write a function sphere_volume that accepts a parameter r and returns the volume of a sphere of radius r.
def sphere_volume(r):
    '''
    Returns the volume of a sphere of radius r.
    '''
    return (4 * 3.14159 / 3)*r**3

# PROBLEM 3: Write first_half and reverse functions
def first_half(my_string):
    '''
    Returns the first half a inputed string.
    Example:
    >>> first_half("python")
    "pyt"
    '''
    return my_string[:len(my_string)/2]
    
def reverse(my_string):
    '''
    Returns the inputed string reversed.
    Example:
    >>> reverse("python")
    "nohtyp"
    '''
    return my_string[::-1]
    
# PROBLEM 4: Perform list operations
my_list =  ["ant","baboon","cat","dog"] 
my_list.append("elephant")
my_list.remove("ant")
my_list.remove(my_list[1])
my_list[2] = "donkey"
my_list.append("fox")
     # Resulting list should be
["baboon","donkey","elephant","fox"]

# PROBLEM 5: Convert list of integers to list of strings using list comprehension
def stringify(my_list):
    '''
    Converts and returns a list of integers to a list of strings
    Example:
    >>> stringify([1,2,3])
    ['1', '2', '3']
    '''
    return [str(n) for n in my_list]
    
# PROBLEM 6: Implement Pig Latin
def pig_latin(word):
    '''
    Translates inputed word to Pig Latin
    Example:
    >>> pig_latin("apple")
    "applehay"
    >>> pig_latin("banana")
    "ananabay"
    '''
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
        
# PROBLEM 7: Translate numbers 1-26 to their corresponding letters of the alphabet using dictionaries
def int_to_string(my_list):
    '''
    Translate a list of numbers 1-26 to corresponding letter of the alphabet
    Example:
    >>> int_to_string([13, 1, 20, 8])
    ['m', 'a', 't', 'h'] 
    '''
    my_dictionary = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i',
                    10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q',
                    18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 
                    25:'y', 26:'z'}
    output = []
    for i in my_list:
        output.append(my_dictionary[i])
    return output

# PROBLEM 8: Generate a list of squares less than n
def squares(n):
    '''
    Yields all squares less than n
    '''
    i = 0
    while i*i < n:
        yield i*i
        i += 1

# PROBLEM 9: Approximate ln(2) using alternating harmonic series
def alt_harm(n):
    '''
    Returns the partial sum of the first n terms of the alternating harmonic series.
    '''
    return sum([(-1)**(i+1)/float(i) for i in xrange(1,n)])
    

        
