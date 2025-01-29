def floydWarshall(G):
    n = len(G)

    D = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if y == x:
                D[y][x] = 0
            else:
                D[y][x] = G[y][x]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                if D[x][k] + D[k][y] < D[x][y]:
                    D[x][y] = D[x][k] + D[k][y]

    for k in range(n):
        for y in range(n):
            for x in range(n):
                if D[y][k] + D[k][x] < D[y][x]:
                    D[y][x] = -float('inf')

    return D

