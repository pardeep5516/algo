class Node:
    def __init__(self, key, left_child, right_child):
        self.left = left_child
        self.right = right_child
        self.value = key

def inorder(root):
    if(root):
        inorder(root.left)
        print(root.value, end = " ")
        inorder(root.right)
def preorder(root):
    if(root):
        print(root.value, end = " ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

d = Node(20, None, None)
e = Node(40, None, None)
f = Node(60, None, None)
g = Node(80, None, None)
b = Node(30, d, e)
c = Node(70, f, g)
a = Node(50, b, c)

print("inorder")
inorder(a)
print("preorder")
preorder(a)
print("postorder")
postorder(a)