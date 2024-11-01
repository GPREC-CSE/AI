def dfs(graph, node):
    visited = set()
    stack = []

    visited.add(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for n in reversed(graph[s]):
            if n not in visited:
                visited.add(n)
                stack.append(n)

def main():
    # Dynamic input for the graph
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v = input("Enter edge (u v): ").split()
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v not in graph:
            graph[v] = []

    # Dynamic input for the starting node
    start_node = input("Enter the starting node: ")
    
    dfs(graph, start_node)

if __name__ == "__main__":
    main()
