from typing import List, Tuple
from part1 import read_input, move_one_step, find_start_pos
from tqdm import tqdm

def add_barriers(grid: List[str], start_pos: Tuple[int, int]) -> List[List[str]]:
    """
    Adds barriers to a grid, except at the starting position and existing barriers.

    Args:
        grid (List[str]): A list of strings representing the grid.
        start_pos (Tuple[int, int]): The starting position (x, y) in the grid.

    Returns:
        List[List[str]]: A new grid with barriers added.
    """
    rows, cols = len(grid), len(grid[0])
    x, y = start_pos
    return [
        [''.join('#' if (i, j) == (r, c) else cell for j, cell in enumerate(row)) for i, row in enumerate(grid)]
        for r in range(rows) for c in range(cols) if (r, c) != (x, y) and grid[r][c] != '#'
    ]

def find_loop(grid: List[str], start_pos: Tuple[int, int], direction: str) -> bool:
    """
    Determines if there is a loop in the grid starting from a given position and direction.
    Args:
        grid (List[str]): The grid represented as a list of strings.
        start_pos (Tuple[int, int]): The starting position in the grid as a tuple (x, y).
        direction (str): The initial direction of movement.
    Returns:
        bool: True if a loop is detected, False otherwise.
    """
    x, y = start_pos
    visited = {(x, y, direction)}
    
    while True:
        x, y, direction = move_one_step(grid, x, y, direction)
        if (x, y, direction) in visited:
            return True
        if x is None or y is None:
            return False
        visited.add((x, y, direction))

def find_loop_count(grid: List[str], start_pos: Tuple[int, int]) -> int:
    """
    Calculates the total number of loops in a grid starting from a given position.

    Args:
        grid (List[str]): A list of strings representing the grid.
        start_pos (Tuple[int, int]): A tuple representing the starting position in the grid.

    Returns:
        int: The total number of loops found in the grid.
    """
    grids = add_barriers(grid, start_pos)
    return sum(find_loop(g, start_pos, '^') for g in tqdm(grids))

if __name__ == "__main__":
    grid = read_input('input.txt')
    x, y = find_start_pos(grid)
    print(find_loop_count(grid, (x, y)))
