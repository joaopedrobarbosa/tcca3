# parser.py
import ply.yacc as yacc
from lexer import tokens

# Symbol table
variables = {}


def p_program(p):
    """program : INICIO statements FIM"""
    execute_statements(p[2])


def p_statements(p):
    """statements : statement
    | statements statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    """statement : var_declaration
    | assignment
    | if_statement
    | while_loop
    | for_loop
    | print_statement"""
    p[0] = p[1]


def p_var_declaration(p):
    """var_declaration : VARIAVEL ID SEMICOLON"""

    def action():
        variables[p[2]] = None

    p[0] = action


def p_assignment(p):
    """assignment : ID ASSIGN expression SEMICOLON"""

    def action():
        variables[p[1]] = p[3]

    p[0] = action


def p_expression(p):
    """expression : expression PLUS term
    | expression MINUS term
    | term"""
    if len(p) == 4:
        if p[2] == "mais_um":
            p[0] = p[1] + p[3]
        elif p[2] == "menos_um":
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]


def p_term(p):
    """term : term TIMES factor
    | term DIVIDE factor
    | factor"""
    if len(p) == 4:
        if p[2] == "xêro":
            p[0] = p[1] * p[3]
        elif p[2] == "partido":
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_factor_number(p):
    """factor : NUMBER"""
    p[0] = p[1]


def p_factor_string(p):
    """factor : STRING"""
    p[0] = p[1]


def p_factor_boolean(p):
    """factor : VERDADEIRO
    | FALSO"""
    p[0] = True if p[1] == "é_sim" else False


def p_factor_id(p):
    """factor : ID"""
    p[0] = variables.get(p[1], 0)


def p_condition(p):
    """condition : expression comparison_operator expression
    | NOT condition
    | LPAREN condition RPAREN"""
    if len(p) == 4:
        if p[2] == "e_océ":
            p[0] = p[1] and p[3]
        elif p[2] == "ou_senão":
            p[0] = p[1] or p[3]
        else:
            operator = p[2]
            if operator == "igualzinho":
                p[0] = p[1] == p[3]
            elif operator == "diferente":
                p[0] = p[1] != p[3]
            elif operator == "menor_que":
                p[0] = p[1] < p[3]
            elif operator == "maior_que":
                p[0] = p[1] > p[3]
            elif operator == "menor_ou_igual":
                p[0] = p[1] <= p[3]
            elif operator == "maior_ou_igual":
                p[0] = p[1] >= p[3]
    elif len(p) == 3:
        p[0] = not p[2]
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_comparison_operator(p):
    """comparison_operator : EQUALS
    | NEQUALS
    | LT
    | GT
    | LE
    | GE"""
    p[0] = p[1]


def p_if_statement(p):
    """if_statement : SE condition bloco optional_else"""

    def action():
        if p[2]:
            execute_statements(p[3])
        else:
            if p[4]:
                execute_statements(p[4])

    p[0] = action


def p_optional_else(p):
    """optional_else : SENAO bloco
    | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None


def p_while_loop(p):
    """while_loop : ENQUANTO condition bloco"""

    def action():
        while p[2]:
            execute_statements(p[3])

    p[0] = action


def p_for_loop(p):
    """for_loop : PARA ID ASSIGN expression ATE expression bloco"""

    def action():
        variables[p[2]] = p[4]
        end = p[6]
        while variables[p[2]] <= end:
            execute_statements(p[7])
            variables[p[2]] += 1

    p[0] = action


def p_bloco(p):
    """bloco : LBRACE statements RBRACE"""
    p[0] = p[2]


def p_print_statement(p):
    """print_statement : IMPRIME expression SEMICOLON"""

    def action():
        print(p[2])

    p[0] = action


def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    if p:
        print(f"Erro de sintaxe perto de '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")


def execute_statements(statements):
    for stmt in statements:
        if callable(stmt):
            stmt()


# Build the parser
parser = yacc.yacc()
