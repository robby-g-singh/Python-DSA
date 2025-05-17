from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)  # default value is set to an empty list
        # flag to determine whether the graph is directed(unidirectional)/undirected(bi-directional):
        self.directed = directed

    def add_edge(self, u, v):  # u, v variables are similar to i,j but for graph theory
        if v not in self.adj[u]:  # checking for duplicate edges
            self.adj[u].append(v)  # Add node v to the adjacency list of node u, i.e. there is an edge from u to v
        if not self.directed:  # if the graph is undirected (bi-directional),
            if u not in self.adj[u]:
                self.adj[v].append(u)  # add node u to the adjacency list of node v, i.e. there is an edge from v to u

    def print_graph(self):
        for node in self.adj:
            print(f"{node}: {self.adj[node]}")
