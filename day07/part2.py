from typing import List, Tuple
from part1 import read_input, sum_valid_expressions

if __name__ == "__main__":
    expressions = read_input('input.txt')
    print( sum_valid_expressions(expressions, ['+', '*', '||']))
