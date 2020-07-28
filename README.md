# SudokuSolver-backtracking

This is a Python program that finds a solution for a given sudoku.
The sudoku is loaded from a text file "sudoku.txt" where entries are delimited by spaces, empty squares are represented by 0 (zero); an example is the following:
0 0 0 0 0 0 0 0 0\
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
The program first checks if the given sudoku is solvable (checks the rows, columns and cells and looks for duplicate values), if it seems to be solvable, it tries to solve it by backtracking using a recursive function that puts random values 1-9 into empty squares and moves to other squares until it finds a solution or finds itself in a situation where a solution does not exist in which case it moves back and tries other values. 
In case it finds a solution, it appends it to the aforementioned text file.

The program uses the NumPy library.
