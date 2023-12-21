def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
# Test Case 1
graph1 = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [],
    6: [],
    7: []
}
print("Test Case 1:")
dfs(1, graph1)
print("\n")
# Test Case 2
graph2 = {
    10: [20, 30],
    20: [40, 50],
    30: [],
    40: [],
    50: [60],
    60: []
}
print("Test Case 2:")
dfs(10, graph2)
print("\n")
# Test Case 3
graph3 = {
    100: [200, 300, 400],
    200: [],
    300: [500],
    400: [600, 700],
    500: [],
    600: [],
    700: []
}
print("Test Case 3:")
dfs(100, graph3)
print("\n")

