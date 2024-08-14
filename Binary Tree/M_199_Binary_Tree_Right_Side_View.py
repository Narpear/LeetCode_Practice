# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        maxDepth = -1

        def check(node, depth):
            nonlocal maxDepth
            if not node:
                return 
            
            if depth > maxDepth:
                maxDepth = depth
                # print(depth, maxDepth)
                result.append(node.val)
                
            check(node.right, depth+1)
            check(node.left, depth+1)
            return

        check(root, 0)
        return result
