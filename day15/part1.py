import re
from typing import List, Tuple

def parse_input(file_path: str) -> Tuple[List[List[str]], List[str]]:
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    grid_part, instructions_part = content.split('\n\n')
    grid = [list(line) for line in grid_part.split('\n')]
    instructions = list(''.join(instructions_part.split('\n')))
    
    return grid, instructions

def find_robot_position(grid: List[List[str]]) -> Tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                return x, y
    return -1, -1

def move_robot(grid: List[List[str]], instructions: List[str]) -> List[List[str]]:
    direction_map = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    
    x, y = find_robot_position(grid)
    
    for instruction in instructions:
        dx, dy = direction_map[instruction]
        new_x, new_y = x + dx, y + dy
        
        if not (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid)):
            continue
        if grid[new_y][new_x] == '#':
            continue
        elif grid[new_y][new_x] == 'O':
            # Check if we can push the box
            box_x, box_y = new_x, new_y
            while 0 <= box_x + dx < len(grid[0]) and 0 <= box_y + dy < len(grid) and grid[box_y][box_x] == 'O':
                box_x += dx
                box_y += dy
                if not (0 <= box_x + dx < len(grid[0]) and 0 <= box_y + dy < len(grid)) or grid[box_y][box_x] == '#':
                    break
            else:
                # Move the robot and push the boxes
                while (box_x, box_y) != (new_x, new_y):
                    box_x -= dx
                    box_y -= dy
                    grid[box_y + dy][box_x + dx] = 'O'
                grid[new_y][new_x] = '@'
                grid[y][x] = '.'
                x, y = new_x, new_y
        else:
            grid[new_y][new_x] = '@'
            grid[y][x] = '.'
            x, y = new_x, new_y
    
    return grid

def calculate_gps_sum(grid: List[List[str]]) -> int:
    gps_sum = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * y + x
    return gps_sum

if __name__ == "__main__":
    file_path = 'input.txt'
    grid, instructions = parse_input(file_path)
    
    print("Initial Grid:")
    for row in grid:
        print(''.join(row))
    
    grid = move_robot(grid, instructions)
    
    print("\nFinal Grid:")
    for row in grid:
        print(''.join(row))
    
    gps_sum = calculate_gps_sum(grid)
    print(f"\nSum of all boxes' GPS coordinates: {gps_sum}")