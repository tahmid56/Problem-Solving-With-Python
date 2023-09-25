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
            
    def dfsRecursive(self, root):
        arr = []
        if(root):    
            arr.append(root.data)
            arr += self.dfsRecursive(root.left)
            arr += self.dfsRecursive(root.right)
        return arr
    
    def bfsIterative(self, root):
        if(root is None):
            return
        queue = [root]
        while(len(queue) > 0):
            curr = queue.pop(0)
            print(curr.data)
            if(curr.left):
                queue.append(curr.left)
            if(curr.right):
                queue.append(curr.right)
    
    def treeIncludesIterative(self, root, target):
        if(root is None):
            return False
        queue = [root]
        while(len(queue) > 0):
            curr = queue.pop(0)
            if(curr.data == target):
                return True
            if(curr.left):
                queue.append(curr.left)
            if(curr.right):
                queue.append(curr.right)
        return False

    def treeIncludesRecursive(self, root, target):
        if(root is None):
            return False
        if(root.data == target):
            return True
        return self.treeIncludesRecursive(root.left, target) or self.treeIncludesRecursive(root.right, target)

tree = TreeNode(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(6)
# tree.dfsIterative(tree)
# print(tree.dfsRecursive(tree))
# tree.bfsIterative(tree)
# print(tree.treeIncludesIterative(tree, 9))
print(tree.treeIncludesRecursive(tree, 7))