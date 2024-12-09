from typing import List

def read_input(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path) as f:
        return f.read()

def generate_disk_map(input: str) -> List[str]:
    """
    Generates a disk map based on the input string.

    Args:
        input (str): A string where each character represents a number. 
                     Even-indexed characters determine the number of times 
                     the corresponding index divided by 2 should be repeated 
                     in the disk map. Odd-indexed characters determine the 
                     number of dots to be added to the disk map.

    Returns:
        List[str]: A list of strings representing the generated disk map.
    """
    disk_map = []
    for i, val in enumerate(input):
        disk_map.extend([str(i // 2)] * int(val) if i % 2 == 0 else ['.'] * int(val))
    return disk_map

def find_first_non_empty_from_end(disk_map: List[str]) -> int:
    """
    Finds the index of the first non-empty element from the end of the list.

    Args:
        disk_map (List[str]): A list of strings representing the disk map.

    Returns:
        int: The index of the first non-empty element from the end of the list.
             Returns -1 if all elements are empty (i.e., '.').
    """
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != '.':
            return i
    return -1

def compact_file(disk_map: List[str]) -> List[str]:
    """
    Compacts the given disk map by moving all non-empty blocks to the beginning
    and all free spaces ('.') to the end.
    Args:
        disk_map (List[str]): A list of strings representing the disk map, where
                              each string is either a non-empty block or a free space ('.').
    Returns:
        List[str]: The compacted disk map with all non-empty blocks at the beginning
                   and all free spaces at the end.
    """
    first_free_space_index = disk_map.index('.')
    end_block_index = find_first_non_empty_from_end(disk_map)
    
    while first_free_space_index < end_block_index:
        disk_map[first_free_space_index], disk_map[end_block_index] = disk_map[end_block_index], disk_map[first_free_space_index]
        first_free_space_index = disk_map.index('.', first_free_space_index + 1)
        end_block_index = find_first_non_empty_from_end(disk_map)
    
    return disk_map

def calculate_checksum(compact_file: List[str]) -> int:
    """
    Calculate the checksum of a compact file.

    The checksum is calculated by summing the product of the index and the integer value
    of each element in the list, excluding elements that are '.'.

    Args:
        compact_file (List[str]): A list of strings representing the compact file.

    Returns:
        int: The calculated checksum.
    """
    return sum(i * int(val) for i, val in enumerate(compact_file) if val != '.')

if __name__ == "__main__":
    input_data = read_input('input.txt')
    disk_map = generate_disk_map(input_data)
    compact = compact_file(disk_map)
    print(calculate_checksum(compact))
