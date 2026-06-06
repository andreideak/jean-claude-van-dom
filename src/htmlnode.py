
class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list[HTMLNode]=None, props:dict[str,str]=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        if self.props is None:
            return ""
        return f" href=\"{self.props["href"]}\" target=\"{self.props["target"]}\""

    def __repr__(self):
        return f""""
        DEBUG | HTMLNode.tag: {self.tag}
        DEBUG | HTMLNode.value: {self.value}
        DEBUG | HTMLNode.children: {self.children}
        DEBUG | HTMLNode.props: {self.props}
        """



