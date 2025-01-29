"""ZAD 4 prosze zaimplementować funkcje sprawdzajaca czy dwa słowa są anagramami "look" i "kool" """

def anagram(w1,w2):
    T=[0]*(ord('z')-ord('a')+1)
    for ch in w1:
        T[ord(ch)-ord('a')]+=1
    for ch in w2:
        T[ord(ch)-ord('a')]-=1
    n = len(T)
    for i in range(n):
        if T[i]!=0:
            return False
    return True

"""ZAD 1 T-tablica n liczb ze zbioru {0,..,n^2-1} - jak najszybszy alg. sortowania

#n=10 a,b={0,...,n^2-1}
#0,9 99
#n=100 
# radix_sort(T,n):
    #counting_sort(T,n,n)
    #counting_sort(T,n,1)
"""

"""ZAD 2 T- tablica n liczb, zawierająca O(nlogn) różnych wartości - sortowanie



ZAD 3 liczba inwersji w tablicy

ZAD 5 T-tablica gdzie T[i]={0,...,k-1} chcemy znaleźć najmniejszzy podprzedział w którym są wszystkie kolory
zaczynamy od 0 indeksu i znajdujemy minimalne p elementów dla którego warunek sie spełnia, zliczamy kolory do tablicy,
później zmniejszamy zakres aż warunek sie wywali i przesuwamy przedział w prawo na kolejne indeksy, 
usuwamy lewy skrajny kolor dodajemy prawy skrajny jak wartość każego koloru>0 to jest git

ZAD 6 T - tablica n różnych kolorów - chcemy dwie liczby z T które po posortowaniu byłyby koło siebie i których różnica jest maks

tworzymy n kubełków, znajdujemy min i max element i dzielimy kubełki na równe przedziały i wrzucamy do nich liczby z T
jeżeli w każdym kubełku jest 1 element to sprawdzamy różnice sąsiednich el,
jeśli nie to niektóre są puste więc znajdujemy najdłuższy ciąg pustych kubełków i bierzemy największy element z lewego kubełka i najmniejszy z prawego

"""