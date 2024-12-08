from typing import List, Tuple
from part1 import read_input, find_character, get_pairs, apply_direction, apply_all_directions, count_unique_locations

def apply_directions(grid: List[List[str]], char: str) -> List[List[str]]:
    """
    Applies directions to a grid based on the positions of a specified character.

    Args:
        grid (List[List[str]]): A 2D list representing the grid.
        char (str): The character to find in the grid and apply directions from.

    Returns:
        List[List[str]]: A new grid with directions applied, where certain positions are marked with '#'.

    The function performs the following steps:
    1. Finds all positions of the specified character in the grid.
    2. Generates pairs of these positions.
    3. Creates a copy of the original grid.
    4. For each pair, applies directions to mark positions in the new grid with '#'.
    5. Ensures that the new positions are within the bounds of the grid.
    """
    positions = find_character(grid, char)
    pairs = get_pairs(positions)
    new_grid = [row.copy() for row in grid]
    for pair in pairs:
        while True:
            new_pos = apply_direction(pair)
            x, y = new_pos
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                new_grid[x][y] = '#'
                pair = (pair[1], new_pos)
            else:
                break
    return new_grid

if __name__ == "__main__":
    grid = read_input('input.txt')
    count = count_unique_locations(apply_all_directions(grid, apply_directions), include_chars=True)
    print(count)