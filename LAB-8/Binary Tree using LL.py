class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BINARY TREE CLASS
class BinaryTree:
    def __init__(self):
        self.root = None

# Create the binary tree
    def create_tree(self):
        self.root = Node('A')
        # Left and right children of A
        self.root.left = Node('B')
        self.root.right = Node('C')
        # Children of B
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        # Right child of C
        self.root.right.right = Node('F')
    # Preorder Traversal
    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

# Inorder Traversal
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)
# Postorder Traversal
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
# Level-order Traversal
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            # Add left child
            if node.left is not None:
                queue.append(node.left)
            # Add right child
            if node.right is not None:
                queue.append(node.right)

# MAIN PROGRAM
tree = BinaryTree()
# Create the binary tree
tree.create_tree()
# Traversals
print("Preorder: ", end="")
tree.preorder(tree.root)
print("\nInorder: ", end="")
tree.inorder(tree.root)
print("\nPostorder: ", end="")
tree.postorder(tree.root)
print("\nLevel-order: ", end="")
tree.level_order()