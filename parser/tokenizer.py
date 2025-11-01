from lark import *

grammar = open(r'lexer\grammar.lark').read()
Praser = Lark(grammar, parser='earley', propagate_positions=True)


if __name__ == "__main__":
    code = open(r'examples\exemplo2.at').read()
    tree = Praser.parse(code)
    print(tree.pretty())

