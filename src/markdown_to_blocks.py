
def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in raw_blocks]
    return [block for block in stripped_blocks if block]