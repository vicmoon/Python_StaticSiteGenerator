from blocknodes import block_to_block_type, BlockType
from markdown_blocks import (
    paragraph_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    unordered_list_to_html_node,
    ordered_list_to_html_node,
)
from markdown_to_blocks import markdown_to_blocks
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))

        elif block_type == BlockType.HEADING:
            children.append(heading_to_html_node(block))

        elif block_type == BlockType.CODE:
            children.append(code_to_html_node(block))

        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))

        elif block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html_node(block))

        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html_node(block))

    return ParentNode("div", children)
