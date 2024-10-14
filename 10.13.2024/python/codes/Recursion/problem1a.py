def is_substring(s1, s2):
    # Traverse the first string
    for i in range(len(s1) - len(s2) + 1):
        # Check if the substring from index i matches s2
        match = True
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return i  # Return the index of the first match
    return -1  # Return -1 if no match is found

# Test program
s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")
index = is_substring(s1, s2)

if index != -1:
    print(f"matched at index {index}")
else:
    print(f"{s2} is not a substring of {s1}")
