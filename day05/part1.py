from typing import List, Tuple

def read_input(file_path: str) -> Tuple[List[str], List[str]]:
    """
    Reads the input file and splits its contents into two parts based on a separator.
    Args:
        file_path (str): The path to the input file.
    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists of strings. The first list
        contains the lines before the separator, and the second list contains the lines
        starting from the separator.
    """
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    
    # Find the index where the second part starts
    separator_index = next(i for i, line in enumerate(lines) if ',' in line)
    
    # Split the contents into two parts
    part1 = lines[:separator_index]
    part2 = lines[separator_index:]

    return part1, part2

def parse_part1(part1: List[str]) -> List[Tuple[int, int]]:
    """
    Parses a list of strings where each string contains two integers separated by a '|'.
    
    Args:
        part1 (List[str]): A list of strings, each containing two integers separated by a '|'.
        
    Returns:
        List[Tuple[int, int]]: A list of tuples, each containing two integers parsed from the input strings.
    """
    return [tuple(map(int, line.split('|'))) for line in part1 if line]

def parse_part2(part2: List[str]) -> List[List[int]]:
    """
    Parses a list of strings where each string contains comma-separated integers.

    Args:
        part2 (List[str]): A list of strings, each containing comma-separated integers.

    Returns:
        List[List[int]]: A list of lists, where each inner list contains integers parsed from the input strings.
    """
    return [list(map(int, line.split(','))) for line in part2 if line]

def follows_rules(rules: List[Tuple[int, int]], sequence: List[int]) -> bool:
    """
    Checks if a given sequence follows a set of rules.

    Args:
        rules (List[Tuple[int, int]]): A list of tuples where each tuple contains two integers (a, b).
                                       The rule is that 'a' should appear before 'b' in the sequence.
        sequence (List[int]): A list of integers representing the sequence to be checked.

    Returns:
        bool: True if the sequence follows all the rules, False otherwise.
    """
    position = {num: idx for idx, num in enumerate(sequence)}
    for a, b in rules:
        if a not in position or b not in position:
            continue
        if position[a] > position[b]:
            return False
    return True

def get_valid_sequences(rules: List[Tuple[int, int]], sequences: List[List[int]]) -> List[List[int]]:
    """
    Filters a list of sequences to return only those that follow the given rules.

    Args:
        rules (List[Tuple[int, int]]): A list of tuples where each tuple represents a rule.
                                       Each rule is a pair of integers.
        sequences (List[List[int]]): A list of sequences, where each sequence is a list of integers.

    Returns:
        List[List[int]]: A list of sequences that follow the given rules.
    """
    return [seq for seq in sequences if follows_rules(rules, seq)]

def find_middle_elements(valid_sequences: List[List[int]]) -> List[int]:
    """
    Given a list of valid sequences, return a list containing the middle element of each sequence.

    Args:
        valid_sequences (List[List[int]]): A list of lists, where each inner list is a sequence of integers.

    Returns:
        List[int]: A list of integers, where each integer is the middle element of the corresponding sequence in valid_sequences.
    """
    return [seq[len(seq) // 2] for seq in valid_sequences]

if __name__ == "__main__":
    part1, part2 = read_input('input.txt')
    pairs = parse_part1(part1)
    part2_lists = parse_part2(part2)
    
    valid_sequences = get_valid_sequences(pairs, part2_lists)

    result = sum(find_middle_elements(valid_sequences))
    print(result)

