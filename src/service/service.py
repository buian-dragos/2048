from src.repo.repo import Repo
from random import randint
from copy import deepcopy

class Service:
    def __init__(self, repo):
        self._repo = repo

    def start(self):
        board = deepcopy(self.randomGenerator(self._repo.getBoard().getElems()))

        self._repo.updateBoard(board)

    def randomGenerator(self,board):
        print(board)

        i1 = randint(0,3)
        i2 = randint(0,3)
        val = randint(0,5)

        if val == 5:
            val = 4
        else:
            val = 2

        if board[i1][i2] == None:
            board[i1][i2] = val
            return board
        return self.randomGenerator(board)


    def upgrade(self,line):
        for i in range(0,len(line)-1):
            for j in range(i + 1,len(line)):
                if line[i] == line[j] and line[i] is not None:
                    line[i] = None
                    line[j] *= 2
                    i = j
                    break
                elif line[j] is not None:
                    break
        return line

    def moveOne(self,line):
        for i in range(0,len(line) - 1):
            for j in range(i + 1, len(line)):
                if line[i] is None and line[j] is not None:
                    line[i], line[j] = line[j], None
                    break

        return line

    def moveAll(self,board: list):
        check_board = deepcopy(board)

        temp_board = []
        for line in board:
            temp_board.append(self.upgrade(line))

        board.clear()

        for line in temp_board:
            board.append(self.moveOne(line))

        if board != check_board:
            board = self.randomGenerator(board)

        return board



    def test_move(self):
        self._repo.updateIndex(0, 0, 2)
        self._repo.updateIndex(1, 0, 4)
        self._repo.updateIndex(2, 0, 4)
        self._repo.updateIndex(3, 0, 4)

        print(self._repo.getBoard().getElems())

    def flipFromLeft(self):

        board = self._repo.getBoard().getElems()
        self._repo.updateUndo(self._repo.getBoard().getElems())
        self.flipToLeft(self.moveAll(board))

    def flipFromRight(self):
        board = self._repo.getBoard().getElems()

        temp_board = []

        for line in board:
            for i in range(len(line)//2):
                line[i], line[len(line)-i-1] = line[len(line)-i-1], line[i]

            temp_board.append(line)

        self._repo.updateUndo(self._repo.getBoard().getElems())
        self.flipToRight(self.moveAll(temp_board))


    def flipFromUp(self):
        board = self._repo.getBoard().getElems()

        temp_board = []

        for i in range(len(board[0])):
            line = []
            for j in range(len(board[0])):
                line.append(board[j][i])
            temp_line = deepcopy(line)
            temp_board.append(temp_line)

        self._repo.updateUndo(self._repo.getBoard().getElems())
        self.flipToUp(self.moveAll(temp_board))

    def flipFromDown(self):
        board = self._repo.getBoard().getElems()

        temp_board = []

        for i in range(len(board[0])):
            line = []
            for j in range(len(board[0])):
                line.append(board[j][i])
            temp_line = deepcopy(line)
            temp_board.append(temp_line)

        board.clear()

        for line in temp_board:
            for i in range(len(line) // 2):
                line[i], line[len(line) - i - 1] = line[len(line) - i - 1], line[i]

            board.append(line)

        self._repo.updateUndo(self._repo.getBoard().getElems())
        self.flipToDown(self.moveAll(temp_board))

    def flipToLeft(self,board):
        self._repo.updateBoard(board)

    def flipToRight(self,board):
        temp_board = []

        for line in board:
            for i in range(len(line) // 2):
                line[i], line[len(line) - i - 1] = line[len(line) - i - 1], line[i]

            temp_board.append(line)
        self._repo.updateBoard(temp_board)


    def flipToUp(self,board):
        temp_board = []

        for i in range(len(board[0])):
            line = []
            for j in range(len(board[0])):
                line.append(board[j][i])
            temp_line = deepcopy(line)
            temp_board.append(temp_line)

        board.clear()

        self._repo.updateBoard(temp_board)

    def flipToDown(self,board):
        temp_board = []

        for line in board:
            for i in range(len(line) // 2):
                line[i], line[len(line) - i - 1] = line[len(line) - i - 1], line[i]

            temp_board.append(line)

        board.clear()

        for i in range(len(temp_board[0])):
            line = []
            for j in range(len(temp_board[0])):
                line.append(temp_board[j][i])
            temp_line = deepcopy(line)
            board.append(temp_line)

        self._repo.updateBoard(board)


    def getBoard(self):
        return self._repo.getBoard().getElems()

    def undo(self):
        self._repo.undo()