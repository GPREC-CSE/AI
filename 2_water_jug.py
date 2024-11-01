from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Queue to keep track of states and the path to reach them
    queue = deque([((0, 0), [])])
    # Set to keep track of visited states
    visited = set()
    visited.add((0, 0))

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Check if we have reached the target amount of water in either jug
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2, "Target reached")]

        # List of possible actions with descriptions
        actions = [
            ((jug1_capacity, jug2), "Fill jug 1"),  # Fill jug1
            ((jug1, jug2_capacity), "Fill jug 2"),  # Fill jug2
            ((0, jug2), "Empty jug 1"),             # Empty jug1
            ((jug1, 0), "Empty jug 2"),             # Empty jug2
            ((min(jug1_capacity, jug1 + jug2), jug2 - (min(jug1_capacity, jug1 + jug2) - jug1)), "Pour jug 2 into jug 1"),  # Pour jug2 into jug1
            ((jug1 - (min(jug2_capacity, jug1 + jug2) - jug2), min(jug2_capacity, jug1 + jug2)), "Pour jug 1 into jug 2")   # Pour jug1 into jug2
        ]

        for (new_state, action) in actions:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(jug1, jug2, action)]))

    return None

# Dynamic input
jug1_capacity = int(input("Enter capacity of jug 1: "))
jug2_capacity = int(input("Enter capacity of jug 2: "))
target = int(input("Enter the target amount: "))

path = water_jug_problem(jug1_capacity, jug2_capacity, target)
if path:
    print("Path of states followed:")
    for state in path:
        print(state[2])
else:
    print("No solution found.")
