from ply import lex, yacc

# Define the lexer tokens (same as before)

# ... lexer code ...

# Define the AST Node classes (same as before)

# Define the symbol table (same as before)

# Define code generation functions (same as before)

# Define error handling functions
def error(message, lineno):
    print(f"Error at line {lineno}: {message}")

def p_error(p):
    if p:
        error(f"Syntax error near token '{p.value}'", p.lineno)
    else:
        error("Syntax error at EOF", lexer.lineno)

# Build the parser (same as before)

# Read the input code (same as before)

# Tokenize and parse the code
lexer.input(data)
result = parser.parse(lexer=lexer)

# Generate code from the AST (same as before)

# Execute the generated code
try:
    exec(generated_code, symbol_table)
except Exception as e:
    error(str(e), 0)  # Provide a generic error message

# Call the standard library functions (same as before)
