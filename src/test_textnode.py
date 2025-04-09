import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node1 = TextNode("Hello", TextType.Bold)
        node2 = TextNode("Hi", TextType.Bold)
        self.assertNotEqual(node1, node2)

    def test_different_type(self):
        node1 = TextNode("Hello", TextType.Bold)
        node2 = TextNode("Hello", TextType.Italic)
        self.assertNotEqual(node1, node2)

    def test_url_present_vs_none(self):
        node1 = TextNode("Click here", TextType.Link, "https://example.com")
        node2 = TextNode("Click here", TextType.Link)
        self.assertNotEqual(node1, node2)




if __name__ == "__main__":
    unittest.main()