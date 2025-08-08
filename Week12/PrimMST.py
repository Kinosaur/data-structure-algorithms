import heapq


# Prim's Algorithm implementation
def prim(graph, V, start=0):
    mst = []  # To store the MST edges
    visited = [False] * V  # To track visited vertices
    min_heap = [(0, start, -1)]  # Min-heap to store (weight, vertex, from_vertex)

    while min_heap:
        weight, u, prev = heapq.heappop(min_heap)

        # Skip if the vertex has already been visited
        if visited[u]:
            continue

        visited[u] = True
        if prev != -1:
            mst.append((prev, u, weight))  # Append the edge to the MST

        # Explore neighbors of the vertex
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))  # Push adjacent vertices to heap

    return mst


# Read the graph type and adjacency list from input
graph_type = input("Enter graph type (Undirected Graph/Directed Graph): ").strip()
V, E = map(int, input().split())  # Number of vertices and edges
adj_list = [[] for _ in range(V)]  # Initialize adjacency list

# Read the edges
for _ in range(E):
    u, v, weight = map(int, input().split())  # Read edge u-v with weight
    u -= 1  # Adjusting index (assuming input is 1-indexed)
    v -= 1  # Adjusting index (assuming input is 1-indexed)

    adj_list[u].append((v, weight))  # Add directed edge u -> v
    if graph_type == "Undirected Graph":
        adj_list[v].append(
            (u, weight)
        )  # Add the reverse edge v -> u for undirected graph

# Run Prim's algorithm on the input graph
mst = prim(adj_list, V)

# Print the MST edges and their weights
print("Edges in the Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"Edge: {edge[0] + 1} - {edge[1] + 1}, Weight: {edge[2]}")
