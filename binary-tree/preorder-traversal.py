def preorderTraversal(root):
    if root == None: 
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)