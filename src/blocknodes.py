import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(rf"^{i+1}\. ", line.strip()) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
