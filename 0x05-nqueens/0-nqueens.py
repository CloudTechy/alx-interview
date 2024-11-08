#!/usr/bin/python3

# The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. a program that solves the N queens problem.

# Usage: nqueens N
# If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
# where N must be an integer greater or equal to 4
# If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
# If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
# The program should print every possible solution to the problem
# One solution per line
# Format: see example
# You don’t have to print the solutions in a specific order
# You are only allowed to import the sys module


import sys

def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col, n):
    """Recursive function to solve N Queen problem."""

    if col == n:
        printBoard(board, n)
        return True

    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res

def printBoard(board, n):
    """Print the board."""
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end=" ")
        print()
    print()

def solveNQ(n):
    """Solves the N Queen problem."""
    board = [[0 for j in range(n)] for i in range(n)]
    if solveNQUtil(board, 0, n) is False:
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(n)
    sys.exit(0)
