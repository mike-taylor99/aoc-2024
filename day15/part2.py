import sys
from collections import defaultdict
from part1 import parse_input
from typing import List, Tuple, Set

# Constants for directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [RIGHT, LEFT, DOWN, UP]
DIR_MAP = {">": RIGHT, "<": LEFT, "v": DOWN, "^": UP}

def add_tuples(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    """
    Adds two tuples element-wise.

    Args:
        x (Tuple[int, int]): The first tuple.
        y (Tuple[int, int]): The second tuple.

    Returns:
        Tuple[int, int]: A tuple containing the element-wise sum of the input tuples.
    """
    return tuple(map(sum, zip(x, y)))

def left(pos: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a position as a tuple of (row, column), return the position to the left.

    Args:
        pos (Tuple[int, int]): The current position as a tuple (row, column).

    Returns:
        Tuple[int, int]: The new position to the left of the current position.
    """
    return (pos[0], pos[1] - 1)

def right(pos: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a position as a tuple of (row, column), returns the position to the right.

    Args:
        pos (Tuple[int, int]): A tuple representing the current position (row, column).

    Returns:
        Tuple[int, int]: A tuple representing the new position to the right (row, column + 1).
    """
    return (pos[0], pos[1] + 1)

def push(box: Tuple[int, int], direction: Tuple[int, int], boxes: Set[Tuple[int, int]], walls: Set[Tuple[int, int]]) -> bool:
    """
    Attempts to push a box in a specified direction within a grid containing boxes and walls.

    Args:
        box (Tuple[int, int]): The current position of the box to be pushed.
        direction (Tuple[int, int]): The direction to push the box, represented as a tuple (dx, dy).
        boxes (Set[Tuple[int, int]]): A set of tuples representing the positions of all boxes on the grid.
        walls (Set[Tuple[int, int]]): A set of tuples representing the positions of all walls on the grid.

    Returns:
        bool: True if the box was successfully pushed, False otherwise.
    """
    assert box in boxes
    next_pos = add_tuples(box, direction)
    if next_pos in walls or right(next_pos) in walls:
        return False
    if direction[0]:  # moving up/down
        if next_pos in boxes and not push(next_pos, direction, boxes, walls):
            return False
        if left(next_pos) in boxes and not push(left(next_pos), direction, boxes, walls):
            return False
        if right(next_pos) in boxes and not push(right(next_pos), direction, boxes, walls):
            return False
    elif direction[1] == 1:  # pushing right
        if right(next_pos) in boxes and not push(right(next_pos), direction, boxes, walls):
            return False
    elif direction[1] == -1:  # pushing left
        if left(next_pos) in boxes and not push(left(next_pos), direction, boxes, walls):
            return False
    boxes.remove(box)
    boxes.add(next_pos)
    return True

def parse_grid(grid: List[str]) -> Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]], Tuple[int, int]]:
    """
    Parses a grid represented as a list of strings and identifies the positions of walls, boxes, and the robot.
    Args:
        grid (List[str]): A list of strings representing the grid. Each character in the string represents a different element:
                          '#' for walls, 'O' for boxes, and '@' for the robot.
    Returns:
        Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]], Tuple[int, int]]:
            - A set of tuples representing the positions of walls.
            - A set of tuples representing the positions of boxes.
            - A tuple representing the position of the robot.
    """
    walls = set()
    boxes = set()
    robot = None

    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            j *= 2
            if ch == "#":
                walls.add((i, j))
                walls.add((i, j + 1))
            elif ch == "O":
                boxes.add((i, j))
            elif ch == "@":
                robot = (i, j)
    
    return walls, boxes, robot

def execute_moves(moves: List[Tuple[int, int]], robot: Tuple[int, int], boxes: Set[Tuple[int, int]], walls: Set[Tuple[int, int]]) -> Tuple[Tuple[int, int], Set[Tuple[int, int]]]:
    """
    Executes a series of moves for a robot in a grid with boxes and walls.

    Args:
        moves (List[Tuple[int, int]]): A list of moves where each move is represented as a tuple (dx, dy).
        robot (Tuple[int, int]): The initial position of the robot as a tuple (x, y).
        boxes (Set[Tuple[int, int]]): A set of positions of boxes in the grid.
        walls (Set[Tuple[int, int]]): A set of positions of walls in the grid.

    Returns:
        Tuple[Tuple[int, int], Set[Tuple[int, int]]]: The final position of the robot and the updated set of box positions.
    """
    for move in moves:
        for box in boxes:
            assert right(box) not in boxes
            assert right(box) not in walls
        next_pos = add_tuples(robot, move)
        if next_pos in walls:
            continue
        if next_pos in boxes:
            copy = boxes.copy()
            if not push(next_pos, move, boxes, walls):
                boxes = copy
                continue
        elif left(next_pos) in boxes:
            copy = boxes.copy()
            if not push(left(next_pos), move, boxes, walls):
                boxes = copy
                continue
        assert next_pos not in boxes
        assert left(next_pos) not in boxes
        robot = next_pos
    return robot, boxes

def calculate_score(boxes: Set[Tuple[int, int]]) -> int:
    """
    Calculate the total score based on a set of boxes.

    Each box is represented as a tuple of two integers. The score for each box
    is calculated as 100 times the first integer plus the second integer. The
    total score is the sum of the scores for all boxes.

    Args:
        boxes (Set[Tuple[int, int]]): A set of tuples, where each tuple contains
                                      two integers representing a box.

    Returns:
        int: The total score calculated from the set of boxes.
    """
    return sum(100 * box[0] + box[1] for box in boxes)

if __name__ == "__main__":
    file_path = 'input.txt'
    grid, instructions = parse_input(file_path)

    moves = [DIR_MAP[m] for m in instructions]

    walls, boxes, robot = parse_grid(grid)
    robot, boxes = execute_moves(moves, robot, boxes, walls)
    score = calculate_score(boxes)
    print(score)
