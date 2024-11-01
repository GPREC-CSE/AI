# Function to create graph and get input from the user
def create_graph():
    n = int(input("Enter number of nodes: "))
    G = []
    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        G.append(row)
    return G

def color_graph(G):
    node = "abcdefghijklmnopqrstuvwxyz"[:len(G)]
    t_ = {node[i]: i for i in range(len(G))}

    degree = [sum(G[i]) for i in range(len(G))]

    # initiate the possible color
    colorDict = {node[i]: ["Blue", "Red", "Yellow", "Green"] for i in range(len(G))}

    sorted_node = []
    indeks = []

    # use selection sort
    for i in range(len(degree)):
        max = 0
        for j in range(len(degree)):
            if j not in indeks and degree[j] > max:
                max = degree[j]
                idx = j
        indeks.append(idx)
        sorted_node.append(node[idx])

    theSolution = {}
    for n in sorted_node:
        setTheColor = colorDict[n]
        theSolution[n] = setTheColor[0]
        adjacentNode = G[t_[n]]
        for j in range(len(adjacentNode)):
            if adjacentNode[j] == 1 and (setTheColor[0] in colorDict[node[j]]):
                colorDict[node[j]].remove(setTheColor[0])

    return theSolution

# Get the graph input
G = create_graph()

# Color the graph and print the solution
theSolution = color_graph(G)
print(theSolution)
for t, w in sorted(theSolution.items()):
    print("Node", t, " = ", w)
