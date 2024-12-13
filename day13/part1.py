import re
from typing import List, Tuple
from collections import deque, namedtuple

def parse_input(file_path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    """
    Parses the input file to extract coordinates for Button A, Button B, and the Prize.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]: A list of tuples, where each tuple contains:
            - A tuple representing the coordinates of Button A (X, Y).
            - A tuple representing the coordinates of Button B (X, Y).
            - A tuple representing the coordinates of the Prize (X, Y).

    The input file is expected to have lines in the following format:
        "Button A: X+<int>, Y+<int>  Button B: X+<int>, Y+<int>  Prize: X=<int>, Y=<int>"
    """
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)")
    results = []

    with open(file_path, 'r') as file:
        content = file.read()
        matches = pattern.findall(content)
        for match in matches:
            button_a = (int(match[0]), int(match[1]))
            button_b = (int(match[2]), int(match[3]))
            prize = (int(match[4]), int(match[5]))
            results.append((button_a, button_b, prize))

    return results

State = namedtuple('State', ['x', 'y', 'presses', 'a_presses', 'b_presses'])

def find_min_presses(button_a: Tuple[int, int], button_b: Tuple[int, int], prize: Tuple[int, int]) -> Tuple[int, int, int]:
    """
    Finds the minimum number of presses required to reach the prize coordinates using two buttons.

    Each button press moves the current position by a fixed amount in the x and y directions.
    The function returns the total number of presses, the number of presses of button A, and the number of presses of button B.

    Args:
        button_a (Tuple[int, int]): The movement in (x, y) coordinates for button A.
        button_b (Tuple[int, int]): The movement in (x, y) coordinates for button B.
        prize (Tuple[int, int]): The target (x, y) coordinates to reach.

    Returns:
        Tuple[int, int, int]: A tuple containing the total number of presses, the number of presses of button A, 
                              and the number of presses of button B. Returns (-1, -1, -1) if no solution exists.
    """
    queue = deque([State(0, 0, 0, 0, 0)])
    visited = set([(0, 0)])

    while queue:
        state = queue.popleft()
        if (state.x, state.y) == prize:
            return (state.presses, state.a_presses, state.b_presses)

        for dx, dy, is_a in [(button_a[0], button_a[1], True), (button_b[0], button_b[1], False)]:
            nx, ny = state.x + dx, state.y + dy
            if (nx, ny) not in visited and (nx <= prize[0] and ny <= prize[1]):
                visited.add((nx, ny))
                queue.append(State(nx, ny, state.presses + 1, state.a_presses + (1 if is_a else 0), state.b_presses + (1 if not is_a else 0)))

    return (-1, -1, -1)  # return -1 if no solution exists

def calculate_cost(a_presses: int, b_presses: int) -> int:
    """
    Calculate the total cost based on the number of 'a' and 'b' presses.

    Args:
        a_presses (int): The number of times 'a' is pressed.
        b_presses (int): The number of times 'b' is pressed.

    Returns:
        int: The total cost calculated as (a_presses * 3) + b_presses.
    """
    return (a_presses * 3) + b_presses

def find_min_cost(button_a: Tuple[int, int], button_b: Tuple[int, int], prize: Tuple[int, int]) -> int:
    """
    Calculate the minimum cost to reach the prize using the given buttons.

    Args:
        button_a (Tuple[int, int]): A tuple representing the cost and value of button A.
        button_b (Tuple[int, int]): A tuple representing the cost and value of button B.
        prize (Tuple[int, int]): A tuple representing the target value and its associated cost.

    Returns:
        int: The minimum cost to reach the prize. Returns 0 if it's not possible to reach the prize.
    """
    min_presses, a_presses, b_presses = find_min_presses(button_a, button_b, prize)
    if min_presses == -1:
        return 0
    return calculate_cost(a_presses, b_presses)

def find_total_cost(data: List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]) -> int:
    """
    Calculate the total cost from a list of data tuples.

    Each tuple in the data list contains three sub-tuples, each with two integers.
    The function uses the find_min_cost function to determine the minimum cost for each tuple
    and returns the sum of these minimum costs.

    Args:
        data (List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]): 
            A list of tuples, where each tuple contains three sub-tuples of two integers.

    Returns:
        int: The total cost calculated by summing the minimum costs of each tuple in the data list.
    """
    return sum(find_min_cost(*d) for d in data)

if __name__ == "__main__":
    file_path = 'input.txt'
    parsed_data = parse_input(file_path)
    print(find_total_cost(parsed_data))