from typing import List, Tuple
from collections import deque
from tqdm import tqdm

def parse_input(file_path: str) -> List[List[str]]:
    """
    Reads a file and parses its contents into a list of lists of strings.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[List[str]]: A list of lists, where each inner list represents a line from the file,
                         with each character in the line as an element of the inner list.
    """
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_positions(racetrack: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Finds the positions of the start ('S') and end ('E') points in a racetrack.

    Args:
        racetrack (List[List[str]]): A 2D list representing the racetrack where each cell is a string.

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: A tuple containing the coordinates of the start and end points.
            The first element is the coordinates of the start point (i, j) and the second element is the coordinates
            of the end point (i, j). If either the start or end point is not found, their respective value will be None.
    """
    start = end = None
    for i, row in enumerate(racetrack):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end

def bfs(racetrack: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Perform a breadth-first search (BFS) on a racetrack to find the shortest path from start to end.
    Args:
        racetrack (List[List[str]]): A 2D grid representing the racetrack where '#' represents obstacles and '.' represents open paths.
        start (Tuple[int, int]): The starting coordinates (x, y) on the racetrack.
        end (Tuple[int, int]): The ending coordinates (x, y) on the racetrack.
    Returns:
        List[Tuple[int, int]]: A list of coordinates representing the shortest path from start to end. 
                               Returns an empty list if no path is found.
    """
    rows, cols = len(racetrack), len(racetrack[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])
    visited = set([start])
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and racetrack[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))
    return []

def count_cheats(racetrack: List[List[str]], start: Tuple[int, int], end: Tuple[int, int], min_save: int) -> int:
    """
    Counts the number of positions on the racetrack where changing a wall ('#') to an open path ('.') 
    results in a time save of at least `min_save` steps from the start to the end position.
    Args:
        racetrack (List[List[str]]): A 2D list representing the racetrack grid where '#' represents walls and '.' represents open paths.
        start (Tuple[int, int]): The starting position on the racetrack as a tuple of (row, column).
        end (Tuple[int, int]): The ending position on the racetrack as a tuple of (row, column).
        min_save (int): The minimum number of steps that must be saved to consider a position as a cheat.
    Returns:
        int: The number of positions that can be considered cheats based on the given criteria.
    """
    rows, cols = len(racetrack), len(racetrack[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cheats = set()
    tried_positions = set()
    
    original_path = bfs(racetrack, start, end)
    original_path_length = len(original_path)
    
    for (i, j) in tqdm(original_path, desc="Path"):
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < rows and 0 <= ny < cols and racetrack[nx][ny] == '#' and (nx, ny) not in tried_positions:
                tried_positions.add((nx, ny))
                racetrack[nx][ny] = '.'
                new_path = bfs(racetrack, start, end)
                racetrack[nx][ny] = '#'
                new_path_length = len(new_path)
                time_saved = original_path_length - new_path_length
                if time_saved >= min_save:
                    cheats.add((nx, ny))
    return len(cheats)

if __name__ == "__main__":
    file_path = 'input.txt'
    racetrack = parse_input(file_path)
    start, end = find_positions(racetrack)
    min_save = 100
    cheats_count = count_cheats(racetrack, start, end, min_save)
    print(f"Number of cheats that save at least {min_save} picoseconds: {cheats_count}")
