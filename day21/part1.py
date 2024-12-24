import functools
from typing import List, Tuple, Optional

# Define the number pad and the direction pad
number_pad = [
    "789", 
    "456", 
    "123", 
    " 0A"
]

direction_pad = [
    " ^A", 
    "<v>"
]

def parse_input(file_path: str) -> List[Tuple[str, int]]:
    """
    Parses the input file and returns a list of tuples.

    Each tuple contains a string (the stripped line) and an integer (the first three characters of the line).

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a string and an integer.
    """
    with open(file_path) as file:
        return [(line.strip(), int(line[:3])) for line in file]

def find_position(pad: List[str], char: str) -> Optional[Tuple[int, int]]:
    """
    Find the position of a character in a 2D list (pad).

    Args:
        pad (List[str]): A 2D list representing the pad where each element is a string.
        char (str): The character to find in the pad.

    Returns:
        Optional[Tuple[int, int]]: A tuple containing the x and y coordinates of the character if found, 
        otherwise None.
    """
    for y, row in enumerate(pad):
        for x, cell in enumerate(row):
            if cell == char:
                return x, y
    return None

def generate_path(pad: List[str], from_char: str, to_char: str) -> str:
    """
    Generate the shortest path from `from_char` to `to_char` in the given pad.

    The path is represented as a string of direction changes:
    - '<' for left
    - '>' for right
    - '^' for up
    - 'v' for down
    - 'A' for arrival at the target position

    Args:
        pad (List[str]): A 2D list representing the pad where each element is a character.
        from_char (str): The character representing the starting position.
        to_char (str): The character representing the target position.

    Returns:
        str: The shortest path from `from_char` to `to_char` based on the number of direction changes.
    """
    from_x, from_y = find_position(pad, from_char)
    to_x, to_y = find_position(pad, to_char)

    def move(x: int, y: int, path: str):
        # If the current position is the target position, yield the path with 'A' appended
        if (x, y) == (to_x, to_y):
            yield path + 'A'
        # Move left if possible and the target is to the left
        if to_x < x and pad[y][x - 1] != ' ':
            yield from move(x - 1, y, path + '<')
        # Move up if possible and the target is above
        if to_y < y and pad[y - 1][x] != ' ':
            yield from move(x, y - 1, path + '^')
        # Move down if possible and the target is below
        if to_y > y and pad[y + 1][x] != ' ':
            yield from move(x, y + 1, path + 'v')
        # Move right if possible and the target is to the right
        if to_x > x and pad[y][x + 1] != ' ':
            yield from move(x + 1, y, path + '>')

    # Return the shortest path based on the number of direction changes
    return min(move(from_x, from_y, ""), key=lambda p: sum(a != b for a, b in zip(p, p[1:])))

@functools.lru_cache(None)
def solve(sequence: str, level: int, max_level: int = 2) -> int:
    """
    Solve the problem recursively.

    Args:
        sequence (str): The input sequence to process.
        level (int): The current recursion level.
        max_level (int, optional): The maximum recursion depth. Defaults to 2.

    Returns:
        int: The result of the recursive computation.
    """
    if level > max_level:
        return len(sequence)
    pad = direction_pad if level else number_pad
    return sum(solve(generate_path(pad, from_char, to_char), level + 1, max_level) for from_char, to_char in zip('A' + sequence, sequence))

if __name__ == "__main__":
    input_data = parse_input('input.txt')
    result = sum(solve(sequence, 0) * multiplier for sequence, multiplier in input_data)
    print(result)