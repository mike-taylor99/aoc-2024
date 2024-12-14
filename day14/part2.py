from typing import List, Tuple
from part1 import parse_input, move_multiple_robots_n_times
from tqdm import tqdm

def find_easter_egg(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], width: int, length: int, max_steps: int) -> int:
    """
    Finds the step at which all robots occupy unique positions on the grid.

    Args:
        robots (List[Tuple[Tuple[int, int], Tuple[int, int]]]): A list of robots, where each robot is represented by a tuple of two tuples.
            The first tuple represents the starting position (x, y) of the robot, and the second tuple represents the direction (dx, dy) of movement.
        width (int): The width of the grid.
        length (int): The length of the grid.
        max_steps (int): The maximum number of steps to simulate.

    Returns:
        int: The step at which all robots occupy unique positions. Returns -1 if no such step is found within the given maximum steps.
    """
    num_robots = len(robots)

    for step in tqdm(range(max_steps)):
        new_positions = move_multiple_robots_n_times(robots, width, length, step)
        unique_positions = set(new_positions)
        if len(unique_positions) == num_robots:
            return step

    return -1

def display_positions(positions: List[Tuple[int, int]], width: int, length: int):
    """
    Displays a grid with specified positions marked.

    Args:
        positions (List[Tuple[int, int]]): A list of tuples where each tuple represents
                                           the (x, y) coordinates to be marked on the grid.
        width (int): The width of the grid.
        length (int): The length of the grid.

    The grid is represented by a list of lists, where each inner list represents a row.
    Positions within the grid are marked with '#', and empty spaces are marked with '.'.
    The grid is printed to the console.
    """
    grid = [['.' for _ in range(width)] for _ in range(length)]
    for x, y in positions:
        if 0 <= x < width and 0 <= y < length:
            grid[y][x] = '#'
    print('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    file_path = 'input.txt'
    robots = parse_input(file_path)
    width = 101
    length = 103
    max_steps = 10000  # Maximum number of steps to simulate

    best_time = find_easter_egg(robots, width, length, max_steps)
    if best_time != -1:
        final_positions = move_multiple_robots_n_times(robots, width, length, best_time)
        display_positions(final_positions, width, length)
        print(f"The robots display the Easter egg after {best_time} seconds.")
    else:
        print("The robots did not display the Easter egg within the given steps.")
