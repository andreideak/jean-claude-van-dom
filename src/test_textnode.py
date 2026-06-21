import unittest
from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_link_url_empty(self):
        node = TextNode("BootDev website", TextType.LINK)
        self.assertEqual(node.url,'')

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value,"Bold text")
    
    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("Code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code node")

    def test_link(self):
        node = TextNode("link text",TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link text")
        self.assertEqual(html_node.props,{"href": "https://google.com"})
    
    def test_image(self):
        node = TextNode("Python logo", TextType.IMAGE, "https://google.com/python_logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value,"")
        self.assertEqual(html_node.props,{
            "src": "https://google.com/python_logo.png",
            "alt": "Python logo"
        })
if __name__ == "__main__":
    unittest.main()
