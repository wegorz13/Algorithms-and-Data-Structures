#ociepka@agh.edu.pl

"""
ZAD 1
Problem sumy podzbiorów
tablica A[n] liczb naturalnych
sprawdzić czy istnieje A' podzbiór niekoniecznie spójny taki że suma A'=T
F(i,k) = F(i-1,k-A[i]) A[i]<=k k=0,...,T
F(0,A[0])=True
"""
def Sum(T,A):
    n=len(A)
    B = [False for _ in range(T+1)]
    B[A[0]]=True

    for i in range(n):
        for k in range(T,0,-1):
            pass

def F(A,k,i):
    if i==0:
        if k==A[0]:
            return True
        return False
    if k<0:
        return False
    if k==0:
        return True

    return F(A,k,i-1) or F(A,k-A[i],i-1)

"""
ZAD 2
Najdłuższy spójny podciąg:
Dwie tablice, A[n] i B[n]
Znaleźć długość najdłuższego wspólnego podciągu

f(i,j) = max( f(i-1,j-1) + 1) A[i]=B[j]
            ( f(i-1,j)      )
            ( f(i,j-1)      )

f(0,0) = 1 A[0]=B[0]
         0 wpp
"""
#T[a][b]=None, złożoność n^2
def pdc(A,B,i,j,T):
    if i==0 and j==0:
        if A[0]==B[0]:
            return 1
        return 0
    if i==0:
        for k in range(j+1):
            if B[k]==A[0]:
                return 1
            return 0
    if j==0:
        for k in range(i+1):
            if A[k]==B[0]:
                return 1
        return 0

    res=0
    if A[i]==B[j]:
        if T[i][j]==None:
            T[i][j]=pdc(A,B,i-1,j-1,T)+1
        res = max(res, T[i][j])

    if T[i-1][j]==None:
        T[i-1][j] = pdc(A,B,i-1,j,T)
        res = max(res,T[i-1][j])
    if T[i][j-1]==None:
        T[i][j-1] = pdc(A,B,i,j-1,T)
        res = max(res,T[i][j-1])

    return res

"""
ZAD 3
najdłuższy podciąg rosnący w A[n]:
a) wykorzystując algorytm z 2
b) O(nlogn)

a) B[n] = sorted(A[n])
    odpalamy alg z zad 2 na A i B koniec
    
b)
"""
# n^2
def Fc(A):
    n=len(A)
    M=[1]*n

    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i]:
                M[i]=max(M[i],M[j]+1)

# nlogn
def b(A):
    def binsearch(T,n):
        pass

    T=[-float('inf') ]

    for n in A:
        if n>T[-1]:
            T.append(n)
        else:
            i = binsearch(T,n)
            T[i]=n

    return len(T)-1

"""
ZAD 4
wydawanie monet
N - tablica nominałów
T - kwota do wydania
A = [1,5,8] T = 15
"""

def coins(A,T,i,cnt):
    if T<0:
        return float('inf')
    if i==0:
        if T==0:
            return cnt
        return float('inf')

    if T>=A[i]:
        return min(coins(A,T-A[i],i,cnt+1) or coins(A,T,i-1,cnt))
    return coins(A,T,i-1,cnt)

"""

"""
def piniendze(A,P,T):
    if T==0:
        return 0
    if T<0:
        return float('inf')

    for i in A:
        if P[T-1]==None:
            P[T-1]=F(A,P,T-i)

    return min([P[T-i] for i in A])

"""
ZAD 5
Szachownica
koszt wejścia na pole i,j to A[i][j]
chcemy przejść z 1,1 do n,n jak najmniejszym kosztem
Dozwolone ruchy o 1 pole w prawo lub w dół
"""