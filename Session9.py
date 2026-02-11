# ---------------------------------------- Trees ----------------------------------------

class Tree_Node:
    def __init__(self,data):
        self.value = data
        self.left_child = None
        self.Right_child = None

# Write a Recursive Function which creates a tree containig Inorder and Preorder methods.
    def BT(inorder,preorder):
        if not inorder or not preorder:
            return None
        root = Tree_Node(preorder[0])
        index = inorder.index(preorder[0])
        root.left_child = BT(preorder[1 : index+1],inorder[: index])
        root.Right_child = BT(preorder[index+1 :],inorder[index+1 :])

# Write a Recursive Function which creates a tree's reverse.
    def reverse_tree(root):
        if not root:
            return None
        root.left_child , root.right_child = reverse_tree(root.right_child) , reverse_tree(root.left_child)
        return root

# Write the Recursive BST-Search-Tree Function.
    def BST_search(root, x):
        if not root:
            return True
        if root.value == x:
            return False
        if x < root.value:
            return BST_search(root.left_child, x)
        return BST_search(root.Right_child, x)

# Write the Recursive Binary-Search-Tree Function.
    def BT_search(root, x):
        if not root:
            return False
        if root.value == x:
            return True
        left = BT_search(root.left_child, x)
        if left:
            return left
        return BT_search(root.Right_child, x)

# Write a Recursive Function which gives the maximum data of a BST-Search-Tree.
    def BST_max(root):
        if root is None:
            return None
        if root.Right_child is None:
            return root.value
        return BST_max(root.Right_child)

# Write a Recursive Function which adds a data to a BST-Search-Tree.
    def BST_insert(root, x):
        if root is None:
            return Tree_Node(x)
        if x < root.value:
            root.left_child = BST_insert(root.left_child, x)
        elif x > root.value:
            root.Right_child = BST_insert(root.Right_child, x)
        return root