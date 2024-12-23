from typing import List, Tuple

def parse_input(file_path: str) -> Tuple[List[str], List[str]]:
    """
    Parses the input file to extract towel patterns and desired designs.
    Args:
        file_path (str): The path to the input file.
    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists:
            - The first list contains towel patterns.
            - The second list contains desired designs.
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    blank_line_index = lines.index('')
    towel_patterns = lines[:blank_line_index][0].split(', ')
    desired_designs = lines[blank_line_index + 1:]
    
    return towel_patterns, desired_designs

def can_construct_design(design: str, towel_patterns: List[str]) -> bool:
    """
    Determines if a given design can be constructed using a list of towel patterns.
    Args:
        design (str): The design string that needs to be constructed.
        towel_patterns (List[str]): A list of towel patterns available for constructing the design.
    Returns:
        bool: True if the design can be constructed using the towel patterns, False otherwise.
    """
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
    
    return dp[n]

def count_possible_designs(towel_patterns: List[str], desired_designs: List[str]) -> int:
    """
    Counts the number of desired designs that can be constructed using the given towel patterns.

    Args:
        towel_patterns (List[str]): A list of strings representing available towel patterns.
        desired_designs (List[str]): A list of strings representing the desired designs to be constructed.

    Returns:
        int: The number of desired designs that can be constructed using the given towel patterns.
    """
    return sum(can_construct_design(design, towel_patterns) for design in desired_designs)

if __name__ == "__main__":
    file_path = 'input.txt'
    towel_patterns, desired_designs = parse_input(file_path)
    result = count_possible_designs(towel_patterns, desired_designs)
    print(result)
