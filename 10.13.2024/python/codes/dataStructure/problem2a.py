def binaryToDecimal(binaryString):
    # The main function starts the helper with initial bounds
    return binaryToDecimalHelper(binaryString, 0, len(binaryString) - 1)

def binaryToDecimalHelper(binaryString, low, high):
    # Base case: when low surpasses high, stop recursion
    if high < low:
        return 0
    # Get the value at the current position
    current_digit = int(binaryString[low])
    # Recursive call for the next digit
    return (current_digit * (2 ** (high - low))) + binaryToDecimalHelper(binaryString, low + 1, high)

# Test Program
binaryString = input("Enter a binary number: ")
decimal_value = binaryToDecimal(binaryString)
print(f"{binaryString} is decimal {decimal_value}")
