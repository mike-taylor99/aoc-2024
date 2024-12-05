from typing import List, Tuple
from part1 import read_input, parse_part1, parse_part2, follows_rules, find_middle_elements

def get_invalid_sequences(rules: List[Tuple[int, int]], sequences: List[List[int]]) -> List[List[int]]:
    """
    Filters out sequences that do not follow the given rules.

    Args:
        rules (List[Tuple[int, int]]): A list of tuples where each tuple represents a rule.
        sequences (List[List[int]]): A list of sequences to be checked against the rules.

    Returns:
        List[List[int]]: A list of sequences that do not follow the given rules.
    """
    return [seq for seq in sequences if not follows_rules(rules, seq)]

def get_correct_order(rules: List[Tuple[int, int]], sequence: List[int]) -> List[int]:
    """
    Sorts a sequence of integers based on a list of rules.

    Each rule is a tuple (a, b) which indicates that integer `a` should come before integer `b` in the sequence.
    The function repeatedly applies these rules until the sequence is sorted correctly according to all rules.

    Args:
        rules (List[Tuple[int, int]]): A list of tuples where each tuple contains two integers (a, b).
                                       Each tuple represents a rule that `a` should come before `b`.
        sequence (List[int]): A list of integers that needs to be sorted according to the rules.

    Returns:
        List[int]: The sorted list of integers.
    """
    position = {num: idx for idx, num in enumerate(sequence)}
    sorted_correctly = False
    while not sorted_correctly:
        sorted_correctly = True
        for a, b in rules:
            if a in position and b in position and position[a] > position[b]:
                sequence[position[a]], sequence[position[b]] = sequence[position[b]], sequence[position[a]]
                position[a], position[b] = position[b], position[a]
                sorted_correctly = False
    return sequence

def get_correct_orders(rules: List[Tuple[int, int]], sequences: List[List[int]]) -> List[List[int]]:
    """
    Given a list of rules and a list of sequences, return a list of sequences
    where each sequence is reordered according to the rules.

    Args:
        rules (List[Tuple[int, int]]): A list of tuples where each tuple represents
            a rule. Each rule is a pair of integers (a, b) indicating that element
            'a' should come before element 'b' in the sequence.
        sequences (List[List[int]]): A list of sequences, where each sequence is a
            list of integers to be reordered according to the rules.

    Returns:
        List[List[int]]: A list of reordered sequences, where each sequence is
            reordered according to the given rules.
    """
    return [get_correct_order(rules, seq) for seq in sequences]

if __name__ == "__main__":
    part1_data, part2_data = read_input('input.txt')
    rules = parse_part1(part1_data)
    sequences = parse_part2(part2_data)

    invalid_sequences = get_invalid_sequences(rules, sequences)
    correct_orders = get_correct_orders(rules, invalid_sequences)

    result = sum(find_middle_elements(correct_orders))
    print(result)
