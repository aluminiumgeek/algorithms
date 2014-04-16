#!/usr/bin/env python 
#
# Implementation of Floyd-Warshall algorithm
# Graph

G = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'E'],
    'C': ['D', 'E', 'F'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G']
}

# Edges
E = {
    'AB': 10,
    'AC': 20,
    'AD': 15,
    'BE': 2,
    'BC': 9,
    'CE': 10,
    'CF': 8,
    'CD': 6,
    'DF': 7,
    'EG': 8,
    'FG': 10
}

# Vertices
V = G.keys()
V.append('G')
V.sort()

sv = 'A' # source vertex
tv = 'G' # target vertex

dist = {}
next = {}
infinity_edge = max(E.values()) + 1
for i in V:
    for j in V:
        dist[i+j] = E[i+j] if i+j in E else infinity_edge
        
        if i == j or dist[i+j] == infinity_edge:
            next[i+j] = 0
        else:
            next[i+j] = i
            

def floyd_warshall():
    for k in V:
        for i in V:
          for j in V:
              if dist[i+k] + dist[k+j] < dist[i+j]:
                  dist[i+j] = dist[i+k] + dist[k+j]
                  next[i+j] = k

floyd_warshall()

# Reconstruct path
def path(i, j):
    if dist[i+j] == infinity_edge:
        return 'no path'

    intermediate = next[i+j]
    
    if intermediate == i:
        return "" # direct edge from i to j
    else:
        return path(i, intermediate) + intermediate + path(intermediate, j)

print path(sv, tv) + tv
