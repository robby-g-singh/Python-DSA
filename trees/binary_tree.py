from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        new_node = BinaryTree(value)
        if self.left_child is None:
            self.left_child = new_node
        else:
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        new_node = BinaryTree(value)
        if self.right_child is None:
            self.right_child = new_node
        else:
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.value, end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value, end=' ')
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value, end=' ')

    def bfs(self):
        root = self
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

        return result


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(5)
tree.left_child.insert_left(3)
tree.left_child.insert_right(4)
tree.right_child.insert_left(6)
tree.right_child.insert_right(7)

tree.pre_order()
print('\n')
tree.in_order()
print('\n')
tree.post_order()
print('\n')
print(tree.bfs())
