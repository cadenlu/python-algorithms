from collections import deque

def level_order_traversal(root):
    res = []
    if root == None:
        return res
    
    queue = deque()
    queue.append(root)
    
    while queue:
        level = []
        level_size = len(queue)
        
        while level_size > 0:
            node = queue.popleft()
            level.append(node.val)
            if (node.left != None):
                queue.append(node.left)
            if (node.right != None):
                queue.append(node.right)
            level_size -= 1
            
        res.append(level)
        
    return res