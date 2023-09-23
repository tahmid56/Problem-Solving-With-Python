class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def dfsIterative(self, root):
        if (root is None):
            return []
        stack = [root]
        while(len(stack) > 0):
            curr = stack.pop(-1)
            print(curr.data)
            if(curr.right):
                stack.append(curr.right)
            if(curr.left):
                stack.append(curr.left)
            


tree = TreeNode(5)
tree.insert(4)
tree.insert(7)
tree.insert(2)
tree.insert(6)
tree.dfsIterative(tree)