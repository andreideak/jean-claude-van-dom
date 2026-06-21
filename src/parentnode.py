from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict[str,str] | None = None
    ):
        super().__init__(tag,None,children,props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("node doesn't have tag")
        if not self.children:
            raise ValueError("node doesn't have children nodes")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}>{child_html}</{self.tag}>"
