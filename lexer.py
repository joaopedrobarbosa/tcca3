from ply.lex import lex


tokens = (
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
    "LBRACE",
    "RBRACE",
    "ASSIGN",
    "SEMICOLON",
)

reserved = {
    "numeric": "NUMERIC",
    "string": "STRING",
    "boolean": "BOOLEAN",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "print": "PRINT",
}

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
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_SEMICOLON = r";"
t_NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"


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
