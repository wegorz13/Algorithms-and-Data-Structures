# czasowa O(VE) pamięciowa O(V)

def bellmanford(G,s):
    n=len(G)
    D = [float('inf') for _ in range(n)]
    D[s]=0

    def relax(u,v,k):
        if D[v]>D[u]+k:
            D[v]=D[u]+k
            return True
        return False

    for i in range(n):
        for u in range(n):
            for v in G[u]:
                relax(u,v[0], v[1])

    for i in range(n):
        for u in range(n):
            for v in G[u]:
                if relax(u,v[0], v[1]):
                    D[v[0]]=float('inf')

    return D