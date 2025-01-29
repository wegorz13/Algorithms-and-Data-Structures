from queue import Queue

def BFS(G,s):
    Q=Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    depth = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    visited[s]=True
    depth[s]=0
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                depth[v]=depth[u]+1
                visited[v]=True
                Q.put(v)

    return depth,parent,visited