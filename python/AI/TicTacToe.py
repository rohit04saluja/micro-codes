# class for a player
class TicTacToePlayer:
	def __init__(self, t, m):
		self.t = t
		self.m = m

# class for tic tac toe game
class TicTacToe:
	# declaring and defining private variables
	__magicSq = (4, 9, 2, 3, 5, 7, 8, 1, 6)
	__board = [[2]*3]*3

	# contructor to take the turn order
	def __init__(self, player1, player2):
		self.players[0] = player1
		self.players[1] = player2

	# function to return possible result
	def make2(self):
		# return center position if blank
		if self.__board[1][1] == 2 :
			return (1,1)
		else :
			# return a non corner point
			for i in range(0, 3):
				j = self.__board[i].index(2)
				if (not (i%2==0 ^ j%2==0)) :
					return (i,j)

			# return any blank point
			for i in range(0, 3):
				j = self.__board[i].index(2)
				if (j>=0) :
					return (i,j)

	# function to make the move
	def go(self, pos, player):
		self.__board[pos[0]][pos[1]] = self.players[player][1]

	# function to check wining position
	def posswin(self, player):
		mark = self.players[player].mark

	# function to print the board
	def printB(self):
		print("")
		print(" "+str(self.__board[0][0])+" | "+str(self.__board[0][1])+" | "+str(self.__board[0][2]))
		print("---+---+---")
		print(" "+str(self.__board[1][0])+" | "+str(self.__board[1][1])+" | "+str(self.__board[1][2]))
		print("---+---+---")
		print(" "+str(self.__board[2][0])+" | "+str(self.__board[2][1])+" | "+str(self.__board[2][2]))
		print("")

	# function for the computer's move
	def turnComputer(self, turn):
		if (turn>2) :
			func = "__turn2"
			func(turn)
		else
			func = "__turn"+str(turn)
			func()

	# set of functions for every move
	def __turn0():
		go([0,0])

	def __turn1(self):
		if (self.__board[1][1] == 2) :
			go([1,1])
		else :
			go([0,0])

	def __turn2(self):
		if (self.__board[2][2] == 2) :
			go([2,2])
		else :
			go([0,2])
	def __turn3(self):
		if (posswin(self.players[1].mark) != 0):
			go(posswin(self.players[1].mark))

# main execution of the program
# welcome message
print("Welcom to Tic Tac Toe")

# initialize players
p1T = input("Player1 type? (c/p) : ")
p1M = input("Player1 mark? (X/O) : ")
p2T = input("Player2 type? (c/p) : ")
p2M = "X"
if (p1M == "X") :
	p2M = "O"

# initialize players
game = TicTacToe(Player(p1T, p1M), Player(p2T, p2M))

# every turn on thte board
for i in range(0, 9):
	game.printB()
