"""ZAD 1 SAT"""

"""ZAD 2 DAG ZNALEŹĆ CZY ISTNIEJE ŚCIEŻKA HAMILTONA
sortujemy topologicznie, jeśli istnieje krawędź między każdą parą sąsiednich wierzchołków
"""

"""ZAD 3 GRAF SKIEROWANY CZY W GRAFIE ZNAJDUJE SIE DOBRY POCZĄTEK 
(wierzchołek z którego możemy dotrzeć ścieżką do każdego z wierzchołków)

puszczamy DFS i zapisujemy czasy przetworzenia
z wierzchołka o największym czasie przetworzenia znowu odpalamy DFS jeśli odwiedzimy wszystkie wierzchołki, to jest DP
mozemy tez włączyć raz BFS i później odpalać go z aktualnie nie odwiedzonych wierzchołków aż zostanie jeden 
i tamten jako jedyny może być DP 

ZAD 4 WYDŁUŻANIE NAJKRÓTSZEJ ŚCIEŻKI Z U DO V USUWAJĄC 1 KRAWĘDŹ
odpalamy BFS z u, zapisujemy odległość v od u
usuwamy 1 krawędź ze ścieżki sprawdzamy ponownie przywracamy ja usuwamy kolejna i tak dla każdej krawędzi
V^2*d(u,v)

-----
robimy BFS z u i v
dla danego wierzchołka znamy odległość od u i od v
bierzemy dwa sąsiednie wierzchołki a i b jeśli d(a,u)+d(b,v)+1==d(u,v) to krawędź ab leży na najkrótszej ścieżce
zliczamy takie krawędzie i grupujemy je według odległości od u, jeśli jest taka krawędź jedyna w swojej grupie odległości to ją trzeba usunąć

"""


