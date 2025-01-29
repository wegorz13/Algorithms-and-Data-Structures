# def multi_num(n):
#     numbers = [0]*10
#     while n>0:
#         numbers[n%10]+=1
#         numbers//=10
#     cnt=0
#     for el in numbers:
#         if el>1:
#             cnt+=1
#     return cnt
#
# def single_num(n):
#     numbers = [0]*10
#     while n>0:
#         numbers[n%10]+=1
#         numbers//=10
#     cnt=0
#     for el in numbers:
#         if el==1:
#             cnt+=1
#     return cnt
#
# def count_sort_1(T):
#     n=len(T)
#     output=[0]*n
#     counter=[0]*10
#
#     for i in range(len(T)):
#         counter[multi_num(T[i])]+=1
#
#     for i in range(1,len(counter)):
#         counter[i]+=counter[i-1]
#
#     for i in range(n-1,-1,-1):
#         output[counter[multi_num(T[i])]-1]=T[i]
#         counter[multi_num(T[i])]-=1
#
# def count_sort_2(T):
#     n=len(T)
#     output=[0]*n
#     counter=[0]*10
#
#     for i in range(len(T)):
#         counter[multi_num(T[i])]+=1
#
#     for i in range(1,len(counter)):
#         counter[i]+=counter[i-1]
#         counter[i-1] = n-1-counter[i-1]
#     counter[9] = n-1-counter[9]
#
#     for i in range(n):
#         output[counter[single_num(T[i])]-1]=T[i]
#         counter[single_num(T[i])]+=1
#
# def pretty(T):
#     count_sort_1(T)
#     count_sort_2(T)
#
#     return T

def countingSort(A, p, way):
    B = [0] * len(A)
    C = [0] * 10
    #
    for i in range( len(A) ):
        C[ A[i][p] ] += 1
    #
    if way == 1:
        for i in range( 1, len(C) ):
            C[i] += C[i-1]
    else:
        for i in range( len(C) - 2, -1, -1):
            C[i] += C[i+1]
    #
    for i in range( len(A) - 1, -1, -1 ):
        B[ C[ A[i][p] ] - 1 ] = A[i]
        C[ A[i][p] ] -= 1
    #
    return B
#end def ^^^


def cyfryKrotne(n):
    T = [0] * 9
    #
    while n > 0:
        T[ n % 10 ] += 1
        n = n // 10
    #end while

    cyfry_jednokrotne = 0
    cyfry_wielokrotne = 0

    for i in range( len(T) ):
        if T[i] > 1: cyfry_wielokrotne += 1
        elif T[i] == 1: cyfry_jednokrotne += 1
    #end for
    return cyfry_jednokrotne, cyfry_wielokrotne
#end def ^^^


def prettySort(T):
    n = len(T)
    #
    for i in range( n ):
        cyfry_jednokrotne, cyfry_wielokrotne = cyfryKrotne( T[i] )
        T[i] = ( T[i], cyfry_jednokrotne, cyfry_wielokrotne )
    #
    T = countingSort(T, 2, 1)
    T = countingSort(T, 1, -1)
    for i in range(n):
        T[i]=T[i][0]

    return T
#end def ^^^

T = [ 123, 445, 28, 22, 4456 ]
T = prettySort(T)
print(T)