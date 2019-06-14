class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        current_node = self
        current_parent = None
        while current_node is not None:
            current_parent = current_node
            if value >= current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        if value >= current_parent.value:
            current_parent.right = BSTNode(value)
        else:
            current_parent.left = BSTNode(value)

    def search(self, value):
        current_node = self
        while current_node is not None:
            if value == current_node.value: # wasted a lot of time putting it below
                return current_node
            if value > current_node.value:
                current_node = current_node.right
            if value < current_node.value:
                current_node = current_node.left
        return None

    def search_parent(self, value):
        current_node = self
        current_parent = None
        while current_node is not None:
            if value == current_node.value:
                return current_parent
            if value > current_node.value:
                current_parent = current_node
                current_node = current_node.right
            if value < current_node.value:
                current_parent = current_node
                current_node = current_node.left
        return current_parent

    def remove(self, value):
        node = self.search(value)
        parent_node = self.search_parent(value)
        parent_child_relationship = 'left' if value < parent_node.value else 'right'
        if node is None: # can't find this value to delete
            return
        if node.left is None and node.right is None: # no children
            if parent_child_relationship == 'right':
                parent_node.right = None
            else:
                parent_node.left = None
        if node.left is not None and node.right is not None: # two children
            # 1. record down the minimum value of the right subtree's minimum
            # 2. remove the right subtree's min node
            # 3. replace the node's value with it's right subtree's minimum value
            right_subtree_minimum_node = node.right.min_node()
            self.remove(right_subtree_minimum_node.value)
            node.value = right_subtree_minimum_node.value
        if node.left is not None:
            if parent_child_relationship == 'right':
                parent_node.right = node.left
            else:
                parent_node.right = node.left
        if node.right is not None:
            if parent_child_relationship == 'right':
                parent_node.right = node.right
            else:
                parent_node.right = node.right

    def min_node(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


    def __repr__(self):
        return '(Node value: ' + str(self.value) + ' ' + str(self.left) + ' ' + str(self.right) + ')'
