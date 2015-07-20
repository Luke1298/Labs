
def generate_graph_data(filename):
	file = open(filename, 'r')
	file = file.read()
	file = file.split('\n')
	
	lines = []
	for line in file[:-1]:
		line = line.split(',')
		nodes = []
		for node in line:
			nodes.append(node)
		lines.append(nodes)

	return lines
	


def generate_movie_data():

	file = 'movieData.txt'
	file = open(file, 'r')
	file = file.read()
	file = file.split('\n')

	graph = {}
	for line in file:
		names = line.split('/')
		movie = names[0]
		graph[movie] = []
		for actor in names[1:]:
			graph[movie].append(actor)

	return graph			
