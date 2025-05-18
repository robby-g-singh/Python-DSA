from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)  # default value is set to an empty list
        # flag to determine whether the graph is directed(unidirectional)/undirected(bi-directional):
        self.directed = directed

    def add_edge(self, u, v):  # u, v variables are similar to i,j but for graph theory
        if v not in self.adj[u]:  # checking for duplicate edges
            self.adj[u].append(v)  # Add node v to the adjacency list of node u, i.e. there is an edge from u to v
        if not self.directed and u not in self.adj[v]:  # if the graph is undirected (bi-directional)
            self.adj[v].append(u)  # add node u to the adjacency list of node v, i.e. there is an edge from v to u

    def bfs(self, start):
        discovered = set()  # set to keep track of nodes already visited
        queue = deque([start])  # initialize queue with starting node
        discovered.add(start)  # same for discovered set

        traversal = []  # empty list to preserve traversal order

        while queue:  # loop through queue
            current = queue.popleft()  # keep track of current node
            traversal.append(current)  # update the traversal list

            for neighbor in self.adj[current]:  # loop for the adjacent list for current
                if neighbor not in discovered:  # if neighbor has not been visisited: add to discovered & queue
                    discovered.add(neighbor)
                    queue.append(neighbor)

        return traversal  # return the order traversed!

    def print_graph(self):
        for node in self.adj:
            print(f"{node}: {self.adj[node]}")


graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
print(graph.bfs())
