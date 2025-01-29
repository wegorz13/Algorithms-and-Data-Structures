def count_sort(T,pos):
    n = len(T)
    count = [0] * (ord("z")-ord("a")+1)
    output = ["" for _ in range(n)]

    for i in range(n):
        if len(T[i])>=pos+1:
            count[ord(T[i][pos])-ord("a")] += 1
        else:
            count[0]+=1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(n-1,-1,-1):
        if len(T[i])>=pos+1:
            output[count[ord(T[i][pos])-ord("a")] - 1] = T[i]
            count[ord(T[i][pos])-ord("a")] -= 1
        else:
            output[count[0]-1]=T[i]
            count[0]-=1

    return output

def radix(T):
    n=len(T)
    max_len=0
    for el in T:
        max_len=max(max_len,len(el))

    pos=max_len-1
    while pos>=0:
        result = count_sort(T,pos)
        print(result)
        pos-=1

    return result

T=["ala","makrela","kot","pentagram","ksiazka","od","karakan"]

print(radix(T))