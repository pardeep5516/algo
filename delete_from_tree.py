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
    def delete(self, data):
        if self.val == data:
            if self.left and self.right:
                [psucc, succ] = find_max(self, self.left)
                if psucc.left == succ:
                    psucc.left = succ.left
                else:
                    psucc.right = succ.left
                self.left = succ.left
                self.right = succ.right
                return succ
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if data < self.val:
                if self.left:
                    self.left = self.left.delete(data)
            else:
                if self.right:
                    self.right = self.right.delete(data)
        return self
def find_max(parent, child):
    if child.right:
        return find_max(child, child.right)
    else:
        return [parent, child]

def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

r = Node(28)
r.insert(17)
r.insert(10)
r.insert(41)
print("inorder tree = ")
inorder(r)
r.delete(10)
print("inorder tree = ")
inorder(r)