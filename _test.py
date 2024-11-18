from ply.lex import lex
from ply.yacc import yacc

# Reserved words
reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "print": "PRINT",
}

# List of token names
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
    "ASSIGN",
    "LBRACE",
    "RBRACE",
    "SEMICOLON",
    "NAME",
    "NUMBER",
    "STRING",
] + list(reserved.values())

# Ignored characters
t_ignore = " \t"

# Token matching rules
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_EQ = r"=="
t_NE = r"!="
t_LE = r"<="
t_GE = r">="
t_LT = r"<"
t_GT = r">"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_ASSIGN = r"="
t_SEMICOLON = r";"


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\"([^\\\n]|(\\.))*?\" "
    t.value = t.value[1:-1]
    return t


def t_NAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "NAME")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling
def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex()

# Operator precedence
precedence = (
    ("left", "EQ", "NE"),
    ("left", "LT", "LE", "GT", "GE"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)

# Define the start symbol
start = "program"


def p_program(p):
    "program : statements"
    p[0] = p[1]


def p_statements_multiple(p):
    "statements : statements statement"
    p[0] = p[1] + "\n" + p[2]


def p_statements_single(p):
    "statements : statement"
    p[0] = p[1]


def p_statement(p):
    """
    statement : assignment SEMICOLON
              | if_statement
              | block_statement
              | print_statement SEMICOLON
    """
    p[0] = p[1]


def p_assignment(p):
    "assignment : NAME ASSIGN expression"
    p[0] = f"{p[1]} = {p[3]}"


def p_if_statement(p):
    """
    if_statement : IF LPAREN expression RPAREN block_statement
                 | IF LPAREN expression RPAREN block_statement ELSE block_statement
    """
    condition = p[3]
    if len(p) == 6:
        # No else clause
        p[0] = f"if ({condition}):\n{indent(p[5])}"
    else:
        # With else clause
        p[0] = f"if ({condition}):\n{indent(p[5])}else:\n{indent(p[7])}"


def p_block_statement(p):
    "block_statement : LBRACE statements RBRACE"
    p[0] = p[2]


def p_print_statement(p):
    "print_statement : PRINT LPAREN expression RPAREN"
    p[0] = f"print({p[3]})"


def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression EQ expression
               | expression NE expression
               | expression LT expression
               | expression LE expression
               | expression GT expression
               | expression GE expression
    """
    p[0] = f"({p[1]} {p[2]} {p[3]})"


def p_expression_factor(p):
    "expression : factor"
    p[0] = p[1]


def p_factor_number(p):
    "factor : NUMBER"
    p[0] = str(p[1])


def p_factor_name(p):
    "factor : NAME"
    p[0] = p[1]


def p_factor_string(p):
    "factor : STRING"
    p[0] = f'"{p[1]}"'


def p_factor_grouped(p):
    "factor : LPAREN expression RPAREN"
    p[0] = f"({p[2]})"


def p_factor_unary(p):
    "factor : MINUS factor"
    p[0] = f"(-{p[2]})"


def p_error(p):
    print(f"Syntax error at {p.value!r}")


def indent(code):
    indented_code = ""
    for line in code.splitlines():
        indented_code += "    " + line + "\n"
    return indented_code


parser = yacc()

# Test input
ast = parser.parse(
    """
x = 2 * 3 + 4 * (5 - x);

if (x > 5) {
    print("x is greater than 5");
} else {
    print("x is less than or equal to 5");
}
"""
)
print(ast)