from typing import Tuple, Set, List
from part1 import read_input, find_groups, find_perimeter_and_area

def count_sides(group: Set[Tuple[int, int]]) -> int:
    """
    Counts the number of sides (corners) in a given group of coordinates.

    Args:
        group (Set[Tuple[int, int]]): A set of tuples representing coordinates.

    Returns:
        int: The total number of sides (corners) in the group.

    The function considers both outer and inner corners:
    - Outer corners are counted when two adjacent cells are not in the group.
    - Inner corners are counted when two adjacent cells are in the group, but the diagonal cell is not.
    """
    def count_corners_at(x, y):
        s = 0
        # Outer corners
        s += ((x - 1, y) not in group and (x, y - 1) not in group)
        s += ((x + 1, y) not in group and (x, y - 1) not in group)
        s += ((x - 1, y) not in group and (x, y + 1) not in group)
        s += ((x + 1, y) not in group and (x, y + 1) not in group)
        # Inner corners
        s += ((x - 1, y) in group and (x, y - 1) in group and (x - 1, y - 1) not in group)
        s += ((x + 1, y) in group and (x, y - 1) in group and (x + 1, y - 1) not in group)
        s += ((x - 1, y) in group and (x, y + 1) in group and (x - 1, y + 1) not in group)
        s += ((x + 1, y) in group and (x, y + 1) in group and (x + 1, y + 1) not in group)
        return s

    return sum(count_corners_at(x, y) for x, y in group)

def find_price_of_region(sides: int, area: int) -> int:
    """
    Calculate the price of a region based on the number of sides and the area.

    Args:
        sides (int): The number of sides of the region.
        area (int): The area of the region.

    Returns:
        int: The calculated price of the region.
    """
    return sides * area

def find_price_per_type(grid: List[str], plant_type: str) -> int:
    """
    Calculate the total price for a specific plant type in a grid.

    Args:
        grid (List[str]): A list of strings representing the grid.
        plant_type (str): The type of plant to calculate the price for.

    Returns:
        int: The total price for the specified plant type.
    """
    groups = find_groups(grid, plant_type)
    total = 0
    for group in groups:
        _, area = find_perimeter_and_area(group)
        sides = count_sides(group)
        total += find_price_of_region(sides, area)
    return total

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
