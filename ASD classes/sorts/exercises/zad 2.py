#scalanie

def scalanie(T1,T2):
    n1=len(T1)
    n2=len(T2)
    i=j=0

    n3 = n1+n2
    T3 = [0 for _ in range(n3)]
    k=0

    while i<n1 and j<n2:
        if T1[i]<=T2[j]:
            T3[k] = T1[i]
            k+=1
            i+=1
        else:
            T3[k] = T2[j]
            k += 1
            j += 1

    if i==n1:
        for l in range(k,n3):
            T3[l] = T2[j]
            j+=1
    elif j==n2:
        for l in range(k,n3):
            T3[l] = T1[i]
            i+=1

    return T3

T1 = [1,5,9,12,16,17]
T2=[2,5,7,11,20,25]

print(scalanie(T1,T2))


class Node:
    def __init__(self,val):
        self.next=None
        self.val=val

def print_list(list):
    while list!=None:
        print(list.val,"-> ",end="")
        list = list.next
    print("None")

a6 = Node(14)
a5 = Node(5)
a5.next=a6
a4 = Node(8)
a4.next=a5
a3 = Node(1)
a3.next=a4
a2 = Node(4)
a2.next=a3
a1 = Node(3)
a1.next=a2


#MERGE SORT

#a impl scalania
# b impl wyciag serii naturalnej
# c impl znalezienia końca listy
# d merge sort

#zad 2 A - posortowana tablica liczb, x - liczba
# szukamy i,j: A[i]+A[j]=x

#zad 3
#zbiorniki z wodą; współrzędna lewego i prawego górnego rogu; znaleźć ile z nich zapełni się całkiem po zalaniu określoną ilością wody

#zad 4
#odcinki na tej samej osi, znaleźć odcinek który zawiera najwięcej pozostałych; znamy ich początki i końce które się nie nakładają

def merge(p1,p2):
    head = l = Node(None)

    while p1!=None and p2!=None:
        if p1.val<=p2.val:
            l.next = p1
            p1=p1.next
        else:
            l.next = p2
            p2=p2.next

        l = l.next

    if p1==None:
        l.next = p2
    elif p2==None:
        l.next = p1

    return head.next

def extract(p):

    while p.next!=None and p.val<=p.next.val:
        p=p.next
    Q = p.next
    p.next=None
    return Q

def end(p):
    if p!=None:
        while p.next!=None:
            p=p.next
    return p

def merge_sort(p):
    h=p
    p=p.next
    e = end(p)
    while True:
        q=extract(p)
        if q==None:
            h.next=p
            return h
        z = extract(q)
        x = merge(p,q)
        if z==None:
            h.next=x
            return h
        e.next=x
        e=end(x)
        p=z

def zad2(T,x):
    n = len(T)



def zad4(T):
    n= len(T)

    # f(ai) - liczba przedziałów zaczynających się przed ai
    #g(bi) - liczba przedziałów kończących się przed bi
    #
    # g(bi) - f(ai)

print_list(merge_sort(a1))















