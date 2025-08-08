## Checking Binary Search Tree (BST) Property

To check whether a binary tree satisfies the Binary Search Tree (BST) property, we will write a function named `Is_BST` in the `BST.py` file. The function will operate based on the following rules and conditions:

### Base Case
If the node being checked is `None`, the subtree is considered valid since an empty tree always satisfies the BST property.

### Validation
For each node in the tree, we will verify that its key lies within a specified range (`min_key`, `max_key`). This range ensures that the node's key is greater than all the keys in its left subtree and less than all the keys in its right subtree. If the node's key falls outside this range, the tree does not satisfy the BST property, and the function will return `False`.

### Recursive Check
If the current node satisfies the range condition, the function will recursively validate its left and right subtrees. For the left subtree, the `max_key` is updated to the current node's key since all nodes in the left subtree must be smaller than the current node. Similarly, for the right subtree, the `min_key` is updated to the current node's key since all nodes in the right subtree must be greater than the current node.

The `Is_BST` function will use these rules to ensure that the entire tree adheres to the BST property. The function will return `True` if the tree satisfies the BST property and `False` otherwise. We will add this function to the `BST.py` file to validate the tree structure after insertion, deletion, or any manual modifications.