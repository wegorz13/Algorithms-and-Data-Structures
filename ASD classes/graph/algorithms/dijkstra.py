from queue import PriorityQueue


def dijkstra(G, s):
    n=len(G)
    D = [float('inf') for _ in range(n)]
    V = [False for _ in range(n)]

    def relax(u, v, t):
        if D[v] > D[u] + t:
            D[v] = D[u] + t
            Q.put((D[v], v))

    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        if not V[u]:
            for s in G[u]:
                relax(u, s[0], s[1])
        V[u] = True

    return D

