INF = 9999999
V = 6
G = [
    [0, 5, 20, 0, 0, 61],
    [4, 0, 12, 8, 18, 22],
    [25, 15, 0, 11, 14,12],
    [0, 7, 13, 0, 6, 34],
    [0, 16, 10, 21, 0, 36],
    [0, 5, 20, 0, 0, 11],
    [4, 0, 12, 8, 18, 45],
    [25, 15, 0, 11, 14, 22]
]
def kruskal(G):
    selected = [0] * V
    no_edge = 0
    selected[0] = True
    print("Edge : Weight\n")
    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and G[i][j]:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1
kruskal(G)
