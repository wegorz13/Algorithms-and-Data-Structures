from queue import PriorityQueue


def Prim(G, s):
    n=len(G)
    weight = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent=[False for _ in range(n)]

    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        w,u = Q.get()

        if not visited[u]:
            visited[u] = True

            for v,e in G[u]:
                if not visited[v] and e<weight[v]:
                    weight[v]=e
                    parent[v]=u
                    Q.put((weight[v],v))


    return parent,weight