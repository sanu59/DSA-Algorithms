INF = float('inf')
def prim(graph):
    V = len(graph)
    parent = [-1] * V  
    key = [INF] * V  
    mst_set = [False] * V  
    key[0] = 0
    for i in range(V - 1):
        u = min_key_vertex(key, mst_set)
        mst_set[u] = True
        for v in range(V):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u
    print_mst(parent, graph)
def min_key_vertex(key, mst_set):
    min_key = INF
    min_vertex = -1
    for v in range(len(key)):
        if key[v] < min_key and not mst_set[v]:
            min_key = key[v]
            min_vertex = v
    return min_vertex
def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
prim(graph)
