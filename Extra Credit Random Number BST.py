import random

#Basic Node definition. Each Node contains a Value, a left child, and a right child
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

#insert Value into the appropiate spot in the tree
def insert(root, node):

    if root is None:
        root=node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder_traversal(root):
    #finish code to print all values with an inorder traversal
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)

        print(root.val),

def preorder_traversal(root):
    if root:
        print(root.val),
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def get_height(node):
    if node is None:
        return 0;

    else:
        left_depth = get_height(node.left)
        right_depth = get_height(node.right)

        if (left_depth > right_depth):
            return left_depth + 1
        else:
            return right_depth + 1

numbers = random.sample(range(0, 100), 100)

bst_random = (numbers)

print (numbers)


root = Node(1)

for i in numbers:
    insert(root, Node(i))

#inorder_traversal(bst)

print ("Height of tree is %d" %(get_height(root)))