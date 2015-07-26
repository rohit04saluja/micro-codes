class Graph:
	__links = {}
	__values = {}

	def createGraphNode(self, label, value):
		self.__links[label] = []
		self.__values[label] = value

	def createGraphLink(self, s, d, t):
		self.__links[s].append({t:d})

	def createGraphLink(self, s, d):
		self.__links[s].append(d)

	def printGraph(self):
		print self.__links

	def getGraphNodeValue(self, label):
		return self.__values[label]

	def getNeighbour(self, label):
		return self.__links[label]

	def findPath(self, s, d, path=[]):
		# initialize the path
		path = path + [s]
		# check if source and destination are same
		if s == d :
			return path
		# check if source in the graph
		if s not in self.__links :
			return None
		# iterating for each vertex in 
		for vertex in self.__links[s] :
			if vertex not in path :
				pathExt = self.findPath(vertex, d, path)

				if pathExt :
					return pathExt
		return None

#	def findAllPaths(self, s, d, path=[]):
		
	def getDegree(self, label):
		return  len(self.__links[label])
