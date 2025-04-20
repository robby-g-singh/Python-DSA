from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        # inserting into an empty tree
        if not self.root:
            self.root = new_node
        # non-empty tree insertion:
        current = self.root
        while True:
            if current.val > val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            elif val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return
            else:
                return

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def delete(self, root, key):
        if not root:
            return None

        if key < root.val:  # search for the Node where node.val == key
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:  # Node found
            if not root.left and not root.right:  # Case 1: node to be deleted has no children
                return None
            elif not root.left:  # Case 2: node to be deleted has one child node. Return the existing node
                return root.right
            elif not root.right:
                return root.left
            else:  # Case 3: node to be deleted has two children
                # find the minimum value in the right subtree of the node we want to delete. because that value will be
                # the next contender for taking the place of this current node:
                min_larger_node = self.get_min(root.right)
                # once the min of the right subtree is found, overwrite the current node we want to delete with the
                # min value of the right subtree:
                root.val = min_larger_node.val
                # now delete the original min value node from the right subtree. this is done by passing the right
                # subtree and the value of min_larger_node. since it is the most minimum value of the right subtree,
                # it will have no children - and therefore deleted and set to None.
                root.right = self.delete(root.right, min_larger_node.val)
        # return the root to continue keeping track of the root of the tree as a whole, but also subtrees that are
        # passed to the delete function.
        return root

    def search(self, key):
        current = self.root
        # similar behavior to Binary Search, if the current node == key - return True
        # otherwise, based on whether the current.val > or < key - set current to either the left or right subtree
        while current:
            if current.val == key:
                return True
            elif current.val > key:
                current = current.left
            else:
                current = current.right

        return False

    # pre-order follows the pattern: Root -> Left -> Right (MLR)
    def pre_order(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def iterative_pre_order(self):
        if not self.root:
            return

        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.val, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # post-order follows the pattern Left -> Right -> Root (LRM)
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val, end=" ")

    def iterative_post_order(self):
        if not self.root:
            return

        stack1 = [self.root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.val, end=" ")

    # In-Order follows the pattern Left -> Root -> Right (LMR)
    def in_order(self, node):
        if node is None:
            return

        self.in_order(node.left)
        print(node.val, end=" ")
        self.in_order(node.right)

    def iterative_in_order(self):
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right

    def bfs(self):
        if not self.root:
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.val, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    @staticmethod
    def get_min(node):
        current = node
        while current and current.left:
            current = current.left
        return current

    @staticmethod
    def get_max(node):
        current = node
        while current and current.right:
            current = current.right
        return current
