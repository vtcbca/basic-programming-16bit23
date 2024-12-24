def reverse_string_reversed(s):
    return ''.join(reversed(s))

input_str = input("Enter a string: ")
print(f"Reversed string (using reversed()): {reverse_string_reversed(input_str)}")
