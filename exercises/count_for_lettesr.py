def count_sort(T):
    n = len(T)
    count = [0] * (ord("z")-ord("a")+1)
    output = ["" for _ in range(n)]

    for i in range(n):
        count[ord(T[i])-ord("a")] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(n-1,-1,-1):
        output[count[ord(T[i])-ord("a")] - 1] = T[i]
        count[ord(T[i])-ord("a")] -= 1

    return output

T = ["c","e","a","b","z","g","j","f"]

print(ord("z")-ord("a"))

print(count_sort(T))