class GameBoard:
    def __init__(self, l=[]):
        self.board = l

        if self.board == []:
            for _ in range(4):
                self.board.append([None]*4)

    def getElems(self):
        return self.board

    def updateIndex(self, i1, i2, val):
        self.board[i1][i2] = val

    def lostNoSpace(self):
        for l in self.board:
            if None in l:
                return False
        return True

    def __str__(self):
        return str(self.board)