""""
ZAD 1
Traktor na osi liczbowej z A do B. Spalanie 1l/km
Bak L litrów
A >= i >= B i naturalne
a) A->B jak najmniej tankowań

b) C[i] - cena litra paliwa, jak najmniejszy koszt

c) jak w b) ale zawsze tankujemy do pełna

"""

def agrimotor(S,L):
    result=i=0
    while i < len(S):
        for j in range(L+i,i,-1):
            if S[i]==True:
                result+=1
                i=j
                break
        return result

def tractor(K,L):
    n=len(K)
    stats=[]
    pos=0

    for i in range(1,L+1):
        if K[pos]>K[i]:
            pos=i

    while True:
        if pos+L >= n-1 and K(min(K[pos+1:-1]))>K[pos]:
            return stats
        new_stat = pos+1
        for i in range(new_stat+1,new_stat+L+1):
            if K[new_stat]>K[i]:
                new_stat=i
        pos = new_stat
        stats.append(pos)


# c) f(i) - najniższy koszt jeżeli tankujemy na i-tej stacji
# f(i) = min(f(i-L)+L*(i-L), f(i-L+1)+

"""
ZAD 2 
X = {x1,x2,..,xn} - zbiór n punktów na prostej
Ile min przedziałów jednostkowych (długości 1) trzeba, by objąć wszystkie punkty
"""

def points(X):
    n=len(X)
    X.sort()
    start=0
    cnt=1

    for i in range(1,n):
        if X[start]+1<X[i]:
            cnt+=1
            start=i
    return cnt

"""
T={t1,...,tn}
d(ti) - termin
g(ti) - zysk
wykonanie każdego zadania - 1 dzień
które zadanie wykonać by max zysk
"""
"""
ZAD 6 z pdf,
po prostu mediana
"""