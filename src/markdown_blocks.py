from htmlnode import ParentNode 
import re
from htmlnode import LeafNode
from textnode_utils import text_to_children


def paragraph_to_html_node(block):
    return ParentNode("p", text_to_children(block))

def heading_to_html_node(block):
    level = block.count("#", 0, block.find(" "))  # count # before first space
    text = block.lstrip("#").strip()
    return ParentNode(f"h{level}", text_to_children(text))

def code_to_html_node(block):
    code_content = "\n".join(block.split("\n")[1:-1]) + "\n"
    return ParentNode("pre", [LeafNode("code", code_content)])

def quote_to_html_node(block):
    text = "\n".join(line.lstrip("> ").rstrip() for line in block.split("\n"))
    return ParentNode("blockquote", text_to_children(text))

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    items = [ParentNode("li", text_to_children(line[2:])) for line in lines]
    return ParentNode("ul", items)
def ordered_list_to_html_node(block):
    lines = block.split("\n")
    items = [ParentNode("li", text_to_children(re.sub(r"^\d+\. ", "", line))) for line in lines]
    return ParentNode("ol", items)

