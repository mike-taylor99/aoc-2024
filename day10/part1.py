from typing import List, Tuple

def read_input(file_path: str) -> List[List[int]]:
    """
    Reads a file and converts its contents into a list of lists of integers.

    Each line in the file is stripped of leading and trailing whitespace, and each character
    in the line is converted to an integer if it is a digit. If a character is not a digit,
    it is converted to float('inf').

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[List[int]]: A list of lists where each inner list represents a line from the file
                         with characters converted to integers or float('inf').
    """
    with open(file_path) as f:
        return [[int(num) if num.isdigit() else float('inf') for num in line.strip()] for line in f]

def get_neighbors(grid: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    """
    Get the neighboring coordinates of a given cell in a 2D grid.

    Args:
        grid (List[List[int]]): The 2D grid represented as a list of lists of integers.
        x (int): The x-coordinate (row index) of the cell.
        y (int): The y-coordinate (column index) of the cell.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing the coordinates of the neighboring cells.
    """
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < rows - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < cols - 1:
        neighbors.append((x, y+1))
    return neighbors

def get_valid_neighbors(grid: List[List[int]], x: int, y: int) -> List[Tuple[int, int]]:
    """
    Given a 2D grid and a specific cell (x, y), this function returns a list of 
    neighboring cells that have a value exactly one greater than the value of 
    the specified cell.

    Args:
        grid (List[List[int]]): A 2D list representing the grid.
        x (int): The x-coordinate (row index) of the specified cell.
        y (int): The y-coordinate (column index) of the specified cell.

    Returns:
        List[Tuple[int, int]]: A list of tuples, where each tuple represents 
        the coordinates (x, y) of a neighboring cell that has a value exactly 
        one greater than the value of the specified cell.
    """
    value = grid[x][y]
    neighbors = get_neighbors(grid, x, y)
    return [neighbor for neighbor in neighbors if grid[neighbor[0]][neighbor[1]] == value + 1]

def find_zeros(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find all positions of zeros in a 2D grid.

    Args:
        grid (List[List[int]]): A 2D list of integers representing the grid.

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple represents the 
        (row, column) position of a zero in the grid.
    """
    return [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]

def find_top(grid: List[List[int]], x: int, y: int) -> int:
    """
    Finds the number of cells with the value 9 starting from a given cell in a grid.

    Args:
        grid (List[List[int]]): A 2D list representing the grid of integers.
        x (int): The x-coordinate (row index) of the starting cell.
        y (int): The y-coordinate (column index) of the starting cell.

    Returns:
        int: The count of cells with the value 9 that are reachable from the starting cell.
    """
    stack = [(x, y)]
    visited = set()
    top_count = 0

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue

        visited.add((cx, cy))
        value = grid[cx][cy]

        if value == 9:
            top_count += 1
            continue

        neighbors = get_valid_neighbors(grid, cx, cy)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return top_count

def find_top_sum(grid: List[List[int]], find_top_func=find_top) -> int:
    """
    Calculate the sum of the top values found by a given function for each zero in the grid.

    Args:
        grid (List[List[int]]): A 2D list of integers representing the grid.
        find_top_func (Callable[[List[List[int]], int, int], int], optional): 
            A function that takes the grid and the coordinates of a zero and returns the top value. 
            Defaults to find_top.

    Returns:
        int: The sum of the top values for each zero in the grid.
    """
    zeros = find_zeros(grid)
    return sum(find_top_func(grid, zero[0], zero[1]) for zero in zeros)

if __name__ == "__main__":
    input_data = read_input('input.txt')
    print(find_top_sum(input_data))
