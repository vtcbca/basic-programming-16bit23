def is_palindrome_slicing(s):
    return s == s[::-1]

input_str = input("Enter a string: ").lower()
if is_palindrome_slicing(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
