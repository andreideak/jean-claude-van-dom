
class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list[HTMLNode] | None = None, 
            props: dict[str,str] | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        
        return "".join(
            f' {key}="{value}"'
            for key, value in self.props.items()
        )

    def __repr__(self):
        return f"""
        DEBUG | HTMLNode.tag: {self.tag}
        DEBUG | HTMLNode.value: {self.value}
        DEBUG | HTMLNode.children: {self.children}
        DEBUG | HTMLNode.props: {self.props}
        """



