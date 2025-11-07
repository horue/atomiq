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
            resolvedArgs = []

            class_name = items[0].value
            method_name = items[1].value
            args = items[3]

            for arg in args:
                if arg in self.scope:
                    resolvedArgs.append(Utils.resulveValue(self.scope[arg]))
                else:
                    resolvedArgs.append(Utils.resulveValue(arg))


            metodo = self.native_classes[class_name][method_name] 

            return metodo(*resolvedArgs)

    def value(self, items):
            item = items[0]
            
            if hasattr(item, 'type') and item.type == 'ESCAPED_STRING':
                return item.value.strip('"').strip("'")
            
            return item