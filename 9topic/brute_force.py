import heapq


def brute_force_paths(graph, start, end, path=[], shortest=None):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = brute_force_paths(graph, node, end, path, shortest)
            if new_path:
                if not shortest or path_length(graph, new_path) < path_length(graph, shortest):
                    shortest = new_path
    return shortest


def path_length(graph, path):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i+1]]
    return length


def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        if current_vertex == end:
            break

    return distances[end]


graph = {'Warehouse': {'A': 2, 'B': 5},
         'A': {'Warehouse': 2, 'C': 3, 'D': 1},
         'B': {'Warehouse': 5, 'D': 2},
         'C': {'A': 3, 'D': 4, 'Destination': 7},
         'D': {'A': 1, 'B': 2, 'C': 4, 'Destination': 1},
         'Destination': {'C': 7, 'D': 1}}

start_vertex = 'Warehouse'
end_vertex = 'Destination'

shortest_path_brute_force = brute_force_paths(graph, start_vertex, end_vertex)
shortest_path_length_brute_force = path_length(graph, shortest_path_brute_force)
shortest_path_dijkstra = dijkstra(graph, start_vertex, end_vertex)
print(f"Кратчайший путь от {start_vertex} до {end_vertex} (Дейкстра): {shortest_path_dijkstra}")
print(f"Кратчайший путь от {start_vertex} до {end_vertex} (Brute Force): {shortest_path_brute_force} с длиной {shortest_path_length_brute_force}")
