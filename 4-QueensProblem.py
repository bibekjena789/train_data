'''The 4-Queens Problem is a classic Constraint Satisfaction Problem (CSP) in Artificial Intelligence.

Problem Statement

Place 4 queens on a 4 × 4 chessboard such that:

No two queens are in the same row.
No two queens are in the same column.
No two queens are on the same diagonal.
CSP Representation
Variables

Each row is a variable.

Q1 = Queen in Row 1
Q2 = Queen in Row 2
Q3 = Queen in Row 3
Q4 = Queen in Row 4
Domain

Each queen can be placed in any column.

Domain(Qi) = {0,1,2,3}

Example:

Q1 = 2

means

Queen in Row 1 is placed in Column 2.
Constraints

For every pair of queens:

1. Different Columns
Qi ≠ Qj
2. Different Diagonals
|Qi − Qj| ≠ |i − j|

where

Qi = column of queen i
Qj = column of queen j
Backtracking Algorithm

Backtracking places one queen at a time.

If a queen violates any constraint:

Remove it.
Try the next column.

If no column works:

Go back (Backtrack).
Change the previous queen's position.
Example Execution

Start with an empty board.

_ _ _ _
_ _ _ _
_ _ _ _
_ _ _ _
Step 1

Place Queen in Row 0

Try Column 0

Q _ _ _
_ _ _ _
_ _ _ _
_ _ _ _
Step 2

Row 1

Try

Column 0 ❌

Same column

Column 1 ❌

Diagonal

Column 2 ✔

Q _ _ _
_ _ Q _
_ _ _ _
_ _ _ _
Step 3

Row 2

Try every column

All fail

Backtrack.

Remove queen from Row 1.

Try Column 3.

Q _ _ _
_ _ _ Q
_ _ _ _
_ _ _ _

Continue until all rows are filled.

One Valid Solution
_ Q _ _
_ _ _ Q
Q _ _ _
_ _ Q _

Coordinates

Row 0 → Column 1

Row 1 → Column 3

Row 2 → Column 0

Row 3 → Column 2

Array Representation

[1,3,0,2]

'''


# -------------------------------------------
# 4-Queens using CSP + Backtracking
# -------------------------------------------

N = 4


def is_safe(board, row, col):
    """
    Check whether a queen can be placed
    """

    # Check previous rows
    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):

    # Base Case
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(board, row, col):

            board[row] = col

            if solve(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board):

    print("\nSolution Board\n")

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# --------------------------
# Driver Program
# --------------------------

board = [-1] * N

if solve(board, 0):

    print("Column Positions:")
    print(board)

    print_board(board)

else:
    print("No Solution")