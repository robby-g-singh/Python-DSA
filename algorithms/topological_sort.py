from collections import deque, defaultdict

num_courses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]

# first define the adjacency list and the in_degree array
adj = defaultdict(list)
in_degree = [0] * num_courses

# build the adjacency list and populate in_degree with the degrees of each node
for dest, src in prerequisites:
    adj[src].append(dest)
    in_degree[dest] += 1

# define a queue to store the nodes with 0 degrees and a topo_order array that will be returned at the end
queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
topo_order = []

while queue:
    node = queue.popleft()
    topo_order.append(node)  # since the node has 0 degrees - we will add it to the topological order

    # now we scan the neighbors of each node in the adjacency list
    for neighbor in adj[node]:
        in_degree[neighbor] -= 1  # node has been processed, the dependency for this neighbor can be decremented
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(topo_order) == num_courses:
    print(topo_order)  # valid topological order!
else:
    print("cycle was detected, no valid topological ordering")
