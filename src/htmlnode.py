
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        pairs = []
        for key, value in self.props.items():
            pairs.append(f' {key}="{value}"')
        return "".join(pairs)

            
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)
  
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a value.")
        if not self.children :
            raise ValueError("ParentNode must have children.")


        children_html = ""
        for child in self.children:
            children_html += child.to_html() 
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        
        






 