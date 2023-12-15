def inorderTraversal(root):
    if root == None: 
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)