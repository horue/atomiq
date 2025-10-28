class Lexer():
    symbol_map = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "TIMES",
        "/": "DIVIDE",
        "(": "LPAREN",
        ")":"RPAREN"
    }
    state_map = {
        "DEFAULT"
        "NUMBER"
        "STRING"
    }

    state = "DEFAULT"

    def changeState(arg):
        Lexer.state = arg

    def resetState():
        Lexer.state = "DEFAULT"


    buffer = ''

    def resetBuffer():
        Lexer.buffer = ''

    tokens = []

    def readNumber(current):
        if Lexer.state == "NUMBER":
            Lexer.buffer += current
        else:
            Lexer.tokens.append(("NUMBER", Lexer.buffer))
            Lexer.resetBuffer()
            Lexer.resetState()
            


    def tokenize(font):
        for char in font:
            if char == " " and Lexer.state == "NUMBER":
                Lexer.tokens.append(("NUMBER", Lexer.buffer))
                Lexer.resetBuffer()
                Lexer.resetState()
            elif char in Lexer.symbol_map:
                Lexer.tokens.append((Lexer.symbol_map[char], char))
            elif char.isdigit():
                Lexer.changeState("NUMBER")
                Lexer.readNumber(char)

    
        return Lexer.tokens
    



if __name__ == "__main__":
    print(Lexer.tokenize("3 + 69 + 9 - 8 * 65"))