def addBinary(a: str, b: str) -> str:
    # Convert binary strings to integers
    num1 = int(a, 2)
    num2 = int(b, 2)

    # Add the numbers
    sum_num = num1 + num2

    # Convert back to binary string and remove '0b' prefix
    return bin(sum_num)[2:]

# Test
a_global = "11"
b_global = "1"
print(addBinary(a_global, b_global))  # "100"
