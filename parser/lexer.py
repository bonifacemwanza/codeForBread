import ply.lex as lex

# Read the EBNF syntax from a file
with open('syntax/main.ebnf', 'r') as f:
    ebnf_syntax = f.read()

# List of token names
tokens = (
    'PROGRAM',
    'IDENTIFIER',
    'EQUALS',
    'STRING',
    'SEMICOLON',
)

# Regular expression rules for tokens
t_PROGRAM = r'program'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='
t_STRING = r'"[^"]*"'
t_SEMICOLON = r';'

# Ignored characters
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
