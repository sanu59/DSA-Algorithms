v = 5
INF = 999999
def floyds(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)
def print_solution(distance):
    for i in range(v):
        for j in range(v):
            if distance[i][j] == INF:
                print("-1", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")
G = [
    [0, 10, INF, 5, INF],
    [INF, 0, 3, INF,4],
    [1, INF, 0, 1, INF],
    [INF, 6, INF, 0, 8],
    [INF,2, INF, 1, 0]
]
print("The shortest distances between every pair of vertices:")
floyds(G)
