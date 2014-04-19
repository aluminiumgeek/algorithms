#!/usr/bin/env python 
#
# Implementation of Dijkstra's algorithm

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

sv = 'A' # source vertex
tv = 'G' # target vertex

dist = {} # distances from the source to each vertex
prev = {} # pointers to preceding vertices
U = V[:] # list of unfinished vertices


def dijkstra():
    infinity_edge = max(E.values()) + 1
    for k in V:
        dist[k] = infinity_edge
        prev[k] = None

    dist[sv] = 0 # distance from the source to the source
    
    while U:
        min_vertex = min(dist.items(), key=lambda x: x[1] if x[0] in U else infinity_edge)[0]
        
        if (min_vertex == sv and sv not in U) or min_vertex == tv:
            break
        
        U.remove(min_vertex)
        
        neighbor_edges = filter(lambda x: x.startswith(min_vertex), E)
    
        for edge in neighbor_edges:
            v1, v2 = edge # AB -> A, B
            alt = dist[v1] + E[edge]
        
            if alt < dist[v2]: # relax
                dist[v2] = alt
                prev[v2] = v1

dijkstra()

# Extract the shortest path
s = []
u = tv
while prev[u]:
    s.insert(0, u)
    u = prev[u]

print s
