import unittest
from bst_node import BSTNode

class TestBSTNode(unittest.TestCase):

    def test_can_init(self):
        BSTNode(5)

    def test_can_add_nodes_and_maintain_bst_property(self):
        bst_node = BSTNode(1)
        bst_node.add(3)
        self.assertEqual(bst_node.right.value, 3)
        bst_node.add(2)
        self.assertEqual(bst_node.right.left.value, 2)

    def test_can_search_for_value(self):
        bst_node = BSTNode(1)
        bst_node.add(3)
        bst_node.add(5)
        self.assertEqual(bst_node.search(3).value, 3)
        self.assertEqual(bst_node.search(5).value, 5)
        self.assertEqual(bst_node.search(2), None)

    def test_can_search_for_node_parent(self):
        bst_node = BSTNode(1)
        bst_node.add(3)
        bst_node.add(5)
        self.assertEqual(bst_node.search_parent(5).value, 3)

    def test_can_get_minimum_node(self):
        bst_node = BSTNode(1)
        bst_node.add(3)
        bst_node.add(2)
        self.assertEqual(bst_node.min_node().value, 1)

    def test_can_delete_value(self):
        bst_node = BSTNode(1)
        bst_node.add(3)
        bst_node.add(5)
        bst_node.remove(3)
        self.assertEqual(bst_node.right.value, 5)

    def test_delete_value_test_cases(self):
        # delete node with zero children
        root = self.setup_tree()
        self.assertEqual(root.right.left.left.value, 3)
        self.assertEqual(root.right.left.right.value, 6)
        self.assertEqual(root.right.left.value, 4)
        root.remove(3)
        self.assertEqual(root.right.left.left, None)

        # delete node with one child
        root = self.setup_tree()
        root.remove(6)
        self.assertEqual(root.right.left.right.value, 5)

        # delete node with two children
        root = self.setup_tree()
        root.remove(4)
        self.assertEqual(root.right.left.value, 5)
        self.assertEqual(root.right.left.right.value, 6)


    def setup_tree(self):
        # Skiena's Algorithm design manual P81
        root = BSTNode(2)
        root.add(1)
        root.add(7)
        root.add(4)
        root.add(8)
        root.add(3)
        root.add(6)
        root.add(5)
        return root
