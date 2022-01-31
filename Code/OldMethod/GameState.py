import copy


def findPositions(board):
    toFind = 0
    testList = []
    while len(testList) < (len(board) * len(board[0])):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == toFind:
                    testList.append((i, j))
                    toFind += 1
    return testList


class GameState:

    def __init__(self, initBoard, goalBoard):
        self.currBoard = initBoard
        self.goalBoard = goalBoard
        self.zeroPos = self.getZeroPos()
        self.goalPositions = findPositions(goalBoard)


    def __str__(self):
        s = ""
        for i in range(len(self.currBoard)): # row number
            for j in range(len(self.currBoard[0])): # column number
                s += str(self.currBoard[i][j]) + " "
            s += "\n"
        return s

    # gets the position of the zero, stored as a tuple
    def getZeroPos(self):
        for i in range(len(self.currBoard)): # row number
            for j in range(len(self.currBoard[0])): # column number
                if self.currBoard[i][j] == 0:
                    return i, j


    def possibleMoves(self):
        moves = []

        if self.zeroPos[0] - 1 >= 0: # row
            numberRow = self.zeroPos[0] - 1
            numberColumn = self.zeroPos[1]
            moves.append(self.newMove(numberRow, numberColumn))

        if self.zeroPos[0] + 1 <= len(self.currBoard) - 1: # row
            numberRow = self.zeroPos[0] + 1
            numberColumn = self.zeroPos[1]
            moves.append(self.newMove(numberRow, numberColumn))

        if self.zeroPos[1] - 1 >= 0: # column
            numberRow = self.zeroPos[0]
            numberColumn = self.zeroPos[1] - 1
            moves.append(self.newMove(numberRow, numberColumn))

        if self.zeroPos[1] + 1 <= len(self.currBoard[0]) - 1: # column
            numberRow = self.zeroPos[0]
            numberColumn = self.zeroPos[1] + 1
            moves.append(self.newMove(numberRow, numberColumn))

        return moves


    def newMove(self, numberRow, numberColumn):
        #print(str(numberRow) + "," + str(numberColumn))
        move = copy.deepcopy(self)
        move.currBoard[move.zeroPos[0]][move.zeroPos[1]] = self.currBoard[numberRow][numberColumn]
        move.currBoard[numberRow][numberColumn] = 0
        move.zeroPos = (numberRow, numberColumn)
        return move
