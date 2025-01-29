def binary_search(T,el,p,r):
    mid = (p+r)//2
    if T[mid]==el:
        return mid
    if T[mid]>el:
        return binary_search(T,el,p,mid-1)
    else:
        return binary_search(T, el, mid+1, r)

def binary_insert(T,el,p,r):
    mid = (p+r)//2
    if el<T[0]:
        return 0
    if el>T[r]:
        return r+1

    if T[mid] <= el <= T[mid+1]:
        return mid+1

    if T[mid] > el:
        return binary_insert(T, el, p, mid - 1)
    else:
        return binary_insert(T, el, mid + 1, r)

