# Importing the necessary modules
import Graph
import PolishNotation

# Defining the class
class FSAGraph() :
	# Definign the operation set
	__opSet = {'*':[4,1], '+':[4,1], '?':[3,1], '|':[2,2], '.':[1,2]}

	def __init__(self, sigma) :
		# Initialise the sigma
		self.__sigma = sigma
	
	# Set a regular expression
	def setRegExpr(self, regExpr):
		# Transform the regular expression according the Automata
		p = regExpr[0]
		out = p
		for i in range(1, len(regExpr)) :
			c = regExpr[i]
			if ((p in self.__sigma and c in self.__sigma) or (p in self.__opSet and self.__opSet[p][1]==1)) :
				out += "."
			out += c
			p = c
		print out
		self.__regExpr = out

	# Get the regular expression
	def getRegExpr(self):
		if (not self.__regExpr) :
			print("No regualr expression stored")

			return ""
		else :
			return self.__regExpr

	# Get the sigma for the NFA
	def getSigma():
		return self.__sigma

	# Function to create sub graph for an operator
	def __ThomsonOperator(self, op, stack):
		# If else ladder for operators
		if (op == '*') :
			# Get the start and end node for the operator from the stack
			start,end = stack.pop()
			# Create a new link for the reverse
			self.__graphNFA.createLink(end, start, "Ep")
			# Get the new start and end node values
			startNew = self.__graphNFA.sizeOfGraph()
			endNew = startNew + 1
			# Create the new start and end nodes
			self.__graphNFA.createNode(startNew)
			self.__graphNFA.createNode(endNew)
			# Create the necessary links between all the nodes
			self.__graphNFA.createLink(startNew, start, "Ep")
			self.__graphNFA.createLink(startNew, endNew, "Ep")
			self.__graphNFA.createLink(end, endNew, "Ep")
			# Push the new sub graph back on the stack
			stack.append((startNew,endNew))
		elif (op == '+') :
			# Get the start and end node for the operator from the stack
			start,end = stack.pop()
			# Create a new link for the reverse
			self.__graphNFA.createLink(end, start, "Ep")
			# Get the new start and end node values
			startNew = self.__graphNFA.sizeOfGraph()
			endNew = startNew + 1
			# Create the new start and end nodes
			self.__graphNFA.createNode(startNew)
			self.__graphNFA.createNode(endNew)
			# Create the necessary links between all the nodes
			self.__graphNFA.createLink(startNew, start, "Ep")
			self.__graphNFA.createLink(end, endNew, "Ep")
			# Push the new sub graph back on the stack
			stack.append((startNew,endNew))
		elif (op == '?') :
			# Pop for the start and end of the sub graph
			start,end = stack.pop()
			# Get label for new end node
			endNew = self.__graphNFA.sizeOfGraph()
			# Create the new end node
			self.__graphNFA.createNode(endNew)
			# Create the necessary links between all the nodes
			self.__graphNFA.createLink(end, endNew, "Ep")
			self.__graphNFA.createLink(start, endNew, "Ep")
			# Push the new sub graph back on the stack
			stack.append((start,endNew))
		elif (op == '|') :
			# Pop twice for operands
			start1,end1 = stack.pop()
			start2,end2 = stack.pop()
			# Join the start and end of the above sub graphs
			start = self.__graphNFA.sizeOfGraph()
			end = start+1
			# Create the new start and end nodes
			self.__graphNFA.createNode(start)
			self.__graphNFA.createNode(end)
			# Create the necessary link between all the nodes
			self.__graphNFA.createLink(start, start1, "Ep")
			self.__graphNFA.createLink(start, start2, "Ep")
			self.__graphNFA.createLink(end1, end, "Ep")
			self.__graphNFA.createLink(end2, end, "Ep")
			# Push the new sub graph back on the stack
			stack.append((start,end))
		elif (op == '.') :
			# Pop twice for operands
			start1,end1 = stack.pop()
			start2,end2 = stack.pop()
			# Link both the graphs with and epsilon
			self.__graphNFA.createLink(end2, start1, "Ep")
			# Push the new sub graph back on the the stack
			stack.append((start2, end1))
		else :
			# Ouput for error
			print("Invaid operator")
		# Return the output in the stack
		return stack

	# Function to create sub graph for an operand
	def __ThomsonOperand(self, op):
		# Create link between 2 nodes with trasition as operand
		start = self.__graphNFA.sizeOfGraph()
		end = start + 1
		# Create the nodes and the link
		self.__graphNFA.createNode(start)
		self.__graphNFA.createNode(end)
		self.__graphNFA.createLink(start, end, op)
		# Return the start and end of the sub graph
		return (start,end)

	# Function to create NFA from given regular expression
	def createNFAFromRegExpr(self):
		# Check if regular expression exists
		if (self.__regExpr) :
			# Get postfix of the regular expression
			postfix = PolishNotation.InfixToPostfix(self.__regExpr, self.__sigma, self.__opSet)
			# Initializing stack and NFA graph
			stack = []
			self.__graphNFA = Graph.Graph()
			# For every element in the postfix conversion
			for i in postfix :
				# If else ladder for operator, operand and error
				if i in self.__opSet :
					stack = self.__ThomsonOperator(i, stack)
				elif i in self.__sigma :
					stack.append(self.__ThomsonOperand(i))
				else :
					print("Undefined character found in the regular expression")
					return
			# Getting the start and end of NFA
			self.NFAstart,self.NFAend = stack.pop()
		else :
			print("Regular expression was not found")

	# Function to print the NFA
	def printNFA(self) :
		# Check if NFA exists
		if (self.__graphNFA) :
			print("Start Node: "+str(self.NFAstart))
			print("End Node(s): "+str(self.NFAend))
			print("Graph:")
			self.__graphNFA.printg()
		else :
			print ("NFA was not found")
	
	# Function to print the NFA without E
	def printNFA_E(self) :
		if (self.__graphNFA_E) :
			print("Start Node: "+str(self.NFAEstart))
