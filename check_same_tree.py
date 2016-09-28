class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def __init__(self):
        A = TreeNode(3)
        A.left = TreeNode(2)
        A.right = TreeNode(5)
        A.left.left = TreeNode(1)
        B = TreeNode(3)
        B.left = TreeNode(2)
        B.right = TreeNode(5)
        B.left.left = TreeNode(1)
        print self.isSameTree(A, B)
    def inorder(self, node, res):
        if node:
            self.inorder(node.left, res)
            res.append(node.val)
            self.inorder(node.right, res)

        return res

    def preorder(self, node, res):
        if (node):
            res.append(node.val)
            self.preorder(node.left, res)
            self.preorder(node.right, res)
        return res

    def isSameTree(self, A, B):
        if self.inorder(B, []) == self.inorder(A, []) and self.preorder(A, []) == self.preorder(B, []):
            return 1
        return 0


if __name__ == '__main__':
    solution = Solution()
