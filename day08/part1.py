from typing import List, Tuple

def read_input(file_path: str) -> List[List[str]]:
    """
    Reads the input file and returns its contents as a list of lists of strings.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[List[str]]: A list where each element is a list of characters from a line in the file.
    """
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def find_character(grid: List[List[str]], char: str) -> List[Tuple[int, int]]:
    """
    Finds all occurrences of a specified character in a 2D grid.

    Args:
        grid (List[List[str]]): A 2D list representing the grid of characters.
        char (str): The character to search for in the grid.

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple contains the 
        row and column indices of an occurrence of the specified character.
    """
    return [(i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == char]

def get_pairs(positions: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Generate all unique pairs of positions from the given list.

    Args:
        positions (List[Tuple[int, int]]): A list of tuples where each tuple represents a position.

    Returns:
        List[Tuple[Tuple[int, int], Tuple[int, int]]]: A list of tuples, where each tuple contains two unique positions from the input list.
    """
    return [(positions[i], positions[j]) for i in range(len(positions)) for j in range(len(positions)) if i != j]

def get_direction(pair: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[int, int]:
    """
    Calculate the direction vector between two points.

    Args:
        pair (Tuple[Tuple[int, int], Tuple[int, int]]): A tuple containing two points,
            where each point is represented as a tuple of two integers (x, y).

    Returns:
        Tuple[int, int]: A tuple representing the direction vector from the first point
            to the second point, calculated as (x2 - x1, y2 - y1).
    """
    (x1, y1), (x2, y2) = pair
    return (x2 - x1, y2 - y1)

def apply_direction(pair: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[int, int]:
    """
    Applies a directional movement to the second coordinate in the given pair.

    Args:
        pair (Tuple[Tuple[int, int], Tuple[int, int]]): A tuple containing two coordinate tuples. 
            The first coordinate tuple is ignored, and the second coordinate tuple is used as the 
            starting point for the directional movement.

    Returns:
        Tuple[int, int]: A new coordinate tuple representing the result of applying the directional 
            movement to the second coordinate in the input pair.
    """
    _, (x2, y2) = pair
    dx, dy = get_direction(pair)
    return (x2 + dx, y2 + dy)

def apply_directions(grid: List[List[str]], char: str) -> List[List[str]]:
    """
    Applies directions to a grid based on the positions of a specified character.

    Args:
        grid (List[List[str]]): A 2D list representing the grid.
        char (str): The character to find in the grid.

    Returns:
        List[List[str]]: A new grid with directions applied, where certain positions are marked with '#'.
    """
    positions = find_character(grid, char)
    pairs = get_pairs(positions)
    new_grid = [row[:] for row in grid]
    for pair in pairs:
        x, y = apply_direction(pair)
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            new_grid[x][y] = '#'
    return new_grid

def apply_all_directions(grid: List[List[str]], apply_func=apply_directions) -> List[List[List[str]]]:
    """
    Applies a given function to a grid for each character in the alphanumeric set.

    Args:
        grid (List[List[str]]): A 2D list representing the grid to which the function will be applied.
        apply_func (Callable[[List[List[str]], str], List[List[str]]], optional): 
            The function to apply to the grid for each character. Defaults to apply_directions.

    Returns:
        List[List[List[str]]]: A list of 2D lists, each representing the grid after applying the function 
        to each character in the alphanumeric set.
    """
    return [apply_func(grid, char) for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

def count_unique_locations(grids: List[List[List[str]]], include_chars: bool = False) -> int:
    """
    Counts the number of unique locations in a 3D grid where '#' is present.

    Args:
        grids (List[List[List[str]]]): A 3D list representing multiple 2D grids.
        include_chars (bool, optional): If True, includes alphanumeric characters in the count. Defaults to False.

    Returns:
        int: The number of unique locations where the character '#' or alphanumeric characters (if include_chars is True) are present.
    """
    unique_locations = {(i, j) for grid in grids for i, row in enumerate(grid) for j, c in enumerate(row) if c == '#' or (include_chars and c.isalnum())}
    return len(unique_locations)

if __name__ == "__main__":
    grid = read_input('input.txt')
    count = count_unique_locations(apply_all_directions(grid))
    print(count)
