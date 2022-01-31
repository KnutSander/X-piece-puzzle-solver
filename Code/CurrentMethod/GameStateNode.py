import numpy as np


# returns an array where the number in every position, reflects the position
# of every number in the original array, used for the manhattan formula
def findPositions(board):
    positions = np.array(range(len(board)))
    for pos, value in enumerate(board):
        positions[value] = pos
    return positions


# returns the number of inversions
def getInversionCount(board):
    inversions = 0
    for i, num in enumerate(board):
        if num == 0: continue
        for nextNum in board[i:]:
            if nextNum == 0: continue
            if num > nextNum:
                inversions += 1
    return inversions


# returns the row in which the zero is positioned
# if the rows are an even number, it returns the row number counted from the top
# if the rows are an odd number, it returns the row number + 1
# this is because the checkSolvable formula is based on counting from the bottom, where bottom row is 1 (odd)
# so by adding 1 when the rows are odd, it ensures that the bottom row is an odd number
def getZeroRow(gs):
    index = 0
    for i in range(gs.rows):
        for j in range(gs.columns):
            if index == gs.zeroPos:
                return i if gs.rows % 2 == 0 else i + 1
            else:
                index += 1


# checks if the given board is solvable, based on what's explained here:
# https://cseegit.essex.ac.uk/2020-year-2-challenge/challenge-software/challenge-software_blakkestad_knut_s_l/-/blob/master/Documentation/Solvable%20puzzles%20research.md
def checkSolvable(gs):
    if gs.columns % 2 == 0:
        if getZeroRow(gs) % 2 == 0:
            return True if getInversionCount(gs.currBoard) % 2 != 0 else False
        else:
            return True if getInversionCount(gs.currBoard) % 2 == 0 else False
    else:
        return True if getInversionCount(gs.currBoard) % 2 == 0 else False


class GSN:

    def __init__(self, board, rows, columns, parent=None, moves=0):
        self.currBoard = np.array(board)
        self.rows = rows
        self.columns = columns
        self.parent = parent
        self.moves = moves
        self.goalBoard = self.createGoal()
        self.goalPositions = findPositions(self.goalBoard)
        self.cost = self.moves + self.getHeuristicEstimate()
        self.zeroPos = self.getZeroPos()

    def __lt__(self, other):
        return self.cost < other.cost

    # returns the goal board
    def createGoal(self):
        goalBoard = np.arange(self.rows * self.columns)
        goalBoard = goalBoard[1:]
        goalBoard = np.append(goalBoard, 0)
        return np.array(goalBoard)

    def isGoal(self):
        return np.array_equal(self.currBoard, self.goalBoard)

    # gets the position of the zero, stored as a tuple
    def getZeroPos(self):
        for i in range(len(self.currBoard)):  # row number
            if self.currBoard[i] == 0:
                return i

    # uses the manhattan formula to calculate the heuristic estimate
    # doesn't include the positional value of 0, because it represents
    # the blank space, and isn't relevant for the calculation
    def getHeuristicEstimate(self):
        currPositions = findPositions(self.currBoard)
        he = 0
        for i in range(len(self.currBoard)):
            if i != 0:
                he += (abs(currPositions[i] // self.columns - self.goalPositions[i] // self.columns)
                       + abs(currPositions[i] % self.columns - self.goalPositions[i] % self.columns))
        return he

    def newMove(self, newNumberPos, newZeroPos):
        move = np.array(self.currBoard)
        move[newNumberPos] = move[newZeroPos]
        move[newZeroPos] = 0
        return move

    def possibleMoves(self):
        moves = []

        # move zero up and number down
        if self.zeroPos > self.columns - 1:
            moves.append(GSN(self.newMove(self.zeroPos, self.zeroPos - self.columns),
                             self.rows, self.columns, self, self.moves + 1))

        # move zero down and number up
        if self.zeroPos < (self.columns * self.rows) - self.columns:
            moves.append(GSN(self.newMove(self.zeroPos, self.zeroPos + self.columns),
                             self.rows, self.columns, self, self.moves + 1))

        # move zero right and number left
        if (self.zeroPos + 1) % self.columns != 0:
            moves.append(GSN(self.newMove(self.zeroPos, self.zeroPos + 1),
                             self.rows, self.columns, self, self.moves + 1))

        # move zero left and number right
        if self.zeroPos % self.columns != 0:
            moves.append(GSN(self.newMove(self.zeroPos, self.zeroPos - 1),
                             self.rows, self.columns, self, self.moves + 1))

        return moves
