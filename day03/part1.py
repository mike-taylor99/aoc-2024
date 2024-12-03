import re
from typing import List, Tuple

def read_input(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path) as f:
        return f.read()

def find_mul_instances(input_string: str) -> List[Tuple[str, str]]:
    """
    Find all instances of the 'mul' function calls in the input string.

    This function searches for patterns in the form of 'mul(x,y)' where x and y are digits,
    and returns a list of tuples containing the matched digits as strings.

    Args:
        input_string (str): The string to search for 'mul' function calls.

    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing two strings representing the digits found in 'mul' function calls.
    """
    pattern = r'mul\((\d+),(\d+)\)'
    return re.findall(pattern, input_string)

def sum_products(matches: List[Tuple[str, str]]) -> int:
    """
    Calculate the sum of the products of pairs of strings converted to integers.

    Args:
        matches (List[Tuple[str, str]]): A list of tuples, where each tuple contains two strings representing integers.

    Returns:
        int: The sum of the products of the integer pairs.
    """
    return sum(int(x) * int(y) for x, y in matches)

if __name__ == "__main__":
    input_string = read_input('input.txt')
    mul_instances = find_mul_instances(input_string)
    total_sum = sum_products(mul_instances)
    print(total_sum)
