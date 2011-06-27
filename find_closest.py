#!/usr/bin/python


import sys
import numpy as np

filename = sys.argv[1]

with open(filename, 'r') as f:
    p = f.readlines()
f.closed


carbons = []
for i,line in enumerate(p):
    if i % 100 == 0:
        print i, line
    letter, x, y, z = line.split('\t')
    carbons.append([i, float(x), float(y), float(z)])

bond_len_max = 2

def within_range(c1,c2):
    result = True
    for a,b in zip(c1,c2)[1:]:
        result = result and (b <= a + bond_len_max and b >= a - bond_len_max)
    return result

def distance_formula(c1,c2):
    dist = np.sqrt((c2[1] - c1[1])**2 + (c2[2] - c1[2])**2 + (c2[3] - c1[3])**2)
    return dist

for carbon in carbons:
    close = []
    print "Finding Closest"
    for carbon_1 in carbons:
        if within_range(carbon, carbon_1):
            close.append(carbon_1)
            print carbon_1
    distance = []
    print "Finding Distances"
    for close_carbon in close:
        distance.append((distance_formula(carbon, close_carbon),close_carbon))
        print close_carbon
    distance.sort()
    for distance, close_carbon in distance[1:4]:
        carbon.append(close_carbon[0])

for carbon in carbons:
    print ",".join(map(str,carbon))


        
