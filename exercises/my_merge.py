def merge(T,l,mid,r):
    len1 = mid-l+1
    len2 = r-mid

    T1 = T[l:mid+1]
    T2=T[mid+1:r+1]
    ind_1=ind_2=0
    Main_ind=l

    while ind_1<len1 and ind_2<len2:
        if T1[ind_1]<=T2[ind_2]:
            T[Main_ind]=T1[ind_1]
            ind_1+=1
        else:
            T[Main_ind] = T2[ind_2]
            ind_2 += 1
        Main_ind+=1

    while ind_1<len1:
        T[Main_ind]=T1[ind_1]
        ind_1+=1
        Main_ind+=1

    while ind_2<len2:
        T[Main_ind]=T2[ind_2]
        ind_2+=1
        Main_ind+=1

def merge_sort(T,l,r):
    if l<r:
        mid=(l+r)//2
        merge_sort(T,l,mid)
        merge_sort(T,mid+1,r)
        merge(T,l,mid,r)