import re
from part1 import read_input, sum_products

def find_mul_instances(input_string):
    """
    Parses the input string to find instances of 'mul' instructions and returns them as a list of tuples.
    The function also respects 'do()' and "don't()" instructions to enable or disable 'mul' instructions.
    Args:
        input_string (str): The input string containing 'mul', 'do()', and "don't()" instructions.
    Returns:
        list of tuples: A list of tuples where each tuple contains two strings representing the arguments of 'mul' instructions.
                        The 'mul' instructions are included only if they are enabled by 'do()' and "don't()" instructions.
    """
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    mul_matches = []
    mul_enabled = True  # Initially, mul instructions are enabled
    
    # Combine all instructions with their positions
    instructions = []
    for match in mul_pattern.finditer(input_string):
        instructions.append((match.start(), 'mul', match.groups()))
    for match in do_pattern.finditer(input_string):
        instructions.append((match.start(), 'do', None))
    for match in dont_pattern.finditer(input_string):
        instructions.append((match.start(), "don't", None))
    
    # Sort instructions by their positions
    instructions.sort()
    
    for _, instruction_type, groups in instructions:
        if instruction_type == 'mul' and mul_enabled:
            mul_matches.append(groups)
        elif instruction_type == 'do':
            mul_enabled = True
        elif instruction_type == "don't":
            mul_enabled = False
    
    return mul_matches

if __name__ == "__main__":
    input_data = read_input('input.txt')
    mul_instances = find_mul_instances(input_data)
    print(sum_products(mul_instances))
