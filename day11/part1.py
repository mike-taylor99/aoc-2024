from typing import List
from collections import Counter, defaultdict
from functools import lru_cache

def read_input(file_path: str) -> List[int]:
    """
    Reads a file containing integers separated by whitespace and returns a list of integers.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[int]: A list of integers read from the file.
    """
    with open(file_path) as f:
        return [int(num) for num in f.read().strip().split()]

@lru_cache(maxsize=None)
def process_single_stone(stone: int) -> List[int]:
    """
    Processes a single stone based on its value.

    If the stone is 0, returns a list containing 1.
    If the length of the stone's string representation is even, splits the stone into two halves and returns them as a list of integers.
    If the length of the stone's string representation is odd, returns a list containing the stone multiplied by 2024.

    Args:
        stone (int): The stone to be processed.

    Returns:
        List[int]: A list of integers resulting from the processing of the stone.
    """
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        mid = len(str_stone) // 2
        left_half = int(str_stone[:mid])
        right_half = int(str_stone[mid:])
        return [left_half, right_half]
    else:
        return [stone * 2024]

def process_stones(stones: Counter) -> Counter:
    """
    Processes a collection of stones and returns a new collection with the processed stones.
    Args:
        stones (Counter): A Counter object where keys are stone types and values are their counts.
    Returns:
        Counter: A Counter object with the processed stones and their counts.
    """
    result = defaultdict(int)
    
    for stone, count in stones.items():
        processed = process_single_stone(stone)
        for processed_stone in processed:
            result[processed_stone] += count
    
    return Counter(result)

def process_stones_n_times(stones: List[int], n: int) -> Counter:
    """
    Processes a list of stones a specified number of times and returns the result as a Counter.

    Args:
        stones (List[int]): A list of integers representing stones.
        n (int): The number of times to process the stones.

    Returns:
        Counter: A Counter object representing the processed stones.
    """
    result = Counter(stones)
    for _ in range(n):
        result = process_stones(result)
    return result

if __name__ == "__main__":
    input_data = read_input('input.txt')
    processed_stones = process_stones_n_times(input_data, 25)
    print(sum(processed_stones.values()))
