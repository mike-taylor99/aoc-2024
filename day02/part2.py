from part1 import read_input, is_monotonic, has_valid_differences
from typing import List

def is_safe(report: List[int]) -> bool:
    """
    Determines if a given report is safe based on specific criteria.

    A report is considered safe if there exists at least one element that can be removed
    such that the remaining elements form a list that is both monotonic and has valid differences.

    Args:
        report (List[int]): A list of integers representing the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    return any(is_monotonic(report[:i] + report[i + 1:]) and has_valid_differences(report[:i] + report[i + 1:]) for i in range(len(report)))

if __name__ == "__main__":
    input_file = 'input.txt'
    reports = read_input(input_file)
    count = sum(1 for report in reports if is_safe(report))
    print(count)
