import re
from typing import Tuple, List

def parse_input(file_path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    """
    Parses the input file to extract button and prize coordinates.

    The input file should contain lines formatted as:
    "Button A: X+<int>, Y+<int>  Button B: X+<int>, Y+<int>  Prize: X=<int>, Y=<int>"

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]: A list of tuples, each containing:
            - A tuple representing the coordinates of Button A (X, Y).
            - A tuple representing the coordinates of Button B (X, Y).
            - A tuple representing the coordinates of the Prize (X, Y) with 10000000000000 added to each coordinate.
    """
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)")
    results = []

    with open(file_path, 'r') as file:
        content = file.read()
        matches = pattern.findall(content)
        for match in matches:
            button_a = (int(match[0]), int(match[1]))
            button_b = (int(match[2]), int(match[3]))
            prize = (int(match[4]) + 10000000000000, int(match[5]) + 10000000000000)
            results.append((button_a, button_b, prize))

    return results

def solve(scenario: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]) -> int:
    """
    Solves the given scenario by finding integers a and b such that the linear combination
    of the vectors (ax, ay) and (bx, by) equals the target vector (tx, ty).

    Args:
        scenario (Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]): A tuple containing
            three tuples, each representing a vector in the form (x, y). The first two tuples
            are the vectors (ax, ay) and (bx, by), and the third tuple is the target vector (tx, ty).

    Returns:
        int: The result of the expression 3 * a + b if the linear combination is valid, otherwise 0.
    """
    (ax, ay), (bx, by), (tx, ty) = scenario
    b = (tx * ay - ty * ax) // (ay * bx - by * ax)
    a = (tx * by - ty * bx) // (by * ax - bx * ay)
    if ax * a + bx * b == tx and ay * a + by * b == ty:
        return 3 * a + b
    else:
        return 0

if __name__ == "__main__":
    file_path = 'input.txt'
    parsed_data = parse_input(file_path)
    results = [solve(scenario) for scenario in parsed_data]
    print(sum(results))