#			print("End Node(s): "+str(self.NFAEend))
			print("Graph:")
			self.__graphNFA_E.printg()
		else :
			print ("NFA without E not found")

	# Function to print DFA
	def printDFA(self) :
		if (self.__graphDFA) :
			print("Start Node: "+str(self.DFAstart))
#			print("End Node(s): "+str(self.DFAend))
			print("Graph:")
			self.__graphDFA.printg()
	
	# Function to create NFA without E from given NFA
	def createNFAWithoutEFromNFA(self) :
		# Check if NFA exits
		if (self.__graphNFA) :
			# Determine the start node
			self.NFAEstart = self.NFAstart
			sizeOfGraph = self.__graphNFA.sizeOfGraph()
			# Initializing the E closure table
			tbl = ['']*sizeOfGraph
			# Finding the E closure of all the nodes in the graph
			for i in range(sizeOfGraph) :
				tbl[i] = [self.__eClosure(i)]*len(self.__sigma)

			# Finding the E' of all the nodes in the E closure
			tbl = self.__eDash(tbl)
			
			# Finding the E closure of all the new nodes obtained
			j = 0
			for i in range(sizeOfGraph) :
				for j in range(len(self.__sigma)) :
					temp = tbl[i][j]
					t = set()
					for k in temp :
						t = t.union(set(self.__eClosure(k)))
					tbl[i][j] = list(t)
			
			# Finding the ending nodes of the graph
			# Create a new graph from the given table
			self.__graphNFA_E = Graph.Graph()
			for i in range(sizeOfGraph) :
				self.__graphNFA_E.createNode(i)
				for j in range(len(self.__sigma)) :
					for k in tbl[i][j] :
						self.__graphNFA_E.createLink(i, k, self.__sigma[j])
		else :
			print ("NFA was not found")

	# Function to find the E closure of the given node
	def __eClosure(self, start) :
		# Perform conditional search operation from the given node
		visited, queue = [], [start]
                while queue:
                        vertex = queue.pop(0)
                        if vertex not in visited:
                                visited.append(vertex)
				neigh = self.__graphNFA.getNeighbour(vertex)
				for v in neigh :
					if("Ep" in neigh[v] and v not in visited) :
		                                queue.append(v)
                return visited

	# Function to find out the E' of the given set
	def __eDash(self, tbl) :
		# Run a loop over every element in the table
		sizeOfGraph = self.__graphNFA.sizeOfGraph()
		for i in range(sizeOfGraph) :
			for j in range(len(self.__sigma)) :
				# Check and extract neighbours that hold the condition of select weight over the edge
				temp = []
				for node in tbl[i][j] :
					neigh = self.__graphNFA.getNeighbour(node)
					for v in neigh :
						if(self.__sigma[j] in neigh[v] and v not in temp) :
							temp.append(v)
				tbl[i][j] = temp
		# Return the update table status
		return tbl

	# Function to create NFA without E from regular expression
	def createNFAWithoutEFromRegExpr(self) :
		# Check if regular expression exists
		if(self.__regExpr) :
			# Conversion of regular expression to NFA to NFA without E
			self.createNFAFromRegExpr()
			self.createNFAWithoutEFromNFA()
		else :
			# Outputting error
			print("Regular expression was not found")

	# Function to create DFA from NFA without E
	def createDFAFromNFAWithoutE(self) :
		# Check if the graph of NFA without E exists
		if(self.__graphNFA_E) :
			
		else :
			# Outputting error
			print ("NFA without E was not found")

	# Function to create DFA from regular expression
	def createDFAFromRegExpr(self) :
		# Check if regualr expression exists
		if(self.__regExpr) :
			# Conversion of regular expression to NFA to NFA without E and then to DFA
			self.createNFAFromRegExpr()
			self.createNFAWithoutEFromNFA()
			self.createDFAFromNFAWithoutE()
		else :
			# Outputting error
			print ("Regular Expression was not found")
