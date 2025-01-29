import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def generate_uniform_points(left, right, n = 10 ** 5):
    """
    Funkcja generuje równomiernie n punktów na kwadratowym obszarze od left do right (jednakowo na osi y) o współrzędnych rzeczywistych
    :param left: lewy kraniec przedziału
    :param right: prawy kraniec przedziału
    :param n: ilość generowanych punktów
    :return: tablica punktów w postaci krotek współrzędnych, np. [(x1, y1), (x2, y2), ... (xn, yn)]
    """
    points = [(round(np.random.uniform(left,right)),round(np.random.uniform(left,right))) for i in range(n)]
    x_cd= [(np.random.uniform(left,right)) for i in range(n)]
    y_cd = [(np.random.uniform(left,right)) for i in range(n)]
    # points = np.array(points)
    return x_cd,y_cd

# x_cd,y_cd = generate_uniform_points(-1000,1000,10**5)
# x_cd,y_cd = generate_uniform_points(-10**14,10**14,10**5)
# plt.scatter(x_cd, y_cd,s=30,color='red')

def generate_uniform_points_circle(Sx,Sy,R,n):
    x_cd = np.array([0 for _ in range(n)])
    y_cd = np.array([0 for _ in range(n)])
    for i in range(n):
        angle = np.random.random()*2*np.pi
        x_cd[i] = R*np.cos(angle)+Sx
        y_cd[i] = R*np.sin(angle)+Sy

    return x_cd,y_cd

# x_cd,y_cd = generate_uniform_points_circle(0,0,100,1000)
# plt.scatter(x_cd, y_cd,s=30,color='green')

def generate_points_vector(left,right,a,b,n):
    vector = (b[0]-a[0],b[1]-a[1])
    # (2, 0.1)
    max_val = min(abs(right/vector[0]),abs(right/vector[1]))

    x_cd = ([0 for _ in range(n)])
    y_cd = ([0 for _ in range(n)])

    for i in range(n):
        k = np.random.uniform(-max_val,max_val)
        x_cd[i] = vector[0]*k
        y_cd[i] = vector[1] * k + 0.05

    return x_cd,y_cd

# x_cd,y_cd = generate_points_vector(-1000,1000,(-1.0,0.0),(1.0,0.1),10000)



def classify_points_matrix(x_cd,y_cd,a,b,eps):
    left_to_vec = []
    right_to_vec = []
    inside_vec = []
    n = len(x_cd)
    for i in range(n):
        c = (x_cd[i], y_cd[i])
        matrix = np.array([[c[0]-a[0], c[1]-a[1]],
                  [b[0]-c[0], b[1]-c[1]]])
        det = np.linalg.det(matrix)
        if det>eps:
            right_to_vec.append(c)
        elif det<-eps:
            left_to_vec.append(c)
        else:
            inside_vec.append(c)
    return left_to_vec,right_to_vec,inside_vec

def draw_points_from_tab(tab,c,size):
    n=len(tab)
    x_cd = [tab[i][0] for i in range(n)]
    y_cd = [tab[i][1] for i in range(n)]
    plt.scatter(x_cd,y_cd,s=size,color=c)

def from_point_to_x_and_y(tab):
    n = len(tab)
    x_cd = [tab[i][0] for i in range(n)]
    y_cd = [tab[i][1] for i in range(n)]
    return x_cd,y_cd

a,b = np.array([-1.0,0.0]), np.array([1.0,0.1])
x_cd,y_cd = generate_uniform_points(-100,100,10**5)
ltv,rtv,inv = classify_points_matrix(x_cd,y_cd,(-1.0,0.0),(1.0,0.1),20)
print(inv)
draw_points_from_tab(ltv,'red',30)
draw_points_from_tab(rtv,'green',30)
draw_points_from_tab(inv,'blue',30)
plt.show()
