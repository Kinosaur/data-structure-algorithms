def build_adjacency_list(num_vertices, edge_list, directed=True):
    # // Create a dictionary with keys 0..(num_vertices-1) and empty list for each vertex
    adj_list = {i: [] for i in range(num_vertices)}
    for u, v in edge_list:
        adj_list[u].append(v)

        # // If the graph is undirected, add the reverse edge as well
        if not directed:
            adj_list[v].append(u)
    return adj_list


def print_adjacency_list(adj_list):
    # // Print each vertex and its corresponding list of neighbors
    # // Convert back to 1-indexed for display clarity
    for vertex in sorted(adj_list.keys()):
        # Convert each neighbor from 0-indexed to 1-indexed
        neighbors = [str(v + 1) for v in adj_list[vertex]]
        print(f"{vertex + 1}: {', '.join(neighbors)}")


def main():
    # // Ask the user if the graph is directed or not
    graph_type = input("Is the graph directed? (yes/no): ").strip().lower()
    directed = True if graph_type.startswith("y") else False

    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    edge_list = []
    print(
        "Enter each edge as two integers (u v) on a new line (vertices are 1-indexed):"
    )
    for _ in range(num_edges):
        try:
            u, v = map(int, input().split())
            # // Convert 1-indexed input to 0-indexed for internal storage
            u -= 1
            v -= 1
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                print("Invalid edge indices after conversion. Please check your input.")
                continue
            edge_list.append((u, v))
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")

    adj_list = build_adjacency_list(num_vertices, edge_list, directed)
    print("\nAdjacency List:")
    print_adjacency_list(adj_list)


if __name__ == "__main__":
    main()
