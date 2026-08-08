'''Implement A* Search Algorithm to Find the Shortest Path in a 4×4 Grid
Aim

To implement the A* (A-Star) search algorithm to find the shortest path from a start node to a goal node in a 4 × 4 grid.

Theory

A* (A-Star) is one of the most efficient informed search algorithms used in Artificial Intelligence. It finds the shortest path by considering:

Actual cost from the start node (g(n))
Estimated cost to the goal (h(n))

The evaluation function is:

f(n)=g(n)+h(n)

where:

g(n) = Cost from the start node to the current node.
h(n) = Heuristic estimate from the current node to the goal.
f(n) = Total estimated cost.

For a grid, the Manhattan Distance is commonly used as the heuristic:
h(n)=∣x1​−x2​∣+∣y1​−y2​∣

Example 4×4 Grid
S  .  .  .
.  X  .  .
.  X  .  .
.  .  .  G


Where:

S = Start
G = Goal
X = Obstacle
. = Free cell


Coordinates:

Start = (0,0)

Goal = (3,3)

Obstacles:

(1,1)
(2,1)


Algorithm
Add the start node to the open list.
Select the node with the lowest f(n).
If it is the goal, stop.
Generate valid neighboring nodes.
Compute:
g(n)
h(n)
f(n)
Add neighbors to the priority queue.
Repeat until the goal is reached.

Evaluation Function: f(n) = g(n) + h(n)
'''



import heapq

ROWS = 4
COLS = 4

# 0 = Free Cell
# 1 = Obstacle

grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)


# Manhattan Distance
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar():

    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    came_from = {}

    g_cost = {start: 0}

    while priority_queue:

        _, current = heapq.heappop(priority_queue)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        x, y = current

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:

                if grid[nx][ny] == 1:
                    continue

                neighbor = (nx, ny)

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                    g_cost[neighbor] = new_cost

                    f = new_cost + heuristic(neighbor, goal)

                    heapq.heappush(priority_queue, (f, neighbor))

                    came_from[neighbor] = current

    return None


path = astar()

print("Shortest Path:")

print(path)

print("\nGrid Path:")

for i in range(ROWS):

    for j in range(COLS):

        if (i, j) == start:
            print("S", end=" ")

        elif (i, j) == goal:
            print("G", end=" ")

        elif (i, j) in path:
            print("*", end=" ")

        elif grid[i][j] == 1:
            print("X", end=" ")

        else:
            print(".", end=" ")

    print()




'''Sample Output
Shortest Path:

[(0,0),
 (0,1),
 (0,2),
 (0,3),
 (1,3),
 (2,3),
 (3,3)]

Grid representation:

S * * *
. X . *
. X . *
. . . G
Step-by-Step Execution
Initial State
S . . .
. X . .
. X . .
. . . G
Step 1

Current = (0,0)

Neighbors:

(0,1)

(1,0)

Both have:

g = 1

h = 5

f = 6

Choose one with the lowest f.

Step 2

Move to (0,1).

S * . .
. X . .
. X . .
. . . G
Step 3

Move to (0,2).

S * * .
. X . .
. X . .
. . . G
Step 4

Move to (0,3).

S * * *
. X . .
. X . .
. . . G
Step 5

Move to (1,3).

S * * *
. X . *
. X . .
. . . G
Step 6

Move to (2,3).

S * * *
. X . *
. X . *
. . . G
Step 7

Move to Goal (3,3).

S * * *
. X . *
. X . *
. . . G

Goal reached.

Complexity
Operation	Complexity
Time	O(E log V)
Space	O(V)

Where:

V = Number of grid cells
E = Number of edges (possible moves)'''