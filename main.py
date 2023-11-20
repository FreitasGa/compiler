from io import open
from sys import argv

from antlr4 import *
from lib.OneLexer import OneLexer
from lib.OneParser import OneParser


def main():
    if len(argv) != 2:
        print(f"Usage {argv[0]} <filename>.one")
        exit(1)

    path = argv[1]

    if not path.endswith(".one"):
        print("File must have .one extension")
        exit(1)

    file = open(path, mode="rt")
    input_stream = InputStream(file.read())
    lexer = OneLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OneParser(stream)
    parse_tree = parser.program()

    result = parse_tree.toStringTree(recog=parser)

    print(result)


if __name__ == '__main__':
    main()
