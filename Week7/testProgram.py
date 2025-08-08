
# ---- BS Tree -----


from BinarySearchTree import *
'''
bst = BSTree()
a = [4, 5, 12, -5, -87, 9, 1023]

import random

random.shuffle(a)

for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)
    
bst.print_BSTree()
'''

bst2 = BSTree()
for k in [56,70,30,60,65,22,11,16,40,95,63,3,67]:
    x = BST_Node(k)
    bst2.Tree_Insert(x)

bst2.print_BSTree()
x = bst2.Tree_Search(40)
bst2.Tree_Delete(x)
bst2.print_BSTree()

# ---- RB Tree -----

from RedBlackTree import *

rbt = RBTree()
a = [12,5,3,11,15,7,10,13,14,6,4,17,8]
for k in a:
    rbt.insert(k)
rbt.print_RBTree()

rbt.delete(5)
rbt.print_RBTree()


    


