class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

# 1 -> (0)-> 3-> 2-> (4)-> 6-> 5

def print_list(list):
    while list!=None:
        print(list.val,"-> ",end="")
        list = list.next
    print("None")


# Filip Węgrzyn
#algorytm dla każdego elementu p.next (dodaje guardiana) listy sprawdza k elementów na prawo od niego i zapisuje najmniejszy z nich (tmp_min)
# oraz el. występujący przed najmniejszym(prev_to_tmp), jeśli wartość tmp_min jest mniejsza od elementu który rozpatrywaliśmy,
# zamienia je miejscami i przechodzi do następnego elementu,
# dla k=1 podmieniane są elementy sąsiadujące jeśli kolejny element ma mniejsza wartość od poprzedniego

#złożoność czasowa
# dla k=1 -> O(n)
# dla k=logn -> O(nlogn)
# dla k=n -> O(n^2)

def SortH(p,k):
    g = Node()
    g.next=p
    p=g
    prev_to_tmp = Node()

    if k == 1:
        while p.next != None:
            if p.next.next != None and p.next.next.val < p.next.val:
                p.next = p.next.next
                p.next.next, p.next.next.next = p.next.next.next, p.next.next
                p=p.next.next
            else: p = p.next
        return g.next

    while p.next!=None:
        print_list(g.next)
        i=0
        q = p.next

        while q.next!=None and i<k:
            i+=1
            if i==1:
                tmp_min=q.next
                prev_to_tmp = q
            elif q.next.val<tmp_min.val:
                tmp_min = q.next
                prev_to_tmp = q
            q=q.next

        if i>0 and tmp_min.val<p.next.val:
            prev_to_tmp.next = p.next
            tmp_min.next, p.next.next = p.next.next, tmp_min.next
            p.next = tmp_min

        p=p.next

    return g.next





