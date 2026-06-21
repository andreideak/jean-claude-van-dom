import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_create(self):
        node = HTMLNode()
        self.assertEqual(type(node),HTMLNode)

    def test_all_defaults(self):
        node = HTMLNode()
        self.assertEqual(node.tag,None)
        self.assertEqual(node.value,None)
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)


    def test_props_to_html(self):
        node = HTMLNode(tag="a",value="Boot.Dev",props={"href": "https://boot.dev", "target": "_blank"})
        if node.props:
            expected = f" href=\"{node.props["href"]}\" target=\"{node.props["target"]}\""
            received = node.props_to_html()
            self.assertEqual(expected,received)
        else:
            raise ValueError("there are no props")


if __name__ == "__main__":
    unittest.main()
