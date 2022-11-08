from math import *
t1 = int(input())
g1 = int(input())
t2 = int(input())
g2 = int(input())
distance = 6371.01*(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print(distance)