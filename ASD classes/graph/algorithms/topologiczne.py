# NA DAGU!

def DFS(G):
    n=len(G)
    visited = [False for _ in range(n)]
    stack=[]

    def DFS_visit(v, G):
        visited[v] = True
        for s in G[v]:
            if not visited[s]:
                DFS_visit(s,G)
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            DFS_visit(i,G)

    return stack