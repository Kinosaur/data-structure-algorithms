def build_adjacency_list(num_vertices, edge_list, directed=True):
    # Create a dictionary with keys 0..(num_vertices-1) and empty list for each vertex
    adj_list = {i: [] for i in range(num_vertices)}

    # Populate the adjacency list with edges and their weights
    for u, v, weight in edge_list:
        adj_list[u].append((v, weight))  # Append the (destination vertex, weight) tuple

        # If the graph is undirected, add the reverse edge as well
        if not directed:
            adj_list[v].append((u, weight))

    return adj_list


def print_adjacency_list(adj_list):
    # Print each vertex and its corresponding list of neighbors with weights
    # Convert back to 1-indexed for display clarity
    for vertex in sorted(adj_list.keys()):
        # Convert each neighbor from 0-indexed to 1-indexed and display the weight
        neighbors = [f"{v + 1} ({weight})" for v, weight in adj_list[vertex]]
        print(f"{vertex + 1}: {', '.join(neighbors)}")


def main():
    # Ask the user if the graph is directed or not
    graph_type = input("Is the graph directed? (yes/no): ").strip().lower()
    directed = True if graph_type.startswith("y") else False

    # Read the number of vertices and edges
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    edge_list = []
    print(
        "Enter each edge as three integers (u v weight) on a new line (vertices are 1-indexed):"
    )

    # Read edge information and weights
    for _ in range(num_edges):
        try:
            u, v, weight = map(int, input().split())
            # Convert 1-indexed input to 0-indexed for internal storage
            u -= 1
            v -= 1
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                print("Invalid edge indices after conversion. Please check your input.")
                continue
            edge_list.append((u, v, weight))
        except ValueError:
            print(
                "Invalid input. Please enter two integers and a weight separated by space."
            )

    # Build and display the adjacency list
    adj_list = build_adjacency_list(num_vertices, edge_list, directed)
    print("\nAdjacency List:")
    print_adjacency_list(adj_list)


if __name__ == "__main__":
    main()
