class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
        
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
    #z założeniem że lista ma wartownika!!!
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

c=Node(3,None)
b=Node(8,c)
a=Node(4,b)
g=Node(None,a)

merge_sort(g)

while g.next!=None:
    print(g.next.val)
    g=g.next