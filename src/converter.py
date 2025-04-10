from htmlnode import LeafNode
from textnode import TextType



def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.Normal:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.Bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.Italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.Code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.Link:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.Image:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
