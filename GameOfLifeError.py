class GameOfLifeError(Exception):
    """Base class for exceptions in this module."""
    pass

class RectangleError(GameOfLifeError):
    """Exception raised when a game board is not rectangular.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

class ValueError(GameOfLifeError):
    """Raised when a value that is not 1 or 0 is found on the board

    Attributes:
        val -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, msg, val):
        self.val = val
        self.msg = msg
