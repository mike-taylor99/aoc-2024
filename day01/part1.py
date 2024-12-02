def read_input(file_path: str) -> list[tuple[int, int]]:
    """
    Reads a file and returns its contents as a list of tuples of integers.

    Args:
        file_path (str): The path to the input file.

    Returns:
        list of tuple of int: A list where each element is a tuple of integers 
        representing a line in the file.
    """
    with open(file_path) as f:
        return [tuple(map(int, line.split())) for line in f]

def calculate_sum_of_differences(pairs: list[tuple[int, int]]) -> int:
    """
    Calculate the sum of absolute differences between corresponding elements 
    of two lists derived from pairs of numbers.

    Args:
        pairs (list of tuple): A list of tuples where each tuple contains two numbers.

    Returns:
        int: The sum of absolute differences between corresponding elements 
             of the two sorted lists derived from the input pairs.
    """
    list1, list2 = zip(*pairs)
    list1, list2 = sorted(list1), sorted(list2)
    return sum(abs(a - b) for a, b in zip(list1, list2))

if __name__ == "__main__":
    input_file = 'input.txt'
    pairs = read_input(input_file)
    result = calculate_sum_of_differences(pairs)
    print(result)
