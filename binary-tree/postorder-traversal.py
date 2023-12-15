def postorderTraversal(root):
    if root == None: 
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]