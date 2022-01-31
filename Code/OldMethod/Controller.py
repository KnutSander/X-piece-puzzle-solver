from OldMethod.Node import *
from Visualization.PuzzleGUI import *
from CurrentMethod.PuzzleProjector import *


class Controller:

    def __init__(self, initBoard, goalBoard, initNode):
        self.initBoard = initBoard
        self.goalBoard = goalBoard
        self.initNode = initNode

    # solver using A* algorithm
    def solver(self):
        #start = time.time()
        unexpanded = []
        expanded = []
        unexpanded.append(self.initNode)
        while len(unexpanded) > 0:
            unexpanded = sorted(unexpanded)
            n = unexpanded.pop(0)
            expanded.append(n)
            if n.gameState.currBoard == self.goalBoard:
                #end = time.time()
                #print("It took " + str(end - start) + " seconds")
                self.solutionFound(n)
                return
            else:
                for move in n.gameState.possibleMoves():
                    if checkIfContains(unexpanded, move) is None and checkIfContains(expanded, move) is None:
                        unexpanded.append(Node(move, n, n.getCost() + 1))
                        """
                        print("Expanded length: " + str(len(expanded)) +
                              " Unexpanded length: " + str(len(unexpanded)))
                        """
        print("Not successfully")

    def solutionFound(self, node):
        print("Solution found!")
        self.printSolution(node)
        print("Amount of moves: " + str(node.getCost()))
        NoteBookTest(node)

    def printSolution(self, node):
        if node.parent is not None: self.printSolution(node.parent)
        print(node.gameState)


# first [] equals row, second [] equals column
# using only 1 [] gives the first array
# temporary creation of the boards, will be implemented as user choice later
"""
initBoard = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
goalBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

"""
initBoard = [[5, 4, 3], [2, 1, 0]]
goalBoard = [[1, 2, 3], [4, 5, 0]]


initGameState = GameState(initBoard, goalBoard)  # starting gameState
initNode = Node(initGameState, None, 0)  # initial node
controller = Controller(initBoard, goalBoard, initNode)  # controls the game

controller.solver()

