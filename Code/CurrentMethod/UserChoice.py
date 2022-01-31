import tkinter as tk
from tkinter import messagebox
import random
from CurrentMethod.PuzzleSolver import solver
from CurrentMethod.GameStateNode import *


# gets all entries and checks for wrong inputs
def getEntries(parent):
    entries = []
    found0 = False
    for child in parent.winfo_children():
        try:
            entries.append(int(child.get()))
        except ValueError:
            if not found0:
                entries.append(0)
                found0 = True
            else:
                tk.messagebox.showerror("Error", "Looks like your board has an error!\n"
                                                 "Only one blank space is allowed on the board")
                return None
    if found0 is False:
        tk.messagebox.showerror("Error", "Looks like your board has an error!\n" 
                                         "It seems you didn't include a blank space,\n"
                                         "the puzzle needs a blank space to be solved")
        return None
    else:
        return entries


class UserChoice:

    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Puzzle Choice")
        self.font = ("Comic Sans", 15)
        # frame with row count
        rowFrame = tk.Frame(self.master)
        tk.Label(rowFrame, text="Rows", font=self.font).pack(side="left")
        self.rowCount = tk.StringVar(value="3")
        tk.Entry(rowFrame, width=2, text="3", textvariable=self.rowCount, font=self.font).pack(side="right")
        rowFrame.grid(row=0, column=0, padx=10, pady=10)

        # frame with column count
        columnFrame = tk.Frame(self.master)
        tk.Label(columnFrame, text="Columns", font=self.font).pack(side="left")
        self.columnCount = tk.StringVar(value="3")
        tk.Entry(columnFrame, width=2, textvariable=self.columnCount, font=self.font).pack(side="right")
        columnFrame.grid(row=0, column=1, padx=10, pady=10)

        # text to describe the boards
        tk.Label(self.master, text="Initial State", font=self.font).grid(row=1, column=0, columnspan=2)

        # crate entry fields based on user set width and height
        rows, columns = 3, 3

        self.state = tk.Frame(self.master)
        self.changeLayout()
        self.state.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # listeners for change of the row and column input
        self.rowCount.trace("w", self.changeLayout)
        self.columnCount.trace("w", self.changeLayout)

        tk.Button(self.master, text="Solve puzzle", command=self.solvePuzzle).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.master, text="Randomise board", command=self.makePuzzleBoard).grid(row=3, column=1, padx=10, pady=10)

        self.master.mainloop()

    def solvePuzzle(self):
        initBoard = getEntries(self.state)
        if initBoard is None: return

        rows, columns = int(self.rowCount.get()), int(self.columnCount.get())
        if rows * columns != len(initBoard):
            tk.messagebox.showerror("Error", "Looks like your board has an error!\n"
                                    "Make sure the column and row fields reflect the size of the board")
            return

        for i in range(rows*columns):
            if i in initBoard:
                continue
            else:
                tk.messagebox.showerror("Error", "Looks like your board has an error!\n" +
                                        "Make sure the numbers are between 1 and " + str((rows * columns) - 1) +
                                        ",\nand that there are no duplicate numbers")
                return

        gs = GSN(initBoard, rows, columns)
        if not checkSolvable(gs):
            tk.messagebox.showerror("Error", "Looks like your board has an error!\n" +
                                    "Your current board isn't solvable, you can press the "
                                    "Randomise puzzle button to create a solvable puzzle")

        self.master.destroy()
        solver(gs)

    # used to change the layout when the numbers in the row and column text boxes are changed
    def changeLayout(self, *args):
        try:
            rows, columns = int(self.rowCount.get()), int(self.columnCount.get())
            self.makePuzzleBoard()
        except ValueError:
            return

    # clears the frame, then places entries based on row and column count
    # also fills the board with a solvable puzzle
    def makePuzzleBoard(self):
        for child in self.state.winfo_children():
            child.destroy()

        rows, columns = int(self.rowCount.get()), int(self.columnCount.get())
        boardLayout = random.sample(range(rows*columns), rows*columns)
        gs = GSN(boardLayout, rows, columns)
        while not checkSolvable(gs):
            boardLayout = random.sample(range(rows * columns), rows * columns)
            gs = GSN(boardLayout, rows, columns)

        index = 0
        for i in range(rows):
            for j in range(columns):
                if boardLayout[index] != 0:
                    tk.Entry(self.state, width=2, font=self.font,
                             textvariable=tk.StringVar(value=boardLayout[index])).grid(row=i, column=j)
                else:
                    tk.Entry(self.state, width=2, font=self.font,
                             textvariable=tk.StringVar()).grid(row=i, column=j)
                index += 1


if __name__ == '__main__':
    UserChoice()
