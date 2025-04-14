from textnode import TextType, TextNode
from text_parser import split_nodes_delimiter 
import re

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.Normal:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(r"(?<!!)\[([^\[\]]+)\]\(([^\(\)]+)\)", text))
        if not matches:
            new_nodes.append(node)
            continue

        current_index = 0
        for match in matches:
            start, end = match.span()
            link_text = match.group(1)
            link_url = match.group(2)

            # Text before the link
            if start > current_index:
                new_nodes.append(TextNode(text[current_index:start], TextType.Normal))

            # The link itself
            new_nodes.append(TextNode(link_text, TextType.Link, link_url))

            current_index = end

        # Remaining text after last link
        if current_index < len(text):
            new_nodes.append(TextNode(text[current_index:], TextType.Normal))

    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.Normal:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(r"!\[([^\[\]]+)\]\(([^\(\)]+)\)", text))
        if not matches:
            new_nodes.append(node)
            continue

        current_index = 0
        for match in matches:
            start, end = match.span()
            alt_text = match.group(1)
            image_url = match.group(2)

            # Text before the image
            if start > current_index:
                new_nodes.append(TextNode(text[current_index:start], TextType.Normal))

            # The image node
            new_nodes.append(TextNode(alt_text, TextType.Image, image_url))

            current_index = end

        # Remaining text after last image
        if current_index < len(text):
            new_nodes.append(TextNode(text[current_index:], TextType.Normal))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.Normal)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.Bold)
    nodes = split_nodes_delimiter(nodes, "_", TextType.Italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.Code)
    return nodes

