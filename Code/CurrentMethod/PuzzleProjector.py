from tkinter import *
import tkinter as tk
from tkinter import ttk


class PuzzleProjector:
    def __init__(self, node):
        top = tk.Tk()
        top.title("Solution")
        notebook = ttk.Notebook(top)
        self.testing = []
        self.printStep(node)
        for x, panel in enumerate(self.testing):
            notebook.add(panel, text=str(x))
        notebook.pack()
        top.mainloop()


    def printStep(self, node):
        if node.parent is not None: self.printStep(node.parent)
        pos = 0
        puzzleList = []
        panel = ttk.Frame()
        while len(puzzleList) < len(node.currBoard) - 1:
            for i in range(node.rows):
                for j in range(node.columns):
                    if pos != node.zeroPos:
                        frame = Frame(panel, highlightbackground="red",
                                      highlightthickness=2, width=100, height=100)
                        puzzleList.append(frame)
                        label = Label(frame, text=str(node.currBoard[pos]), width=4, height=2, font=("Comic Sans", 20))
                        label.pack()
                        frame.grid(padx=10, pady=10, row=i, column=j)
                    pos += 1
        self.testing.append(panel)
        return
