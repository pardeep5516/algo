class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def insert(self, data):
        if data < self.val:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r = Node(28)
r.insert(17)
r.insert(10)
r.insert(41)
r.insert(31)
r.insert(51)
inorder(r)