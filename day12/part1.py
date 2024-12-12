from typing import List, Tuple, Set

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

def dfs(grid: List[str], plant_type: str, i: int, j: int, visited: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """
    Perform a depth-first search (DFS) on a grid to find all connected cells of the same plant type.

    Args:
        grid (List[str]): The grid representing the garden, where each cell contains a plant type.
        plant_type (str): The type of plant to search for.
        i (int): The starting row index for the DFS.
        j (int): The starting column index for the DFS.
        visited (Set[Tuple[int, int]]): A set of coordinates that have already been visited.

    Returns:
        Set[Tuple[int, int]]: A set of coordinates representing the connected group of the same plant type.
    """
    stack = [(i, j)]
    group = set()
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            group.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == plant_type:
                    stack.append((new_x, new_y))
    return group

def find_groups(grid: List[str], plant_type: str) -> List[Set[Tuple[int, int]]]:
    """
    Find all groups of a specific plant type in a grid.

    Args:
        grid (List[str]): A 2D grid represented as a list of strings, where each string is a row in the grid.
        plant_type (str): The character representing the plant type to find in the grid.

    Returns:
        List[Set[Tuple[int, int]]]: A list of sets, where each set contains the coordinates (i, j) of a group of the specified plant type.
    """
    groups = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == plant_type and (i, j) not in visited:
                groups.append(dfs(grid, plant_type, i, j, visited))
    return groups

def find_perimeter_and_area(group: Set[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Calculate the perimeter and area of a group of cells.

    Args:
        group (Set[Tuple[int, int]]): A set of tuples representing the coordinates of the cells.

    Returns:
        Tuple[int, int]: A tuple containing the perimeter and the area of the group.
    """
    perimeter = 0
    for i, j in group:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (i + dx, j + dy) not in group:
                perimeter += 1
    return perimeter, len(group)

def find_price_of_region(perimeter: int, area: int) -> int:
    """
    Calculate the price of a region based on its perimeter and area.

    Args:
        perimeter (int): The perimeter of the region.
        area (int): The area of the region.

    Returns:
        int: The calculated price of the region.
    """
    return perimeter * area

def find_price_per_type(grid: List[str], plant_type: str) -> int:
    """
    Calculate the total price for all regions of a specific plant type in a grid.

    Args:
        grid (List[str]): A list of strings representing the grid where each character represents a plant type.
        plant_type (str): The plant type for which the price needs to be calculated.

    Returns:
        int: The total price for all regions of the specified plant type.
    """
    groups = find_groups(grid, plant_type)
    return sum(find_price_of_region(*find_perimeter_and_area(group)) for group in groups)

def find_total_price(grid: List[str]) -> int:
    """
    Calculate the total price of all plant types in the given grid.

    Args:
        grid (List[str]): A list of strings representing the grid, where each character
                          corresponds to a plant type.

    Returns:
        int: The total price of all plant types in the grid.
    """
    return sum(find_price_per_type(grid, plant_type) for plant_type in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if __name__ == "__main__":
    input_data = read_input('input.txt')
    print(find_total_price(input_data))
