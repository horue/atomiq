from lark import Transformer
from interpreter.stdlib import *


class Utils():
    def resulveValue(value):
        from lark.lexer import Token
        if isinstance(value, Token):
            if value.type == "INT":
                return int(value.value)
            elif value.type == "FLOAT":
                return float(value.value)
            elif value.type == "ESCAPED_STRING":
                return value.value.strip('"').strip("'")
            else:
                return value.value
        return value


class AtomiqInterpreter(Transformer):
    def __init__(self):
        self.scope={}
        self.codeVars={}
        self.native_classes=STD

    def declaration_statement(self, items):
        name = items[1].value
        value = items[3] 
        self.scope[name] = value
        self.codeVars[name] = value
        return None
    
    def args(self, items):
        return items

    def expression(self, items):
            if len(items) > 1:
                pass 
            return items[0]

    def function_call(self, items):
            class_name = items[0].value
            method_name = items[1].value
            args = items[3]

            if args[0] in self.scope:
                resolved = Utils.resulveValue(self.scope[args[0]])
            else:
                resolved = Utils.resulveValue(args[0])


            metodo = self.native_classes[class_name][method_name] 

            return metodo(resolved)

    def value(self, items):
            item = items[0]
            
            if hasattr(item, 'type') and item.type == 'ESCAPED_STRING':
                return item.value.strip('"').strip("'")
            
            return item