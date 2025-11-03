from lark import *

class AtomiqParser():
    grammar = open(r'parser\grammar.lark').read()
    praser = Lark(grammar, parser='earley', propagate_positions=True)

    @staticmethod
    def build(code):
        tree = AtomiqParser.praser.parse(code)
        return tree



if __name__ == "__main__":
    code = open(r'examples\exemplo2.at').read()
    tree = AtomiqParser.build(code)
    transformer = Transformer()
    print(tree)


