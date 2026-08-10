from collections import deque

# Create a binary tree using A-Z
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X', 'Y'],
    'M': ['Z'],
    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}

def bfs_search(tree, start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == target:
            break

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                parent[child] = node
                queue.append(child)

    if target not in parent:
        print("Node not found!")
        return

    # Find path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nNode Found:", target)
    print("Path:", " -> ".join(path))

# --------------------------
# User Input
# --------------------------
target = input("Enter a letter (A-Z): ").upper()

if target < 'A' or target > 'Z':
    print("Invalid input!")
else:
    bfs_search(tree, 'A', target)





# its a change 
