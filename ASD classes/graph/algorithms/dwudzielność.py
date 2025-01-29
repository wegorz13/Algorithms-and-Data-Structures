def is_bipartite(G):
    n=len(G)
    visited = [False for _ in range(n)]
    colors = [-1 for _ in range(n)]


    def DFS_visit(v, G,color):
        visited[v] = True

        colors[v]=color
        for s in G[v]:
            if colors[s] == color:
                return False
            elif colors[s]==-1:
                res = DFS_visit(s,G,1-color)
                if not res:
                    return False
        return True

    return DFS_visit(0,G,1)