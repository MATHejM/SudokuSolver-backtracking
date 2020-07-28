import numpy as np

def Solvable(): # Function checking if any of the numbers 1-9 does not have a duplicate value within a row, column or a cell
    for x in range(1,10):
        count = 0
        for i in range(9): #Checking the rows
            for j in range(9):
                if sudoku[i][j] == x:
                    count +=1
                    if count > 1:
                        return False
            count = 0
        for j in range(9): #Checking the columns
            for i in range(9):
                if sudoku[i][j] == x:
                    count += 1
                    if count > 1:
                        return False
            count = 0
        for i in (0, 3, 6): #Checking the cells
            for j in (0, 3, 6):
                for m in (0, 1, 2):
                    for n in (0, 1, 2):
                        if sudoku[i+m][j+n] == x:
                            count += 1
                            if count > 1:
                                return False
                count = 0
    return True

def Row(row,value):  #Function checking if "value" is already somewhere in the "row" - Returns False, if the "value" is not in the "row"
    for j in range(9):
        if sudoku[row][j] == value:
            return True
    return False

def Column(column,value):  #Function checking if the "value" is in the "column" - Returns False if the "value" is not in the "column"
    for i in range(9):
        if sudoku[i][column] == value:
            return True
    return False

def Cell(row,column,value): #Function checking if "value" is in a cell - takes as arguments the index of the upper left square of the cell
    for i in range(row,row+3):               #Returns True if the "value" is in the cell;
        for j in range(column,column+3):
            if sudoku[i][j] == value:
                return True
    return False

#Solving recursive function
def Solve(row,column):
    if row == 9 and column == 0: #solution found, return True
        return True
    else:
        if sudoku[row][column] == 0:  #the square is still empty
            for i in np.random.permutation([1,2,3,4,5,6,7,8,9]): #Try all the possible values
                if (not Row(row,i)) and (not Column(column,i)) and (not Cell((row // 3)*3,(column // 3)*3,i)): #if value "i" is not in the column, row nor the cell
                    sudoku[row][column] = i
                    if column < 8: #we are not yet at the end of the row
                        if Solve(row,column+1) == False: #the value "i" cannot be in the square so we take it away and try with another value
                            sudoku[row][column] = 0
                        else:
                            return True #we found a solution with the value "i" at (row,column)-index
                    else: #we are at the end of the row
                        if Solve(row+1,0) == False: #the value "i" cannot be in the square so we take it away and try with another value
                            sudoku[row][column] = 0
                        else:
                            return True #we found a solution with the value "i" at (row,column)-index
            return False # we have tried all the numbers 1-9, have not found a solution with none of them, means that we had made a mistake previously
        else: #we are at a square with a value so we move on the next square
            if column < 8:
                if Solve(row,column+1) == False:
                    return False
                return True
            else:
                if Solve(row+1,0) == False:
                    return False
                return True

# Loading the sudoku in 2-dimensional list "sudoku" by rows, in each row, numbers are delimited by spaces, empty squares represented by 0 (zero)
if __name__ == '__main__':
    a = open("sudoku.txt","r")
    f = a.readlines()
    sudoku = []
    for line in f:
        sudoku.append(line.strip())
    a.close()
    for i in range(9):
        sudoku[i] = sudoku[i].split(" ")
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = int(sudoku[i][j])

    # Checking if the sudoku is solvable
    if (not Solvable()):
        file = open("sudoku.txt", "a")
        file.write("\nSudoku is not solvable.\n")
        file.close()
    else:
        # Solving the sudoku
        if (not Solve(0, 0)):
            file = open("sudoku.txt", "a")
            file.write("\nSudoku is not solvable.\n")
            file.close()

        else:
            file = open("sudoku.txt","a")
            file.write("\nHere is one possible solution: \n")
            for i in range(9):
                file.write(str(sudoku[i])+"\n")
            file.close()


