# Initialize lists to store different data types
integers = []
floats = []
strings = []
alphanumerics = []
special_alphanums = []
specials = []

# Read from the file
with open("mixeddata.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        # Check and classify each line
        if line.isdigit():
            integers.append(int(line))
        elif line.replace('.', '', 1).isdigit():
            floats.append(float(line))
        elif line.isalpha():
            strings.append(line)
        elif line.isalnum():
            alphanumerics.append(line)
        elif any(c.isalnum() for c in line):
            special_alphanums.append(line)
        else:
            specials.append(line)

# Output the lists
print("List of integers:", integers)
print("List of floating points:", floats)
print("List of strings:", strings)
print("List of alphanumerics:", alphanumerics)
print("List of special alphanumerics:", special_alphanums)
print("List of specials:", specials)
