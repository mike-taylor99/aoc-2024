import re
from typing import List, Tuple

def parse_input(file_path: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parses the input file to extract position and velocity coordinates.

    The input file should contain lines formatted as:
    "p=<int>,<int> v=<int>,<int>"

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[Tuple[Tuple[int, int], Tuple[int, int]]]: A list of tuples, each containing:
            - A tuple representing the position coordinates (p_x, p_y).
            - A tuple representing the velocity coordinates (v_x, v_y).
    """
    pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    with open(file_path, 'r') as file:
        return [((int(p_x), int(p_y)), (int(v_x), int(v_y))) for p_x, p_y, v_x, v_y in pattern.findall(file.read())]

def move_robot_n_times(position: Tuple[int, int], velocity: Tuple[int, int], width: int, length: int, n: int) -> Tuple[int, int]:
    """
    Moves the robot according to its velocity n number of times and wraps around the edges if it runs into the edge of the space.

    Args:
        position (Tuple[int, int]): The current position of the robot (x, y).
        velocity (Tuple[int, int]): The velocity of the robot (vx, vy).
        width (int): The width of the space.
        length (int): The length of the space.
        n (int): The number of times to move the robot.

    Returns:
        Tuple[int, int]: The new position of the robot after moving n times.
    """
    x, y = position
    vx, vy = velocity
    return (x + vx * n) % width, (y + vy * n) % length

def move_multiple_robots_n_times(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], width: int, length: int, n: int) -> List[Tuple[int, int]]:
    """
    Moves multiple robots according to their velocities n number of times and wraps around the edges if they run into the edge of the space.

    Args:
        robots (List[Tuple[Tuple[int, int], Tuple[int, int]]]): A list of tuples, each containing:
            - A tuple representing the position coordinates (x, y).
            - A tuple representing the velocity coordinates (vx, vy).
        width (int): The width of the space.
        length (int): The length of the space.
        n (int): The number of times to move the robots.

    Returns:
        List[Tuple[int, int]]: A list of new positions of the robots after moving n times.
    """
    return [move_robot_n_times(position, velocity, width, length, n) for position, velocity in robots]

def count_robots_in_quadrants(positions: List[Tuple[int, int]], width: int, length: int) -> Tuple[int, int, int, int]:
    """
    Counts the number of robots in each quadrant. Robots that are exactly in the middle (horizontally or vertically) don't count as being in any quadrant.

    Args:
        positions (List[Tuple[int, int]]): A list of positions (x, y) of the robots.
        width (int): The width of the space.
        length (int): The length of the space.

    Returns:
        Tuple[int, int, int, int]: A tuple containing the counts of robots in the first, second, third, and fourth quadrants respectively.
    """
    q1 = q2 = q3 = q4 = 0
    mid_x = width // 2
    mid_y = length // 2

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x > mid_x and y > mid_y:
            q1 += 1
        elif x < mid_x and y > mid_y:
            q2 += 1
        elif x < mid_x and y < mid_y:
            q3 += 1
        elif x > mid_x and y < mid_y:
            q4 += 1

    return q1, q2, q3, q4

def calculate_safety_factor(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]], width: int, length: int, n: int) -> int:
    """
    Calculates the safety factor by moving robots n times and counting the number of robots in each quadrant.
    The safety factor is the product of the number of robots in each quadrant.

    Args:
        robots (List[Tuple[Tuple[int, int], Tuple[int, int]]]): A list of tuples, each containing:
            - A tuple representing the position coordinates (x, y).
            - A tuple representing the velocity coordinates (vx, vy).
        width (int): The width of the space.
        length (int): The length of the space.
        n (int): The number of times to move the robots.

    Returns:
        int: The safety factor, which is the product of the number of robots in each quadrant.
    """
    new_positions = move_multiple_robots_n_times(robots, width, length, n)
    q1, q2, q3, q4 = count_robots_in_quadrants(new_positions, width, length)
    return q1 * q2 * q3 * q4

if __name__ == "__main__":
    file_path = 'input.txt'
    parsed_data = parse_input(file_path)
    width = 101
    length = 103
    n = 100  # Number of times to move the robots

    safety_factor = calculate_safety_factor(parsed_data, width, length, n)
    print(f"Safety Factor: {safety_factor}")
