import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://example.com", "target": "_blank"}
        )
        result = node.props_to_html()
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))


    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")


    def test_props_to_html_single(self):
        node = HTMLNode(tag="img", props={"src": "image.jpg"})
        result = node.props_to_html()
        self.assertEqual(result, ' src="image.jpg"')

    def test_props_to_html_spacing(self):
        node = HTMLNode(tag="a", props={"href": "url", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="url"', result)
        self.assertIn(' target="_blank"', result)

    def test_children_default(self):
        node = HTMLNode(tag="p", value="hello")
        self.assertIsInstance(node.children, list)
        self.assertEqual(len(node.children), 0)


    def test_repr_output(self):
        node = HTMLNode(tag="a", value="link", props={"href": "url"})
        repr_str = repr(node)
        self.assertIn("HTMLNode", repr_str)
        self.assertIn("a", repr_str)
        self.assertIn("link", repr_str)
        self.assertIn("href", repr_str)



        


