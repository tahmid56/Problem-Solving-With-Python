class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.inorder_traversal()