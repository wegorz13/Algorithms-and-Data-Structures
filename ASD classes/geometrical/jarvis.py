import numpy as np
import matplotlib.pyplot as plt
from lab1 import draw_points_from_tab,generate_uniform_points,from_point_to_x_and_y
import math

def find_min(points):
    start = (float('inf'), float('inf'))
    for p in points:
        if p[1] < start[1]:
            start = p
        elif p[1] == start[1]:
            if p[0] < start[0]:
                start = p
    return start

def vec_len(v):
    return math.sqrt(v[0]**2+v[1]**2)

def find_angle(a,b,c):
    AB = (b[0]-a[0],b[1]-a[1])
    BC = (c[0]-b[0],c[1]-b[1])

    dot = AB[0]*BC[0]+AB[1]*BC[1]
    return np.arcsin(dot/(vec_len(AB)*vec_len(BC)))

def find_angles_to_x(s,b):
    delta_x=b[0]-s[0]
    delta_y=b[1]-s[1]
    dist=vec_len((delta_x,delta_y))
    angle=(int(np.arccos(delta_x/dist)*10**12))/10**12
    return angle

def jarvis(points):
    start = find_min(points)
    stack=[start]

    next=(0,0,float('inf'))
    for p in points:
        if p!=start:
            angle = find_angles_to_x(start,p)
            if angle<next[2]:
                next=(p[0],p[1],angle)
            elif angle==next[2]:
                if vec_len((p[0]-start[0],p[1]-start[1]))>vec_len((next[0]-start[0],next[1]-start[1])):
                    next = (p[0], p[1], angle)

    stack.append((next[0],next[1]))
    points.remove((next[0],next[1]))

    t=0
    while stack[-1]!=start:
        next = (0, 0, -float('inf'))
        a = stack[t]
        b=stack[t+1]
        print(a,b)
        for c in points:
            if c!=b: #dla intow
                angle = find_angle(a, b,c)
                print(c,angle,next)
                if angle > next[2]:
                    next = (c[0], c[1], angle)
                elif angle == next[2]:
                    if vec_len((c[0] - b[0], c[1] - b[1])) > vec_len((next[0] - b[0], next[1] - b[1])):
                        next = (c[0], c[1], angle)
        stack.append((next[0],next[1]))
        points.remove((next[0],next[1]))
        t+=1

    print(stack)
    t=len(stack)
    for i in range(0, t):
        plt.plot([stack[i][0], stack[(i + 1) % t][0]], [stack[i][1], stack[(i + 1) % t][1]], 'bo-')
    plt.show()

# points=[(3,3),(3,1),(6,2),(6,5),(8,6),(6,9)]
points = generate_uniform_points(0,10,50)
print(points)
draw_points_from_tab(points,"red",30)
jarvis(points)
