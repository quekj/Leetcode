# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        ret = 0
        if root.val <= high and root.val >= low:
            ret += root.val
        ret += self.rangeSumBST(root.left, low, high)
        ret += self.rangeSumBST(root.right, low, high)
        return ret
