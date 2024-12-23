from collections import deque
from typing import List, Tuple

def parse_input(file_path: str) -> List[Tuple[int, int]]:
    """
    Parses the input file and returns a list of tuples containing integer pairs.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[int, int]]: A list of tuples, where each tuple contains two integers
        parsed from a line in the input file. Each line in the file should contain two
        integers separated by a comma.
    """
    with open(file_path, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def initialize_grid(size: int) -> List[List[str]]:
    """
    Initializes a square grid of the given size with all cells set to '.'.

    Args:
        size (int): The size of the grid (number of rows and columns).

    Returns:
        List[List[str]]: A 2D list representing the initialized grid.
    """
    return [['.' for _ in range(size)] for _ in range(size)]

def simulate_falling_bytes(grid: List[List[str]], byte_positions: List[Tuple[int, int]], num_bytes: int):
    """
    Simulates the falling of bytes in a grid.

    Args:
        grid (List[List[str]]): A 2D list representing the grid where bytes will fall.
        byte_positions (List[Tuple[int, int]]): A list of tuples representing the (x, y) positions of bytes.
        num_bytes (int): The number of bytes to simulate falling.

    Returns:
        None
    """
    for x, y in byte_positions[:num_bytes]:
        grid[y][x] = '#'

def find_shortest_path(grid: List[List[str]]) -> int:
    """
    Finds the shortest path in a grid from the top-left corner to the bottom-right corner.
    The grid is represented as a list of lists of strings, where '.' represents an open cell
    and any other character represents an obstacle.
    Args:
        grid (List[List[str]]): The grid to search, where each element is a string representing a cell.
    Returns:
        int: The number of steps in the shortest path from the top-left to the bottom-right corner.
             Returns -1 if no such path exists.
    """
    size = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 0)])  # (x, y, steps)
    visited = set([(0, 0)])
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == (size - 1, size - 1):
            return steps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return -1  # No path found

if __name__ == "__main__":
    file_path = 'input.txt'
    byte_positions = parse_input(file_path)
    grid_size = 71  # For the actual problem, use 71; for the example, use 7
    grid = initialize_grid(grid_size)
    simulate_falling_bytes(grid, byte_positions, 1024)
    steps = find_shortest_path(grid)
    print(f"Minimum number of steps needed to reach the exit: {steps}")
