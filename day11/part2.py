from part1 import read_input, process_stones_n_times

if __name__ == "__main__":
    input_data = read_input('input.txt')
    processed_stones = process_stones_n_times(input_data, 75)
    print(sum(processed_stones.values()))
