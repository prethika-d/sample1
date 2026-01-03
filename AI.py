
from collections import deque

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Input graph
graph = {}
print("Enter each vertex and its neighbors (space separated):")
for _ in range(n):
    v = input("Vertex: ")
    graph[v] = input(f"Neighbors of {v}: ").split()

# Input starting vertex
start = input("Enter starting vertex: ")

# Two queues
visited = deque()
not_visited = deque()

# Start BFS
not_visited.append(start)

print("BFS Traversal:", end=" ")

while not_visited:
    node = not_visited.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                not_visited.append(neighbor)
