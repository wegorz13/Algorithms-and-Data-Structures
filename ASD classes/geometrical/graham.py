import numpy as np
import matplotlib.pyplot as plt
from lab1 import draw_points_from_tab,generate_uniform_points,from_point_to_x_and_y

def mergeSort(Array, Left, Right, start):
    def merge(Array, Left, Mid, Right):
        Len1 = Mid - Left + 1
        Len2 = Right - Mid
        Left_Array = Array[Left:Mid + 1]
        Right_Array = Array[Mid + 1:Right + 1]
        Left_index = Right_index = 0
        Main_index = Left

        while Left_index < Len1 and Right_index < Len2:

            det = orient(start, Left_Array[Left_index], Right_Array[Right_index])

            if det == 1:
                Array[Main_index] = Left_Array[Left_index]
                Left_index += 1
            elif det == -1:
                Array[Main_index] = Right_Array[Right_index]
                Right_index += 1
            Main_index += 1

        while Left_index < Len1:
            Array[Main_index] = Left_Array[Left_index]
            Left_index += 1
            Main_index += 1

        while Right_index < Len2:
            Array[Main_index] = Right_Array[Right_index]
            Right_index += 1
            Main_index += 1

    if Left < Right:
        Mid = (Left + Right) // 2
        mergeSort(Array, Left, Mid, start)
        mergeSort(Array, Mid + 1, Right, start)
        merge(Array, Left, Mid, Right)


def find_min(points):
    start = (float('inf'), float('inf'))
    for p in points:
        if p[1] < start[1]:
            start = p
        elif p[1] == start[1]:
            if p[0] < start[0]:
                start = p
    return start


def dist(s, x, y):
    dx = (s[0] - x[0]) ** 2 + (s[1] - x[1]) ** 2
    dy = (s[0] - y[0]) ** 2 + (s[1] - y[1]) ** 2

    return dx, dy


def orient(s, x, y):  # x<y prosta s->x
    matrix = np.array([[y[0] - s[0], y[1] - s[1]],
                       [x[0] - y[0], x[1] - y[1]]])
    det = np.linalg.det(matrix)
    if det > 0:
        return 1
    elif det == 0:
        return 0
    else:
        return -1


def graham(points):
    start = find_min(points)
    points.remove(start)
    n = len(points)
    mergeSort(points, 0, n - 1, start)
    print(points)
    points.reverse()
    stack = [start, points[0], points[1]]
    t = 3
    i = 2

    while i < n:
        if orient(stack[t - 2], stack[t - 1], points[i]) == -1:
            stack.append(points[i])
            t += 1
            i += 1
        else:
            stack.pop()
            t -= 1
    print(stack)
    draw_points_from_tab(points, "red", 30)

    for i in range(0, t):
        plt.plot([stack[i][0],stack[(i+1)%t][0]], [stack[i][1],stack[(i+1)%t][1]], 'bo-')
    plt.show()

points = generate_uniform_points(0,30,50)

graham(points)
