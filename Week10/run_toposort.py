import topological_sort

def read_graph_from_file(filename):
    with open(filename, "r") as file:
        V, E = map(int, file.readline().split())  # Read number of vertices and edges
        adj = [[] for _ in range(V)]  # Initialize adjacency list
        for _ in range(E):
            u, v = map(int, file.readline().split())  # Read directed edges
            adj[u].append(v)  # Add edge u → v
    return V, adj

def main():
    # Read and process the first graph
    print("Topological Sorting for graph1.in:")
    V1, adj1 = read_graph_from_file("graph1.in")
    result1 = topological_sort.topological_sort(V1, adj1)
    print(result1)

    # Read and process the second graph
    print("\nTopological Sorting for graph2.in:")
    V2, adj2 = read_graph_from_file("graph2.in")
    result2 = topological_sort.topological_sort(V2, adj2)
    print(result2)

if __name__ == "__main__":
    main()
