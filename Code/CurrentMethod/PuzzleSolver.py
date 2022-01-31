import heapq

from CurrentMethod.GameStateNode import *
from CurrentMethod.PuzzleProjector import PuzzleProjector


# Uses A* algorithm to find the optimal path
def solver(gameState):
    movesMade = 0
    unexpanded = []
    heapq.heapify(unexpanded)
    heapq.heappush(unexpanded, gameState)
    expanded = set()
    while unexpanded:
        gs = heapq.heappop(unexpanded)
        expanded.add(tuple(gs.currBoard))
        if gs.moves > movesMade:
            movesMade += 1
            print("Moves made " + str(gs.moves))

        if gs.isGoal():
            PuzzleProjector(gs)
            return
        elif gs.moves > 100:
            print("Reached threshold of 100 moves")
            break
        else:
            for nextState in gs.possibleMoves():
                if tuple(nextState.currBoard) not in expanded:
                    heapq.heappush(unexpanded, nextState)
                    expanded.add(tuple(nextState.currBoard))
    print("Me me big sad :(")
