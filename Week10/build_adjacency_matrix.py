def build_adjacency_matrix(num_vertices, edge_list, directed=True):
    # // Initialize a num_vertices x num_vertices matrix with zeros
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edge_list:
        matrix[u][v] = 1
        # // If the graph is undirected, add the reverse edge as well
        if not directed:
            matrix[v][u] = 1
    return matrix


def print_adjacency_matrix(matrix):
    num_vertices = len(matrix)

    # // Print header row
    print("    ", end="")
    for j in range(num_vertices):
        print(f"{j + 1:3}", end="")  # // Print vertices 1-indexed
    print()  # // New line

    # // Print a separator line
    print("   " + "-" * (3 * num_vertices))

    # // Print each row with the row vertex label on the left
    for i, row in enumerate(matrix):
        print(f"{i + 1:3}|", end="")  # // 1-indexed vertex label for the row
        for val in row:
            print(f"{val:3}", end="")
        print()  # // New line after each row


def main():
    # // Ask the user if the graph is directed or not
    graph_type = input("Is the graph directed? (yes/no): ").strip().lower()
    directed = True if graph_type.startswith("y") else False

    # // Read the number of vertices and edges
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    edge_list = []

    print(
        "Enter each edge as two integers (u v) on a new line (vertices are 1-indexed):"
    )
    for _ in range(num_edges):
        try:
            # // Read the input vertices (assumed to be 1-indexed) and convert to 0-indexed
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            edge_list.append((u, v))
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")

    # // Build and display the adjacency matrix
    matrix = build_adjacency_matrix(num_vertices, edge_list, directed)
    print("\nAdjacency Matrix:")
    print_adjacency_matrix(matrix)


if __name__ == "__main__":
    main()
