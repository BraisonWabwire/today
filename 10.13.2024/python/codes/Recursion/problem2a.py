def longest_same_number_subsequence(numbers):
    max_count = 1
    current_count = 1
    longest_num = numbers[0]
    start_index = 0
    longest_start_index = 0
    
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                longest_num = numbers[i - 1]
                longest_start_index = start_index
            current_count = 1
            start_index = i
    
    # Check if the last subsequence is the longest
    if current_count > max_count:
        max_count = current_count
        longest_num = numbers[-1]
        longest_start_index = start_index
    
    return longest_start_index, longest_num, max_count

# Test program
numbers = list(map(int, input("Enter a series of numbers: ").split()))
start_index, longest_num, max_count = longest_same_number_subsequence(numbers)

print(f"The longest same number sequence starts at index {start_index} with {max_count} values of {longest_num}")
