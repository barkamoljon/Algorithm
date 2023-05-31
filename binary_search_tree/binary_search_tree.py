class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value:
            if current_node.left is None:
                return None
            else:
                return self._find(value, current_node.left)
        else:
            if current_node.right is None:
                return None
            else:
                return self._find(value, current_node.right)

    def delete(self, value):
        if self.root is None:
            return
        else:
            self._delete(value, self.root)

    def _delete(self, value, current_node):
        if value < current_node.value:
            if current_node.left is not None:
                self._delete(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is not None:
                self._delete(value, current_node.right)
        else:
            if current_node.left is None and current_node.right is None:
                # This is a leaf node.
                current_node = None
            elif current_node.left is None:
                # This node has only a right child.
                current_node = current_node.right
            elif current_node.right is None:
                # This node has only a left child.
                current_node = current_node.left
            else:
                # This node has two children.
                # Find the inorder successor.
                successor = current_node.right
                while successor.left is not None:
                    successor = successor.left

                # Swap the value of the current node with the inorder successor.
                current_node.value = successor.value

                # Delete the inorder successor.
                self._delete(successor.value, current_node.right)
