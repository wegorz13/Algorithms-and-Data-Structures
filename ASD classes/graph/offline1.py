from queue import Queue


def BFS(x,y,L,t):
    maxlen=0
    for e in L:
        maxlen=max(maxlen,e[1])
    n=maxlen
    P=[-1 for _ in range(n)]
    MM=[[-1,-1] for _ in range(n)]

    Q=Queue()
    P[x]=x
    Q.put(x)

    while not Q.empty():
        v=Q.get()
        for e in L:
            if v==x:
                MM[v]=[e[2],e[2]]
            if P[e[0]]!=-1 and e[0]==x:
                u=e[0]
                P[u]=v
                MM[u][0]=min(MM[v][0],e[2])
                MM[u][1]=max(MM[v][1],e[2])
                if MM[u][1]-MM[u][0]<=2*t:
                    if u==y:
                        return True
                    Q.put(u)
            elif P[e[1]]!=-1 and e[1]==x:
                u = e[1]
                P[u] = v
                MM[u][0] = min(MM[v][0], e[2])
                MM[u][1] = max(MM[v][1], e[2])
                if MM[u][1] - MM[u][0] <= 2 * t:
                    if u==y:
                        return True
                    Q.put(u)
    return False