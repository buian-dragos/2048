from src.domain.board import GameBoard
from copy import deepcopy

class Repo:
    def __init__(self):
        self._board = GameBoard()
        self._undo_board = None

    def getBoard(self):
        return self._board

    def checkIndex(self,i1,i2):
        if self._board.getElems()[i1][i2] is None:
            return True
        return False

    def updateIndex(self,i1,i2,val):
        self._board.updateIndex(i1, i2, val)

    def updateBoard(self,board: list):
        print("aaaa")
        print(str(self._undo_board))
        self._undo_board = deepcopy(GameBoard(self._board.getElems()))
        self._board = GameBoard(board)
        print(self._board)
        print(self._undo_board)

    def undo(self):
        self._board = GameBoard(self._undo_board.getElems())
        self._undo_board = None
