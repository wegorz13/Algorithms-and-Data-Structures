#sortowanie listy jednokierunkowej

class Node:
    def __init__(self,val,next):
        self.next=next
        self.val=val

def print_list(list):
    while list!=None:
        print(list.val,"-> ",end="")
        list = list.next
    print("None")

# a) implementacja wstawiania
# b) insertion sort
# c) wyjmowanie elementu maksymalnego
# d) selection sort

def insert(first,n):

    while first.next is not None and first.next.val<n.val:
        first=first.next

    n.next=first.next
    first.next=n

def insertion_sort(first):
    s=Node(None,None)
    while first.next!=None:
        tmp=first.next
        first.next = first.next.next
        insert(s,tmp)

    first.next=s.next
    return first

def min_max(T):
    minT=T[0]
    maxT=T[0]
    n=len(T)

    for i in range(n):
        minT=min(minT,T[i])
        maxT = max(maxT, T[i])

    return minT,maxT


def get_max(L):
    p=L
    q=p.next

    while q.next!=None:
        if q.next.val>p.next.val:
            p=q
        q=q.next
    el_max=p.next
    p.next=el_max.next

    return el_max

def selection_sort(H):
    l=H
    new = Node(None,None)
    while l.next is not None:
        a = get_max(l)
        a.next=new.next
        new.next=a

    l.next=H.next

f=Node(4,None)
e=Node(2,f)
d=Node(1,e)
c=Node(8,d)
b=Node(3,c)
a=Node(None,b)

p = insertion_sort(a)
print_list(p)



