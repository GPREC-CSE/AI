graph = {}
print("Number of nodes:")
nnodes = int(input().strip())
nodes = []
for _ in range(nnodes):
    node = input("Enter node: ")
    nodes.append(node)
print("Number of edges:")
nedges = int(input().strip())
for _ in range(nedges):
    s, e, cost = input("Enter start, end, and cost of the edge").strip().split()
    cost = int(cost)
    graph.setdefault(s, []).append((e, cost))
    graph.setdefault(e, []).append((s, cost))  
heu = {}
for node in nodes:
    heur = int(input(f"Enter heuristic value for {node}: "))
    heu[node] = heur
startn, goaln = input("Enter start node and goal node (separated by space): ").strip().split()
open_set = [(startn, 0)] 
closed_set = set()
g_scores = {startn: 0}
came_from = {}
while open_set:
    current_node = min(open_set, key=lambda x: g_scores.get(x[0], float('inf')) + heu.get(x[0], float('inf')))
    open_set.remove(current_node)
    if current_node[0] == goaln:
        break
    closed_set.add(current_node[0])
    for neighbor, cost in graph.get(current_node[0], []):
        if neighbor in closed_set:
            continue
        tentative_g_score = g_scores[current_node[0]] + cost
        if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
            came_from[neighbor] = current_node[0]
            g_scores[neighbor] = tentative_g_score
            if neighbor not in [n[0] for n in open_set]:
                open_set.append((neighbor, tentative_g_score))
path = []
current = goaln
while current in came_from:
    path.append(current)
    current = came_from[current]
path.append(startn)
path.reverse()
print("Path from start to goal:", path)

Number of nodes:
6
Enter node: s 
Enter node: a
Enter node: b
Enter node: c
Enter node: d
Enter node: g
Number of edges:
8
Enter start, end, and cost of the edge (separated by spaces): s a 1
Enter start, end, and cost of the edge (separated by spaces): a b 2
Enter start, end, and cost of the edge (separated by spaces): a c 1
Enter start, end, and cost of the edge (separated by spaces): s g 10
Enter start, end, and cost of the edge (separated by spaces): c d 3
Enter start, end, and cost of the edge (separated by spaces): d g 2
Enter start, end, and cost of the edge (separated by spaces): b d 5
Enter start, end, and cost of the edge (separated by spaces): c g 4
Enter heuristic value for s : 5
Enter heuristic value for a: 3
Enter heuristic value for b: 4
Enter heuristic value for c: 2
Enter heuristic value for d: 6
Enter heuristic value for g: 0
Enter start node and goal node (separated by space): s g
Closed list (visited nodes): {'s', 'c', 'a'}
Path from start to goal: ['s', 'a', 'c', 'g']
