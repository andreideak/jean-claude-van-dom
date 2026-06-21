from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag : str | None,
            value : str, 
            props: dict[str,str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise Exception(ValueError)

        if self.tag is None:
            return self.value
        
        if self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"""
        DEBUG | HTMLNode.tag: {self.tag}
        DEBUG | HTMLNode.value: {self.value}
        DEBUG | HTMLNode.children: {self.children}
        DEBUG | HTMLNode.props: {self.props}
        """