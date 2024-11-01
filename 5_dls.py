class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def depth_limited_search(self, start, goal, limit):
        visited = set()

        def dls(node, depth):
            if depth > limit:
                return False
            visited.add(node)
            print(f"Visiting: {node} at depth {depth}")

            if node == goal:
                return True

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if dls(neighbor, depth + 1):
                            return True

            visited.remove(node)  # Unmark the node for other paths
            return False

        return dls(start, 0)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('E', 'I')

    start_node = 'A'
    goal_node = 'I'
    depth_limit = 3

    if g.depth_limited_search(start_node, goal_node, depth_limit):
        print(f"Goal {goal_node} found within depth limit.")
    else:
        print(f"Goal {goal_node} not found within depth limit.")