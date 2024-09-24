# 1.Remove Duplicates from Sorted Array 
def removeDuplicates(nums):
    if len(nums) == 0:  # Edge case: empty array
        return 0
    
    k = 1  # Start with the first element (always unique)

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:  # Found a new unique element
            nums[k] = nums[i]  # Place the unique element in the next position
            k += 1  # Increment the count of unique elements

    # Replace elements after the k-th element with underscores
    modified_nums = nums[:k] + ['_'] * (len(nums) - k)

    # Output the results as requested
    print()
    print(f"{k}"+","+ f"nums = {modified_nums}")
    
    return k

# Test usage examples:
# examples 1
nums = [1,1,2]
removeDuplicates(nums)
# examples 2
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)





# 2.Remove Element 
def removeElement(nums, val):
    k = 0  # Initialize a pointer for tracking the position of non-val elements

    for i in range(len(nums)):
        if nums[i] != val:  # If the current element is not equal to val
            nums[k] = nums[i]  # Place the element at position k
            k += 1  # Increment k to move to the next position

    # Output the result in the required format
    print()
    print(f"{k}" +"," + f"nums = {nums[:k] + ['_'] * (len(nums) - k)}")
    
    return k

# Test examples
# example 1
nums = [3,2,2,3]
val = 3
removeElement(nums, val)
# example 2
nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)





# 3.Two Sum 
def twoSum(nums, target):
    # Dictionary to store the numbers and their indices
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        
        # If the complement exists in the dictionary, return the pair of indices
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        num_to_index[num] = i

# test examples for two sum
# example 1
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target)) 

# example 2
nums = [3,2,4]
target = 6
print(twoSum(nums, target)) 

# example 3
nums = [3,3]
target = 6
print(twoSum(nums, target)) 