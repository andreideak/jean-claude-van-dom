from textnode import TextType
from textnode import TextNode


def main():
    test1 = TextNode("Das ist eine ankor!", TextType.LINK, "https://andreideak.com")
    print(repr(test1)) 

if __name__ == "__main__":
	main()
