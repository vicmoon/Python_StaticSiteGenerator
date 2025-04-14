import re
import unittest
from textnode import TextType, TextNode
from textnode_utils import split_nodes_link, split_nodes_image, text_to_textnodes



class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_link(self):
        text = "A link [to google](https://google.com) and some text"
        node = TextNode(text, TextType.Normal)
        result = split_nodes_link([node])

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "A link ")
        self.assertEqual(result[0].text_type, TextType.Normal)

        self.assertEqual(result[1].text, "to google")
        self.assertEqual(result[1].text_type, TextType.Link)
        self.assertEqual(result[1].url, "https://google.com")

        self.assertEqual(result[2].text, " and some text")
        self.assertEqual(result[2].text_type, TextType.Normal)

    def test_split_nodes_image(self):
        text = "An image ![alt](https://img.com/pic.png) at the start"
        node = TextNode(text, TextType.Normal)
        result = split_nodes_image([node])

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "An image ")
        self.assertEqual(result[0].text_type, TextType.Normal)

        self.assertEqual(result[1].text, "alt")
        self.assertEqual(result[1].text_type, TextType.Image)
        self.assertEqual(result[1].url, "https://img.com/pic.png")

        self.assertEqual(result[2].text, " at the start")
        self.assertEqual(result[2].text_type, TextType.Normal)

    def test_nodes_are_unchanged_if_not_text_type(self):
        node = TextNode("![alt](img.png)", TextType.Image, "img.png")
        result_links = split_nodes_link([node])
        result_images = split_nodes_image([node])

        self.assertEqual(result_links, [node])
        self.assertEqual(result_images, [node])


    def test_text_to_textnodes_combined(self):
      
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.Normal),
            TextNode("text", TextType.Bold),
            TextNode(" with an ", TextType.Normal),
            TextNode("italic", TextType.Italic),
            TextNode(" word and a ", TextType.Normal),
            TextNode("code block", TextType.Code),
            TextNode(" and an ", TextType.Normal),
            TextNode("obi wan image", TextType.Image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.Normal),
            TextNode("link", TextType.Link, "https://boot.dev"),
        ]

        self.assertEqual(nodes, expected)

 


