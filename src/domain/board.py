from copy import deepcopy


class GameBoard:
    def __init__(self, l=[]):
        self._board = l

        if self._board == []:
            for _ in range(4):
                self._board.append([None] * 4)

    def getElems(self):
        return deepcopy(self._board)

    def updateIndex(self, i1, i2, val):
        self._board[i1][i2] = val

    def lostNoSpace(self):
        for l in self._board:
            if None in l:
                return False
        return True

    def __str__(self):
        return str(self._board)