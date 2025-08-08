from collections import deque

graph_type = input()
V, E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

# BFS Initialization
color = ["WHITE"] * V  # Node colors (WHITE, GRAY, BLACK)
d = [-1] * V  # Distance from source
p = [None] * V  # Predecessors


# Write your Breast-First Search code below
# BFS Algorithm (Starting from vertex 1, which is index 0)
def bfs(source):
    queue = deque([source])
    color[source] = "GRAY"
    d[source] = 0

    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if color[v] == "WHITE":
                color[v] = "GRAY"
                d[v] = d[u] + 1
                p[v] = u
                queue.append(v)
        color[u] = "BLACK"


bfs(0)  # Start BFS from vertex 1 (index 0)


# The code below is for printing output
print("vertex, color, distance, predecessors")
for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"

    print("%d %5s" % (v + 1, color[v]), dv, pv)
