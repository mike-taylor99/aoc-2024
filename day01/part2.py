from part1 import read_input
from collections import Counter
from typing import List, Tuple

def calculate_similarity_score(pairs: List[Tuple[int, int]]) -> int:
    """
    Calculate the similarity score between two lists of integers.

    The function takes a list of pairs of integers, where each pair consists of 
    an element from two different lists. It calculates the similarity score by 
    counting the occurrences of each element in both lists and summing the 
    product of the counts and the element value for each unique element.

    Args:
        pairs (list of tuple): A list of tuples, where each tuple contains two integers.

    Returns:
        int: The similarity score calculated based on the given pairs.
    """
    list1, list2 = zip(*pairs)
    count1, count2 = Counter(list1), Counter(list2)
    return sum(count1[element] * count2[element] * element for element in count1)

if __name__ == "__main__":
    input_file = 'input.txt'
    pairs = read_input(input_file)
    result = calculate_similarity_score(pairs)
    print(result)
