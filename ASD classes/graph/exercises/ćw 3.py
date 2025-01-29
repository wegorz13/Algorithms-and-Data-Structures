"""IMPLEMENTACJA DIJKSTRY"""
from queue import PriorityQueue
def dijkstra(s,G):

    n=len(G)
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((d[s], s))

    def relax(u,v,d):
        if d[v]>d(u)+d:
            d[v]=d[u]+d
            Q.put((d[v],v))

    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            relax(u,v[0],v[1])

    return d

"""DIJKSTRA ALE LICZYMY ILOCZYN WAG - korzystamy z logarytmów ale jeśli liczby są między 0,1 w jakimś cyklu to logarytm bedzie ujemny,
a mnozac te liczby bedziemy sobie zmniejszac koszt w nieskonczonosc"""


"""ZAD 3 mamy kursy walut k[u][v]eR+
1u -> k[u][v] jednostek waluty v
chcemy znaleźć cykl w którym będziemy zaczynać z 1u a kończyć z większą ilością (karuzela pieniędzy)
chyba szukamy dodatniego cyklu na logarytmach, mozna zmienic warunek w bellmanie albo przemnożyć wierzchołki przez -1
"""

"""
ZAD 4 G=(V,E,W)
szukamy najkrótszej ścieżki ale możemy użyć tylko krawędzi o niższej wadze niż poprzednia
zmodyfikowany dijkstra, dajemy do kolejki krotkę wierzchołek,ostatnia waga krawędzi
"""

"""
ZAD 5 ALICJA I BOB

"""

