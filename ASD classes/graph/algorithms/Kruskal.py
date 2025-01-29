class Node:
    def __init__(self,value):
        self.val=value
        self.parent=self
        self.rank=0

def find(x):
    if x.parent!=x:
        x.parent = find(x.parent)
    return x.parent

def sortEdges(E):
    #
    E.sort( key = lambda x: x[2] )
    return E

def union(X,Y):
    X = find(X)
    Y = find(Y)

    if X==Y:
        return

    if X.rank > Y.rank:
        Y.parent = X
    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent=Y
        Y.rank+=1

def Kruskal(G):
    n=len(G)
    V, E = G
    MST=[]

    W = [Node(v) for v in V]
    E = sortEdges(E)

    for edge in E:
        u,v,k = edge
        u_parent = find(u)
        v_parent = find(v)

        if u_parent!=v_parent:
            union(u,v)
            MST.append(edge)

    return MST


