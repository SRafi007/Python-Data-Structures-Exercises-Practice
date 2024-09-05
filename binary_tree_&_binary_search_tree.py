
"""
Binary Tree
A Binary Tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child. It does not have any specific order of elements.

Procedure for a Binary Tree:
Step 1: Define the structure for a Node with data, left child, and right child.
Step 2: Create methods for inserting nodes into the tree.
Step 3: Implement tree traversal methods (inorder, preorder, postorder).


Binary Search Tree (BST)
A Binary Search Tree (BST) is a special type of Binary Tree where each node follows the property:

All values in the left subtree are less than the node's value.
All values in the right subtree are greater than the node's value.
Procedure for a Binary Search Tree:
Step 1: Define the structure for a Node with data, left child, and right child.
Step 2: Implement methods for inserting nodes into the tree based on the BST property.
Step 3: Implement traversal methods (inorder, preorder, postorder).

"""

#Python Code for Binary Search Tree:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node while maintaining the BST property
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        elif new_node.data > current.data:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    # Inorder traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

# Example Usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder traversal (Sorted Order):")
bst.inorder(bst.root)  # Output: 2 3 4 5 6 7 8

print("\nPreorder traversal:")
bst.preorder(bst.root)  # Output: 5 3 2 4 7 6 8

print("\nPostorder traversal:")
bst.postorder(bst.root)  # Output: 2 4 3 6 8 7 5
