from lark import Transformer
from interpreter.stdlib import *


class AtomiqInterpreter(Transformer):
    def __init__(self):
        self.scope={}
        self.native_classes=STD

    def declaration_statement(self, items):
        name = items[1].value
        value = items[3] 
        self.scope[name] = value
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

            metodo = self.native_classes[class_name][method_name] 

            return metodo(*args)

    def value(self, items):
            item = items[0]
            
            if hasattr(item, 'type') and item.type == 'ESCAPED_STRING':
                return item.value.strip('"').strip("'")
            
            return item