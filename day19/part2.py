from typing import List, Tuple
from collections import defaultdict
from part1 import parse_input

def count_ways_to_construct_design(design: str, towel_patterns: List[str]) -> int:
    """
    Counts the number of ways to construct a given design using a list of towel patterns.
    Args:
        design (str): The design string that needs to be constructed.
        towel_patterns (List[str]): A list of towel patterns that can be used to construct the design.
    Returns:
        int: The number of ways to construct the design using the given towel patterns.
    """
    n = len(design)
    dp = defaultdict(int)
    dp[0] = 1  # Base case: there's one way to construct an empty design
    
    for i in range(1, n + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    
    return dp[n]

def total_ways_to_construct_designs(towel_patterns: List[str], desired_designs: List[str]) -> int:
    """
    Calculate the total number of ways to construct each design in the desired designs list
    using the given towel patterns.

    Args:
        towel_patterns (List[str]): A list of available towel patterns.
        desired_designs (List[str]): A list of desired designs to be constructed.

    Returns:
        int: The total number of ways to construct all the desired designs using the towel patterns.
    """
    return sum(count_ways_to_construct_design(design, towel_patterns) for design in desired_designs)

if __name__ == "__main__":
    file_path = 'input.txt'
    towel_patterns, desired_designs = parse_input(file_path)
    result = total_ways_to_construct_designs(towel_patterns, desired_designs)
    print(result)
