import sys
from typing import List, Tuple

def parse_track(file_path: str) -> List[Tuple[int, int]]:
    """
    Parses a track from a given file and returns the path from the start ('S') to the end ('E').
    Args:
        file_path (str): The path to the file containing the track grid.
    Returns:
        List[Tuple[int, int]]: A list of tuples representing the coordinates of the path from the start to the end.
    """
    with open(file_path, 'r') as f:
        grid = [line.rstrip() for line in f]
    
    start_pos = next((x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == 'S')
    track = [None, start_pos]
    x, y = start_pos
    
    while grid[y][x] != 'E':
        next_pos = next((nx, ny) for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                        if (nx, ny) != track[-2] and grid[ny][nx] != '#')
        track.append(next_pos)
        x, y = next_pos
    
    return track[1:]

def cheats(track: List[Tuple[int, int]], max_dist: int) -> List[int]:
    """
    Identifies potential cheating instances in a race track based on the given maximum distance.

    Args:
        track (List[Tuple[int, int]]): A list of tuples representing the coordinates (x, y) of each checkpoint on the track.
        max_dist (int): The maximum allowable distance between two checkpoints to consider it as a valid move.

    Returns:
        List[int]: A list of integers representing the difference between the time indices of the checkpoints where cheating is detected.
    """
    results = []
    for t1, (x1, y1) in enumerate(track):
        for t2 in range(t1 + 3, len(track)):
            x2, y2 = track[t2]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if dist <= max_dist and t2 - t1 > dist:
                results.append(t2 - t1 - dist)
    return results

if __name__ == "__main__":
    track = parse_track('input.txt')
    result = sum(saved >= 100 for saved in cheats(track, 20))
    print(result)