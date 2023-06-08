import ply.yacc as yacc
from .lexer import tokens
from .ast import ProgramNode

# Define the parser rules
def p_program(p):
    'program : PROGRAM IDENTIFIER EQUALS STRING SEMICOLON'
    p[0] = ProgramNode(p[2], p[4])

def p_error(p):
    if p:
        print(f"Syntax error near token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
