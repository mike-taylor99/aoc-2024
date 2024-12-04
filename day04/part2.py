from typing import List
from part1 import read_input, find_word_count

directions = [
    (1, 1),  # diagonal down-right
    (-1, -1),# diagonal up-left
    (1, -1), # diagonal down-left
    (-1, 1)  # diagonal up-right
]

def get_subgrids(grid: List[str]) -> List[str]:
    """
    Extracts all 3x3 subgrids from a given 2D grid.

    Args:
        grid (List[str]): A 2D grid represented as a list of strings.

    Returns:
        List[str]: A list of 3x3 subgrids, each represented as a list of strings.
    """
    return [
        [grid[i + k][j:j + 3] for k in range(3)]
        for i in range(len(grid) - 2)
        for j in range(len(grid[0]) - 2)
    ]

def find_x_mas(subgrid: List[str]) -> bool:
    """
    Checks if the word "MAS" appears exactly twice in the given subgrid.

    Args:
        subgrid (List[str]): A list of strings representing the subgrid to search within.

    Returns:
        bool: True if the word "MAS" appears exactly twice in the subgrid, False otherwise.
    """
    mas = "MAS"
    return find_word_count(subgrid, mas, directions) == 2
    
if __name__ == "__main__":
    grid: List[List[str]] = read_input('input.txt')
    subgrids: List[List[List[str]]] = get_subgrids(grid)
    count: int = sum(find_x_mas(subgrid) for subgrid in subgrids)
    print(count)
