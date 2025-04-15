from extract_title import extract_title 
import unittest


def test_extract_title():
    self.assertEqual(extract_title("# My Title"), "My Title")
    with self.assertRaises(Exception):
        extract_title("No title here")
