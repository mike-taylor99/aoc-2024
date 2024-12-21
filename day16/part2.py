import heapq
from typing import List, Tuple
from part1 import parse_input, get_possible_moves, find_starting_position

def find_scores_and_paths(grid: List[str], i: int, j: int, direction: str) -> List[Tuple[int, set]]:
    """
    Finds all possible scores and best paths from a starting position in a grid.
    Args:
        grid (List[str]): The grid represented as a list of strings.
        i (int): The starting row index.
        j (int): The starting column index.
        direction (str): The initial direction of movement.
    Returns:
        List[Tuple[int, set]]: A list of tuples where each tuple contains a score and a set representing a path.
    """
    scores_and_paths = []
    visited = {}
    lowest_score = float('inf')
    heap = [(0, i, j, direction, {(i, j)})]  # (score, row, col, direction, path)
    
    while heap:
        score, i, j, direction, path = heapq.heappop(heap)
        if ((i, j, direction) in visited and visited[(i, j, direction)] < score) or score > lowest_score:
            continue
        visited[(i, j, direction)] = score
        if grid[i][j] == 'E':
            lowest_score = score
            scores_and_paths.append((score, path | {(i, j)}))
        for new_i, new_j, new_direction in get_possible_moves(grid, i, j, direction):
            new_score = score + 1 if new_direction == direction else score + 1000
            new_path = path | {(new_i, new_j)}
            heapq.heappush(heap, (new_score, new_i, new_j, new_direction, new_path))
    return scores_and_paths

def find_shortest_path_tiles(grid: List[str]) -> set:
    """
    Finds the set of tiles that are part of the shortest path from the starting position to the target 'E' in the given grid.

    Args:
        grid (List[str]): A list of strings representing the grid where each string is a row of the grid.

    Returns:
        set: A set of tiles (coordinates) that are part of the shortest path to the target 'E'.
    """
    i, j = find_starting_position(grid)
    paths_and_scores = find_scores_and_paths(grid, i, j, 'E')
    return {tile for _, path in paths_and_scores for tile in path}

if __name__ == "__main__":
    file_path = 'input.txt'
    input = parse_input(file_path)
    print(len(find_shortest_path_tiles(input)))
