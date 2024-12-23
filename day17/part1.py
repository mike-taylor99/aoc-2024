import re
from typing import List, Tuple, Dict

# Define opcodes as constants
ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = range(8)

def parse_input(file_path: str) -> Tuple[Dict[str, int], List[int]]:
    """
    Parses the input file to extract register values and program instructions.
    Args:
        file_path (str): The path to the input file.
    Returns:
        Tuple[Dict[str, int], List[int]]: A tuple containing a dictionary of register names and their values,
                                          and a list of program instructions.
    """
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    
    registers = {}
    program = []
    for line in lines:
        if line.startswith("Register"):
            register, value = line.split(':')
            registers[register.split()[1]] = int(value)
        elif line.startswith("Program"):
            program = [int(x) for x in line.split(':')[1].split(',')]
    
    return registers, program

def execute_program(registers: Dict[str, int], program: List[int]) -> str:
    """
    Executes a given program on a set of registers and returns the output as a comma-separated string.

    Args:
        registers (Dict[str, int]): A dictionary representing the registers with their initial values.
        program (List[int]): A list of integers representing the program instructions.

    Returns:
        str: A comma-separated string of the output values.

    Raises:
        ValueError: If an invalid combo operand or opcode is encountered.

    The program supports the following opcodes:
        - ADV: Advances register 'A' by dividing it by 2 raised to the power of the combo value.
        - BXL: Performs an XOR operation on register 'B' with the operand.
        - BST: Sets register 'B' to the combo value modulo 8.
        - JNZ: Jumps to the operand index if register 'A' is not zero.
        - BXC: Performs an XOR operation between registers 'B' and 'C'.
        - OUT: Appends the combo value modulo 8 to the output.
        - BDV: Sets register 'B' to register 'A' divided by 2 raised to the power of the combo value.
        - CDV: Sets register 'C' to register 'A' divided by 2 raised to the power of the combo value.

    The combo values are:
        - 0: 0
        - 1: 1
        - 2: 2
        - 3: 3
        - 4: Value of register 'A'
        - 5: Value of register 'B'
        - 6: Value of register 'C'
    """
    ip = 0
    output = []

    combo_values = {
        0: 0, 1: 1, 2: 2, 3: 3,
        4: lambda: registers['A'],
        5: lambda: registers['B'],
        6: lambda: registers['C']
    }

    def get_combo_value(operand):
        if operand in combo_values:
            return combo_values[operand]() if callable(combo_values[operand]) else combo_values[operand]
        else:
            raise ValueError("Invalid combo operand")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == ADV:
            registers['A'] //= 2 ** get_combo_value(operand)
        elif opcode == BXL:
            registers['B'] ^= operand
        elif opcode == BST:
            registers['B'] = get_combo_value(operand) % 8
        elif opcode == JNZ:
            if registers['A'] != 0:
                ip = operand
                continue
        elif opcode == BXC:
            registers['B'] ^= registers['C']
        elif opcode == OUT:
            output.append(get_combo_value(operand) % 8)
        elif opcode == BDV:
            registers['B'] = registers['A'] // (2 ** get_combo_value(operand))
        elif opcode == CDV:
            registers['C'] = registers['A'] // (2 ** get_combo_value(operand))
        else:
            raise ValueError("Invalid opcode")

        ip += 2

    return ','.join(map(str, output))

if __name__ == "__main__":
    file_path = 'input.txt'
    registers, program = parse_input(file_path)
    result = execute_program(registers, program)
    print(result)
