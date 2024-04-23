"""
Delete Node in a BST script.
"""
# Definition for a binary tree node.
class TreeNode:
    """
    Tree node class.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution class.
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete node from the tree.
        """
        if not root:
            return None
        parent = None
        curr = root
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr:
            return root
        if curr.left and curr.right:
            min_node_parent = curr
            min_node = curr.right
            while min_node.left:
                min_node_parent = min_node
                min_node = min_node.left
            curr.val = min_node.val
            if min_node_parent.left == min_node:
                min_node_parent.left = min_node.right
            else:
                min_node_parent.right = min_node.right
        else:
            child = curr.left if curr.left else curr.right
            if not parent:
                root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        return root
