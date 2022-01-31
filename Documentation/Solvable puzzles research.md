# Solvable Puzzles
As stated in the challenge brief, not all boards are necessarily solvable, so I’ve been trying to figure out how to check if any given puzzle is solvable, and I believe I have a solution.

## Inspiration Sources
Through searching I found the two following articles from GeeksForGeeks. 
- [GeeksForGeeks 8x8](https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/)
- [GeeksForGeeks 15x15](https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/) 

They solve part of the problem, but have no solution for puzzles that are 3x2, 4x3, etc. 
 
Further searching led me upon this website, where a modular NxN puzzle can be chosen and solved, very similar to the challenge.
- [15 Puzzle](https://www.jaapsch.net/puzzles/javascript/fifteenj.htm)

This solution always creates solvable problems, so I decided to use the inversion counting method I had already implemented and check what made each type of puzzle solvable.

## Findings
I started with the smallest solvable puzzle and worked my way up:

    - 2x2: Inversion must always be even
    
    - 3x2:
        - 0 in the first row, inversion must be even 
        - 0 in the middle row, inversion must be odd
        - 0 in the last row, inversion must be even
    
    - 2x3: Inversion must always be even 
    
    - 3x3: Inversion must always be even
    
    - 3x4:
        - 0 in the first row, inversion must be even
        - 0 in the middle row, inversion must be odd
        - 0 in the last row, inversion must be even

    - 4x3: Inversion must always be even
    
    - 4x4:
        - 0 in first row, inversion must be odd
        - 0 in second-first row, inversion must be even
        - 0 in second-last, inversion must be odd
        - 0 in last row, inversion must be even
    
    - 4x5: Inversion must always be even
    
    - 5x4: 
        - 0 in top row, inversion must be even
        - 0 in second-first row, inversion must be odd. 
        - 0 in middle row, inversion must be even
        - 0 in second-last row, inversion must be odd
        - 0 in last row, inversion must be even.

I had an idea formula already in my head after the 3x4 and 4x3 check, but I tested the 4x5 and 5x4 just to confirm it. The test also confirmed that the formulas from GeeksForGeeks were correct.

## Conclusion
- If the number of columns are even, the row the zero is positioned in matters.
    - If the zero is positioned in an even row from the bottom (second-last, fourth-last), the inversion must be odd.
    - If the zero is positioned in an odd row from the bottom (last, third-last), the inversion must be even.
- If the number of columns are odd, the row the zero is positioned in doesn't matter. The inversion must be even.

In short, the formula from GeeksForGeeks on the 15 number puzzle works for all puzzles where N = number of columns. 
Not only N*N-1 puzzles.
