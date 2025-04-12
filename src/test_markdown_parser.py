import unittest
from markdown_parser import extract_markdown_images, extract_markdown_links



def test_extract_multiple_images(self):
    text = "![alt1](url1) and ![alt2](url2)"
    expected = [("alt1", "url1"), ("alt2", "url2")]
    self.assertListEqual(extract_markdown_images(text), expected)


def test_links_not_confused_with_images(self):
    text = "![alt](url) and [link](https://example.com)"
    expected_links = [("link", "https://example.com")]
    self.assertListEqual(extract_markdown_links(text), expected_links)
