from typing import List, Tuple

def read_input(file_path: str) -> List[Tuple[int, List[int]]]:
    """
    Reads the input file and parses its contents.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[int, List[int]]]: A list of tuples where each tuple contains an integer and a list of integers.
    """
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    return [parse_string(line) for line in lines]

def parse_string(s: str) -> Tuple[int, List[int]]:
    """
    Parses a string in the format 'int: int int int ...' into a tuple.

    Args:
        s (str): The input string to parse.

    Returns:
        Tuple[int, List[int]]: A tuple where the first element is an integer
        parsed from the part before the colon, and the second element is a list
        of integers parsed from the part after the colon.
    """
    left, right = s.split(':')
    left_int = int(left.strip())
    right_list = [int(num) for num in right.strip().split()]
    return left_int, right_list

def combine_numbers(num1: int, num2: int) -> int:
    """
    Combines two integers by concatenating their string representations and converting back to an integer.

    Args:
        num1 (int): The first integer to combine.
        num2 (int): The second integer to combine.

    Returns:
        int: The combined integer formed by concatenating the string representations of num1 and num2.
    """
    return int(str(num1) + str(num2))

def apply_operator(left: int, right: int, operator: str) -> int:
    """
    Applies the specified operator to the given operands.

    Args:
        left (int): The left operand.
        right (int): The right operand.
        operator (str): The operator to apply. Supported operators are '+', '*', and '||'.

    Returns:
        int: The result of applying the operator to the operands.

    Raises:
        ValueError: If the operator is not one of the supported operators.
    """
    if operator == '+':
        return left + right
    elif operator == '*':
        return left * right
    elif operator == '||':
        return combine_numbers(left, right)
    else:
        raise ValueError(f'Invalid operator: {operator}')

def evaluate_expression(target: int, nums: List[int], operators: List[str] = ['+', '*']) -> bool:
    """
    Evaluates whether a target value can be obtained by applying a sequence of operators
    to a list of numbers.

    Args:
        target (int): The target value to be obtained.
        nums (List[int]): A list of integers to be used in the expression.
        operators (List[str], optional): A list of operators to be used in the expression.
            Defaults to ['+', '*'].

    Returns:
        bool: True if the target value can be obtained, False otherwise.
    """
    if len(nums) == 1:
        return nums[0] == target
    left, right = nums[0], nums[1]
    for operator in operators:
        new_num = apply_operator(left, right, operator)
        if evaluate_expression(target, [new_num] + nums[2:], operators):
            return True
    return False

def sum_valid_expressions(expressions: List[Tuple[int, List[int]]], operators: List[str] = ['+', '*']) -> int:
    """
    Sums the target values of valid expressions.

    An expression is considered valid if the target value can be obtained by 
    applying the given operators to the list of numbers.

    Args:
        expressions (List[Tuple[int, List[int]]]): A list of tuples where each tuple 
            contains a target integer and a list of integers.
        operators (List[str], optional): A list of operators to be used in the 
            expressions. Defaults to ['+', '*'].

    Returns:
        int: The sum of the target values of valid expressions.
    """
    return sum(target for target, nums in expressions if evaluate_expression(target, nums, operators))

if __name__ == "__main__":
    expressions = read_input('input.txt')
    print(sum_valid_expressions(expressions))