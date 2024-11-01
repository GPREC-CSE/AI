import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, start, end, cost=1):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))
    def best_first_search(self, start, goal, heuristic):
        pq = [(heuristic[start], start, [start], 0)]  
        visited = set()
        while pq:
            _, current_node, path, current_cost = heapq.heappop(pq)
            if current_node == goal:
                return path, current_cost
            visited.add(current_node)
            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = current_cost + cost
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, new_path, new_cost))
        return None, float('inf')
graph = Graph()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    start, end, cost = input("Enter edge (start end cost): ").split()
    cost = int(cost)
    graph.add_edge(start, end, cost)
heuristic = {}
num_nodes = int(input("Enter the number of nodes for heuristic values: "))
for _ in range(num_nodes):
    node, h_value = input("Enter node and its heuristic value (node heuristic_value): ").split()
    heuristic[node] = int(h_value)
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
path, total_cost = graph.best_first_search(start_node, goal_node, heuristic)
if path:
    print("Path found:", ' -> '.join(path))
    print("Total cost:", total_cost)
else:
    print(f"No path found from {start_node} to {goal_node}.")

Enter the number of edges: 9
Enter edge (start end cost): s a 3
Enter edge (start end cost): a c 4
Enter edge (start end cost): a d 1
Enter edge (start end cost): s b 2
Enter edge (start end cost): b e 3
Enter edge (start end cost): b f 1
Enter edge (start end cost): e h 5
Enter edge (start end cost): f i 2
Enter edge (start end cost): f g 3
Enter the number of nodes for heuristic values: 10
Enter node and its heuristic value (node heuristic_value): a 12
Enter node and its heuristic value (node heuristic_value): b 4
Enter node and its heuristic value (node heuristic_value): c 7
Enter node and its heuristic value (node heuristic_value): d 3
Enter node and its heuristic value (node heuristic_value): e 8
Enter node and its heuristic value (node heuristic_value): f 2
Enter node and its heuristic value (node heuristic_value): h 4
Enter node and its heuristic value (node heuristic_value): i 9
Enter node and its heuristic value (node heuristic_value): s 13
Enter node and its heuristic value (node heuristic_value): g 0
Enter the start node: s
Enter the goal node: g
Path found: s -> b -> f -> g
Total cost: 6
