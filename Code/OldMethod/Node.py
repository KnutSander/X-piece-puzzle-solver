from OldMethod.GameState import findPositions


def checkIfContains(nodeList, gameState):
    for node in nodeList:
        if node.gameState.currBoard == gameState.currBoard:
            return node
    return None


class Node:

    def __init__(self, gameState, parent, cost):
        self.gameState = gameState
        self.parent = parent
        self.cost = cost
        self.he = self.getHeuristicEstimate()
        self.totalCost = self.cost + self.he

    # heapq is able to find the lowest cost item using this
    def __lt__(self, other):
        return self.totalCost < other.totalCost


    def __str__(self):
        return "Node: " + str(self.cost)


    def getCost(self):
        return self.cost


    def getHeuristicEstimate(self):
        he = 0
        count = 0
        currPositions = findPositions(self.gameState.currBoard)
        while count < len(currPositions):
            goalTuple = self.gameState.goalPositions[count]
            currPosTuple = currPositions[count]
            he += abs(goalTuple[0] - currPosTuple[0]) + abs(goalTuple[1] - currPosTuple[1])
            count += 1
        return he
