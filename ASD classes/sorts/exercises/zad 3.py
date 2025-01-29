#ZAD 1
#implementacja quick sort tak by nigdy nie zużywał więcej niż O(nlogn) pamieci

#ZAD 2
# implementacja QS bez rekurencji (ale z wlasnym stosem)
#
# ZAD 3 = 1 + 2
#
# ZAD4
# algorytm scalający k list
#
# ZAD5
# struktura danych z operacjami:
# -insert
# -remove median
#
# ZAD6
# znowu pojemniki z woda
def partition(T,p,k):
    return 1

def quicksort(T,p,k):
    while p<k:
        q = partition(T,p,k)
        if q-p<k-q:
            quicksort(T,p,q-1)
            p=q+1
        else:
            quicksort(T,q+1,k)
            k=q-1

def stack():
    pass

def QSCT(T,p,k):
    S=stack()
    S.push(p)
    S.push(k)
    while not S.is_empty:
        b = S.pop()
        a=S.pop()
        q=partition(T,a,b)
        if a!=b:
            S.push(a)
            S.push(q-1)
            S.push(q+1)
            S.push(b)
            S.push(k)
            S.pop()
            S.is_empty()