from typing import List, Tuple
from part1 import read_input, get_valid_neighbors, find_top_sum

def find_top(grid: List[List[int]], x, y, visited = set()) -> int:
    """
    Recursively finds the sum of values in a grid starting from a given cell (x, y) 
    and exploring its valid neighbors, stopping when a cell with value 9 is encountered.
    Args:
        grid (List[List[int]]): A 2D list representing the grid of integers.
        x (int): The x-coordinate (row index) of the starting cell.
        y (int): The y-coordinate (column index) of the starting cell.
        visited (set, optional): A set of tuples representing the coordinates of visited cells. Defaults to an empty set.
    Returns:
        int: The sum of values from the starting cell to the cells explored, stopping at cells with value 9.
    """
    value = grid[x][y]

    if value == 9:
        return 1
    
    neighbors = get_valid_neighbors(grid, x, y)
    sum = 0
    for neighbor in neighbors:
        if (neighbor[0], neighbor[1]) in visited:
            continue
        else:
            sum += find_top(grid, neighbor[0], neighbor[1], visited | {(x, y)})
    return sum

if __name__ == "__main__":
    input_data = read_input('input.txt')
    print(find_top_sum(input_data, find_top))