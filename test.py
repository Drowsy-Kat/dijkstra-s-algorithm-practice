import heapq

def dijkstra(graph, start, destinations):
    # Initialize distances dictionary with start node distance 0 and others as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Predecessor dictionary to store the predecessor node for each node in the shortest path
    predecessors = {}
    
    # Priority queue to store nodes with their current distance from start
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current node is one of the destinations, construct and return the path
        if current_node in destinations:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors.get(current_node)
            return current_distance, list(reversed(path))
        
        # If the current distance is greater than the known distance to this node, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the new distance is less than the known distance, update and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # If none of the destinations are reachable from start node, return infinity and an empty path
    return float('inf'), []

# Example graph representation (adjacency list)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = input("Enter start node: ").strip()
destinations = input("Enter destinations separated by spaces: ").strip().split()

print("Start node:", start_node)
print("Destinations:", destinations)
print("Graph keys:", list(graph.keys()))

quickest_distance, quickest_path = dijkstra(graph, start_node, destinations)
if quickest_path:
    print(f"The quickest destination reachable from {start_node} is: {quickest_path[-1]}")
    print(f"The shortest distance is: {quickest_distance}")
    print(f"The shortest path is: {' -> '.join(quickest_path)}")
else:
    print("None of the destinations are reachable from the start node.")
