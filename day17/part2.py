from part1 import parse_input

def run(program, regs):
    """
    Executes a given program with specified registers.

    Args:
        program (list of int): A list of integers representing the program's opcodes and operands.
        regs (list of int): A list of initial values for the registers.

    Yields:
        int: The result of the operation specified by opcode 5, modulo 8.

    The program supports the following opcodes:
        0: Divide the value in reg_a by 2 raised to the power of the value in the register specified by operand.
        1: XOR the value in reg_b with the operand.
        2: Set reg_b to the value in the register specified by operand, modulo 8.
        3: If the value in reg_a is non-zero, set the instruction pointer to operand - 2.
        4: XOR the value in reg_b with the value in reg_c.
        5: Yield the value in the register specified by operand, modulo 8.
        6: Set reg_b to the value in reg_a divided by 2 raised to the power of the value in the register specified by operand.
        7: Set reg_c to the value in reg_a divided by 2 raised to the power of the value in the register specified by operand.
    """
    reg_a, reg_b, reg_c = range(4, 7)
    ip = 0
    combo = [0, 1, 2, 3, *regs]
    while ip < len(program):
        opcode, operand = program[ip:ip + 2]
        if opcode == 0:
            combo[reg_a] //= 2 ** combo[operand]
        elif opcode == 1:
            combo[reg_b] ^= operand
        elif opcode == 2:
            combo[reg_b] = combo[operand] % 8
        elif opcode == 3:
            if combo[reg_a]:
                ip = operand - 2
        elif opcode == 4:
            combo[reg_b] ^= combo[reg_c]
        elif opcode == 5:
            yield combo[operand] % 8
        elif opcode == 6:
            combo[reg_b] = combo[reg_a] // (2 ** combo[operand])
        elif opcode == 7:
            combo[reg_c] = combo[reg_a] // (2 ** combo[operand])
        ip += 2

def expect(program, target_output, prev_a=0):
    """
    Tries to find an integer 'a' such that when the 'program' is run with inputs derived from 'a',
    it produces the 'target_output' sequence.

    Args:
        program (iterable): The program to be run, which yields outputs based on inputs.
        target_output (list): The desired sequence of outputs that the program should produce.
        prev_a (int, optional): The previous value of 'a' used in the recursive calls. Defaults to 0.

    Returns:
        int or None: The integer 'a' that produces the 'target_output' when the program is run,
                     or None if no such 'a' can be found.
    """
    def helper(program, target_output, prev_a):
        if not target_output:
            return prev_a
        for a in range(1 << 10):
            if a >> 3 == prev_a & 127 and next(run(program, (a, 0, 0))) == target_output[-1]:
                result = helper(program, target_output[:-1], (prev_a << 3) | (a % 8))
                if result is not None:
                    return result
        return None

    return helper(program, target_output, prev_a)

if __name__ == "__main__":
    file_path = 'input.txt'
    registers, program = parse_input(file_path)
    
    # Example target output
    target_output = program.copy()
    
    initial_value = expect(program, target_output)
    if initial_value is not None:
        print(f"The initial value for register A that produces the target output is: {initial_value}")
    else:
        print("No initial value found that produces the target output within the given attempts.")