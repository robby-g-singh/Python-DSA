import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}


def dijkstra_search_algorithm(adj_list, start):
    min_heap = [(0, start)]
    distances = {node: float('inf') for node in adj_list}
    previous = {node: None for node in adj_list}

    distances[start] = 0

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in adj_list[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    if path[0] == start:
        return path
    else:
        return []


dist, prev = dijkstra_search_algorithm(graph, 'A')
print(dist)
print(reconstruct_path(prev, 'A', 'D'))
