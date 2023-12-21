def bfs(node, graph):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Test Case 1
graph1 = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'F'],
    'C': ['A', 'G'],
    'D': ['A'],
    'E': ['A'],
    'F': ['B'],
    'G': ['C']
}
print("Test Case 1:")
bfs('A', graph1)
print("\n")
# Test Case 2
graph2 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W'],
    'Z': ['X'],
    'W': ['Y']
}
print("Test Case 2:")
bfs('X', graph2)
print("\n")
# Test Case 3
graph3 = {
    'M': ['N', 'O'],
    'N': ['M'],
    'O': ['M', 'P'],
    'P': ['O']
}

print("Test Case 3:")
bfs('M', graph3)
print("\n")


