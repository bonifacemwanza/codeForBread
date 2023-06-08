from .ast import ProgramNode

def analyze_semantics(node, analyze_semantics):
    if isinstance(node, ProgramNode):
        analyze_program(node,analyze_semantics)
    # Add more semantic analysis functions for other node types

def analyze_program(node,symbol_table):

    program_name = node.name
    program_string = node.value

    # Perform semantic analysis on the program node
    # Example: Check if program name is already defined
    if program_name in symbol_table:
        print(f"Error: Program name '{program_name}' is already defined")
        return

    # Add program name to symbol table
    symbol_table[program_name] = program_string
