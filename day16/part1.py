import re
from typing import List, Tuple
import heapq

def parse_input(file_path: str):
    """
    Parse the input file to extract the data.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[str]: A list of strings representing the data from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
def find_starting_position(grid: List[str]) -> Tuple[int, int]:
    """
    Find the starting position marked as 'S' in the grid.

    Args:
        grid (List[str]): A list of strings representing the grid.

    Returns:
        Tuple[int, int]: A tuple containing the row and column indices of the starting position.
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return -1, -1

# given a grid and a current position as well as a direction,
# return the list of next possible moves either moving forward in the current direction or turning left or right
def get_possible_moves(grid: List[str], i: int, j: int, direction: str) -> List[Tuple[int, int, str]]:
    """
    Get the possible moves from the current position in the grid.

    Args:
        grid (List[str]): A list of strings representing the grid.
        i (int): The row index of the current position.
        j (int): The column index of the current position.
        direction (str): The current direction ('N', 'E', 'S', 'W').

    Returns:
        List[Tuple[int, int, str]]: A list of tuples where each tuple contains the row index, column index, and the direction of the possible moves.
    """
    rows, cols = len(grid), len(grid[0])
    moves = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    left_turns = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
    right_turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    possible_moves = []

    # Check forward move
    dx, dy = moves[direction]
    new_i, new_j = i + dx, j + dy
    if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] != '#':
        possible_moves.append((new_i, new_j, direction))

    # Check left turn
    left_direction = left_turns[direction]
    left_dx, left_dy = moves[left_direction]
    left_i, left_j = i + left_dx, j + left_dy
    if 0 <= left_i < rows and 0 <= left_j < cols and grid[left_i][left_j] != '#':
        possible_moves.append((i, j, left_direction))

    # Check right turn
    right_direction = right_turns[direction]
    right_dx, right_dy = moves[right_direction]
    right_i, right_j = i + right_dx, j + right_dy
    if 0 <= right_i < rows and 0 <= right_j < cols and grid[right_i][right_j] != '#':
        possible_moves.append((i, j, right_direction))

    return possible_moves

def find_lowest_score(grid: List[str], i: int, j: int, direction: str) -> int:
    """
    Finds the shortest path in a grid from a starting position (i, j) in a given direction.

    Args:
        grid (List[str]): A 2D grid represented as a list of strings.
        i (int): The starting row index.
        j (int): The starting column index.
        direction (str): The initial direction of movement.

    Returns:
        int: The shortest path score to reach the target 'E' in the grid. If the target is not reachable, returns float('inf').
    """
    visited = set()
    heap = [(0, i, j, direction)]  # (score, row, col, direction)
    while heap:
        score, i, j, direction = heapq.heappop(heap)
        if (i, j, direction) in visited:
            continue
        visited.add((i, j, direction))
        if grid[i][j] == 'E':
            return score
        for new_i, new_j, new_direction in get_possible_moves(grid, i, j, direction):
            new_score = score + 1 if new_direction == direction else score + 1000
            heapq.heappush(heap, (new_score, new_i, new_j, new_direction))
    return float('inf')

if __name__ == "__main__":
    file_path = 'input.txt'
    parsed_data = parse_input(file_path)
    i, j = find_starting_position(parsed_data)
    score = find_lowest_score(parsed_data, i, j, 'E')
    print(score)