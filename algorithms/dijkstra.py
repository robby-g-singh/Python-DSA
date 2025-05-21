import heapq


# Dijkstra's search algorithm is used for finding the shortest path from a source node to all other nodes in weighted
# graphs. So the idea is to find the shortest path by expanding to the next adjacent node with the smallest
# cumulative weight (lowest total cost so far)
# structure of each node along with its adjacency list is as follows:
# u: [(v, w)] -
# u being the source
# v being the adjacent node
# w being the weight/cost for u -> v
# Time: O((V + E) * logV)
# Space: O(V)
# Use Case: weighted graphs, with non-negative edge weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}


def dijkstra_search_algorithm(adj_list, start):
    min_heap = [(0, start)]  # initialize a MinHeap with the starting node & set its weight to 0 since it is the source
    distances = {node: float('inf') for node in adj_list}  # create a dictionary to keep track of distances of each node
    previous = {node: None for node in adj_list}  # dictionary to keep track of the prev node for reconstruct_path()

    distances[start] = 0  # initialize the empty distances dictionary with the first starting node, and set weight to 0

    while min_heap:
        # in the MinHeap, elements are stored in the order of (distance/weight, node),
        # hence the arrangement below to store the variables for further processing
        current_dist, current_node = heapq.heappop(min_heap)
        # check if the weight of the current node is more than the overall total distance cost:
        if current_dist > distances[current_node]:
            continue
        # if not, store variables neighbor, eight from adj_list[current_node] which stores variables in the order of:
        # (node, distance/weight)
        for neighbor, weight in adj_list[current_node]:
            distance = current_dist + weight  # keep track of a cumulative distance
            # compare it with the cost of going from current -> neighbor currently stored in distances
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # if its less costly, update distances[neighbor]
                # update the previous field to be the current node, as we are now going to push neighbor to the heap
                previous[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, end):
    path = []  # empty list to keep track/build the path
    current = end  # start from the end
    while current is not None:
        path.append(current)
        current = previous[current]  # keep traversing previous until current == None
    path.reverse()  # reverse the list

    if path[0] == start:  # check to see if the start is correct
        return path
    else:
        return []
