stringMatch = r""""[^"]*"|'[^']*'"""

TOKENS = [
    ## Basic Types ##
    
    ("NUMBER", r"\d+"),
    ("STRING", stringMatch),
    ("IDENT", r"[a-zA-Z_][a-zA-Z0-9_]*"),

    ## Basic Signals ##

    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("DIVIDE", r"/"),

    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),

    ## Identifiers ##

    ("METHOD", r"\@method"),
    ("CLASS", r"\@[[:upper:]][^.\s]*"),
    ("CLASS_CALLED", r"\.[[:lower:]]*")
]

if __name__ == '__main__':
    pass