#macierzowa reprezentacja G

def sss(Gs):
    n=len(Gs)
    visited = [False for _ in range(n)]
    stack=[]

    G = [[0 for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for s in Gs[v]:
            G[v][s]=1

    def DFS_visit(v, G):
        n = len(G)
        visited[v] = True
        for s in range(n):
            if G[v][s] and not visited[s]:
                DFS_visit(s,G)
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            DFS_visit(i,G)

    stack = stack[::-1]
    visited2 = [False for _ in range(n)]
    result = []
    substack=[]

    def DFS_reversed(v, G):
        n = len(G)
        visited2[v] = True
        for s in range(n):
            if G[s][v]==1 and not visited2[s]:
                DFS_reversed(s,G)
        substack.append(v)

    for el in stack:
        if not visited2[el]:
            DFS_reversed(el,G)
            result.append(substack)
            substack=[]

    return result

Graf=[[1,7],[2],[0,3],[6],[3,9],[4,8],[5],[8],[9],[7,10],[8]]

print(sss(Graf))