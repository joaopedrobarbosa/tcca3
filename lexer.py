# lexer.py
import ply.lex as lex

# List of token names
tokens = [
    "NUMBER",
    "STRING",
    "ID",
    # Remove operator tokens from here if they're added to reserved
    "LPAREN",
    "RPAREN",
    "SEMICOLON",
    "LBRACE",
    "RBRACE",
]

# Reserved words and operators
reserved = {
    # Keywords
    "vumbora": "INICIO",
    "acabou_mermo": "FIM",
    "se_pá": "SE",
    "senão_pode_ser": "SENAO",
    "enquanto_rolar": "ENQUANTO",
    "pru_mode_de": "PARA",
    "até": "ATE",
    "bote_fé": "IMPRIME",
    "é_sim": "VERDADEIRO",
    "nada_vez": "FALSO",
    "coisinha": "VARIAVEL",
    # Operators
    "recebeu": "ASSIGN",
    "mais_um": "PLUS",
    "menos_um": "MINUS",
    "xêro": "TIMES",
    "partido": "DIVIDE",
    "e_océ": "AND",
    "ou_senão": "OR",
    "nada_não": "NOT",
    "igualzinho": "EQUALS",
    "diferente": "NEQUALS",
    "menor_que": "LT",
    "maior_que": "GT",
    "menor_ou_igual": "LE",
    "maior_ou_igual": "GE",
}

tokens = tokens + list(set(reserved.values()))

# Regular expression rules for simple tokens
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMICOLON = r";"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

# Ignore spaces and tabs
t_ignore = " \t"


# Token definitions
def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_STRING(t):
    r"\"(.*?)\" "
    t.value = t.value.strip('"')
    return t


def t_ID(t):
    r"[a-zA-Z_à-úÀ-Ú][a-zA-Z_à-úÀ-Ú0-9]*"
    t.type = reserved.get(t.value, "ID")  # Check for reserved words and operators
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
