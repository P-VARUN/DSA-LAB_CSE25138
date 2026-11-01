# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    # Insert a node
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Search for a node
    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    # Find minimum value node
    def find_min(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    # Delete a node
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            elif root.left is None:
                return root.right

            # Case 3: Only left child
            elif root.right is None:
                return root.left

            # Case 4: Two children
            else:
                temp = self.find_min(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)

        return root

    # Inorder: Left -> Root -> Right
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder: Root -> Left -> Right
    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder: Left -> Right -> Root
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Main program
bst = BinarySearchTree()
root = None

while True:
    print("\n\n--- BINARY SEARCH TREE ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        root = bst.insert(root, data)
        print("Node inserted successfully.")

    elif choice == 2:
        data = int(input("Enter value to search: "))

        if bst.search(root, data):
            print("Element found.")
        else:
            print("Element not found.")

    elif choice == 3:
        data = int(input("Enter value to delete: "))
        root = bst.delete(root, data)
        print("Node deleted successfully.")

    elif choice == 4:
        print("Inorder Traversal:")
        bst.inorder(root)

    elif choice == 5:
        print("Preorder Traversal:")
        bst.preorder(root)

    elif choice == 6:
        print("Postorder Traversal:")
        bst.postorder(root)

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")