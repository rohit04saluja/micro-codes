# Class for the jug in the problem
class Jug:
	# Initializing the jug
	def __init__(self, c, vol=0) :
		self.cap = c
		self.vol = vol

	# Method to returnn if jug can hold given volume
	def canhold(self, vol) :
		return self.vol+vol<self.cap

	# Method to return if the jug is full
	def full(self) :
		return self.vol == self.cap

	# Method to return if the jug is empty
	def empty(self) :
		return self.vol==0

	# Overloading == operator
	def __eq__(self, other) :
		return self.cap == other.cap and self.vol == other.vol

	# Overloading the string output
	def __str__(self) :
		return "volume={0}, capacity={1}".format(self.vol, self.cap)

# Class for Problem State for the state search algorithm
class State:
	# Initialize the state	
	def __init__(self, jug1, jug2) :
		self.jug1 = jug1
		self.jug2 = jug2

	# Method to define the next possible state
	def nextState(self) :
		ns = []
		#1# Fill jug1 to full capacity
		if(not self.jug1.full()) :
			ns.append(State(Jug(self.jug1.cap, self.jug1.cap), jug2))
		#2# Fill jug2 to full capacity
		if(not self.jug2.full()) :
			ns.append(State(jug1, Jug(self.jug2.cap, self.jug2.cap)))
		#3# Empty jug1
		if(not self.jug1.empty()) :
			ns.append(State(Jug(self.jug1.cap), jug2))
		#4# Empty jug2
		if(not self.jug2.empty()) :
			ns.append(State(jug1, Jug(self.jug2.cap)))
		#5# Transfer from jug1 to jug2
		if(self.jug2.cap-self.jug2.vol < self.jug1.vol) :
			ns.append(Jug(self.jug1.cap, self.jug1.vol-(self.jug2.cap-self.jug2.vol)), Jug(self.jug2.cap, self.jug2.cap))
		elif(self.jug2.cap-self.jug2.vol == self.jug1.vol) :
			ns.append(Jug(self.jug1.cap), Jug(self.jug2.cap, self.jug2.cap))
		else :
			ns.append(Jug(self.jug1.cap), Jug(self.jug2.cap, self.jug2.vol+self.jug1.vol))
		#6# Transfer from jug2 to jug1
		if(self.jug1.cap-self.jug1.vol < self.jug2.cap) :
			ns.append(Jug(self.jug1.cap, self.jug1.cap), Jug(self.jug2.cap, self.jug2.vol-(self.ju1.cap-self.jug1.vol)))
		elif(self.jug1.cap-self.jug1.vol < self.jug2.cap) :
			ns.append(Jug(self.jug1.cap, self.jug1.cap), Jug(self.jug2.cap))
		else :
			ns.append(Jug(self.jug1.cap, self.jug1.vol+self.jug2.vol), Jug(self.jug2.cap))
		# Return the list of possible next states
		return ns

	# Overloading == operator
	def __eq__(self, other) :
		return self.jug1 == other.jug1 and self.jug2 == other.jug2

	# Overloading the string output
	def __str__(self) :
		return "<Jug1: {0}, Jug2: {1}>".format(self.jug1, self.jug2)

class Game:
	__path = []
	# Initializing the game
	def __init__(self, jug1, jug2, vol) :
		self.__ini = State(jug1, jug2)
		self.__vol = vol
		if(jug1.canhold(vol)) :
			jug1.add(vol)
		else :
			jug2.add(vol)
		self.__des = State(jug1, jug2)

	# Method to solve the problem
	def solve(self) :
		if(self.__path) :
			# Find path from source and destination state
			self.__path = self.__findPath(self.__ini, self.__des)
		else :	
			return self.__path

	def __findPath(self, s, d, path=[]) :
		# Initialize the path
		path += [s]
		# Check if souce and destination are same
		if(s==d) :
			path += [d]
		# Iterate for all possible states
		for state in s.nextState() :
			if(state not in path) :
				pathExt = self.__findPath(state, d, path)
				# return obtained path if it is not empty
				if(pathExt) :
					return pathExt
		return None

# Initialize the game
cap1 = int(input("Enter capacity of jug1: "))
cap2 = int(input("Enter capacity of jug2: "))
vol = int(input("Enter the final volume desired: "))

# Initialize the game
game = Game(Jug(cap1), Jug(cap2), vol)
path = game.solve()
for s in path :
	print(s)
