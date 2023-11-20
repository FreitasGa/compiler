from antlr4 import *
from lib.OneLexer import OneLexer
from lib.OneParser import OneParser


def main():
    input_stream = InputStream("int x = 5")
    lexer = OneLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OneParser(stream)
    parse_tree = parser.program()

    result = parse_tree.toStringTree(recog=parser)

    print(result)


if __name__ == '__main__':
    main()
