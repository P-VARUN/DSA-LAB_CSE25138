class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

# Insert root
    def set_root(self, data):
        self.tree[0] = data
# Set left child
    def set_left(self, parent_index, data):
        child_index = 2 * parent_index + 1
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range!")
# Set right child
    def set_right(self, parent_index, data):
        child_index = 2 * parent_index + 2
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range!")
    # Preorder Traversal
    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)

# Inorder Traversal
    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)
# Postorder Traversal
    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")
# Level-order Traversal
    def level_order(self):
        for value in self.tree:
            if value is not None:
                print(value, end=" ")
# Display Array
    def display(self):
        print("\nArray Representation:")
        for i in range(self.size):
            print(f"Index {i}: {self.tree[i]}")
# MAIN PROGRAM
tree = BinaryTreeArray(7)
# Create the tree
tree.set_root('A')
# Children of A
tree.set_left(0, 'B')
tree.set_right(0, 'C')
# Children of B
tree.set_left(1, 'D')
tree.set_right(1, 'E')
# Right child of C
tree.set_right(2, 'F')
# Display tree
tree.display()
# Traversals
print("\nPreorder: ", end="")
tree.preorder()
print("\nInorder: ", end="")
tree.inorder()
print("\nPostorder: ", end="")
tree.postorder()
print("\nLevel-order: ", end="")
tree.level_order()