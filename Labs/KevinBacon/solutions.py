# solutions.py
"""Volume II Lab 8: Breadth-First Search (Kevin Bacon)
Solutions file. Written by Shane A. McQuarrie.
"""

# =========================== solutions.py ============================== #

from collections import deque
import networkx as nx
from matplotlib import pyplot as plt


# Problems 1-4: Implement the following class
class Graph(object):
    """A graph object, stored as an adjacency dictionary. Each node in the graph is a key in the dictionary.
    The value of each key is a list of the corresponding node's neighbors.
    """

    def __init__(self, adjacency):
        """Store the adjacency dictionary as a class attribute"""
        self.dictionary = adjacency

    # Problem 1
    def __str__(self):
        """String representation: a sorted view of the adjacency dictionary.
        
        Example:
            >>> test = {'A':['D', 'C', 'B'], 'D':['A', 'C'],
            ...         'C':['B', 'A', 'D'], 'B':['A', 'C']}
            >>> print(Graph(test))
            A: B; C; D
            B: A; C
            C: A; B; D
            D: A; C
        """
        out = ""
        keys = self.dictionary.keys()
        keys.sort()
        # join() approach
        for key in keys:
            out += str(key) + ": "              # add each node
            values = self.dictionary[key]
            values.sort()
            out += "; ".join(values) + "\n"     # add the node's neighborhood
        return out
        # for loop approach
        for key in keys:
            out += str(key) + ": "              # add each node
            values = self.dictionary[key]
            values.sort()
            for value in values:                # add each neighbor
                out += str(value) + "; "
            out = out.strip("; ") + "\n"        # strip off the last "; "
        return out

    # Problem 2
    def traverse(self, start):
        """Begin at 'start' and perform a breadth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited. If 'start' is not in the
        adjacency dictionary, raise a ValueError.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation)

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).traverse('B')
            ['B', 'A', 'C']
        """

        # Validate input
        if start not in self.dictionary:
            raise ValueError(str(start) + " is not in the graph.")

        # Set up the data structures
        visited = list()
        marked = set(start)
        visit_queue = deque(start)

        # Search the graph until done:
        while len(visit_queue) > 0:
            # get the next node from the queue and visit it
            current = visit_queue.popleft()
            visited.append(current)

            # put any unvisited, unmarked neighbors of the
            # current node on the visiting queue
            for neighbor in self.dictionary[current]:
                if neighbor not in marked:
                    visit_queue.append(neighbor)
                    marked.add(neighbor)
        return visited

    # Problem 3 (Optional)
    def DFS(self, start):
        """Begin at 'start' and perform a depth-first search until all
        nodes in the graph have been searched. Return a list of values, in
        the order that they were visited. If 'start' is not in the
        adjacency dictionary, raise a ValueError.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation)

        Example:
            >>> test = {'A':['B', 'D'], 'B':['A', 'C'],
            ...         'C':['B', 'D'], 'D':['A', 'C']}
            >>> Graph(test).DFS('A')
            ['A', 'B', 'C', 'D']
        """
        if start not in self.dictionary:
            raise ValueError(str(start) + " is not in the graph.")

        visited = list()
        marked = set(start)
        visit_queue = deque(start)          # for DFS, use this as a stack

        while len(visit_queue) > 0:
            current = visit_queue.pop()     # This line is different from BFS
            visited.append(current)
            for neighbor in self.dictionary[current]:
                if neighbor not in marked:
                    visit_queue.append(neighbor)
                    marked.add(neighbor)
        return visited

    # Problem 4
    def shortest_path(self, start, target):
        """Begin at the node containing 'start' and perform a breadth-first
        search until the node containing 'target' is found. Return a list
        containg the shortest path from 'start' to 'target'. If either of
        the inputs are not in the adjacency graph, raise a ValueError.

        Inputs:
            start: the node to start the search at.
            target: the node to search for.

        Returns:
            A list of nodes along the shortest path from start to target,
                including the endpoints.

        Example:
            >>> test = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],
            ...         'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],
            ...         'G':['A', 'F']}
            >>> Graph(test).shortest_path('A', 'G')
            ['A', 'F', 'G']
        """
        if start not in self.dictionary:
            raise ValueError("Starting point " + str(start) 
                                    + " is not in the graph.")
        # if target not in self.dictionary: raise ValueError

        visited = list()
        marked = set(start)
        visit_queue = deque(start)
        all_paths = {}
        final_path = deque()

        while len(visit_queue) > 0:
            current = visit_queue.popleft()
            visited.append(current)

            # Check for the target
            if current == target:
                # Build the shortest path
                final_path.append(current)
                while current in all_paths:
                    final_path.appendleft(all_paths[current])
                    current = all_paths[current]
                return list(final_path)
            # Otherwise continue as before
            else:
                for neighbor in self.dictionary[current]:
                    if neighbor not in marked:
                        visit_queue.append(neighbor)
                        marked.add(neighbor)
                        # Track the path
                        all_paths[neighbor] = current

        # If all neighbors have been checked, the target isn't in the graph.
        raise ValueError("Target " + str(target) + " is not in the graph.")

    def cheater(self, start, target):
        return nx.shortest_path(
            convert_to_networkx(self.dictionary), start, target)


