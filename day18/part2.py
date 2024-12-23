from typing import List, Tuple
from part1 import parse_input, initialize_grid, find_shortest_path

def find_blocking_byte(byte_positions: List[Tuple[int, int]], grid_size: int) -> Tuple[int, int]:
    """
    Identifies the first byte position that blocks the shortest path in a grid.
    Args:
        byte_positions (List[Tuple[int, int]]): A list of tuples representing the positions of bytes in the grid.
        grid_size (int): The size of the grid (assuming a square grid).
    Returns:
        Tuple[int, int]: The coordinates of the first blocking byte. Returns (-1, -1) if no blocking byte is found.
    """
    grid = initialize_grid(grid_size)
    
    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = '#'
        if find_shortest_path(grid) == -1:
            return (x, y)
    
    return (-1, -1)  # If no blocking byte is found

if __name__ == "__main__":
    file_path = 'input.txt'
    byte_positions = parse_input(file_path)
    grid_size = 71  # For the actual problem, use 71; for the example, use 7
    blocking_byte = find_blocking_byte(byte_positions, grid_size)
    print(f"{blocking_byte[0]},{blocking_byte[1]}")