class Graph:
	__graph = {}

	def createNode(self, label):
		self.__graph[label] = {}

	def createLink(self, s, d, t):
		if( d in self.__graph[s] ) :
			self.__graph[s][d].append(t)
		else :
			self.__graph[s].update({d:[t]})

	def printg(self):
		print self.__graph

	def getNeighbour(self, label):
		return self.__graph[label]
		
	def getDegree(self, label):
		return len(self.__graph[label])

	def dfs(self, start, visited=None):
		if visited is None:
			visited = set()
		visited.add(start)
		for next in graph[start] - visited:
			dfs(graph, next, visited)
		return visited

	def dfsPaths(self, start, goal, path=None):
		if path is None:
			path = [start]
		if start == goal:
			yield path
		for next in self.__graph[start] - set(path):
			yield dfsPaths(next, goal, path + [next])

	def bfs(self, start):
		visited, queue = set(), [start]
		while queue:
			vertex = queue.pop(0)
			if vertex not in visited:
				visited.add(vertex)
				queue.extend(self.__graph[vertex] - visited)
		return visited

	def bfs_paths(self, start, goal):
		queue = [(start, [start])]
		while queue:
			(vertex, path) = queue.pop(0)
			for next in self.__graph[vertex] - set(path):
				if next == goal:
					yield path + [next]
				else:
					queue.append((next, path + [next]))

	def sizeOfGraph(self) :
		return len(self.__graph)
