class Solution(object):
    def maxPathSum1(self, root):
        maxPathSumTree = root.val
        maxPathSumNode = root.val     
                                      
        left, right = None, None
        if root.left != None:
            left = self.maxPathSum1(root.left)
            maxPathSumNode = max(maxPathSumNode, root.val + left[1])
            maxPathSumTree = max(maxPathSumTree,maxPathSumNode,left[0])
            
        if root.right != None:
            right = self.maxPathSum1(root.right)
            maxPathSumNode = max(maxPathSumNode, root.val + right[1])
            maxPathSumTree = max(maxPathSumTree,maxPathSumNode,right[0])

        if left != None and right != None:
            maxPathSumTree = max(maxPathSumTree,root.val + left[1] + right[1])
        return maxPathSumTree, maxPathSumNode

    def maxPathSum(self, root):
        return self.maxPathSum1(root)[0]