class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props is props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
                return
        pairs = []
        for key, value in self.props.items():
            pairs.append(f' {key}="{value}"')
            
            
        return "".join.(pairs)
            

        

    def __repr__(self):
