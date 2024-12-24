from part1 import parse_input, solve

if __name__ == "__main__":
    input_data = parse_input('input.txt')
    result = sum(solve(sequence, 0, 25) * multiplier for sequence, multiplier in input_data)
    print(result)