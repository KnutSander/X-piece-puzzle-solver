from tkinter import *
from OldMethod.GameState import *


# custom class for the puzzle pieces to be able to move them easily
class PuzzlePiece(Frame):
    def move(self, newPos):
        self.grid(row=newPos[0], column=newPos[1])


# method for getting the grid position of frames, saved for later maybe
# https://www.geeksforgeeks.org/python-tkinter-grid_location-and-grid_size-method/

class PuzzleGUI:
        def __init__(self, endNode):
            self.endNode = endNode
            self.showSteps(self.endNode)
    # send class the finishing node
    # call recursive function to output a frame for every step

        def showSteps(self, node):
            if node.parent is not None: self.showSteps(node.parent)
            self.printStep(node)

        def printStep(self, node):
            # creating the frame, and placing the puzzle pieces on it
            numb = len(node.gameState.currBoard) * len(node.gameState.currBoard[0]) - 1  # starts at the highest number
            puzzleList = []
            numbPositions = findPositions(node.gameState.currBoard)  # get position of every number
            top = Tk()
            while len(puzzleList) < (len(node.gameState.currBoard) * len(node.gameState.currBoard[0])) - 1:
                for i in range(len(node.gameState.currBoard)):
                    for j in range(len(node.gameState.currBoard[0])):
                        if numb != 0:
                            currPos = numbPositions[numb]  # gets the tuple with the current numbers position
                            frame = PuzzlePiece(top, highlightbackground="red",
                                                highlightthickness=2, width=100, height=100)
                            puzzleList.append(frame)
                            label = Label(frame, text=str(numb), width=4, height=2, font=("Comic Sans", 20))
                            label.pack()
                            frame.grid(padx=10, pady=10, row=currPos[0], column=currPos[1])
                            numb -= 1
            top.mainloop()
            return

"""
moveTo = (2, 2)
# running a for loop like this to find the element we want to move
for piece in puzzleList:
        if piece.grid_info().get("row") == 1 and piece.grid_info().get("column") == 2:
            piece.move(moveTo)
"""