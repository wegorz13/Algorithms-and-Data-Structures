def left(i):
    return i*2+1

def right(i):
    return i*2+2

def parent(i):
    return (i-1)//2

def heapify(A,n,i):
    l=left(i)
    r=right(i)
    max_ind=i

    if l<n and A[l]>A[i]:
        max_ind=l

    if r<n and A[r]>A[i]:
        max_ind=r

    if max_ind!=i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def build_heap(A):
    n=len(A)

    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)

def heap_sort(A):
    n=len(A)

    build_heap(A)

    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapify(A,i,0)