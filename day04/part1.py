from typing import List, Tuple

def read_input(file_path: str) -> List[str]:
    """
    Reads a file and returns a list of stripped lines.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[str]: A list of lines from the file, with leading and trailing whitespace removed.
    """
    with open(file_path) as f:
        return [line.strip() for line in f]

def find_word_count(grid: List[str], word: str, directions: List[Tuple[int, int]]) -> int:
    """
    Finds the number of times a word appears in a grid of characters in specified directions.
    Args:
        grid (List[str]): A list of strings representing the grid of characters.
        word (str): The word to search for in the grid.
        directions (List[Tuple[int, int]]): A list of tuples representing the directions to search in.
            Each tuple contains two integers (dx, dy) representing the direction vector.
    Returns:
        int: The number of times the word appears in the grid in the specified directions.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    def in_bounds(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols
    
    def search_from(x: int, y: int, dx: int, dy: int) -> bool:
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    match_count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    match_count += 1
    
    return match_count


directions = [
    (0, 1),   # horizontal right
    (0, -1),  # horizontal left
    (1, 0),   # vertical down
    (-1, 0),  # vertical up
    (1, 1),   # diagonal down-right
    (-1, -1), # diagonal up-left
    (1, -1),  # diagonal down-left
    (-1, 1)   # diagonal up-right
]

if __name__ == "__main__":
    grid = read_input('input.txt')
    word = "XMAS"
    match_count = find_word_count(grid, word, directions)
    print(f"Total matches: {match_count}")
