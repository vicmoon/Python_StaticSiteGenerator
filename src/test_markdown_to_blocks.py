import unittest
import textwrap
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = textwrap.dedent("""
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
        """).strip()
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocks_heading_paragraph_list(self):
        md = textwrap.dedent("""
            # Heading

            This is a paragraph

            - item 1
            - item 2
        """).strip()
        expected = [
            "# Heading",
            "This is a paragraph",
            "- item 1\n- item 2",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_blocks_with_extra_blank_lines(self):
        md = textwrap.dedent("""
            
            
            Paragraph one
            
            
            Paragraph two
            
            
            
        """).strip()
        expected = [
            "Paragraph one",
            "Paragraph two"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_blocks_with_whitespace_lines(self):
        md = "Paragraph one\n   \n   \nParagraph two"
        expected = ["Paragraph one\n   \n   \nParagraph two"]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_single_line_markdown(self):
        md = "This is just a single line."
        expected = ["This is just a single line."]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty_markdown(self):
        md = ""
        expected = []
        self.assertEqual(markdown_to_blocks(md), expected)
