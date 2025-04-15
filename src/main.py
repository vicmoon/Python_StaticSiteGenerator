from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
from file_utils import copy_directory_recursive
from textnode_utils import text_to_children



def main():
    node = TextNode("**Bold text**", TextType.Bold)
    print(node)

    copy_directory_recursive("static", "public")
  



main()