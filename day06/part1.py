from typing import List, Tuple

def read_input(file_path: str) -> List[str]:
    """
    Reads the input from a file and returns a list of stripped lines.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[str]: A list of lines from the file, with leading and trailing whitespace removed.
    """
    with open(file_path) as f:
        return [line.strip() for line in f]

def turn_right(direction: str) -> str:
    """
    Turns the given direction 90 degrees to the right.

    Args:
        direction (str): The current direction, which should be one of the following:
                         '^' for up, '>' for right, 'v' for down, or '<' for left.

    Returns:
        str: The new direction after turning 90 degrees to the right.
    """
    directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return directions[direction]

def move_one_step(grid: List[List[str]], x: int, y: int, direction: str) -> Tuple[int, int, str]:
    """
    Move one step in the given direction on the grid.

    Args:
        grid (List[List[str]]): The grid representing the environment.
        x (int): The current x-coordinate (row index).
        y (int): The current y-coordinate (column index).
        direction (str): The current direction ('^', '>', 'v', '<').

    Returns:
        Tuple[int, int, str]: A tuple containing the new x-coordinate, new y-coordinate, and the direction.
                              If the move is not possible, returns (None, None, None).
    """
    rows, cols = len(grid), len(grid[0])
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    while True:
        dx, dy = moves[direction]
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != '#':
            return new_x, new_y, direction
        else:
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                return None, None, None
            direction = turn_right(direction)

def move_tracker(grid: List[str], start_pos: Tuple[int, int], direction: str) -> List[str]:
    """
    Tracks movement on a grid starting from a given position and direction.
    Args:
        grid (List[str]): A list of strings representing the grid.
        start_pos (Tuple[int, int]): The starting position as a tuple (x, y).
        direction (str): The initial direction of movement.
    Returns:
        List[str]: The updated grid with the path marked by 'X'.
    """
    x, y = start_pos
    grid = [list(row) for row in grid]  # Convert to list of lists for mutability

    # Mark the starting position
    grid[x][y] = 'X'
    
    while True:
        x, y, direction = move_one_step(grid, x, y, direction)
        if x is None or y is None:
            break
        grid[x][y] = 'X'
    
    return [''.join(row) for row in grid]

def find_start_pos(grid: List[str]) -> Tuple[int, int]:
    """
    Finds the starting position in a grid.

    Args:
        grid (List[str]): A list of strings representing the grid.

    Returns:
        Tuple[int, int]: A tuple containing the row and column indices of the starting position marked by '^'.
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i, j)
            
def count_visited(grid: List[str]) -> int:
    """
    Counts the number of visited cells in a grid.

    Args:
        grid (List[str]): A list of strings representing the grid, where each string is a row and 'X' denotes a visited cell.

    Returns:
        int: The total number of visited cells in the grid.
    """
    return sum(row.count('X') for row in grid)

if __name__ == "__main__":
    grid = read_input('input.txt')
    x, y = find_start_pos(grid)
    end_grid = move_tracker(grid, (x, y), '^')
    print(count_visited(end_grid))
