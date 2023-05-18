
from collections import deque

def solve_bfs(x, y, target):
    queue = deque([(0, 0, [])])  # (x, y, path)
    visited = set()

    while queue:
        curr_x, curr_y, path = queue.popleft()
        if curr_x == target or curr_y == target:
            return path + [(curr_x, curr_y)]

        if (curr_x, curr_y) in visited:
            continue

        visited.add((curr_x, curr_y))

        operations = [
            ('Fill X', x, curr_y),
            ('Fill Y', curr_x, y),
            ('Empty X', 0, curr_y),
            ('Empty Y', curr_x, 0),
            ('Pour X to Y', max(0, curr_x + curr_y - y), min(y, curr_x + curr_y)),
            ('Pour Y to X', min(x, curr_x + curr_y), max(0, curr_x + curr_y - x))
        ]

        for operation, next_x, next_y in operations:
            queue.append((next_x, next_y, path + [(curr_x, curr_y, operation)]))

    return None

bfs_solution = solve_bfs(4,3,2)
if bfs_solution:
    print("BFS solution:\n")
    print("X","Y","Opeartion\n")
    for state in bfs_solution:
        print(state)
