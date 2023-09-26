import math

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

    def treeSumIterative(self, root):
        if(root is None):
            return 0
        total = 0
        stack = [root]
        while(len(stack)>0):
            curr = stack.pop(-1)
            total += curr.data
            if(curr.right):
                stack.append(curr.right)
            if(curr.left):
                stack.append(curr.left)
        return total
    
    def treeSumRecursive(self, root):
        if(root is None):
            return 0
        return root.data + self.treeSumRecursive(root.left) + self.treeSumRecursive(root.right)

    def treeMinIterative(self, root):
        smallest = math.inf
        if(root is None):
            return 
        stack = [root]
        while(len(stack) > 0):
            curr = stack.pop(-1)
            if(curr.data < smallest):
                smallest = curr.data
            if(curr.left):
                stack.append(curr.left)
            if(curr.right):
                stack.append(curr.right)
        return smallest

    def treeMinRecursive(self, root):
        if(root is None):
            return math.inf
        
        leftMin = self.treeMinRecursive(root.left)
        rightMin = self.treeMinRecursive(root.right)
        return min(root.data, leftMin, rightMin)


tree = TreeNode(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(6)
tree.insert(1)
# tree.dfsIterative(tree)
# print(tree.dfsRecursive(tree))
# tree.bfsIterative(tree)
# print(tree.treeIncludesIterative(tree, 9))
# print(tree.treeIncludesRecursive(tree, 7))
# print(tree.treeSumIterative(tree))
# print(tree.treeSumRecursive(tree))
# print(tree.treeMinIterative(tree))
print(tree.treeMinRecursive(tree))