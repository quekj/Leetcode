# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def inOrder(root, order):
            if root is None:
                return
            inOrder(root.left, order)
            order.append(root.val)
            inOrder(root.right, order)
            
        order = []
        inOrder(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True
