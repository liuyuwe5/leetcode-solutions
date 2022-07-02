# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        search = root
        def findPlace(search):
            if search:
                if search.val < val:
                    if search.right:
                        findPlace(search.right)
                    else:
                        new = TreeNode()
                        new.val = val
                        search.right = new
                if search.val > val:
                    if search.left:
                        findPlace(search.left)
                    else:
                        new = TreeNode()
                        new.val = val
                        search.left = new
            
        if root:
            findPlace(search)
        else:
            root = TreeNode()
            root.val = val
        return root