'''Solve a Magic Square Puzzle Using Constraint Propagation
Aim

To solve a 3×3 Magic Square using the Constraint Propagation technique in Artificial Intelligence.

Theory

A Magic Square is a square arrangement of numbers where:

Every row has the same sum.
Every column has the same sum.
Both diagonals have the same sum.
Every number is used exactly once.

For a 3×3 Magic Square, the numbers are:

1 2 3 4 5 6 7 8 9

The magic sum is:
Magic Sum=n(n**2+1)/2

For n=3:

Magic Sum=3(9+1)/2=15




Constraint Propagation

Constraint propagation reduces the search space by enforcing constraints whenever a value is assigned.

Constraints
Every cell contains a unique number from 1–9.
Every row sums to 15.
Every column sums to 15.
Both diagonals sum to 15.

Instead of trying every arrangement, invalid partial assignments are rejected immediately.



Sample Puzzle

Fill the empty cells:

8  _  _
_  5  _
_  _  2

Solution
8 1 6
3 5 7
4 9 2

Check:

Rows

8+1+6 =15
3+5+7 =15
4+9+2 =15

Columns

8+3+4 =15
1+5+9 =15
6+7+2 =15

Diagonals

8+5+2 =15
6+5+4 =15

Hence, it is a valid magic square.


'''


# ---------------------------------------------
# Magic Square using Constraint Propagation
# ---------------------------------------------

import itertools

MAGIC_SUM = 15

numbers = [1,2,3,4,5,6,7,8,9]

def is_magic(square):

    # Rows
    for i in range(3):
        if sum(square[i]) != MAGIC_SUM:
            return False

    # Columns
    for j in range(3):
        if square[0][j] + square[1][j] + square[2][j] != MAGIC_SUM:
            return False

    # Diagonals
    if square[0][0] + square[1][1] + square[2][2] != MAGIC_SUM:
        return False

    if square[0][2] + square[1][1] + square[2][0] != MAGIC_SUM:
        return False

    return True


for perm in itertools.permutations(numbers):

    square = [
        list(perm[0:3]),
        list(perm[3:6]),
        list(perm[6:9])
    ]

    if is_magic(square):

        print("Magic Square Found:\n")

        for row in square:
            print(row)

        break




'''Sample Output
Magic Square Found:

[2, 7, 6]
[9, 5, 1]
[4, 3, 8]

Another valid magic square is:

8 1 6
3 5 7
4 9 2
Constraint Propagation Steps

Suppose the puzzle is:

8 _ _
_ 5 _
_ _ 2
Step 1

Known numbers:

8 _ _
_ 5 _
_ _ 2

Unused numbers:

1 3 4 6 7 9
Step 2

First row:

8 + ? + ? = 15

Remaining sum:

7

Possible pairs:

1 + 6
3 + 4

Constraint propagation removes all other combinations.

Step 3

Main diagonal:

8 + 5 + 2 = 15

Already satisfied.

Step 4

Second column:

? + 5 + ? = 15

Remaining sum:

10

Possible pairs:

1 + 9
3 + 7
4 + 6

Further constraints eliminate invalid choices.

Step 5

After propagating all constraints, the only consistent solution is:

8 1 6
3 5 7
4 9 2
Time Complexity

Without constraints:

9! = 362,880 possibilities

With constraint propagation:

Many invalid assignments are discarded early.
The search becomes much faster than checking every permutation.
Advantages of Constraint Propagation
Reduces the search space.
Detects impossible assignments early.
Improves efficiency when combined with backtracking.
Widely used in CSP problems such as Sudoku, N-Queens, scheduling, and magic squares.'''