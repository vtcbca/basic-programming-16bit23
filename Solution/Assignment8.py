def alphabet_pattern_nested_loops(n):
    for i in range(1, n + 1):
        print(" " * (n - i) * 2, end="")  # Add spaces for alignment
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")  # Increasing order
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")  # Decreasing order
        print()

n = int(input("Enter the number of lines: "))
alphabet_pattern_nested_loops(n)
