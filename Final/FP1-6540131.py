class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def inorder_tree_walk(x, result):
    if x is not None:
        inorder_tree_walk(x.left, result)
        result.append(x.key)
        inorder_tree_walk(x.right, result)


def tree_insert(root, z):
    y = None
    x = root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.p = y
    if y is None:
        root = z  # Tree was empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return root


def find_minimum_difference(bst):
    if len(bst) < 2:
        return 0
    min_diff = float("inf")
    for i in range(1, len(bst)):
        min_diff = min(min_diff, bst[i] - bst[i - 1])
    return min_diff


number = input("Enter a list of integers separated by spaces: ").strip()
BST = list(map(int, number.split()))

root = None
for key in BST:
    node_to_insert = Node(key, f"data-{key}")
    root = tree_insert(root, node_to_insert)

sorted_keys = []
inorder_tree_walk(root, sorted_keys)

min_diff = find_minimum_difference(sorted_keys)
print(f"Output: {min_diff}")
