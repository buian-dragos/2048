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
        self._board = GameBoard(board)

    def updateUndo(self, undo):
        self._undo_board = deepcopy(undo)

    def undo(self):
        if self._undo_board is not None:
            self._board = GameBoard(self._undo_board)
            self._undo_board = None
