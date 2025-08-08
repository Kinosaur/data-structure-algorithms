from disjointsets3 import DisjointSets

def get_index(row, col, num_cols):
    return row * num_cols + col

def is_valid(row, col, num_rows, num_cols):
    return 0 <= row < num_rows and 0 <= col < num_cols

def find_largest_cloud_size(M, N, matrix):
    dsu = DisjointSets(M * N)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 1:
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if is_valid(new_row, new_col, M, N) and matrix[new_row][new_col] == 1:
                        dsu.union(get_index(row, col, N), get_index(new_row, new_col, N))
    
    cloud_sizes = [0] * (M * N)
    max_cloud_size = 0
    
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 1:
                root = dsu.findset(get_index(row, col, N))
                cloud_sizes[root] += 1
                max_cloud_size = max(max_cloud_size, cloud_sizes[root])
    
    return max_cloud_size

M,N = map(int, input().split())
matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)
    
print(find_largest_cloud_size(M, N, matrix))