# Problem 5: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    # Make the graph
    output = nx.Graph()
    for key in dictionary:
        for value in dictionary[key]:
            # Add each edge. Duplicates are automatically ignored.
            output.add_edge(key, value)
    return output


# Helper function for problem 6
def parse(filename="movieData.txt"):
    """Generate an adjacency dictionary where each key is
    a movie and each value is a list of actors in the movie.
    """

    # open the file, read it in, and split the text by '\n'
    movieFile = open(filename, 'r')
    movieFile = movieFile.read()
    movieFile = movieFile.split('\n')
    graph = dict()

    # for each movie in the file,
    for line in movieFile:
        # get movie name and list of actors
        names = line.split('/')
        movie = names[0]
        graph[movie] = []
        # add the actors to the dictionary
        for actor in names[1:]:
            graph[movie].append(actor)

    return graph 


# Problems 6-8: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 6
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph and with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as a class attribute.
        """
        # Get the adjacency dictionary from the file
        movie_to_actors = parse(filename)

        # Extract the actors from the adjacency dictionary (values) 
        self.actors = set()
        for movie in movie_to_actors:
            for actor in movie_to_actors[movie]:
                self.actors.add(actor)

        # Convert the adjacency matrix to networkX
        self.bacon_graph = convert_to_networkx(movie_to_actors)
        

    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        """Find the shortest path from 'start' to 'target'."""
        if start not in self.actors:
            raise ValueError(str(start) + " is not in the set of actors")
        if target not in self.actors:
            raise ValueError(str(target) + " is not in the set of actors")
        return nx.shortest_path(self.bacon_graph, start, target)

    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        """Return the Bacon number of 'start'."""
        # Integer divide by two to account for movies in the path.
        return len(self.path_to_bacon(start, target)) // 2

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        """Calculate the average Bacon number in the data set.
        Note that actors are not guaranteed to be connected to the target.
        """
        connected = 0
        isolated = 0
        total = 0
        for actor in self.actors:
            # if nx.has_path(self.bacon_graph, actor, target):
            try:
                total += self.bacon_number(actor, target)
                connected += 1
            except nx.NetworkXNoPath:
                isolated += 1
    
        return float(total)/connected, isolated

    # Problem 8 (Optional)
    def plot_bacon(self, target="Bacon, Kevin"):
        """Create and show a histogram displaying the frequency of the Bacon
        numbers in the data set. Ignore entries with no path to 'target'.
        """
        bacon = deque()
        for actor in self.actors:
            try:
                bacon.append(self.bacon_number(actor, target))
            except nx.NetworkXNoPath:
                pass
        name = target.partition(",")[0]
        plt.hist(bacon, bins=7)
        plt.title(name + " Number Distribution")
        plt.xlabel(name + " Number")
        plt.ylabel("Actors")
        plt.show()

# =========================== END OF SOLUTIONS ========================== #

import inspect

def getCode():
    rawcode = inspect.getsource(Graph.shortest_path).splitlines()[21:]
    code = ""
    for line in rawcode: code += line
    if len(code.partition('shortest_path(')[1]) > 0:
        for line in rawcode:
            print line

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
     5 points for problem 1
    10 points for problem 2
    15 points for problem 3
     3 points for problem 4 (Extra Credit)
    10 points for problem 5
    10 points for problem 6
    10 points for problem 7
     3 points for problem 8 (Extra Credit)
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 60.
        feedback (str): a printout of results for the student.
    """
    
    # possible helper functions
    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\tCorrect response:\n" + str(x)
            m += "\n\tStudent response:\n" + str(y)
            return 0, m
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p,""
        else: return part,m

    s = student_module
    score = 0
    total = 60
    feedback = s.__doc__

    # Test cases
    graph1 = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
    graph2 = {'A':['D', 'B'], 'D':['A', 'C'],
              'C':['B', 'D'], 'B':['C', 'A']}
    graph3 = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],
              'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],
              'G':['A', 'F']}
    graph4 = {'A':['B'], 'B':['C', 'D'], 'C':['B', 'D'], 'D':['B', 'E'],
              'E':['F', 'G'], 'F':['E', 'H'], 'H':['F'],
              'G':['E', 'I', 'J'], 'I':['G', 'J'], 'J':['G', 'J', 'K'],
              'K':['J', 'L'], 'L':['K']}

    solution1 = Graph(graph1); student1 = s.Graph(graph1)
    solution2 = Graph(graph2); student2 = s.Graph(graph2)
    solution3 = Graph(graph3); student3 = s.Graph(graph3)
    solution4 = Graph(graph4); student4 = s.Graph(graph4)
    
    try:    # Problem 1: 5 points
        feedback += "\n\nTesting problem 1 (5 points):"
        points = 0

        p,f = strTest(solution1, student1, "\n\tGraph.__str__ failed")
        points += p; feedback += f
        p,f = strTest(solution2, student2, "\n\tGraph.__str__ failed")
        points += p; feedback += f
        p,f = strTest(solution3, student3, "\n\tGraph.__str__ failed")
        points += p; feedback += f
        p,f = strTest(solution4, student4, "\n\tGraph.__str__ failed")
        points += (p * 2); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 10 points
        feedback += "\n\nTesting problem 2 (10 points):"
        points = 0
        p,f = strTest(solution1.traverse('A'), student1.traverse('A'),
                                    "\n\tGraph.traverse() failed")
        points += (p * 2); feedback += f
        p,f = strTest(solution2.traverse('A'), student2.traverse('A'),
                                    "\n\tGraph.traverse() failed")
        points += (p * 2); feedback += f
        p,f = strTest(solution3.traverse('A'), student3.traverse('A'),
                                    "\n\tGraph.traverse() failed")
        points += (p * 2); feedback += f
        p,f = strTest(solution4.traverse('A'), student4.traverse('A'),
                                    "\n\tGraph.traverse() failed")
        points += (p * 4); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    if hasattr(student1, 'DFS'):
        try:    # Problem 3: 3 points, Extra Credit
            feedback += "\n\nTesting problem 3 (3 points, Extra Credit):"
            points = 0
            p,f = strTest(solution2.DFS('A'), student2.DFS('A'),
                                        "\n\tGraph.DFS() failed")
            points += p; feedback += f
            p,f = strTest(solution3.DFS('A'), student3.DFS('A'),
                                        "\n\tGraph.DFS() failed")
            points += p; feedback += f
            p,f = strTest(solution4.DFS('A'), student4.DFS('A'),
                                        "\n\tGraph.DFS() failed")
            points += p; feedback += f
        
            score += points; feedback += "\nScore += " + str(points)
        except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 15 points
        feedback += "\n\nTesting problem 4 (15 points):"
        points = 0
        p,f = strTest(solution1.shortest_path('A', 'C'),
                       student1.shortest_path('A', 'C'),
                      "\n\tGraph.shortest_path() failed")
        points += (p * 3); feedback += f
        p,f = strTest(solution2.shortest_path('A', 'C'),
                       student2.shortest_path('A', 'C'),
                      "\n\tGraph.shortest_path() failed")
        points += (p * 3); feedback += f
        p,f = strTest(solution3.shortest_path('A', 'G'),
                       student3.shortest_path('A', 'G'),
                      "\n\tGraph.shortest_path() failed")
        points += (p * 4); feedback += f
        p,f = strTest(solution4.shortest_path('A', 'K'),
                       student4.shortest_path('A', 'K'),
                      "\n\tGraph.shortest_path() failed")
        points += (p * 5); feedback += f

        # Check for cheating
        rawcode = inspect.getsource(s.Graph.shortest_path).splitlines()[21:]
        code = ""
        for line in rawcode: code += line
        if len(code.partition('shortest_path(')[1]) > 0:
            for line in rawcode: print line
            print("\nEnter 1 if the above code is NetworkX-free")
            p,f = grade(1, "\n\tNetworkX cannot be used for problem 4!")
            points *= p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 5: 10 points
        feedback += "\n\nTesting problem 5 (10 points):"
        points = 0

        solution1 = convert_to_networkx(solution1.dictionary)
        solution2 = convert_to_networkx(solution2.dictionary)
        solution3 = convert_to_networkx(solution3.dictionary)
        solution4 = convert_to_networkx(solution4.dictionary)
        student1 = s.convert_to_networkx(student1.dictionary)
        student2 = s.convert_to_networkx(student2.dictionary)
        student3 = s.convert_to_networkx(student3.dictionary)
        student4 = s.convert_to_networkx(student4.dictionary)
        node_message = "\n\tconvert_to_networkx() failed (nodes)"
        edge_message = "\n\tconvert_to_networkx() failed (edges)"

        p,f = strTest(solution1.nodes(), student1.nodes(), node_message)
        points += p; feedback += f
        p,f = strTest(solution2.nodes(), student2.nodes(), node_message)
        points += p; feedback += f
        p,f = strTest(solution3.nodes(), student3.nodes(), node_message)
        points += p; feedback += f
        p,f = strTest(solution4.nodes(), student4.nodes(), node_message)
        points += (p * 2); feedback += f
        p,f = strTest(solution1.edges(), student1.edges(), edge_message)
        points += p; feedback += f
        p,f = strTest(solution2.edges(), student2.edges(), edge_message)
        points += p; feedback += f
        p,f = strTest(solution3.edges(), student3.edges(), edge_message)
        points += p; feedback += f
        p,f = strTest(solution4.edges(), student4.edges(), edge_message)
        points += (p * 2); feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 6: 10 points
        feedback += "\n\nTesting problem 6 (10 points):"
        points = 0
        sBacon = s.BaconSolver()
        
        try: # Test invalid input
            sBacon.path_to_bacon("Bad Name")
            feedback += "\n\tBaconSolver.path_to_bacon(x) failed"
            feedback += " to raise an exception for invalid x"
        except ValueError: points += 2
        
        try: # Test no connection to Kevin Bacon
            sBacon.path_to_bacon("Arandi, Jose")
            feedback += "\n\tBaconSolver.path_to_bacon('Arandi, Jose') failed"
            feedback += " to raise an exception for no connection to target"
        except nx.NetworkXNoPath: points += 2
        
        # Test BaconSolver.path_to_bacon() for valid cases
        print("Student path from Thurman, Uma to Bacon, Kevin:")
        print(sBacon.path_to_bacon('Thurman, Uma'))
        p,f = grade(2,
            "\n\tBaconSolver.path_to_bacon('Thurman, Uma') failed")
        points += p; feedback += f
        print("Student path from Bartseh, Peter to Bacon, Kevin:")
        print(sBacon.path_to_bacon('Bartseh, Peter'))
        p,f = grade(2,
            "\n\tBaconSolver.path_to_bacon('Bartseh, Peter') failed")
        points += p; feedback += f
        print("Student path from Clooney, George to Damon, Matt:")
        print(sBacon.path_to_bacon('Clooney, George', 'Damon, Matt'))
        p,f = grade(2,"\n\tBaconSolver.path_to_bacon("
                        + "'Clooney, George', 'Damon, Matt') failed")
        points += p; feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 7: 10 points
        feedback += "\n\nTesting problem 7 (10 points):"
        points = 0
        sBacon = s.BaconSolver()
        
        try: # Test invalid input
            sBacon.bacon_number("Bad Name")
            feedback += "\n\tBaconSolver.bacon_number(x) failed"
            feedback += " to raise an exception for invalid x"
        except ValueError: points += 1
        
        try: # Test no connection to Kevin Bacon
            sBacon.bacon_number("Arandi, Jose")
            feedback += "\n\tBaconSolver.bacon_number('Arandi, Jose') failed"
            feedback += " to raise an exception for no connection to target"
        except nx.NetworkXNoPath: points += 1

        # Test BaconSolver.bacon_number() for valid cases
        if 5 == sBacon.bacon_number('Bartseh, Peter'): points += 1
        else:
            feedback += "\n\tBaconSolver.bacon_number('Bartseh, Peter') failed"
        if 2 == sBacon.bacon_number('Clooney, George', 'Damon, Matt'):
            points += 1
        else:
            feedback += "\n\tBaconSolver.bacon_number("
            feedback += "'Clooney, George', 'Damon, Matt') failed"
        
        # Test BaconSolver.average_bacon()
        average, isolated = sBacon.average_bacon()
        if 847 == isolated: points += 2
        else:
            feedback += "\n\tBaconSolver.average_bacon() failed"
            feedback += " for actors not connected to Kevin Bacon"
        if abs(average - 2.66) < .01: points += 4
        else:
            feedback += "\n\tBaconSolver.average_bacon() failed"
            feedback += " for average Bacon number"
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    if hasattr(sBacon, 'plot_bacon'):
        try:    # Problem 8: 3 points
            feedback += "\n\nTesting problem 8 (3 points):"
            points = 0
            sBacon.plot_bacon()
            p,f = grade(3, "\n\tBaconSolver.plot_bacon() failed")
            points += p; feedback += f
            
            score += points; feedback += "\nScore += " + str(points)
        except Exception as e: feedback += "\nError: " + e.message
 
    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback
