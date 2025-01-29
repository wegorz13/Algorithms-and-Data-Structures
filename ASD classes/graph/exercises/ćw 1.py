"""
1 DWUDZIELNOŚĆ GRAFU
DFS
"""
from queue import Queue


def dfs_visit(G,v,colors,c):
    colors[v] = c
    for i in G[v]:
        if colors[i]==c:
            return False
        elif colors[i]==-1:
            res = dfs_visit(G,i,colors,1-c)
            if res==False:
                return False
    return True

def is_bipartite(G):
    n=len(G)
    colors = [-1 for _ in range(G)]
    return dfs_visit(G,0,colors,1)
"""
LICZBA SKŁADOWYCH SPÓJNYCH W GRAFIE REPREZENTACJA MACIERZOWA
"""
def DFSvisit(A,u,visited):
    visited[u]=True
    n=len(A)

    for v in range(n):
        if A[u][v] and not visited[v]:
            DFSvisit(A,v,visited)


def skladowe(A):
    n=len(A)
    visited=[False]*n
    res=0

    for i in range(n):
        if not visited[i]:
            DFSvisit(A,i,visited)
            res+=1

    return res

"""
CZY ISTNIEJE CYKL DŁUGOŚCI 4
n^3 dla wszystkich par wierzchołków szukamy ich 2 wspólnych sąsiadów w reprezentacji macierzowej to proste
w listowej reprezentajci możemy zapisać sąsiadów wierzchołka 1 do tablicy i dla 2 sprawdzać po liście
n^2logn sortujemy sąsiadów każdej pary wierzchołków i sprawdzamy czy mają 2 wspólnych
"""
def cycle_4(A):
    n=len(A)

    for i in range(n):
        for j in range(i,n):
            if A[i][j]==1:
                cnt=2
                for k in range(n):
                    if A[i][k]==A[j][k]==1:
                        cnt+=1
                    if cnt==4:
                        return True
    return False

"""
BFS odległości wierzchołków i ścieżki
"""

def BFS(s,G):
    n=len(G)
    D=[-1 for _ in range(n)]
    P=[-1 for _ in range(n)]

    Q=Queue()
    D[s]=0
    P[s]=s
    Q.put(s)

    while not Q.empty():
        v=Q.get()
        for u in G[v]:
            if D[u]==-1:
                D[u]=D[v]+1
                P[u]=v
                Q.put(u)
    return (D,P)

def path(s,t,P):
    T=[]
    T.append(t)
    while t!=s:
        t=P[t]
        T.append(t)

    return T[::-1]

"""
GRAF SIECI TELEKOMUNIKACYJNEJ KTÓRA SIE ZWIJA I WYŁĄCZA POSZCZEGÓLNE WĘZŁY SIECI
przechodzimy przez graf dfsem i do tablicy zapisujemy indeks grafu i jego depth, sortujemy te tablice i usuwamy od najwiekszego elementu
"""
"""
graf skierowany macierzowy, wierzchołek T jest uniwersalnym ujściem jeśli każdy wierzchołek ma do niego krawędź, a on nie ma do nikogo

"""
