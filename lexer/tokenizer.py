class Lexer():
    symbol_map = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "TIMES",
        "/": "DIVIDE",
        "(": "LPAREN",
        ")":"RPAREN",
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
    
    def readString(current):
        if Lexer.state == "STRING":
            Lexer.buffer += current
            print("Buffer: " + Lexer.buffer)
    


    def tokenize(font):
        quote = ''
        quoteList = ['"', "'"]
        for char in font:
            if Lexer.state == "STRING":
                if char == quote:
                    Lexer.tokens.append(("STRING", Lexer.buffer))
                    Lexer.resetBuffer()
                    Lexer.resetState()
                    quote = ''
                else:
                    Lexer.readString(char)
            elif char in quoteList:
                Lexer.changeState("STRING")
                quote = char
            elif char == " " and Lexer.state != "DEFAULT":
                Lexer.tokens.append((Lexer.state, Lexer.buffer))
                Lexer.resetBuffer()
                Lexer.resetState()
            elif char in Lexer.symbol_map:
                Lexer.tokens.append((Lexer.symbol_map[char], char))
            elif char.isdigit():
                Lexer.changeState("NUMBER")
                Lexer.readNumber(char)
            elif char in quoteList or Lexer.state == "STRING":
                if char in quoteList:
                    char = quote
                Lexer.changeState("STRING")
                Lexer.readString(char)
    
        return Lexer.tokens
    



if __name__ == "__main__":
    print(Lexer.tokenize('3 + 69 + 9 - 8 * 65 + "aa++--//**aa" + 5 "teste MALUCO" + "olá, mundo"'))