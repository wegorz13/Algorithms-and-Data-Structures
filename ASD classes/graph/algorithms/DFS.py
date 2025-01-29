

def DFS(G):
    n=len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    times = [0 for _ in range(n)]

    def DFS_visit(v, G):
        nonlocal time
        visited[v] = True
        for s in G[v]:
            if not visited[s]:
                parent[s]=v
                DFS_visit(s,G)
        time+=1
        times[v]=time
    time=0

    for i in range(n):
        if not visited[i]:
            DFS_visit(i,G)

    print(times)

G = [
[1, 2, 3 ],
[0, 2, 4, 5],
[0, 1, 4, 3 ],
[0, 2, 4, 5],
[1, 2, 3, 5 ],
[1, 4, 3 ]
]

DFS(G)


