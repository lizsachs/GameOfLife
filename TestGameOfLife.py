import GameOfLife
import unittest
import GameOfLifeError

class TestGameOfLife(unittest.TestCase):
        
	def test_SampleBoard(self):
		# make sure the example given in the original problem works
		self.initialGame = GameOfLife.GameOfLife([[0,1,0,0,0],
												  [1,0,0,1,1],
												  [1,1,0,0,1],
												  [0,1,0,0,0],
												  [1,0,0,0,1]])
		self.targetGame = GameOfLife.GameOfLife([[0,0,0,0,0],
											 	 [1,0,1,1,1],
											 	 [1,1,1,1,1],
											 	 [0,1,0,0,0],
											 	 [0,0,0,0,0]])
		newGame = self.initialGame.evolveBoard()
		# make sure new game is equal to expected game
		self.assertEqual(self.targetGame.board,newGame.board)

		
	def test_IncorrectBoard(self):
		# double check that we can test when boards are NOT equal
		self.initialGame = GameOfLife.GameOfLife([[0,1,0,0,0],
												  [1,0,0,1,1],
												  [1,1,0,0,1],
												  [0,1,0,0,0],
												  [1,0,0,0,1]])
		self.targetGame = GameOfLife.GameOfLife([[0,0,0,0,0],
											 	 [1,0,1,1,1],
											 	 [1,1,1,1,1],
											 	 [0,1,0,0,0],
											 	 [0,0,0,0,0]])
		# show boards are not equal
		self.assertNotEqual(self.targetGame.board, self.initialGame.board)
		
	def test_Underpopulation(self):
		self.initialGame = GameOfLife.GameOfLife([[0,0,0],
												  [0,1,0],
												  [1,0,0]])
		self.targetGame = GameOfLife.GameOfLife([[0,0,0],
											 	 [0,0,0],
											 	 [0,0,0]])
		newGame = self.initialGame.evolveBoard()
		# make sure new game is equal to expected game
		self.assertEqual(self.targetGame.board, newGame.board)
		
	def test_Survival(self):
		self.initialGame = GameOfLife.GameOfLife([[1,0,0],
												  [0,1,0],
												  [0,0,1]])
		self.targetGame = GameOfLife.GameOfLife([[0,0,0],
											 	 [0,1,0],
											 	 [0,0,0]])
		newGame = self.initialGame.evolveBoard()
		# make sure new game is equal to expected game
		self.assertEqual(self.targetGame.board, newGame.board)
		
	def test_Overcrowding(self):
		self.initialGame = GameOfLife.GameOfLife([[1,0,1],
												  [0,1,0],
												  [1,0,1]])
		self.targetGame = GameOfLife.GameOfLife([[0,1,0],
											 	 [1,0,1],
											 	 [0,1,0]])
		newGame = self.initialGame.evolveBoard()
		# make sure new game is equal to expected game
		self.assertEqual(self.targetGame.board, newGame.board)
			
	def test_NonSquareBoard(self):
		# test ability to handle rectangular but non square boards
		self.initialGame = GameOfLife.GameOfLife([[0,1,0],
												  [1,0,0],
												  [1,1,0],
												  [0,1,0],
												  [1,0,0]])
		self.targetGame = GameOfLife.GameOfLife([[0,0,0],
												  [1,0,0],
												  [1,1,0],
												  [0,1,0],
												  [0,0,0]])

		newGame = self.initialGame.evolveBoard()
		# make sure new game is equal to expected game
		self.assertEqual(self.targetGame.board, newGame.board)

		
	def test_MalformedBoard(self):
		# test exception handing when boards are not rectangular
		self.initialGame = GameOfLife.GameOfLife([[0,1,0,0],
												  [1,0,0,1,1],
												  [1,1,0,0,1,1,0],
												  [0,1,0],
												  [1,0,0,0,1]])

		with self.assertRaises(GameOfLifeError.RectangleError):
			self.initialGame.evolveBoard()
			
	def test_InvalidValue(self):
		# test exception handling when a board with invalid values is submitted
		self.initialGame = GameOfLife.GameOfLife([[0,3],
											 	  [1,0]])

		with self.assertRaises(GameOfLifeError.ValueError) as e:
			self.initialGame.evolveBoard()
			
		self.assertEqual(e.exception.val, 3)
		
	def test_NewStatus_Underpopulation(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		newStatus = self.initialGame.newStatus(1,1)
		self.assertEqual(newStatus,0)
		
	def test_NewStatus_Survival(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		newStatus = self.initialGame.newStatus(3,1)
		self.assertEqual(newStatus,1)  
		
	def test_NewStatus_Overcrowding(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		newStatus = self.initialGame.newStatus(4,1)
		self.assertEqual(newStatus,0)   
		
	def test_NewStatus_Reproduction(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		newStatus = self.initialGame.newStatus(3,0)
		self.assertEqual(newStatus,1)
		
	def test_NewStatus_Reproduction_Negative(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		newStatus = self.initialGame.newStatus(2,0)
		self.assertEqual(newStatus,0)
		
	def test_NewStatus_Bad_Value(self):
		self.initialGame = GameOfLife.GameOfLife([[]])
		
		with self.assertRaises(GameOfLifeError.ValueError) as e:
			self.initialGame.newStatus(2,2)
			
		self.assertEqual(e.exception.val, 2)
		
	def test_CheckBoardSize_Error(self):
		# test exception handing when boards are not rectangular
		self.initialGame = GameOfLife.GameOfLife([[0,1,0,0],
												  [1,0,0,1,1]])

		with self.assertRaises(GameOfLifeError.RectangleError):
			self.initialGame.checkBoardSize()
			
	def test_CheckBoardSize(self):
		# test exceptions not thrown when boards are rectangular
		self.initialGame = GameOfLife.GameOfLife([[0,1,0,0],
												  [1,0,0,1]])

		self.initialGame.checkBoardSize() # error should not be thrown
		
		
       
if __name__ == '__main__':
    unittest.main()