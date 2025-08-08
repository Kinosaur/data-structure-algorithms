import sys

sys.setrecursionlimit(10001)

root = None


class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x is not None:
        Inorder_Tree_Walk(x.left)
        print(x.key, end=" ")
        Inorder_Tree_Walk(x.right)


def Tree_Minimum(node):
    while node.left is not None:
        node = node.left
    return node


def Tree_Maximum(node):
    while node.right is not None:
        node = node.right
    return node


def Tree_Predecessor(x):
    if x.left is not None:
        return Tree_Maximum(x.left)
    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p


def Tree_Successor(x):
    if x.right is not None:
        return Tree_Minimum(x.right)

    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p

    return y


def Transplant(u, v):
    if u.p is None:
        global root
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p


def Tree_Delete(root, z):
    if z.left is None:
        Transplant(z, z.right)
    elif z.right is None:
        Transplant(z, z.left)
    else:
        y = Tree_Minimum(z.right)
        if y.p != z:
            Transplant(y, y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z, y)
        y.left = z.left
        y.left.p = y
    return root


def Tree_Search(node, k):
    while node is not None and k != node.key:
        if k < node.key:
            node = node.left
        else:
            node = node.right
    return node


def Tree_Insert(root, z):
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


def printCall(node, indent, last):
    if node is not None:
        print(indent, end="")
        if last:
            print("R----", end="")
            indent += "     "
        else:
            print("L----", end="")
            indent += "|    "
        print(str(node.key))
        printCall(node.left, indent, False)
        printCall(node.right, indent, True)


def print_BSTree(root):
    printCall(root, "", True)


def Is_BST(node, min_key=float("-inf"), max_key=float("inf")):
    if node is None:
        return True
    if not (min_key < node.key < max_key):
        return False
    return Is_BST(node.left, min_key, node.key) and Is_BST(
        node.right, node.key, max_key
    )


# Test cases
if __name__ == "__main__":
    # Create a BST and insert nodes
    print("Test Tree_Insert")
    keys = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    root = None
    for key in keys:
        node_to_insert = node(key, f"data-{key}")
        root = Tree_Insert(root, node_to_insert)

    print("Tree after insertion:")
    print_BSTree(root)

    # Test Is_BST
    print("\nTest Is_BST")
    print(f"Is the tree a valid BST? {'Yes' if Is_BST(root) else 'No'}")

    # Test Inorder_Tree_Walk
    print("\nTest Inorder_Tree_Walk")
    print("Inorder traversal of the tree:")
    Inorder_Tree_Walk(root)  # Should print keys in sorted order
    print()

    # Test Tree_Search
    print("\nTest Tree_Search")
    search_key = 7
    found_node = Tree_Search(root, search_key)
    if found_node:
        print(f"Node with key {search_key} found: {found_node.data}")
    else:
        print(f"Node with key {search_key} not found.")

    # Test Tree_Minimum
    print("\nTest Tree_Minimum")
    min_node = Tree_Minimum(root)
    print(f"The minimum key in the tree is: {min_node.key}")

    # Test Tree_Maximum
    print("\nTest Tree_Maximum")
    max_node = Tree_Maximum(root)
    print(f"The maximum key in the tree is: {max_node.key}")

    # Test Tree_Successor
    print("\nTest Tree_Successor")
    node_to_find_successor = Tree_Search(root, 13)
    if node_to_find_successor:
        successor = Tree_Successor(node_to_find_successor)
        if successor:
            print(f"The successor of {node_to_find_successor.key} is {successor.key}")
        else:
            print(f"No successor exists for {node_to_find_successor.key}")
    else:
        print("Node to find successor not found.")

    # Test Tree_Delete
    print("\nTest Tree_Delete")
    delete_key = 6
    node_to_delete = Tree_Search(root, delete_key)
    if node_to_delete:
        root = Tree_Delete(root, node_to_delete)
        print(f"Tree after deleting node with key {delete_key}:")
        print_BSTree(root)
    else:
        print(f"Node with key {delete_key} not found, cannot delete.")

    # Test Is_BST again after deletion
    print("\nTest Is_BST after Deletion")
    print(f"Is the tree a valid BST? {'Yes' if Is_BST(root) else 'No'}")
