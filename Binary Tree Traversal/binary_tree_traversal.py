"""
Binary Tree Traversal.
"""
class Node:
    """
    Node class.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Pre-order traversal
def pre_order(node):
    """
    Pre order tree traversal.
    """
    if node:
        result = [node.data]
        result.extend(pre_order(node.left))
        result.extend(pre_order(node.right))
        return result
    return []

# In-order traversal
def in_order(node):
    """
    In order traversal.
    """
    if node:
        result = []
        result.extend(in_order(node.left))
        result.append(node.data)
        result.extend(in_order(node.right))
        return result
    return []

# Post-order traversal
def post_order(node):
    """
    Post order traversal.
    """
    if node:
        result = []
        result.extend(post_order(node.left))
        result.extend(post_order(node.right))
        result.append(node.data)
        return result
    return []
