from antlr4 import *
from lib.OneLexer import OneLexer
from lib.OneParser import OneParser


def main():

    stream = InputStream("Hi Trekkie")

    lexer = OneLexer(stream)
    parser = OneParser(CommonTokenStream(lexer))

    parse_tree = parser.parse()
    result = parse_tree.toStringTree(recog=parser)

    print(result)


if __name__ == '__main__':
    main()
