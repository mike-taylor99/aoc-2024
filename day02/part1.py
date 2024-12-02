from typing import List, Tuple

def read_input(file_path: str) -> List[List[int]]:
    """
    Reads a file and converts its contents into a list of lists of integers.

    Args:
        file_path (str): The path to the input file.

    Returns:
        List[List[int]]: A list of lists, where each inner list contains integers
                         parsed from a line in the input file.
    """
    with open(file_path) as f:
        return [list(map(int, line.split())) for line in f]

def is_monotonic(report: List[int]) -> bool:
    """
    Determines if a list of integers is monotonic.
    
    A list is considered monotonic if it is either entirely increasing or decreasing.
    
    Args:
        report (List[int]): A list of integers to be checked.
        
    Returns:
        bool: True if the list is monotonic, False otherwise.
    """
    return all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1))

def has_valid_differences(report: List[int]) -> bool:
    """
    Checks if the differences between consecutive elements in the report list
    are within the valid range of 1 to 3 inclusive.

    Args:
        report (List[int]): A list of integers representing the report.

    Returns:
        bool: True if all consecutive differences are between 1 and 3 inclusive, False otherwise.
    """
    return all(1 <= abs(report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))

def is_safe(report: List[int]) -> bool:
    """
    Determines if the given report is safe based on specific criteria.

    A report is considered safe if it is monotonic and has valid differences.

    Args:
        report (List[int]): A list of integers representing the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    return is_monotonic(report) and has_valid_differences(report)

if __name__ == "__main__":
    reports = read_input('input.txt')
    count = sum(1 for report in reports if is_safe(report))
    print(count)
