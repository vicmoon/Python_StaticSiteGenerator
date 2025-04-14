from enum import Enum

class TextType(Enum):
    Normal = "normal"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Link = "link"
    Image = "image"

    


class TextNode:
    def __init__(self,text,text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 

    
    def __eq__(self, other):
        """When you want to do node1== node2"""
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
            


    def __repr__(self):
        """ Gives a string representation. Useful in debugging """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


  