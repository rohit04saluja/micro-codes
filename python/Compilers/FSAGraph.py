# import essential modules
import Graph
import PolishNotation

class Graph(Graph.Graph) :
	__opSet = {'*':[4,1], '+':[4,1], '?':[3,1], '|':[2,2], '.':[1,2]}
	__regExpr = ""
	start = ""
	end = ""

	def __init__(self, sigma) :
		self.__sigma = sigma
	
	def setRegExpr(self, regExpr):
		self.__regExpr = regExpr

	def getRegExpr(self):
		if (self.__regExpr == "") :
			print("No regualr expression stored")
			return ""
		else :
			return self.__regExpr

	# function to create sub graph for an operator
	def __ThomsonOperator(self, op, stack):
		if (op == '*') :
			start,end = stack.pop()
			self.createLink(end, start, "Ep")
			startNew = self.sizeOfGraph()
			endNew = startNew + 1
			self.createNode(startNew)
			self.createNode(endNew)
			self.createLink(startNew, start, "Ep")
			self.createLink(startNew, endNew, "Ep")
			self.createLink(end, endNew, "Ep")
			# push the new sub graph back on the stack
			stack.append((startNew,endNew))
		elif (op == '+') :
			start,end = stack.pop()
			self.createLink(end, start, "Ep")
			startNew = self.sizeOfGraph()
			endNew = startNew + 1
			self.createNode(startNew)
			self.createNode(endNew)
			self.createLink(startNew, start, "Ep")
			self.createLink(end, endNew, "Ep")
			# push the new sub graph back on the stack
			stack.append((startNew,endNew))
		elif (op == '?') :
			start,end = stack.pop()
			endNew = self.sizeOfGraph()
			self.createLink(end, endNew, "Ep")
			self.createLink(start, endNew, "Ep")
			# push the new sub graph back on the stack
			stack.append((start,endNew))
		elif (op == '|') :
			# pop twice for operands
			start1,end1 = stack.pop()
			start2,end2 = stack.pop()
			# join the start and end of the above sub graphs
			start = self.sizeOfGraph()
			end = start+1
			self.createNode(start)
			self.createNode(end)
			self.createLink(start, start1, "Ep")
			self.createLink(start, start2, "Ep")
			self.createLink(end1, end, "Ep")
			self.createLink(end2, end, "Ep")
			# push the new sub graph back on the stack
			stack.append((start,end))
		elif (op == '.') :
			# pop twice for operands
			start1,end1 = stack.pop()
			start2,end2 = stack.pop()
			# link both the graphs with and epsilon
			self.createLink(end2, start1, "Ep")
			# push the new sub graph back on the the stack
			stack.append((start2, end1))
		else :
			print("Invaid operator")
		return stack

	# function to create sub graph for an operand
	def __ThomsonOperand(self, op):
		# create link between 2 nodes with trasition as operand
		start = self.sizeOfGraph()
		end = start + 1
		self.createNode(start)
		self.createNode(end)
		self.createLink(start, end, op)
		return (start,end)

	# function to create NFA from given regular expression
	def createNFAFromRegExpr(self):
		# get postfix of the regular expression
		postfix = PolishNotation.InfixToPostfix(self.__regExpr, self.__sigma, self.__opSet)
		stack = []
		for i in range(0, len(postfix)) :
			if postfix[i] in self.__opSet :
				stack = self.__ThomsonOperator(postfix[i], stack)
			elif postfix[i] in self.__sigma :
				stack.append(self.__ThomsonOperand(postfix[i]))
			else :
				print("Undefined character found in the regular expression")
				return
		self.start,self.end = stack.pop()

	def printFSA(self):
		print("Start Node: "+str(self.start))
		print("End Node: "+str(self.end))
		print("Graph:")
		self.printg()
