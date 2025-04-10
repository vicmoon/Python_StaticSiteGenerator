import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_renders_nested_html(self):
        child1 = LeafNode("p", "Hello")
        child2 = LeafNode("p", "World")
        parent = ParentNode("div", [child1, child2])
        expected = "<div><p>Hello</p><p>World</p></div>"
        self.assertEqual(parent.to_html(), expected)

    def test_missing_tag_raises_error(self):
        child = LeafNode("p", "Hello")
        with self.assertRaises(ValueError):
            ParentNode(None, [child]).to_html()
    
    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

