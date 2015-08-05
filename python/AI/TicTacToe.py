# class for a player
class TicTacToePlayer:
	def __init__(self, t, m):
		self.t = t
		self.m = m

# class for tic tac toe game
class TicTacToe:
	# declaring and defining private variables
	__magicSq = (4, 9, 2, 3, 5, 7, 8, 1, 6)
	__board = [[" " for x in range(3)] for x in range(3)]
	players = []

	# contructor to take the turn order
	def __init__(self, player1, player2):
		self.players.append(player1)
		self.players.append(player2)

	# function to return possible result
	def __make2(self):
		# return center position if blank
		if self.__board[1][1] == " " :
			return (1,1)
		else :
			# return a non corner point
			for i in range(0, 3):
				j = self.__board[i].index(" ")
				if (not (i%2==0 ^ j%2==0)) :
					return (i,j)

			# return any blank point
			for i in range(0, 3):
				j = self.__board[i].index(" ")
				if (j>=0) :
					return (i,j)

	# function to make the move
	def go(self, pos, player):
		self.__board[pos[0]][pos[1]] = self.players[player].m

	# function to check wining position
	def posswin(self, mark):
		# for all row
		for i in range(0, 3) :
			count = 0
			for j in range(0, 3) :
				if (self.__board[i][j] == mark) :
					count += 1
			if (count > 1 and count < 3) :
				for j in range(0, 3) :
					if (self.__board[i][j] == " ") :
						return (i,j)
		# for all column
		for i in range(0, 3) :
			count = 0
			for j in range(0, 3) :
				if (self.__board[j][i] == mark) :
					count += 1
			if (count > 1 and count < 3) :
				for j in range(0, 3) :
					if (self.__board[j][i] == " ") :
						return (j,i)
		# for both diagonals
		count = 0
		for i in range(0, 3) :
			if (self.__board[i][i] == mark) :
				count += 1
		if (count > 1 and  count < 3) :
			for i in range(0, 3) :
				if (self.__board[i][i] == " ") :
					return (i,i)
		count = 0
		for i in range(0, 3) :
			if (self.__board[i][2-i] == mark) :
				count += 1
		if (count > 1 and count < 3) :
			for i in range(0, 3) :
				if (self.__board[i][2-i] == " ") :
					return (i,2-i)
		return (-1,-1)

	# check if player tieh 'mark' has won
	def checkWin(self, mark):
		# for all rows
		for i in range(0, 3) :
			count = 0
			for j in range(0, 3):
				if (self.__board[i][j] == mark) :
					count += 1
			if (count==3) :
				return True

		# for all columns
		for i in range(0, 3):
			count = 0
			for j in range(0, 3):
				if (self.__board[j][i] == mark) :
					count += 1
			if (count==3) :
				return True

		# for both diagonals
		count = 0
		for i in range(0, 3) :
			if (self.__board[i][i] == mark) :
				count += 1
		if (count == 3) :
			return True

		count = 0
		for i in range(0, 3) :
			if(self.__board[i][2-i] == mark) :
				count += 1
		if (count == 3) :
			return True

		# if no combo found
		return False

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
		if (turn<4) :
			if (turn==0) :
				self.go([0,0], 0)
			elif (turn==1) :
				if (self.__board[1][1] == " ") :
					self.go([1,1], 1)
				else :
					self.go([0,0], 1)
			elif (turn==2) :
				if (self.__board[2][2] == " ") :
					self.go([2,2], 0)
				else :
					self.go([0,2], 0)
			else :
				poss = self.posswin(self.players[1].m)
				if (poss != (-1, -1)):
					self.go(poss, 1)
				else :
					self.go(self.__make2(), 1)
		else :
			if (turn%2==0) :
				mark1 = self.players[0].m
				mark2 = self.players[1].m
			else :
				mark1 = self.players[1].m
				mark2 = self.players[0].m
			poss = self.posswin(mark1)
			if (poss != (-1, -1)) :
				self.go(poss, turn%2)
			else :
				poss = self.posswin(mark2)
				if (poss != (-1, -1)) :
					self.go(poss, turn%2)
				else :
					self.go(self.__make2(), turn%2)

	# check if the given cell is empty
	def checkEmpty(self, pos) :
		if(self.__board[pos[0]][pos[1]] == " ") :
			return True
		else :
			return False

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
game = TicTacToe(TicTacToePlayer(p1T, p1M), TicTacToePlayer(p2T, p2M))

# every turn on thte board
game.printB()
for i in range(0, 9):
	p = i%2
	# check who's turn is it
	if (game.players[p].t == "c") :
		game.turnComputer(i)
	else :
		# loop untill valid data is inputted
		while True :
			inStr = input("Enter coordinates of next turn (x,y) : ")
			inStr = inStr.split(',')
			coor = [int(inStr[0]), int(inStr[1])]
			# check if the cell is empty at the inputed location
			if (game.checkEmpty(coor)) :
				game.go(coor, p)
				break
			else :
				print("The position is not free, try again")
	# print the game board
	game.printB()
	# check if the player has won
	if (game.checkWin(game.players[p].m)) :
		print("Player "+str(p)+" wins")
		break;
