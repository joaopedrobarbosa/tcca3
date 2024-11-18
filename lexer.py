from ply.lex import lex


reserved = {
    "numeric": "NUMERIC",
    "string": "STRING",
    "boolean": "BOOLEAN",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "print": "PRINT",
}

tokens = [
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "EQ",
    "NE",
    "LT",
    "GT",
    "LE",
    "GE",
    "NAME",
    "NUMBER",
    "LBRACKET",
    "RBRACKET",
    "ASSIGN",
    "SEMICOLON",
] + list(reserved.values())

t_ignore = " \t"

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ASSIGN = r"="
t_EQ = r"=="
t_NE = r"!="
t_LE = r"<="
t_GE = r">="
t_LT = r"<"
t_GT = r">"
t_LBRACKET = r"\{"
t_RBRACKET = r"\}"
t_SEMICOLON = r";"


def t_NAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "NAME")
    return t


def indent(code):
    indented_code = ""
    for line in code.splitlines():
        indented_code += "    " + line + "\n"
    return indented_code


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_ignore_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex()
