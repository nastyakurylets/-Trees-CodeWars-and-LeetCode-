"""
Sort binary tree by levels script.
"""
from collections import deque
class Node:
    """
    Node class.
    """
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """
    Tree by levels function.
    """
    if node is None:
        return []
    result = []
    queue = deque([node])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
