from lexer import tokens
from ply.yacc import yacc


def p_assignment(p):
    """
    assignment : NAME ASSIGN expression
    """
    # This creates an assignment node in the AST
    # p[0] = ("assign", p[1], p[3])
    p[0] = f"{p[1]} = {p[3]}"


# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression(p):
    """
    expression : term PLUS term
               | term MINUS term
    """
    # p is a sequence that represents rule contents.
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    #
    # p[0] = ("binop", p[2], p[1], p[3])
    p[0] = f"{p[1]} {p[2]} {p[3]}"


def p_expression_term(p):
    """
    expression : term
    """
    p[0] = p[1]


def p_term(p):
    """
    term : factor TIMES factor
         | factor DIVIDE factor
    """
    # p[0] = ("binop", p[2], p[1], p[3])
    p[0] = f"{p[1]} {p[2]} {p[3]}"


def p_term_factor(p):
    """
    term : factor
    """
    p[0] = p[1]


def p_factor_number(p):
    """
    factor : NUMBER
    """
    p[0] = p[1]


def p_factor_name(p):
    """
    factor : NAME
    """
    p[0] = p[1]


def p_factor_unary(p):
    """
    factor : PLUS factor
           | MINUS factor
    """
    # p[0] = ("unary", p[1], p[2])
    p[0] = f"{p[1]}{p[2]}"


def p_factor_grouped(p):
    """
    factor : LPAREN expression RPAREN
    """
    # p[0] = ("grouped", p[2])
    p[0] = f"({p[2]})"


def p_statements_multiple(p):
    "statements : statements statement"
    p[0] = p[1] + p[2]


def p_statements_single(p):
    "statements : statement"
    p[0] = p[1]


def p_statement(p):
    """
    statement : assignment
              | if_statement
              | block_statement
              | SEMICOLON
    """
    if p.slice[1].type == "SEMICOLON":
        p[0] = ""
    else:
        p[0] = p[1]


def p_block_statement(p):
    "block_statement : LBRACE statements RBRACE"
    p[0] = p[2]


def p_if_statement(p):
    """
    if_statement : IF LPAREN expression RPAREN block_statement
                 | IF LPAREN expression RPAREN block_statement ELSE block_statement
    """

    print(p)
    # cond_code, _ = p[3]
    # if len(p) == 6:
    #     # No else
    #     p[0] = f"if {cond_code}:\n" + indent(p[5])
    # else:
    #     # With else
    #     p[0] = f"if {cond_code}:\n" + indent(p[5]) + "else:\n" + indent(p[7])
    p[0] = "manowell"


def p_error(p):
    print(f"Syntax error at {p.value!r}")


# Build the parser
parser = yacc()
