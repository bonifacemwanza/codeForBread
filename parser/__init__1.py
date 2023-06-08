from ply.yacc import ParserReflect
from .lexer import *
from .parser import *
from .ast import *
from .semantics import *
from .codegen import *
from .stdlib import *


# Define a function to run the code
def run_code(input_code):
    # Pass the input code to the lexer
    lexer.input(input_code)

    # Tokenize the input code
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)

    # Parse the input code
    parse_tree = parser.parse(input_code)

    # Print the parse tree
    print(parse_tree)

       # Create an empty symbol table
    symbol_table = {}

    # Perform semantic analysis
    analyze_semantics(parse_tree, symbol_table)


    # Generate code
    generated_code = generate_code(parse_tree)

    # Print the generated code
    print(generated_code)

    # Execute the generated code
    try:
        exec(generated_code, {})
    except Exception as e:
        print(f"Error executing code: {e}")

    # Call standard library functions
    if 'print' in symbol_table:
        print_func = symbol_table['print']
        print_func(["Hello, World!"])
    return

