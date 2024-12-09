from typing import List, Tuple
from part1 import read_input, generate_disk_map, calculate_checksum

def find_starting_index(disk_map: List[str], num: int) -> int:
    """
    Finds the starting index of the first sequence of `num` consecutive '.' characters in the given disk map.

    Args:
        disk_map (List[str]): A list of strings representing the disk map.
        num (int): The number of consecutive '.' characters to find.

    Returns:
        int: The starting index of the first sequence of `num` consecutive '.' characters.
             Returns -1 if no such sequence is found.
    """
    count = 0
    for i, val in enumerate(disk_map):
        if val == '.':
            count += 1
            if count == num:
                return i - (count - 1)
        else:
            count = 0
    return -1

def find_group(disk_map: List[str], char: str) -> Tuple[int, int]:
    """
    Finds the start and end indices of a contiguous group of the specified character in the disk map.

    Args:
        disk_map (List[str]): A list of characters representing the disk map.
        char (str): The character to find in the disk map.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices (inclusive) of the contiguous group of the specified character.
    """
    start = disk_map.index(char)
    end = start
    while end < len(disk_map) and disk_map[end] == char:
        end += 1
    return start, end - 1

def compact_file(disk_map: List[str]) -> List[str]:
    """
    Compacts the given disk map by moving groups of contiguous blocks to the first available free space.
    Args:
        disk_map (List[str]): A list of strings representing the disk map, where each string is a block ID.
    Returns:
        List[str]: The compacted disk map with groups moved to the first available free spaces.
    The function works by iterating through the disk map in reverse order of block IDs, finding groups of contiguous blocks,
    and moving them to the first available free space if possible.
    """
    current_id = int(disk_map[-1])

    while current_id > 0:
        start, end = find_group(disk_map, str(current_id))
        group_length = end - start + 1
        first_free_space_index = find_starting_index(disk_map, group_length)

        if first_free_space_index != -1 and first_free_space_index < start:
            disk_map[first_free_space_index:first_free_space_index + group_length], disk_map[start:end + 1] = disk_map[start:end + 1], disk_map[first_free_space_index:first_free_space_index + group_length]
        
        current_id -= 1
    
    return disk_map

if __name__ == "__main__":
    input_data = read_input('input.txt')
    disk_map = generate_disk_map(input_data)
    compacted_disk_map = compact_file(disk_map)
    print(calculate_checksum(compacted_disk_map))
