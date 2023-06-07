def generate_code(node):
    if isinstance(node, ProgramNode):
        return generate_program(node)
    # Add more code generation functions for other node types

def generate_program(node):
    program_name = node.name
    program_string = node.value

    # Generate code to print the program string
    code = f'print("{program_string}")'

    return code
