import GameOfLifeError

class GameOfLife:
	board = [[]]
	numCols = 0
	numRows = 0
	
	def __init__(self, board):
		self.board = board
		self.numCols = len(self.board[0])
		self.numRows = len(self.board)
	
	# print the current board
	def printBoard(self):
		for row in self.board:
			print row
	
	# find a cell's neighbor score = the number of neighbor cells that are living
	def calcNeighborScore(self, x, y):
		score = 0
		for xModifier in (-1, 0, 1):
			for yModifier in (-1, 0, 1):
				if not (xModifier == 0 and yModifier == 0):
					modifiedX = x+xModifier
					modifiedY = y + yModifier
					if (modifiedX >= 0 and modifiedY >= 0 and modifiedX < self.numRows and modifiedY < self.numCols):
						score = score + self.board[modifiedX][modifiedY]
		return score
	
	# based on the neighbor score and the previous status, find a cell's new status
	# 0 = dead cell
	# 1 = live cell
	def newStatus(self,score,oldStatus): 
		if oldStatus == 1:
			if score < 2:
				return 0
			elif score in (2, 3):
				return 1
			elif score > 3:
				return 0
		elif oldStatus == 0: 
			if score == 3:
				return 1
			else:
				return 0 
		else:
			raise GameOfLifeError.ValueError("This board contains an invalid value", oldStatus)
			
	
	def checkBoardSize(self):
		rowLen = len(self.board[0])
		for row in self.board:
			if len(row) != rowLen:
				raise GameOfLifeError.RectangleError("This board is not rectangular")
		
	# iterate over a game board evaluating each position to calculate a new value
	# make a new game instance to hold the new board - we don't want to overwrite current board as we go
	# because that would throw off calculations. We could replace the board in the current object instead of
	# creating a new one and returning it if we wish			
	def evolveBoard(self):
		newBoard = []
		self.checkBoardSize()
		for i,row in enumerate(self.board):
			newRow = []
			for j,colVal in enumerate(row):
				if self.board[i][j] not in (1,0):
					raise GameOfLifeError.ValueError("This board contains an invalid value", self.board[i][j])
				score = self.calcNeighborScore(i,j)
				newRow.append(self.newStatus(score,self.board[i][j]))
			newBoard.append(newRow)
		newGame = GameOfLife(newBoard)
		return newGame	
		
gameBoard = GameOfLife([[0,1,0,0,0],
                                         [1,0,0,1,1],
                                         [1,1,0,0,1],
                                         [0,1,0,0,0],
                                         [1,0,0,0,1]])
print "Original Board: "
gameBoard.printBoard()
newGame = gameBoard.evolveBoard()
print "Evolved Board: "
newGame.printBoard()