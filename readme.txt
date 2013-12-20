I wrote this using Python 2.7.5.  Note that Python isn't my "first language", so to speak, but for a problem of this caliber it seemed simplest to just write a small Python class and some tests rather than build up a more heavyweight app.

This class has an init method for creating a new Game instance with a game board.
There's an instance variable that holds the board for a given game.

The following methods are available on a game instance:
printBoard() - prints the current board to the terminal

sumNeighbors(i, j,rowLength, colLength) - given a position i, j and the dimensions of the game board, find the total number of living neighbor cells and return it

newStatus(score,oldStatus) - given the neighbor score and the previous status of this cell, calculate a new status

evolveBoard() - iterates over each position in a game board, calling sumNeighbors and newStatus to find the new status for each position. Builds a new game board and saves it in a new GameOfLife instance - this could be modified to just replace the board in the current instance, but you'd want to make sure to do that after you were finished calculating so that you don't muck up the calculations as you go.






You can run the game on your own input from a python interpreter as follows:

>>> import GameOfLife
>>> gameBoard = GameOfLife.GameOfLife([[0,1,0,0,0],
...                                         [1,0,0,1,1],
...                                         [1,1,0,0,1],
...                                         [0,1,0,0,0],
...                                         [1,0,0,0,1]])
>>> newGame = gameBoard.evolveBoard()
>>> newGame.printBoard()
[0, 0, 0, 0, 0]
[1, 0, 1, 1, 1]
[1, 1, 1, 1, 1]
[0, 1, 0, 0, 0]
[0, 0, 0, 0, 0]



Alternately, you can see an example based on the original problem simply by running the script:
$ python GameOfLife.py




You can run the unit tests in TestGameOfLife from a command line:
$ python TestGameOfLife.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK

