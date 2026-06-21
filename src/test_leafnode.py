import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_create(self):
        leaf_node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(leaf_node.tag,"p")
        self.assertEqual(leaf_node.value, "This is a paragraph.")

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_link(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), f'<a href="https://boot.dev" target="_blank">Boot.dev</a>')

if __name__ == "__main__":
    unittest.main()
