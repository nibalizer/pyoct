#!/usr/bin/python


import numpy as np

import pylab as plt

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    p = f.readlines()
f.closed

z = [i.rstrip() for i in p]
p = z



darray = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]

carbons = []
for i in range(len(p)):
    letter, x, y, z = p[i].split('\t')
    carbons.append((i, float(x), float(y), float(z)))
xs =[]
ys =[]
zs =[]
for i in carbons:
    xs.append(i[1])
    ys.append(i[2])
    zs.append(i[3])

minx = min(xs)
miny = min(ys)
minz = min(zs)

new_xs = [i+abs(minx) for i in xs]
new_ys = [i+abs(miny) for i in ys]
new_zs = [i+abs(minz) for i in zs]

maxx = max(new_xs)
maxy = max(new_ys)
maxz = max(new_zs)

size = 1000000

factor_x = size / maxx
factor_y = size / maxy
factor_z = size / maxz

xs = [i * factor_x for i in new_xs]
ys = [i * factor_y for i in new_ys]
zs = [i * factor_z for i in new_zs]

carbons = []
for i in range(len(xs)):
    carbons.append((i, xs[i], ys[i], zs[i]))


#threetree = []
#for i in range(size):
#    threetree.append([])
#    for p in range(size):
#        threetree[i].append([])

threetree = np.zeros((size, size, size))

for i in carbons:
    x = i[1]
    y = i[2]
    z = i[3]
    index = i[0]
    threetree[x][y][z] = index




