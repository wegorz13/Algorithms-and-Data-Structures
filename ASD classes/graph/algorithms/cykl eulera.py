def wk_euler(G):
    n=len(G)

    for i in range(n):
        cnt=0
        for j in range(n):
            if G[i][j]==1:
                cnt+=1
        if cnt%2!=0:
            return False
    return True


def euler(G):
    if not wk_euler(G):
        return False

    n=len(G)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    scycle = []


    def DFS_visit(v):
        for s in G[v]:
            if not visited[v][s]:
                visited[v][s]=1
                visited[s][v]=1
                DFS_visit(s)
        scycle.append(v)

    DFS_visit(0)

    return scycle

G = [
[1, 2, 3 ],
[0, 2, 4, 5],
[0, 1, 4, 3 ],
[0, 2, 4, 5],
[1, 2, 3, 5 ],
[1, 4, 3 ]
]

Graf=[[1,2],[0,3,4],[0,4,5],[1,5],[1,2],[2,3]]

print(euler(Graf))
