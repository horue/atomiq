class Lexer():
    state = "DEFAULT"
    tokens = []

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

    def changeState(arg):
        Lexer.state = arg

    def resetState():
        Lexer.state = "DEFAULT"

    def readNumber(current):
        number = current
        if Lexer.state == "NUMBER":
            number += current
        else:
            Lexer.tokens.append(("NUMBER", number))
            Lexer.resetState()


        

    
    def tokenize(font):
        i = 0
        context = font.split()
        for i in range(len(context)):
            char = context[i]
            if char == " ":
                Lexer.changeState("DEFAULT")
            elif char in Lexer.symbol_map:
                Lexer.tokens.append((Lexer.symbol_map[char], char))
            elif char.isdigit():
                Lexer.changeState("NUMBER")
                Lexer.readNumber(char)

    
        return Lexer.tokens
    



if __name__ == "__main__":
    print(Lexer.tokenize("3 + 6 + 9"))